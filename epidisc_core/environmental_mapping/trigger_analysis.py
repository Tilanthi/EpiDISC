"""
EPIDISC Environmental Trigger Mapping System
Identifies and maps environmental seizure triggers for personalized avoidance
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import json


class TriggerCategory(Enum):
    """Categories of environmental triggers"""
    WEATHER = "weather"
    AIR_QUALITY = "air_quality"
    LIGHT = "light"
    SOUND = "sound"
    CHEMICAL = "chemical"
    HORMONAL = "hormonal"
    STRESS = "stress"
    SLEEP = "sleep"
    DIETARY = "dietary"
    ACTIVITY = "activity"


@dataclass
class EnvironmentalTrigger:
    """Environmental trigger identification"""
    trigger_type: TriggerCategory
    trigger_name: str
    severity: float  # 0.0-1.0
    latency_minutes: int
    duration_hours: int
    confidence: float
    patterns: List[str]
    avoidance_strategies: List[str]


@dataclass
class TriggerMapping:
    """Personal trigger map for patient"""
    patient_id: str
    identified_triggers: List[EnvironmentalTrigger]
    trigger_combinations: List[List[str]]
    environmental_sensitivities: Dict[str, float]
    avoidance_plan: Dict[str, List[str]]


class EnvironmentalTriggerMapper:
    """
    Maps and analyzes environmental seizure triggers.

    Identifies personal trigger sensitivities and develops
    personalized avoidance strategies.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.trigger_map = None
        self.environmental_history = []
        self.sensitivities = {}

    def analyze_environmental_triggers(self, seizure_events: List[Dict],
                                       environmental_exposures: List[Dict]) -> TriggerMapping:
        """Analyze environmental triggers from seizure and exposure data"""
        identified_triggers = []
        trigger_combinations = []
        sensitivities = {}

        # Analyze each seizure event for environmental associations
        for seizure in seizure_events:
            seizure_time = datetime.fromisoformat(seizure.get('timestamp'))
            triggers = self._identify_precipitating_exposures(seizure_time, environmental_exposures)

            for trigger in triggers:
                existing = self._find_or_create_trigger(identified_triggers, trigger)
                existing.severity = max(existing.severity, trigger.get('severity', 0.5))

        # Identify trigger combinations
        trigger_combinations = self._identify_trigger_combinations(seizure_events, environmental_exposures)

        # Calculate sensitivities
        sensitivities = self._calculate_sensitivities(identified_triggers, environmental_exposures)

        # Generate avoidance plan
        avoidance_plan = self._generate_avoidance_plan(identified_triggers, sensitivities)

        self.trigger_map = TriggerMapping(
            patient_id=self.patient_id,
            identified_triggers=identified_triggers,
            trigger_combinations=trigger_combinations,
            environmental_sensitivities=sensitivities,
            avoidance_plan=avoidance_plan
        )

        return self.trigger_map

    def _identify_precipitating_exposures(self, seizure_time: datetime, exposures: List[Dict]) -> List[Dict]:
        """Identify environmental exposures preceding seizure"""
        precipitating = []

        # Look for exposures in 24-48 hours before seizure
        window_start = seizure_time - timedelta(hours=48)
        window_end = seizure_time

        for exposure in exposures:
            exposure_time = datetime.fromisoformat(exposure.get('timestamp'))

            if window_start <= exposure_time <= window_end:
                # Check if exposure meets trigger threshold
                if self._meets_trigger_threshold(exposure):
                    precipitating.append(exposure)

        return precipitating

    def _meets_trigger_threshold(self, exposure: Dict) -> bool:
        """Check if exposure meets trigger threshold"""
        # Different trigger types have different thresholds
        exposure_type = exposure.get('type')

        if exposure_type == 'weather':
            return exposure.get('weather_changing', False) or exposure.get('extreme_temp', False)
        elif exposure_type == 'air_quality':
            return exposure.get('aqi', 50) > 100  # AQI > 100
        elif exposure_type == 'light':
            return exposure.get('flourescent_exposure', False) or exposure.get('strobe_light', False)
        elif exposure_type == 'sound':
            return exposure.get('loud_noise', False) or exposure.get('sudden_noise', False)
        elif exposure_type == 'chemical':
            return exposure.get('chemical_exposure', False)
        else:
            return False

    def _find_or_create_trigger(self, triggers: List, trigger_data: Dict) -> EnvironmentalTrigger:
        """Find existing trigger or create new one"""
        trigger_type = TriggerCategory(trigger_data.get('type', 'stress'))

        for trigger in triggers:
            if trigger.trigger_type == trigger_type:
                return trigger

        # Create new trigger
        new_trigger = EnvironmentalTrigger(
            trigger_type=trigger_type,
            trigger_name=trigger_data.get('name'),
            severity=trigger_data.get('severity', 0.5),
            latency_minutes=trigger_data.get('latency', 0),
            duration_hours=trigger_data.get('duration', 24),
            confidence=0.5,
            patterns=[],
            avoidance_strategies=[]
        )

        triggers.append(new_trigger)
        return new_trigger

    def _identify_trigger_combinations(self, seizures: List[Dict], exposures: List[Dict]) -> List[List[str]]:
        """Identify combinations of triggers that lead to seizures"""
        combinations = []

        # Analyze for multi-trigger patterns
        for seizure in seizures:
            precipitating = self._identify_precipitating_exposures(
                datetime.fromisoformat(seizure.get('timestamp')),
                exposures
            )

            if len(precipitating) >= 2:
                combination = [p.get('type', 'unknown') for p in precipitating]
                if combination not in combinations:
                    combinations.append(combination)

        return combinations

    def _calculate_sensitivities(self, triggers: List[EnvironmentalTrigger], exposures: List[Dict]) -> Dict[str, float]:
        """Calculate environmental sensitivities"""
        sensitivities = {}

        for trigger in triggers:
            # Calculate sensitivity score based on trigger frequency and severity
            sensitivity_score = trigger.severity * trigger.confidence
            sensitivities[trigger.trigger_type.value] = sensitivity_score

        return sensitivities

    def _generate_avoidance_plan(self, triggers: List[EnvironmentalTrigger], sensitivities: Dict) -> Dict[str, List[str]]:
        """Generate personalized avoidance plan"""
        avoidance_plan = {}

        for trigger in triggers:
            strategies = self._generate_trigger_avoidance_strategies(trigger)
            avoidance_plan[trigger.trigger_name] = strategies

        return avoidance_plan

    def _generate_trigger_avoidance_strategies(self, trigger: EnvironmentalTrigger) -> List[str]:
        """Generate avoidance strategies for specific trigger"""
        strategies = []

        if trigger.trigger_type == TriggerCategory.WEATHER:
            strategies.extend([
                "Monitor weather forecasts",
                "Stay indoors during extreme weather",
                "Maintain stable indoor environment"
            ])
        elif trigger.trigger_type == TriggerCategory.AIR_QUALITY:
            strategies.extend([
                "Check air quality index daily",
                "Limit outdoor activities on poor air quality days",
                "Use air purifier indoors"
            ])
        elif trigger.trigger_type == TriggerCategory.LIGHT:
            strategies.extend([
                "Avoid fluorescent lights when possible",
                "Use natural light or warm LED lighting",
                "Wear sunglasses indoors if needed"
            ])
        elif trigger.trigger_type == TriggerCategory.SOUND:
            strategies.extend([
                "Use earplugs in noisy environments",
                "Avoid sudden loud noises",
                "Noise-canceling headphones"
            ])
        elif trigger.trigger_type == TriggerCategory.STRESS:
            strategies.extend([
                "Practice regular stress reduction",
                "Identify and avoid stressful situations",
                "Use relaxation techniques"
            ])
        elif trigger.trigger_type == TriggerCategory.SLEEP:
            strategies.extend([
                "Maintain consistent sleep schedule",
                "Prioritize adequate sleep duration",
                "Practice good sleep hygiene"
            ])

        return strategies


