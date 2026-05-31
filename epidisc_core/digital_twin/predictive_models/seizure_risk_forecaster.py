"""
EPIDISC Predictive Modeling System
Seizure risk forecasting based on learned patterns and continuous data
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import json
from collections import defaultdict
import statistics


class RiskLevel(Enum):
    """Seizure risk levels"""
    VERY_LOW = "very_low"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"


class PredictionHorizon(Enum):
    """Prediction time horizons"""
    IMMEDIATE = "immediate"  # Next 1-6 hours
    SHORT_TERM = "short_term"  # Next 24 hours
    MEDIUM_TERM = "medium_term"  # Next 72 hours
    LONG_TERM = "long_term"  # Next 7 days


@dataclass
class RiskPrediction:
    """A single risk prediction"""
    horizon: PredictionHorizon
    risk_level: RiskLevel
    probability: float  # 0.0-1.0
    confidence: float  # 0.0-1.0
    factors: List[str]
    timestamp: datetime
    recommendations: List[str]
    peak_risk_time: Optional[datetime] = None


@dataclass
class TriggerSensitivity:
    """Learned sensitivity to specific triggers"""
    trigger_name: str
    sensitivity_score: float  # 0.0-1.0
    threshold: float
    latency_hours: float
    duration_hours: float


class SeizureRiskForecaster:
    """
    Predictive modeling system for seizure risk forecasting.

    Uses learned individual patterns to predict seizure risk
    across multiple time horizons with confidence intervals.
    """

    def __init__(self):
        self.model_version = "1.0.0"
        self.last_trained = None
        self.feature_importance = {}
        self.trigger_sensitivities = {}
        self.temporal_patterns = {}
        self.model_accuracy = {}

    def train_model(self, training_data: List[Dict]) -> Dict[str, Any]:
        """
        Train the prediction model on historical data.

        Args:
            training_data: List of historical records with features and outcomes

        Returns:
            Training metrics and model performance
        """
        # Extract features and outcomes
        features = []
        outcomes = []

        for record in training_data:
            features.append(self._extract_features(record))
            outcomes.append(record.get('seizure_occurred', False))

        # Train model (simplified - would use ML in production)
        model_metrics = self._train_prediction_model(features, outcomes)

        # Calculate feature importance
        self.feature_importance = self._calculate_feature_importance(features, outcomes)

        # Learn trigger sensitivities
        self.trigger_sensitivities = self._learn_trigger_sensitivities(training_data)

        # Learn temporal patterns
        self.temporal_patterns = self._learn_temporal_patterns(training_data)

        self.last_trained = datetime.now()

        return model_metrics

    def predict_risk(self, current_state: Dict[str, Any],
                    horizon: PredictionHorizon = PredictionHorizon.SHORT_TERM) -> RiskPrediction:
        """
        Predict seizure risk for given time horizon.

        Args:
            current_state: Current patient state and recent data
            horizon: Prediction time horizon

        Returns:
            Risk prediction with confidence and recommendations
        """
        # Extract features from current state
        features = self._extract_features(current_state)

        # Calculate base risk probability
        risk_probability = self._calculate_risk_probability(features, horizon)

        # Determine risk level
        risk_level = self._probability_to_risk_level(risk_probability)

        # Calculate confidence based on data quality and model certainty
        confidence = self._calculate_prediction_confidence(features, horizon)

        # Identify contributing factors
        factors = self._identify_risk_factors(features)

        # Generate personalized recommendations
        recommendations = self._generate_recommendations(risk_level, factors, features)

        # Calculate peak risk time if applicable
        peak_risk_time = self._estimate_peak_risk_time(features, horizon) if horizon != PredictionHorizon.IMMEDIATE else None

        return RiskPrediction(
            horizon=horizon,
            risk_level=risk_level,
            probability=risk_probability,
            confidence=confidence,
            factors=factors,
            timestamp=datetime.now(),
            recommendations=recommendations,
            peak_risk_time=peak_risk_time
        )

    def predict_risk_multi_horizon(self, current_state: Dict[str, Any]) -> List[RiskPrediction]:
        """Generate predictions for multiple time horizons"""
        predictions = []

        for horizon in [PredictionHorizon.IMMEDIATE, PredictionHorizon.SHORT_TERM,
                       PredictionHorizon.MEDIUM_TERM, PredictionHorizon.LONG_TERM]:
            prediction = self.predict_risk(current_state, horizon)
            predictions.append(prediction)

        return predictions

    def _extract_features(self, state: Dict[str, Any]) -> Dict[str, float]:
        """Extract predictive features from state"""
        features = {}

        # Sleep features
        if 'sleep' in state:
            sleep = state['sleep']
            features['sleep_duration'] = sleep.get('duration_hours', 7.0) / 24.0
            features['sleep_quality'] = sleep.get('quality_score', 0.5)
            features['sleep_deprivation'] = 1.0 if sleep.get('duration_hours', 7.0) < 6 else 0.0

        # Stress features
        if 'stress' in state:
            stress = state['stress']
            features['stress_level'] = stress.get('level', 5) / 10.0
            features['high_stress'] = 1.0 if stress.get('level', 5) > 7 else 0.0

        # Medication features
        if 'medication' in state:
            medication = state['medication']
            features['medication_adherence'] = 1.0 - medication.get('missed_doses_24h', 0) / max(medication.get('scheduled_doses_24h', 1), 1)
            features['recent_dose_change'] = 1.0 if medication.get('recent_change', False) else 0.0

        # Environmental features
        if 'environmental' in state:
            env = state['environmental']
            features['weather_change'] = 1.0 if env.get('weather_changing', False) else 0.0
            features['poor_air_quality'] = 1.0 if env.get('aqi', 50) > 100 else 0.0

        # Temporal features
        now = datetime.now()
        features['hour_of_day'] = now.hour / 24.0
        features['day_of_week'] = now.weekday() / 7.0
        features['is_weekend'] = 1.0 if now.weekday() >= 5 else 0.0

        # Hormonal features (if applicable)
        if 'menstrual_cycle' in state:
            cycle = state['menstrual_cycle']
            features['catamenial_risk'] = cycle.get('seizure_risk_phase', 0.0)

        return features

    def _calculate_risk_probability(self, features: Dict[str, float],
                                   horizon: PredictionHorizon) -> float:
        """Calculate seizure risk probability"""
        base_risk = 0.05  # Baseline seizure risk

        # Adjust based on features
        risk_multiplier = 1.0

        # Sleep deprivation
        if features.get('sleep_deprivation', 0) > 0:
            risk_multiplier += 0.3

        # High stress
        if features.get('high_stress', 0) > 0:
            risk_multiplier += 0.2

        # Medication nonadherence
        risk_multiplier += (1.0 - features.get('medication_adherence', 1.0)) * 0.4

        # Environmental triggers
        if features.get('weather_change', 0) > 0:
            risk_multiplier += 0.1

        # Catamenial pattern
        if features.get('catamenial_risk', 0) > 0:
            risk_multiplier += features.get('catamenial_risk', 0) * 0.2

        # Apply horizon-specific adjustments
        horizon_multiplier = self._get_horizon_multiplier(horizon)

        risk_probability = base_risk * risk_multiplier * horizon_multiplier

        return min(risk_probability, 1.0)

    def _get_horizon_multiplier(self, horizon: PredictionHorizon) -> float:
        """Get risk multiplier based on prediction horizon"""
        multipliers = {
            PredictionHorizon.IMMEDIATE: 1.5,    # Higher risk for immediate predictions
            PredictionHorizon.SHORT_TERM: 1.2,
            PredictionHorizon.MEDIUM_TERM: 1.0,
            PredictionHorizon.LONG_TERM: 0.8      # More uncertainty for longer horizons
        }
        return multipliers.get(horizon, 1.0)

    def _probability_to_risk_level(self, probability: float) -> RiskLevel:
        """Convert probability to risk level"""
        if probability < 0.1:
            return RiskLevel.VERY_LOW
        elif probability < 0.3:
            return RiskLevel.LOW
        elif probability < 0.5:
            return RiskLevel.MODERATE
        elif probability < 0.7:
            return RiskLevel.HIGH
        else:
            return RiskLevel.VERY_HIGH

    def _calculate_prediction_confidence(self, features: Dict[str, float],
                                        horizon: PredictionHorizon) -> float:
        """Calculate confidence in prediction"""
        confidence = 0.7  # Base confidence

        # Higher confidence with more complete data
        feature_completeness = sum(1 for v in features.values() if v is not None) / len(features)
        confidence += feature_completeness * 0.2

        # Lower confidence for longer horizons
        if horizon == PredictionHorizon.LONG_TERM:
            confidence -= 0.2
        elif horizon == PredictionHorizon.IMMEDIATE:
            confidence += 0.1

        return min(confidence, 1.0)

    def _identify_risk_factors(self, features: Dict[str, float]) -> List[str]:
        """Identify factors contributing to current risk"""
        factors = []

        if features.get('sleep_deprivation', 0) > 0:
            factors.append("Sleep deprivation")

        if features.get('high_stress', 0) > 0:
            factors.append("High stress levels")

        if features.get('medication_adherence', 1.0) < 0.8:
            factors.append("Medication nonadherence")

        if features.get('weather_change', 0) > 0:
            factors.append("Weather changes")

        if features.get('poor_air_quality', 0) > 0:
            factors.append("Poor air quality")

        if features.get('catamenial_risk', 0) > 0.5:
            factors.append("Hormonal cycle pattern")

        return factors

    def _generate_recommendations(self, risk_level: RiskLevel,
                                 factors: List[str],
                                 features: Dict[str, float]) -> List[str]:
        """Generate personalized recommendations based on risk level"""
        recommendations = []

        # High-risk recommendations
        if risk_level in [RiskLevel.HIGH, RiskLevel.VERY_HIGH]:
            recommendations.append("Avoid activities where seizures could be dangerous")
            recommendations.append("Ensure someone can check on you")
            recommendations.append("Keep rescue medication accessible")

            if "Sleep deprivation" in factors:
                recommendations.append("Prioritize getting adequate sleep tonight")

            if "High stress levels" in factors:
                recommendations.append("Practice stress reduction techniques")

            if "Medication nonadherence" in factors:
                recommendations.append("Take all scheduled medications on time")

            if features.get('medication_adherence', 1.0) < 0.5:
                recommendations.append("Consider using medication reminders")

        # Moderate-risk recommendations
        elif risk_level == RiskLevel.MODERATE:
            recommendations.append("Be cautious with risky activities")

            if "Sleep deprivation" in factors:
                recommendations.append("Try to get extra sleep tonight")

            if "High stress levels" in factors:
                recommendations.append("Consider stress management techniques")

        # Low-risk recommendations
        else:
            recommendations.append("Continue normal activities")
            recommendations.append("Maintain regular routine")

        # Add general recommendations based on factors
        if features.get('sleep_quality', 1.0) < 0.5:
            recommendations.append("Focus on improving sleep quality")

        if features.get('medication_adherence', 1.0) < 0.9:
            recommendations.append("Set up medication reminders")

        return recommendations

    def _estimate_peak_risk_time(self, features: Dict[str, float],
                                horizon: PredictionHorizon) -> Optional[datetime]:
        """Estimate when risk will be highest"""
        # Simple implementation - would be more sophisticated in production
        now = datetime.now()

        if horizon == PredictionHorizon.SHORT_TERM:
            # Peak risk often occurs during sleep deprivation or stress periods
            if features.get('sleep_deprivation', 0) > 0:
                return now + timedelta(hours=6)  # 6 hours from now

        return None

    def _train_prediction_model(self, features: List[Dict], outcomes: List[bool]) -> Dict[str, Any]:
        """Train the prediction model (simplified)"""
        # In production, this would use actual ML algorithms
        # For now, return placeholder metrics

        if len(features) < 10:
            return {
                'status': 'insufficient_data',
                'samples_needed': 10 - len(features)
            }

        # Calculate basic metrics
        correct_predictions = sum(1 for f, o in zip(features, outcomes)
                                 if self._would_predict_correctly(f, o))
        accuracy = correct_predictions / len(outcomes) if outcomes else 0

        return {
            'status': 'trained',
            'accuracy': accuracy,
            'samples': len(outcomes),
            'training_date': datetime.now().isoformat()
        }

    def _would_predict_correctly(self, features: Dict, outcome: bool) -> bool:
        """Helper function to check if prediction would be correct"""
        risk_prob = self._calculate_risk_probability(features, PredictionHorizon.SHORT_TERM)
        predicted_seizure = risk_prob > 0.5
        return predicted_seizure == outcome

    def _calculate_feature_importance(self, features: List[Dict], outcomes: List[bool]) -> Dict[str, float]:
        """Calculate importance of each feature"""
        # Simplified feature importance calculation
        # In production, would use actual feature importance algorithms

        importance = {
            'sleep_deprivation': 0.85,
            'medication_adherence': 0.90,
            'high_stress': 0.75,
            'weather_change': 0.60,
            'catamenial_risk': 0.70
        }

        return importance

    def _learn_trigger_sensitivities(self, training_data: List[Dict]) -> Dict[str, TriggerSensitivity]:
        """Learn individual sensitivities to triggers"""
        # Simplified trigger sensitivity learning
        # In production, would analyze actual trigger-seizure correlations

        sensitivities = {
            'sleep_deprivation': TriggerSensitivity(
                trigger_name='sleep_deprivation',
                sensitivity_score=0.85,
                threshold=0.3,  # Hours below normal
                latency_hours=12.0,
                duration_hours=24.0
            ),
            'high_stress': TriggerSensitivity(
                trigger_name='high_stress',
                sensitivity_score=0.75,
                threshold=7.0,  # On 1-10 scale
                latency_hours=6.0,
                duration_hours=18.0
            )
        }

        return sensitivities

    def _learn_temporal_patterns(self, training_data: List[Dict]) -> Dict[str, Any]:
        """Learn temporal seizure patterns"""
        # Simplified temporal pattern learning
        # In production, would use time series analysis

        patterns = {
            'time_of_day_risk': {
                'morning': 0.3,
                'afternoon': 0.2,
                'evening': 0.25,
                'night': 0.35
            },
            'day_of_week_risk': {
                'weekday': 0.3,
                'weekend': 0.25
            }
        }

        return patterns

    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the prediction model"""
        return {
            'version': self.model_version,
            'last_trained': self.last_trained.isoformat() if self.last_trained else None,
            'feature_importance': self.feature_importance,
            'trigger_sensitivities': {
                name: {
                    'sensitivity_score': ts.sensitivity_score,
                    'threshold': ts.threshold
                }
                for name, ts in self.trigger_sensitivities.items()
            },
            'temporal_patterns': self.temporal_patterns
        }


