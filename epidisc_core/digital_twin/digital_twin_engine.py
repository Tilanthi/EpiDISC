"""
EPIDISC Digital Twin Engine - Core Architecture
Creates living digital models of epilepsy patients that learn and predict
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import json
from collections import defaultdict


class DataStreamType(Enum):
    """Types of continuous data streams"""
    SEIZURE_EVENTS = "seizure_events"
    SLEEP_PATTERN = "sleep_pattern"
    MEDICATION_ADHERENCE = "medication_adherence"
    STRESS_LEVEL = "stress_level"
    MOOD_SCORE = "mood_score"
    ENVIRONMENTAL = "environmental"
    ACTIVITY_LEVEL = "activity_level"
    COGNITIVE_METRIC = "cognitive_metric"
    MENSTRUAL_CYCLE = "menstrual_cycle"
    HEART_RATE_VARIABILITY = "heart_rate_variability"


@dataclass
class DataPoint:
    """A single data point from any stream"""
    stream_type: DataStreamType
    timestamp: datetime
    value: Any
    source: str
    confidence: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SeizureEvent:
    """Detailed seizure event recording"""
    timestamp: datetime
    seizure_type: str
    duration: float
    severity: str  # mild, moderate, severe
    aura_present: bool
    aura_description: Optional[str]
    triggers_identified: List[str]
    postictal_state: str
    context: Dict[str, Any]


@dataclass
class MedicationEvent:
    """Medication administration tracking"""
    timestamp: datetime
    medication_name: str
    dose: float
    unit: str
    adherence_status: str  # taken, missed, late, partial
    side_effects: List[str]
    context: Dict[str, Any]


class DigitalTwinEngine:
    """
    Core engine for creating and maintaining digital twins of epilepsy patients.

    The digital twin continuously learns individual patterns, identifies triggers,
    and predicts seizure risk based on integrated data streams.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.created_at = datetime.now()
        self.data_streams = defaultdict(list)
        self.learned_patterns = {}
        self.predictions = {}
        self.baseline_metrics = {}

    def ingest_data_point(self, data_point: DataPoint) -> None:
        """Ingest a single data point into the appropriate stream"""
        self.data_streams[data_point.stream_type].append(data_point)
        self._update_learned_patterns(data_point)
        self._update_predictions()

    def ingest_seizure_event(self, event: SeizureEvent) -> None:
        """Record a detailed seizure event"""
        data_point = DataPoint(
            stream_type=DataStreamType.SEIZURE_EVENTS,
            timestamp=event.timestamp,
            value=event,
            source="patient_report"
        )
        self.ingest_data_point(data_point)

    def ingest_medication_event(self, event: MedicationEvent) -> None:
        """Record medication administration"""
        data_point = DataPoint(
            stream_type=DataStreamType.MEDICATION_ADHERENCE,
            timestamp=event.timestamp,
            value=event,
            source="patient_report"
        )
        self.ingest_data_point(data_point)

    def _update_learned_patterns(self, new_data: DataPoint) -> None:
        """Update learned patterns based on new data"""
        # Pattern learning happens incrementally
        # This is where individual patterns are discovered

        if new_data.stream_type == DataStreamType.SEIZURE_EVENTS:
            self._learn_seizure_patterns()
        elif new_data.stream_type == DataStreamType.SLEEP_PATTERN:
            self._learn_sleep_patterns()
        elif new_data.stream_type == DataStreamType.STRESS_LEVEL:
            self._learn_stress_patterns()

    def _learn_seizure_patterns(self) -> None:
        """Learn individual seizure patterns"""
        seizure_events = [dp.value for dp in self.data_streams[DataStreamType.SEIZURE_EVENTS]]

        if len(seizure_events) < 3:
            return  # Need minimum data for pattern learning

        # Analyze temporal patterns
        self.learned_patterns['seizure_precursors'] = self._identify_seizure_precursors(seizure_events)
        self.learned_patterns['trigger_combinations'] = self._identify_trigger_combinations(seizure_events)
        self.learned_patterns['temporal_patterns'] = self._identify_temporal_patterns(seizure_events)

    def _identify_seizure_precursors(self, events: List[SeizureEvent]) -> List[Dict]:
        """Identify common precursors to seizures"""
        precursors = []

        for event in events:
            # Look for patterns in the 24-48 hours before seizure
            precursor_window = self._get_data_in_window(
                event.timestamp - timedelta(hours=48),
                event.timestamp
            )

            # Analyze for common precursor patterns
            # (This would be more sophisticated in full implementation)
            if self._has_sleep_deprivation(precursor_window):
                precursors.append({
                    'type': 'sleep_deprivation',
                    'frequency': self._calculate_frequency('sleep_deprivation', events)
                })

            if self._has_high_stress(precursor_window):
                precursors.append({
                    'type': 'high_stress',
                    'frequency': self._calculate_frequency('high_stress', events)
                })

            if self._has_missed_medication(precursor_window):
                precursors.append({
                    'type': 'medication_nonadherence',
                    'frequency': self._calculate_frequency('medication_nonadherence', events)
                })

        return precursors

    def _identify_trigger_combinations(self, events: List[SeizureEvent]) -> List[Dict]:
        """Identify combinations of triggers that lead to seizures"""
        combinations = []

        # Analyze events for multiple trigger combinations
        for event in events:
            triggers = event.triggers_identified
            if len(triggers) > 1:
                combinations.append({
                    'triggers': triggers,
                    'seizure_type': event.seizure_type,
                    'severity': event.severity
                })

        return combinations

    def _identify_temporal_patterns(self, events: List[SeizureEvent]) -> Dict:
        """Identify temporal patterns in seizures"""
        patterns = {
            'time_of_day': self._analyze_time_patterns(events),
            'day_of_week': self._analyze_day_patterns(events),
            'monthly_patterns': self._analyze_monthly_patterns(events),
            'seasonal_patterns': self._analyze_seasonal_patterns(events)
        }
        return patterns

    def _learn_sleep_patterns(self) -> None:
        """Learn individual sleep patterns and their relationship to seizures"""
        sleep_data = [dp for dp in self.data_streams[DataStreamType.SLEEP_PATTERN]]

        if len(sleep_data) < 7:
            return

        # Analyze sleep quality, duration, timing
        # Correlate with seizure events
        pass  # Placeholder for sophisticated sleep analysis

    def _learn_stress_patterns(self) -> None:
        """Learn stress patterns and their relationship to seizures"""
        stress_data = [dp for dp in self.data_streams[DataStreamType.STRESS_LEVEL]]

        if len(stress_data) < 7:
            return

        # Analyze stress levels, timing, patterns
        # Correlate with seizure events
        pass  # Placeholder for sophisticated stress analysis

    def _update_predictions(self) -> None:
        """Update seizure risk predictions based on current state"""
        current_risk = self._calculate_current_risk()
        future_risk_24h = self._predict_risk_24h()
        future_risk_72h = self._predict_risk_72h()

        self.predictions = {
            'current_risk': current_risk,
            '24h_risk': future_risk_24h,
            '72h_risk': future_risk_72h,
            'risk_factors': self._identify_current_risk_factors(),
            'recommendations': self._generate_recommendations()
        }

    def _calculate_current_risk(self) -> float:
        """Calculate current seizure risk (0-1 scale)"""
        risk_score = 0.0

        # Factor in recent patterns
        recent_window = self._get_data_in_window(
            datetime.now() - timedelta(hours=24),
            datetime.now()
        )

        # Sleep factor
        if self._has_sleep_deprivation(recent_window):
            risk_score += 0.3

        # Stress factor
        if self._has_high_stress(recent_window):
            risk_score += 0.2

        # Medication adherence
        if self._has_missed_medication(recent_window):
            risk_score += 0.4

        # Hormonal factors (if applicable)
        if self._has_catamenial_pattern(recent_window):
            risk_score += 0.2

        # Environmental factors
        environmental_risk = self._assess_environmental_risk(recent_window)
        risk_score += environmental_risk

        return min(risk_score, 1.0)

    def _predict_risk_24h(self) -> float:
        """Predict seizure risk for next 24 hours"""
        current_risk = self.predictions.get('current_risk', 0.0)

        # Modify based on learned patterns and scheduled activities
        # (This would be more sophisticated in full implementation)

        predicted_risk = current_risk  # Base prediction

        # Adjust for known patterns
        if self._has_high_risk_period_scheduled():
            predicted_risk += 0.2

        return min(predicted_risk, 1.0)

    def _predict_risk_72h(self) -> float:
        """Predict seizure risk for next 72 hours"""
        # Similar to 24h but with longer horizon
        return self._predict_risk_24h()  # Simplified

    def _identify_current_risk_factors(self) -> List[str]:
        """Identify current factors contributing to seizure risk"""
        factors = []

        recent_window = self._get_data_in_window(
            datetime.now() - timedelta(hours=24),
            datetime.now()
        )

        if self._has_sleep_deprivation(recent_window):
            factors.append("Sleep deprivation")

        if self._has_high_stress(recent_window):
            factors.append("High stress levels")

        if self._has_missed_medication(recent_window):
            factors.append("Recent medication nonadherence")

        if self._has_catamenial_pattern(recent_window):
            factors.append("Hormonal cycle pattern")

        environmental = self._assess_environmental_factors(recent_window)
        factors.extend(environmental)

        return factors

    def _generate_recommendations(self) -> List[str]:
        """Generate personalized recommendations based on current state"""
        recommendations = []

        risk_factors = self._identify_current_risk_factors()

        if "Sleep deprivation" in risk_factors:
            recommendations.append("Prioritize sleep tonight - aim for 8 hours")
            recommendations.append("Avoid screens 1 hour before bed")

        if "High stress levels" in risk_factors:
            recommendations.append("Practice stress reduction techniques")
            recommendations.append("Consider meditation or deep breathing exercises")

        if "Recent medication nonadherence" in risk_factors:
            recommendations.append("Set medication reminders")
            recommendations.append("Use pill organizer or smart bottle")

        if self.predictions.get('24h_risk', 0) > 0.7:
            recommendations.append("Avoid driving tomorrow")
            recommendations.append("Ensure someone can check on you")
            recommendations.append("Keep rescue medication accessible")

        return recommendations

    def _get_data_in_window(self, start: datetime, end: datetime) -> List[DataPoint]:
        """Get all data points within a time window"""
        window_data = []
        for stream_type, data_points in self.data_streams.items():
            for dp in data_points:
                if start <= dp.timestamp <= end:
                    window_data.append(dp)
        return window_data

    def _has_sleep_deprivation(self, data: List[DataPoint]) -> bool:
        """Check if sleep deprivation is present in data"""
        sleep_data = [dp for dp in data if dp.stream_type == DataStreamType.SLEEP_PATTERN]
        if not sleep_data:
            return False

        # Analyze sleep data for deprivation patterns
        # (Simplified - full implementation would be more sophisticated)
        for dp in sleep_data[-3:]:  # Check last 3 sleep records
            if isinstance(dp.value, dict) and dp.value.get('duration', 0) < 6:
                return True

        return False

    def _has_high_stress(self, data: List[DataPoint]) -> bool:
        """Check if high stress is present in data"""
        stress_data = [dp for dp in data if dp.stream_type == DataStreamType.STRESS_LEVEL]
        if not stress_data:
            return False

        for dp in stress_data[-5:]:  # Check last 5 stress readings
            if isinstance(dp.value, (int, float)) and dp.value > 7:  # On 1-10 scale
                return True

        return False

    def _has_missed_medication(self, data: List[DataPoint]) -> bool:
        """Check if medication has been missed"""
        med_data = [dp for dp in data if dp.stream_type == DataStreamType.MEDICATION_ADHERENCE]
        if not med_data:
            return False

        for dp in med_data[-3:]:  # Check last 3 medication events
            if isinstance(dp.value, MedicationEvent):
                if dp.value.adherence_status in ['missed', 'late']:
                    return True

        return False

    def _has_catamenial_pattern(self, data: List[DataPoint]) -> bool:
        """Check for catamenial epilepsy patterns"""
        cycle_data = [dp for dp in data if dp.stream_type == DataStreamType.MENSTRUAL_CYCLE]
        seizure_data = [dp for dp in data if dp.stream_type == DataStreamType.SEIZURE_EVENTS]

        if not cycle_data or len(seizure_data) < 2:
            return False

        # Analyze if seizures cluster around menstrual cycle
        # (Simplified - full implementation would be more sophisticated)
        return len(cycle_data) > 0  # Placeholder

    def _assess_environmental_risk(self, data: List[DataPoint]) -> float:
        """Assess environmental risk factors"""
        environmental_data = [dp for dp in data if dp.stream_type == DataStreamType.ENVIRONMENTAL]
        if not environmental_data:
            return 0.0

        risk = 0.0
        for dp in environmental_data:
            if isinstance(dp.value, dict):
                # Check for various environmental triggers
                if dp.value.get('weather_changes'):
                    risk += 0.1
                if dp.value.get('air_quality_poor'):
                    risk += 0.1

        return min(risk, 0.3)

    def _assess_environmental_factors(self, data: List[DataPoint]) -> List[str]:
        """Identify specific environmental risk factors"""
        factors = []
        environmental_data = [dp for dp in data if dp.stream_type == DataStreamType.ENVIRONMENTAL]

        for dp in environmental_data:
            if isinstance(dp.value, dict):
                if dp.value.get('weather_changes'):
                    factors.append("Weather changes")
                if dp.value.get('air_quality_poor'):
                    factors.append("Poor air quality")

        return factors

    def _has_high_risk_period_scheduled(self) -> bool:
        """Check if high-risk period is scheduled based on patterns"""
        # Check against learned temporal patterns
        return False  # Placeholder

    def _calculate_frequency(self, precursor_type: str, events: List[SeizureEvent]) -> float:
        """Calculate how often a precursor is associated with seizures"""
        if not events:
            return 0.0
        return 0.5  # Placeholder

    def _analyze_time_patterns(self, events: List[SeizureEvent]) -> Dict:
        """Analyze time-of-day patterns"""
        return {}  # Placeholder

    def _analyze_day_patterns(self, events: List[SeizureEvent]) -> Dict:
        """Analyze day-of-week patterns"""
        return {}  # Placeholder

    def _analyze_monthly_patterns(self, events: List[SeizureEvent]) -> Dict:
        """Analyze monthly patterns"""
        return {}  # Placeholder

    def _analyze_seasonal_patterns(self, events: List[SeizureEvent]) -> Dict:
        """Analyze seasonal patterns"""
        return {}  # Placeholder

    def get_current_state(self) -> Dict[str, Any]:
        """Get current digital twin state"""
        return {
            'patient_id': self.patient_id,
            'created_at': self.created_at.isoformat(),
            'data_points_count': sum(len(stream) for stream in self.data_streams.values()),
            'learned_patterns': self.learned_patterns,
            'predictions': self.predictions,
            'baseline_metrics': self.baseline_metrics
        }

    def export_state(self) -> str:
        """Export digital twin state for storage/transfer"""
        state = self.get_current_state()
        # Convert datetime objects to ISO format
        for stream_type, data_points in self.data_streams.items():
            serialized = []
            for dp in data_points:
                serialized.append({
                    'stream_type': dp.stream_type.value,
                    'timestamp': dp.timestamp.isoformat(),
                    'value': dp.value,
                    'source': dp.source,
                    'confidence': dp.confidence,
                    'metadata': dp.metadata
                })
            state['data_streams'][stream_type.value] = serialized

        return json.dumps(state, indent=2)

    def import_state(self, state_json: str) -> None:
        """Import digital twin state from storage"""
        state = json.loads(state_json)

        # Restore data streams
        for stream_type, data_points in state.get('data_streams', {}).items():
            for dp_data in data_points:
                dp = DataPoint(
                    stream_type=DataStreamType(stream_type),
                    timestamp=datetime.fromisoformat(dp_data['timestamp']),
                    value=dp_data['value'],
                    source=dp_data['source'],
                    confidence=dp_data.get('confidence', 1.0),
                    metadata=dp_data.get('metadata', {})
                )
                self.data_streams[DataStreamType(stream_type)].append(dp)

        # Restore learned patterns and predictions
        self.learned_patterns = state.get('learned_patterns', {})
        self.predictions = state.get('predictions', {})
        self.baseline_metrics = state.get('baseline_metrics', {})