class LifestylePatternAnalyzer:
    """
    Analyzes lifestyle patterns and their relationship to seizures.

    Identifies patterns in sleep, exercise, diet, and substance use.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.sleep_patterns = {}
        self.exercise_patterns = {}
        self.dietary_patterns = {}
        self.substance_use_patterns = {}

    def analyze_sleep_patterns(self, sleep_data: List[Dict], seizures: List[Dict]) -> Dict[str, Any]:
        """Analyze sleep patterns and seizure relationship"""
        analysis = {
            'average_sleep_duration': 0,
            'sleep_variability': 0,
            'sleep_quality_trends': [],
            'seizure_correlation': {},
            'recommendations': []
        }

        if not sleep_data:
            return analysis

        # Calculate average sleep duration
        durations = [s.get('duration_hours', 0) for s in sleep_data]
        analysis['average_sleep_duration'] = sum(durations) / len(durations) if durations else 0

        # Calculate variability
        if len(durations) > 1:
            avg = analysis['average_sleep_duration']
            variance = sum((d - avg) ** 2 for d in durations) / len(durations)
            analysis['sleep_variability'] = variance ** 0.5

        # Analyze seizure correlation
        analysis['seizure_correlation'] = self._correlate_sleep_with_seizures(sleep_data, seizures)

        # Generate recommendations
        analysis['recommendations'] = self._generate_sleep_recommendations(analysis)

        return analysis

    def _correlate_sleep_with_seizures(self, sleep_data: List[Dict], seizures: List[Dict]) -> Dict:
        """Correlate sleep patterns with seizure occurrence"""
        correlation = {}

        # Check for sleep deprivation correlation
        sleep_deprivation_seizures = 0
        total_seizures = len(seizures)

        for seizure in seizures:
            seizure_time = datetime.fromisoformat(seizure.get('timestamp'))
            preceding_sleep = self._get_preceding_sleep(seizure_time, sleep_data)

            if preceding_sleep and preceding_sleep.get('duration_hours', 7) < 6:
                sleep_deprivation_seizures += 1

        if total_seizures > 0:
            correlation['sleep_deprivation_correlation'] = sleep_deprivation_seizures / total_seizures

        return correlation

    def _get_preceding_sleep(self, seizure_time: datetime, sleep_data: List[Dict]) -> Optional[Dict]:
        """Get sleep episode preceding seizure"""
        for sleep in reversed(sleep_data):
            sleep_time = datetime.fromisoformat(sleep.get('timestamp'))
            if sleep_time < seizure_time - timedelta(hours=12):  # Within 12 hours
                return sleep
        return None

    def _generate_sleep_recommendations(self, analysis: Dict) -> List[str]:
        """Generate sleep-related recommendations"""
        recommendations = []

        if analysis['average_sleep_duration'] < 7:
            recommendations.append("Aim for 7-9 hours of sleep per night")

        if analysis['sleep_variability'] > 2:
            recommendations.append("Maintain consistent sleep schedule")

        if analysis['seizure_correlation'].get('sleep_deprivation_correlation', 0) > 0.3:
            recommendations.append("HIGH PRIORITY: Avoid sleep deprivation")

        recommendations.append("Practice good sleep hygiene")
        recommendations.append("Avoid screens 1 hour before bed")

        return recommendations


class WorkplaceAssessment:
    """
    Assesses workplace environment for seizure triggers.

    Evaluates work environment factors and recommends accommodations.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.workplace_factors = {}

    def assess_workplace_triggers(self, workplace_data: Dict) -> Dict[str, Any]:
        """Assess workplace environmental factors"""
        assessment = {
            'identified_triggers': [],
            'safety_considerations': [],
            'accommodations_needed': [],
            'recommendations': []
        }

        # Assess common workplace triggers
        if workplace_data.get('fluorescent_lighting', False):
            assessment['identified_triggers'].append("Fluorescent lighting")
            assessment['accommodations_needed'].append("Natural light or desk lamp")

        if workplace_data.get('computer_screens', True):
            assessment['identified_triggers'].append("Extended screen time")
            assessment['accommodations_needed'].append("Regular screen breaks")

        if workplace_data.get('high_stress_environment', False):
            assessment['identified_triggers'].append("Work stress")
            assessment['accommodations_needed'].append("Stress management breaks")

        if workplace_data.get('shift_work', False):
            assessment['identified_triggers'].append("Shift work/irregular hours")
            assessment['accommodations_needed'].append("Schedule consistency")

        # Safety considerations
        assessment['safety_considerations'].extend([
            "Emergency response plan at workplace",
            "Inform coworkers about seizure first aid",
            "Safe work environment assessment"
        ])

        return assessment