class RiskPredictionEngine:
    """High-level engine for risk prediction and alerting"""

    def __init__(self):
        self.forecaster = SeizureRiskForecaster()
        self.alert_thresholds = {
            RiskLevel.VERY_HIGH: 0.9,
            RiskLevel.HIGH: 0.7,
            RiskLevel.MODERATE: 0.5
        }

    def analyze_current_state(self, current_state: Dict[str, Any]) -> Dict[str, Any]:
        """Comprehensive risk analysis of current state"""
        predictions = self.forecaster.predict_risk_multi_horizon(current_state)

        return {
            'timestamp': datetime.now().isoformat(),
            'predictions': [
                {
                    'horizon': p.horizon.value,
                    'risk_level': p.risk_level.value,
                    'probability': p.probability,
                    'confidence': p.confidence,
                    'factors': p.factors,
                    'recommendations': p.recommendations,
                    'peak_risk_time': p.peak_risk_time.isoformat() if p.peak_risk_time else None
                }
                for p in predictions
            ],
            'should_alert': self._should_alert(predictions),
            'urgent_recommendations': self._get_urgent_recommendations(predictions)
        }

    def _should_alert(self, predictions: List[RiskPrediction]) -> bool:
        """Determine if alert should be triggered"""
        return any(p.probability >= self.alert_thresholds.get(p.risk_level, 1.0)
                  for p in predictions)

    def _get_urgent_recommendations(self, predictions: List[RiskPrediction]) -> List[str]:
        """Get urgent recommendations based on high-risk predictions"""
        urgent = []

        for p in predictions:
            if p.risk_level in [RiskLevel.HIGH, RiskLevel.VERY_HIGH]:
                urgent.extend(p.recommendations)

        return list(set(urgent))  # Remove duplicates

    def export_prediction_config(self) -> str:
        """Export prediction system configuration"""
        return json.dumps({
            'forecaster': self.forecaster.get_model_info(),
            'alert_thresholds': {
                level.value: threshold
                for level, threshold in self.alert_thresholds.items()
            }
        }, indent=2)


# Convenience functions
def create_risk_forecaster() -> SeizureRiskForecaster:
    """Create a new seizure risk forecaster"""
    return SeizureRiskForecaster()


def create_prediction_engine() -> RiskPredictionEngine:
    """Create a new risk prediction engine"""
    return RiskPredictionEngine()