class DigitalTwinFactory:
    """Factory for creating and managing digital twins"""

    def __init__(self):
        self.active_twins = {}

    def create_twin(self, patient_id: str) -> DigitalTwinEngine:
        """Create a new digital twin"""
        if patient_id in self.active_twins:
            return self.active_twins[patient_id]

        twin = DigitalTwinEngine(patient_id)
        self.active_twins[patient_id] = twin
        return twin

    def get_twin(self, patient_id: str) -> Optional[DigitalTwinEngine]:
        """Get existing digital twin"""
        return self.active_twins.get(patient_id)

    def save_twin(self, patient_id: str, filepath: str) -> None:
        """Save digital twin to file"""
        twin = self.get_twin(patient_id)
        if twin:
            with open(filepath, 'w') as f:
                f.write(twin.export_state())

    def load_twin(self, patient_id: str, filepath: str) -> DigitalTwinEngine:
        """Load digital twin from file"""
        with open(filepath, 'r') as f:
            state_json = f.read()

        if patient_id not in self.active_twins:
            self.active_twins[patient_id] = DigitalTwinEngine(patient_id)

        self.active_twins[patient_id].import_state(state_json)
        return self.active_twins[patient_id]


# Convenience function for creating digital twins
def create_digital_twin(patient_id: str) -> DigitalTwinEngine:
    """Create a new digital twin for a patient"""
    factory = DigitalTwinFactory()
    return factory.create_twin(patient_id)
