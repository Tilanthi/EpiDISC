"""
EPIDISC Emotional-Cognitive Integration Layer
Comprehensive mental health and cognitive function monitoring for epilepsy patients
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import json
from collections import defaultdict


class EmotionalState(Enum):
    """Emotional state categories"""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"


class CognitiveDomain(Enum):
    """Cognitive domains to monitor"""
    MEMORY = "memory"
    ATTENTION = "attention"
    EXECUTIVE_FUNCTION = "executive_function"
    PROCESSING_SPEED = "processing_speed"
    LANGUAGE = "language"
    VISUAL_SPATIAL = "visual_spatial"
    PSYCHOMOTOR = "psychomotor"


@dataclass
class MoodAssessment:
    """Comprehensive mood assessment"""
    timestamp: datetime
    depression_score: float  # PHQ-9 score (0-27)
    anxiety_score: float  # GAD-7 score (0-21)
    overall_mood: float  # 1-10 scale
    stress_level: float  # 1-10 scale
    energy_level: float  # 1-10 scale
    sleep_quality: float  # 1-10 scale
    social_engagement: float  # 1-10 scale
    factors: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class CognitiveAssessment:
    """Cognitive function assessment"""
    timestamp: datetime
    domain_scores: Dict[CognitiveDomain, float]  # 0-100 scale
    overall_cognitive_score: float
    subjective_complaints: List[str]
    objective_findings: List[str]
    medication_effects: List[str]
    functional_impact: str


@dataclass
class PsychiatricIntegration:
    """Psychiatric medication and therapy integration"""
    timestamp: datetime
    psychiatric_diagnoses: List[str]
    psychiatric_medications: List[Dict[str, Any]]
    therapy_status: str
    crisis_history: List[Dict[str, Any]]
    risk_factors: List[str]
    protective_factors: List[str]


@dataclass
class QualityOfLifeMetrics:
    """Patient-centered quality of life metrics"""
    timestamp: datetime
    seizure_freedom: bool
    seizure_control_satisfaction: float  # 1-10
    side_effect_burden: float  # 1-10
    independence_level: float  # 1-10
    social_functioning: float  # 1-10
    occupational_functioning: float  # 1-10
    overall_qol: float  # 1-10
    life_satisfaction: float  # 1-10
    future_outlook: float  # 1-10


class EmotionalHealthMonitor:
    """
    Continuous monitoring and analysis of emotional health in epilepsy patients.

    Tracks mood, anxiety, depression, stress, and their relationship
    to seizure control and medication effects.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.mood_history: List[MoodAssessment] = []
        self.trend_analysis = {}
        self.crisis_alerts = []
        self.intervention_recommendations = []

    def record_mood_assessment(self, assessment: MoodAssessment) -> Dict[str, Any]:
        """Record a new mood assessment and generate insights"""
        self.mood_history.append(assessment)

        analysis = {
            'timestamp': assessment.timestamp.isoformat(),
            'current_state': self._determine_emotional_state(assessment),
            'trend_analysis': self._analyze_trends(),
            'risk_assessment': self._assess_emotional_risks(assessment),
            'recommendations': self._generate_emotional_recommendations(assessment),
            'crisis_alert': self._check_for_crisis(assessment)
        }

        if analysis['crisis_alert']:
            self.crisis_alerts.append(analysis['crisis_alert'])

        return analysis

    def _determine_emotional_state(self, assessment: MoodAssessment) -> EmotionalState:
        """Determine overall emotional state"""
        # Combine depression, anxiety, and overall mood
        depression_severity = self._get_depression_severity(assessment.depression_score)
        anxiety_severity = self._get_anxiety_severity(assessment.anxiety_score)

        if depression_severity == 'severe' or anxiety_severity == 'severe':
            return EmotionalState.CRITICAL
        elif depression_severity == 'moderate' or anxiety_severity == 'moderate':
            return EmotionalState.POOR
        elif assessment.overall_mood >= 7:
            return EmotionalState.GOOD
        elif assessment.overall_mood >= 5:
            return EmotionalState.FAIR
        else:
            return EmotionalState.POOR

    def _get_depression_severity(self, score: float) -> str:
        """Categorize depression severity"""
        if score >= 20:
            return 'severe'
        elif score >= 15:
            return 'moderately_severe'
        elif score >= 10:
            return 'moderate'
        elif score >= 5:
            return 'mild'
        else:
            return 'none'

    def _get_anxiety_severity(self, score: float) -> str:
        """Categorize anxiety severity"""
        if score >= 15:
            return 'severe'
        elif score >= 10:
            return 'moderate'
        elif score >= 5:
            return 'mild'
        else:
            return 'none'

    def _analyze_trends(self) -> Dict[str, Any]:
        """Analyze emotional health trends over time"""
        if len(self.mood_history) < 3:
            return {'status': 'insufficient_data'}

        recent = self.mood_history[-4:]  # Last 4 assessments

        trends = {
            'depression_trend': self._calculate_trend([a.depression_score for a in recent]),
            'anxiety_trend': self._calculate_trend([a.anxiety_score for a in recent]),
            'mood_trend': self._calculate_trend([a.overall_mood for a in recent]),
            'stress_trend': self._calculate_trend([a.stress_level for a in recent]),
            'energy_trend': self._calculate_trend([a.energy_level for a in recent])
        }

        return trends

    def _calculate_trend(self, values: List[float]) -> str:
        """Calculate trend direction"""
        if len(values) < 2:
            return 'stable'

        # Simple linear trend
        first_half = values[:len(values)//2]
        second_half = values[len(values)//2:]

        avg_first = sum(first_half) / len(first_half)
        avg_second = sum(second_half) / len(second_half)

        difference = avg_second - avg_first

        if difference > 1.0:
            return 'improving'
        elif difference < -1.0:
            return 'declining'
        else:
            return 'stable'

    def _assess_emotional_risks(self, assessment: MoodAssessment) -> List[str]:
        """Identify emotional health risks"""
        risks = []

        if assessment.depression_score >= 15:
            risks.append("Moderate to severe depression")

        if assessment.anxiety_score >= 10:
            risks.append("Moderate to severe anxiety")

        if assessment.stress_level >= 8:
            risks.append("High stress levels")

        if assessment.energy_level <= 3:
            risks.append("Severe fatigue/low energy")

        if assessment.sleep_quality <= 3:
            risks.append("Poor sleep quality")

        if assessment.social_engagement <= 3:
            risks.append("Social isolation")

        return risks

    def _generate_emotional_recommendations(self, assessment: MoodAssessment) -> List[str]:
        """Generate personalized emotional health recommendations"""
        recommendations = []

        # Depression recommendations
        if assessment.depression_score >= 10:
            recommendations.append("Consider professional mental health evaluation")
            recommendations.append("Maintain regular social contact even when not feeling motivated")
            if assessment.depression_score >= 15:
                recommendations.append("URGENT: Professional evaluation recommended")

        # Anxiety recommendations
        if assessment.anxiety_score >= 10:
            recommendations.append("Consider anxiety management techniques")
            recommendations.append("Regular exercise may help reduce anxiety")
            if assessment.anxiety_score >= 15:
                recommendations.append("Consider anti-anxiety medication consultation")

        # Stress recommendations
        if assessment.stress_level >= 7:
            recommendations.append("Practice stress reduction techniques daily")
            recommendations.append("Consider mindfulness meditation or deep breathing exercises")

        # Energy recommendations
        if assessment.energy_level <= 4:
            recommendations.append("Evaluate sleep patterns and quality")
            recommendations.append("Consider medical evaluation for fatigue causes")

        # Sleep recommendations
        if assessment.sleep_quality <= 4:
            recommendations.append("Focus on sleep hygiene improvements")
            recommendations.append("Maintain consistent sleep schedule")

        # Social recommendations
        if assessment.social_engagement <= 4:
            recommendations.append("Gradually increase social interactions")
            recommendations.append("Consider support group participation")

        return recommendations

    def _check_for_crisis(self, assessment: MoodAssessment) -> Optional[Dict[str, Any]]:
        """Check for mental health crisis indicators"""
        crisis_indicators = []

        # Severe depression
        if assessment.depression_score >= 20:
            crisis_indicators.append("Severe depression")

        # Severe anxiety
        if assessment.anxiety_score >= 15:
            crisis_indicators.append("Severe anxiety")

        # Very low mood
        if assessment.overall_mood <= 2:
            crisis_indicators.append("Severe mood disturbance")

        # Hopelessness indicator (would be extracted from notes in real implementation)
        if "hopeless" in assessment.notes.lower() or "suicidal" in assessment.notes.lower():
            crisis_indicators.append("Potential suicidal ideation")

        if crisis_indicators:
            return {
                'timestamp': assessment.timestamp.isoformat(),
                'indicators': crisis_indicators,
                'severity': 'high',
                'recommendation': 'IMMEDIATE mental health evaluation recommended',
                'emergency_contacts': ['Crisis hotline', 'Mental health professional', 'Emergency services']
            }

        return None


class CognitiveFunctionMonitor:
    """
    Monitoring and assessment of cognitive function in epilepsy patients.

    Tracks cognitive domains affected by seizures and medications,
    providing early detection of cognitive decline.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.cognitive_history: List[CognitiveAssessment] = []
        self.baseline_function = {}
        self.decline_alerts = []

    def establish_baseline(self, assessment: CognitiveAssessment) -> None:
        """Establish baseline cognitive function"""
        self.baseline_function = {
            'timestamp': assessment.timestamp.isoformat(),
            'domain_scores': {domain.value: score for domain, score in assessment.domain_scores.items()},
            'overall_score': assessment.overall_cognitive_score
        }

    def record_assessment(self, assessment: CognitiveAssessment) -> Dict[str, Any]:
        """Record new cognitive assessment"""
        self.cognitive_history.append(assessment)

        analysis = {
            'timestamp': assessment.timestamp.isoformat(),
            'current_function': self._describe_current_function(assessment),
            'decline_analysis': self._analyze_decline(assessment),
            'medication_effects': self._assess_medication_effects(assessment),
            'functional_impact': self._analyze_functional_impact(assessment),
            'recommendations': self._generate_cognitive_recommendations(assessment)
        }

        return analysis

    def _describe_current_function(self, assessment: CognitiveAssessment) -> Dict[str, str]:
        """Describe current cognitive function level"""
        function_level = {}

        for domain, score in assessment.domain_scores.items():
            if score >= 80:
                function_level[domain.value] = 'normal'
            elif score >= 60:
                function_level[domain.value] = 'mild_impairment'
            elif score >= 40:
                function_level[domain.value] = 'moderate_impairment'
            else:
                function_level[domain.value] = 'severe_impairment'

        return function_level

    def _analyze_decline(self, assessment: CognitiveAssessment) -> Dict[str, Any]:
        """Analyze cognitive decline from baseline"""
        if not self.baseline_function:
            return {'status': 'no_baseline'}

        decline_analysis = {}
        baseline_scores = self.baseline_function.get('domain_scores', {})

        for domain, current_score in assessment.domain_scores.items():
            baseline_score = baseline_scores.get(domain.value, current_score)
            decline_percentage = ((baseline_score - current_score) / baseline_score) * 100 if baseline_score > 0 else 0

            if decline_percentage >= 20:
                severity = 'significant_decline'
            elif decline_percentage >= 10:
                severity = 'mild_decline'
            elif decline_percentage >= 5:
                severity = 'minimal_decline'
            else:
                severity = 'stable'

            decline_analysis[domain.value] = {
                'baseline': baseline_score,
                'current': current_score,
                'decline_percentage': decline_percentage,
                'severity': severity
            }

        return decline_analysis

    def _assess_medication_effects(self, assessment: CognitiveAssessment) -> List[str]:
        """Assess cognitive effects of medications"""
        effects = []

        for effect in assessment.medication_effects:
            effects.append(effect)

        # Add analysis of which medications might be causing which effects
        # (Would be more sophisticated in full implementation)

        return effects

    def _analyze_functional_impact(self, assessment: CognitiveAssessment) -> Dict[str, Any]:
        """Analyze functional impact of cognitive changes"""
        impact = {
            'daily_living': self._assess_daily_living_impact(assessment),
            'work_school': self._assess_work_impact(assessment),
            'social': self._assess_social_impact(assessment),
            'overall_functional_impact': assessment.functional_impact
        }

        return impact

    def _assess_daily_living_impact(self, assessment: CognitiveAssessment) -> str:
        """Assess impact on daily living"""
        if assessment.overall_cognitive_score >= 70:
            return 'minimal_impact'
        elif assessment.overall_cognitive_score >= 50:
            return 'moderate_impact'
        else:
            return 'significant_impact'

    def _assess_work_impact(self, assessment: CognitiveAssessment) -> str:
        """Assess impact on work/school functioning"""
        executive_score = assessment.domain_scores.get(CognitiveDomain.EXECUTIVE_FUNCTION, 0)
        attention_score = assessment.domain_scores.get(CognitiveDomain.ATTENTION, 0)

        if executive_score >= 70 and attention_score >= 70:
            return 'minimal_impact'
        elif executive_score >= 50 and attention_score >= 50:
            return 'moderate_impact'
        else:
            return 'significant_impact'

    def _assess_social_impact(self, assessment: CognitiveAssessment) -> str:
        """Assess impact on social functioning"""
        language_score = assessment.domain_scores.get(CognitiveDomain.LANGUAGE, 0)
        social_score = assessment.domain_scores.get(CognitiveDomain.ATTENTION, 0)

        if language_score >= 70 and social_score >= 70:
            return 'minimal_impact'
        elif language_score >= 50 and social_score >= 50:
            return 'moderate_impact'
        else:
            return 'significant_impact'

    def _generate_cognitive_recommendations(self, assessment: CognitiveAssessment) -> List[str]:
        """Generate cognitive health recommendations"""
        recommendations = []

        # Check for significant decline
        decline_analysis = self._analyze_decline(assessment)

        for domain, analysis in decline_analysis.items():
            if analysis.get('severity') == 'significant_decline':
                recommendations.append(f"Significant decline in {domain} - professional evaluation recommended")
            elif analysis.get('severity') == 'mild_decline':
                recommendations.append(f"Mild decline in {domain} - monitor closely")

        # Medication effects
        if assessment.medication_effects:
            recommendations.append("Review cognitive side effects of current medications")
            recommendations.append("Consider medication adjustment if cognitive burden is high")

        # Overall cognitive score
        if assessment.overall_cognitive_score < 60:
            recommendations.append("Comprehensive cognitive assessment recommended")
            recommendations.append("Consider cognitive rehabilitation strategies")

        return recommendations


class PsychiatricCareIntegrator:
    """
    Integration of psychiatric care with epilepsy management.

    Coordinates psychiatric medications, therapy, and crisis planning
    with seizure control strategies.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.psychiatric_history: List[PsychiatricIntegration] = []
        self.medication_interactions = []
        self.crisis_plan = None

    def record_psychiatric_status(self, integration: PsychiatricIntegration) -> Dict[str, Any]:
        """Record current psychiatric status and integration needs"""
        self.psychiatric_history.append(integration)

        analysis = {
            'timestamp': integration.timestamp.isoformat(),
            'medication_interactions': self._analyze_medication_interactions(integration),
            'therapy_needs': self._assess_therapy_needs(integration),
            'risk_assessment': self._assess_psychiatric_risks(integration),
            'coordination_recommendations': self._generate_coordination_recommendations(integration)
        }

        return analysis

    def _analyze_medication_interactions(self, integration: PsychiatricIntegration) -> List[Dict]:
        """Analyze interactions between psychiatric and epilepsy medications"""
        interactions = []

        # Check for known interactions
        # (This would be more sophisticated in full implementation)
        for psych_med in integration.psychiatric_medications:
            # Check for interactions with AEDs
            if 'antidepressant' in psych_med.get('type', '').lower():
                interactions.append({
                    'psychiatric_medication': psych_med.get('name'),
                    'potential_interactions': ['May lower seizure threshold', 'May interact with AEDs'],
                    'recommendations': ['Monitor seizure frequency', 'Consider drug levels']
                })

        return interactions

    def _assess_therapy_needs(self, integration: PsychiatricIntegration) -> List[str]:
        """Assess therapy and counseling needs"""
        needs = []

        if integration.psychiatric_diagnoses:
            needs.append("Consider ongoing psychotherapy")

        if any('depression' in d.lower() or 'anxiety' in d.lower()
               for d in integration.psychiatric_diagnoses):
            needs.append("CBT or similar evidence-based therapy recommended")

        if integration.risk_factors:
            needs.append("Address identified risk factors in therapy")

        return needs

    def _assess_psychiatric_risks(self, integration: PsychiatricIntegration) -> Dict[str, Any]:
        """Assess psychiatric risk factors"""
        risk_assessment = {
            'suicide_risk': self._assess_suicide_risk(integration),
            'crris_risk': self._assess_crisis_risk(integration),
            'decompensation_risk': self._assess_decompensation_risk(integration)
        }

        return risk_assessment

    def _assess_suicide_risk(self, integration: PsychiatricIntegration) -> str:
        """Assess suicide risk"""
        if 'suicidal_ideation' in [str(c).lower() for c in integration.crisis_history]:
            return 'high'
        elif any('depression' in d.lower() for d in integration.psychiatric_diagnoses):
            return 'moderate'
        else:
            return 'low'

    def _assess_crisis_risk(self, integration: PsychiatricIntegration) -> str:
        """Assess crisis risk"""
        recent_crises = [c for c in integration.crisis_history
                        if datetime.fromisoformat(c.get('timestamp', '')) > datetime.now() - timedelta(days=30)]

        if len(recent_crises) >= 2:
            return 'high'
        elif len(recent_crises) == 1:
            return 'moderate'
        else:
            return 'low'

    def _assess_decompensation_risk(self, integration: PsychiatricIntegration) -> str:
        """Assess psychiatric decompensation risk"""
        high_risk_factors = ['medication_nonadherence', 'substance_use', 'social_isolation']

        if any(rf in integration.risk_factors for rf in high_risk_factors):
            return 'high'
        elif integration.risk_factors:
            return 'moderate'
        else:
            return 'low'

    def _generate_coordination_recommendations(self, integration: PsychiatricIntegration) -> List[str]:
        """Generate recommendations for coordinated care"""
        recommendations = []

        if integration.psychiatric_medications:
            recommendations.append("Regular medication interaction monitoring")
            recommendations.append("Coordinate dose adjustments between neurologist and psychiatrist")

        if integration.psychiatric_diagnoses:
            recommendations.append("Integrated treatment planning for psychiatric and epilepsy conditions")

        if integration.risk_factors:
            recommendations.append("Address psychiatric risk factors proactively")

        recommendations.append("Ensure crisis plan addresses both psychiatric and seizure emergencies")

        return recommendations


class QualityOfLifeTracker:
    """
    Patient-centered quality of life tracking for epilepsy patients.

    Focuses on what matters most to patients: independence, relationships,
    work, and overall life satisfaction.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.qol_history: List[QualityOfLifeMetrics] = []
        self.improvement_targets = {}
        self.success_milestones = []

    def record_qol_assessment(self, metrics: QualityOfLifeMetrics) -> Dict[str, Any]:
        """Record quality of life assessment"""
        self.qol_history.append(metrics)

        analysis = {
            'timestamp': metrics.timestamp.isoformat(),
            'current_qol': self._describe_current_qol(metrics),
            'trend_analysis': self._analyze_qol_trends(metrics),
            'improvement_opportunities': self._identify_improvement_opportunities(metrics),
            'success_recognition': self._recognize_successes(metrics),
            'goal_recommendations': self._generate_goal_recommendations(metrics)
        }

        return analysis

    def _describe_current_qol(self, metrics: QualityOfLifeMetrics) -> Dict[str, str]:
        """Describe current quality of life status"""
        qol_description = {}

        if metrics.overall_qol >= 8:
            qol_description['overall'] = 'excellent'
        elif metrics.overall_qol >= 6:
            qol_description['overall'] = 'good'
        elif metrics.overall_qol >= 4:
            qol_description['overall'] = 'fair'
        else:
            qol_description['overall'] = 'poor'

        if metrics.seizure_freedom:
            qol_description['seizure_status'] = 'seizure_free'
        elif metrics.seizure_control_satisfaction >= 7:
            qol_description['seizure_status'] = 'good_control'
        else:
            qol_description['seizure_status'] = 'poor_control'

        return qol_description

    def _analyze_qol_trends(self, metrics: QualityOfLifeMetrics) -> Dict[str, str]:
        """Analyze quality of life trends"""
        if len(self.qol_history) < 3:
            return {'status': 'insufficient_data'}

        recent = self.qol_history[-4:]
        trends = {}

        # Analyze overall QOL trend
        overall_scores = [m.overall_qol for m in recent]
        trends['overall_qol'] = self._calculate_qol_trend(overall_scores)

        # Analyze specific domains
        trends['independence'] = self._calculate_qol_trend([m.independence_level for m in recent])
        trends['social'] = self._calculate_qol_trend([m.social_functioning for m in recent])
        trends['occupational'] = self._calculate_qol_trend([m.occupational_functioning for m in recent])

        return trends

    def _calculate_qol_trend(self, values: List[float]) -> str:
        """Calculate QOL trend direction"""
        if len(values) < 2:
            return 'stable'

        first_half_avg = sum(values[:len(values)//2]) / len(values[:len(values)//2])
        second_half_avg = sum(values[len(values)//2:]) / len(values[len(values)//2:])

        difference = second_half_avg - first_half_avg

        if difference > 1.0:
            return 'improving'
        elif difference < -1.0:
            return 'declining'
        else:
            return 'stable'

    def _identify_improvement_opportunities(self, metrics: QualityOfLifeMetrics) -> List[str]:
        """Identify areas for quality of life improvement"""
        opportunities = []

        if metrics.side_effect_burden >= 6:
            opportunities.append("Reduce medication side effects")

        if metrics.independence_level <= 5:
            opportunities.append("Increase independence and autonomy")

        if metrics.social_functioning <= 5:
            opportunities.append("Improve social relationships and support")

        if metrics.occupational_functioning <= 5:
            opportunities.append("Enhance work or school functioning")

        if metrics.life_satisfaction <= 5:
            opportunities.append("Increase overall life satisfaction")

        if metrics.future_outlook <= 5:
            opportunities.append("Improve optimism about future")

        return opportunities

    def _recognize_successes(self, metrics: QualityOfLifeMetrics) -> List[str]:
        """Recognize and celebrate successes"""
        successes = []

        if metrics.seizure_freedom:
            successes.append("Seizure freedom achieved - excellent!")

        if metrics.seizure_control_satisfaction >= 8:
            successes.append("Good seizure control satisfaction")

        if metrics.side_effect_burden <= 3:
            successes.append("Minimal side effect burden")

        if metrics.independence_level >= 8:
            successes.append("High level of independence maintained")

        if metrics.social_functioning >= 8:
            successes.append("Strong social functioning")

        if metrics.occupational_functioning >= 8:
            successes.append("Excellent work/school functioning")

        if metrics.overall_qol >= 8:
            successes.append("Excellent overall quality of life")

        return successes

    def _generate_goal_recommendations(self, metrics: QualityOfLifeMetrics) -> List[str]:
        """Generate personalized goal recommendations"""
        goals = []

        # Side effect goals
        if metrics.side_effect_burden >= 6:
            goals.append("Work with neurologist to optimize medication regimen")

        # Independence goals
        if metrics.independence_level <= 6:
            goals.append("Set incremental independence goals with support system")

        # Social goals
        if metrics.social_functioning <= 6:
            goals.append("Gradually increase social engagement and support network")

        # Occupational goals
        if metrics.occupational_functioning <= 6:
            goals.append("Develop workplace accommodations or school support plan")

        # Overall life satisfaction goals
        if metrics.life_satisfaction <= 6:
            goals.append("Identify and pursue activities that bring satisfaction and meaning")

        return goals


class EmotionalCognitiveIntegrator:
    """
    High-level integration of all emotional-cognitive health monitoring.

    Combines mood, cognitive, psychiatric, and quality of life monitoring
    into a comprehensive whole-person health assessment.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.mood_monitor = EmotionalHealthMonitor(patient_id)
        self.cognitive_monitor = CognitiveFunctionMonitor(patient_id)
        self.psychiatric_integrator = PsychiatricCareIntegrator(patient_id)
        self.qol_tracker = QualityOfLifeTracker(patient_id)

    def comprehensive_assessment(self) -> Dict[str, Any]:
        """Generate comprehensive emotional-cognitive health assessment"""
        return {
            'patient_id': self.patient_id,
            'assessment_date': datetime.now().isoformat(),
            'emotional_health': {
                'current_state': self._summarize_emotional_state(),
                'trends': self._summarize_emotional_trends(),
                'crisis_alerts': self.mood_monitor.crisis_alerts
            },
            'cognitive_function': {
                'current_function': self._summarize_cognitive_function(),
                'decline_analysis': self._summarize_cognitive_decline(),
                'medication_effects': self._summarize_cognitive_medication_effects()
            },
            'psychiatric_integration': {
                'medication_interactions': self._summarize_medication_interactions(),
                'therapy_needs': self._summarize_therapy_needs(),
                'risk_assessment': self._summarize_psychiatric_risks()
            },
            'quality_of_life': {
                'current_qol': self._summarize_qol_status(),
                'trends': self._summarize_qol_trends(),
                'improvement_opportunities': self._summarize_improvement_opportunities()
            },
            'recommendations': self._generate_integrated_recommendations()
        }

    def _summarize_emotional_state(self) -> Dict:
        """Summarize current emotional state"""
        if not self.mood_monitor.mood_history:
            return {'status': 'no_data'}

        latest = self.mood_monitor.mood_history[-1]
        return {
            'state': self.mood_monitor._determine_emotional_state(latest).value,
            'depression_score': latest.depression_score,
            'anxiety_score': latest.anxiety_score,
            'overall_mood': latest.overall_mood
        }

    def _summarize_emotional_trends(self) -> Dict:
        """Summarize emotional health trends"""
        return self.mood_monitor._analyze_trends()

    def _summarize_cognitive_function(self) -> Dict:
        """Summarize current cognitive function"""
        if not self.cognitive_monitor.cognitive_history:
            return {'status': 'no_data'}

        latest = self.cognitive_monitor.cognitive_history[-1]
        return self.cognitive_monitor._describe_current_function(latest)

    def _summarize_cognitive_decline(self) -> Dict:
        """Summarize cognitive decline analysis"""
        if not self.cognitive_monitor.cognitive_history:
            return {'status': 'no_data'}

        latest = self.cognitive_monitor.cognitive_history[-1]
        return self.cognitive_monitor._analyze_decline(latest)

    def _summarize_cognitive_medication_effects(self) -> List[str]:
        """Summarize cognitive medication effects"""
        if not self.cognitive_monitor.cognitive_history:
            return []

        latest = self.cognitive_monitor.cognitive_history[-1]
        return latest.medication_effects

    def _summarize_medication_interactions(self) -> List:
        """Summarize medication interactions"""
        if not self.psychiatric_integrator.psychiatric_history:
            return []

        latest = self.psychiatric_integrator.psychiatric_history[-1]
        return self.psychiatric_integrator._analyze_medication_interactions(latest)

    def _summarize_therapy_needs(self) -> List[str]:
        """Summarize therapy needs"""
        if not self.psychiatric_integrator.psychiatric_history:
            return []

        latest = self.psychiatric_integrator.psychiatric_history[-1]
        return self.psychiatric_integrator._assess_therapy_needs(latest)

    def _summarize_psychiatric_risks(self) -> Dict:
        """Summarize psychiatric risks"""
        if not self.psychiatric_integrator.psychiatric_history:
            return {'status': 'no_data'}

        latest = self.psychiatric_integrator.psychiatric_history[-1]
        return self.psychiatric_integrator._assess_psychiatric_risks(latest)

    def _summarize_qol_status(self) -> Dict:
        """Summarize current quality of life status"""
        if not self.qol_tracker.qol_history:
            return {'status': 'no_data'}

        latest = self.qol_tracker.qol_history[-1]
        return self.qol_tracker._describe_current_qol(latest)

    def _summarize_qol_trends(self) -> Dict:
        """Summarize quality of life trends"""
        if not self.qol_tracker.qol_history:
            return {'status': 'no_data'}

        latest = self.qol_tracker.qol_history[-1]
        return self.qol_tracker._analyze_qol_trends(latest)

    def _summarize_improvement_opportunities(self) -> List[str]:
        """Summarize improvement opportunities"""
        if not self.qol_tracker.qol_history:
            return []

        latest = self.qol_tracker.qol_history[-1]
        return self.qol_tracker._identify_improvement_opportunities(latest)

    def _generate_integrated_recommendations(self) -> List[str]:
        """Generate integrated recommendations across all domains"""
        recommendations = []

        # Emotional health recommendations
        if self.mood_monitor.mood_history:
            latest_mood = self.mood_monitor.mood_history[-1]
            emotional_recs = self.mood_monitor._generate_emotional_recommendations(latest_mood)
            recommendations.extend(emotional_recs[:3])  # Top 3

        # Cognitive recommendations
        if self.cognitive_monitor.cognitive_history:
            latest_cognitive = self.cognitive_monitor.cognitive_history[-1]
            cognitive_recs = self.cognitive_monitor._generate_cognitive_recommendations(latest_cognitive)
            recommendations.extend(cognitive_recs[:2])  # Top 2

        # QOL recommendations
        if self.qol_tracker.qol_history:
            latest_qol = self.qol_tracker.qol_history[-1]
            qol_recs = self.qol_tracker._generate_goal_recommendations(latest_qol)
            recommendations.extend(qol_recs[:2])  # Top 2

        return recommendations


# Convenience functions
def create_emotional_cognitive_system(patient_id: str) -> EmotionalCognitiveIntegrator:
    """Create comprehensive emotional-cognitive monitoring system"""
    return EmotionalCognitiveIntegrator(patient_id)