class TriggerMitigationSpecialist:
    """
    Specialist in trigger mitigation and avoidance planning.

    Creates personalized trigger avoidance strategies.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.mitigation_plans = {}

    def create_comprehensive_mitigation_plan(self, trigger_map: TriggerMapping) -> Dict[str, Any]:
        """Create comprehensive trigger mitigation plan"""
        plan = {
            'primary_triggers': [t.trigger_name for t in trigger_map.identified_triggers if t.severity > 0.6],
            'secondary_triggers': [t.trigger_name for t in trigger_map.identified_triggers if 0.3 < t.severity <= 0.6],
            'trigger_combinations': trigger_map.trigger_combinations,
            'sensitivities': trigger_map.environmental_sensitivities,
            'mitigation_strategies': trigger_map.avoidance_plan,
            'monitoring_recommendations': self._generate_monitoring_recommendations(trigger_map),
            'emergency_preparedness': self._generate_emergency_preparedness(trigger_map)
        }

        self.mitigation_plans[self.patient_id] = plan
        return plan

    def _generate_monitoring_recommendations(self, trigger_map: TriggerMapping) -> List[str]:
        """Generate trigger monitoring recommendations"""
        recommendations = []

        if any(t.trigger_type == TriggerCategory.WEATHER for t in trigger_map.identified_triggers):
            recommendations.append("Monitor weather forecasts regularly")

        if any(t.trigger_type == TriggerCategory.AIR_QUALITY for t in trigger_map.identified_triggers):
            recommendations.append("Check air quality daily")

        if any(t.trigger_type == TriggerCategory.STRESS for t in trigger_map.identified_triggers):
            recommendations.append("Monitor stress levels daily")

        recommendations.append("Track trigger exposures in diary")
        recommendations.append("Review trigger patterns monthly")

        return recommendations

    def _generate_emergency_preparedness(self, trigger_map: TriggerMapping) -> List[str]:
        """Generate emergency preparedness recommendations"""
        preparedness = [
            "Carry emergency seizure information",
            "Have rescue medication available",
            "Inform close contacts about triggers"
        ]

        # Add trigger-specific preparedness
        for trigger in trigger_map.identified_triggers:
            if trigger.severity > 0.7:
                preparedness.append(f"Extra precaution for {trigger.trigger_name}")

        return preparedness


class EnvironmentalTriggerIntegrator:
    """
    Main integrator for environmental trigger mapping and mitigation.

    Combines trigger identification, pattern analysis, and mitigation
    planning into comprehensive trigger management.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.trigger_mapper = EnvironmentalTriggerMapper(patient_id)
        self.pattern_analyzer = LifestylePatternAnalyzer(patient_id)
        self.workplace_assessor = WorkplaceAssessment(patient_id)
        self.mitigation_specialist = TriggerMitigationSpecialist(patient_id)

    def comprehensive_trigger_analysis(self, seizure_events: List[Dict],
                                     environmental_exposures: List[Dict],
                                     lifestyle_data: Dict,
                                     workplace_data: Dict) -> Dict[str, Any]:
        """Comprehensive environmental trigger analysis"""

        # Map triggers
        trigger_map = self.trigger_mapper.analyze_environmental_triggers(
            seizure_events, environmental_exposures
        )

        # Analyze lifestyle patterns
        sleep_analysis = self.pattern_analyzer.analyze_sleep_patterns(
            lifestyle_data.get('sleep_data', []), seizure_events
        )

        # Assess workplace
        workplace_assessment = self.workplace_assessor.assess_workplace_triggers(workplace_data)

        # Create mitigation plan
        mitigation_plan = self.mitigation_specialist.create_comprehensive_mitigation_plan(trigger_map)

        return {
            'patient_id': self.patient_id,
            'analysis_date': datetime.now().isoformat(),
            'identified_triggers': [
                {
                    'type': t.trigger_type.value,
                    'name': t.trigger_name,
                    'severity': t.severity,
                    'latency': f"{t.latency_minutes} minutes",
                    'confidence': t.confidence
                }
                for t in trigger_map.identified_triggers
            ],
            'trigger_combinations': trigger_map.trigger_combinations,
            'environmental_sensitivities': trigger_map.environmental_sensitivities,
            'lifestyle_patterns': {
                'sleep_analysis': sleep_analysis
            },
            'workplace_assessment': workplace_assessment,
            'mitigation_strategies': mitigation_plan,
            'overall_recommendations': self._generate_integrated_recommendations(trigger_map, workplace_assessment)
        }

    def _generate_integrated_recommendations(self, trigger_map: TriggerMapping, workplace: Dict) -> List[str]:
        """Generate integrated recommendations"""
        recommendations = []

        # Primary trigger recommendations
        high_severity_triggers = [t for t in trigger_map.identified_triggers if t.severity > 0.6]
        if high_severity_triggers:
            recommendations.append(f"Focus on avoiding: {', '.join(t.trigger_name for t in high_severity_triggers)}")

        # Workplace recommendations
        if workplace.get('accommodations_needed'):
            recommendations.append("Request workplace accommodations for trigger avoidance")

        # Overall recommendations
        recommendations.append("Use trigger diary app to track exposures")
        recommendations.append("Review trigger patterns monthly")
        recommendations.append("Adjust mitigation strategies as needed")

        return recommendations


# Convenience function
def create_environmental_trigger_system(patient_id: str) -> EnvironmentalTriggerIntegrator:
    """Create comprehensive environmental trigger mapping system"""
    return EnvironmentalTriggerIntegrator(patient_id)
