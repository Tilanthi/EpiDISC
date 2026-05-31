"""
EPIDISC Therapeutic Optimization Engine
Dynamic treatment optimization based on continuous monitoring and real-world outcomes
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import json
from collections import defaultdict


class TreatmentStatus(Enum):
    """Treatment status categories"""
    EXCELLENT = "excellent"  # Seizure-free, minimal side effects
    GOOD = "good"  # Significant seizure reduction, manageable side effects
    FAIR = "fair"  # Some seizure reduction, tolerable side effects
    POOR = "poor"  # Minimal seizure reduction or significant side effects
    TREATMENT_FAILURE = "treatment_failure"  # No improvement or intolerable


@dataclass
class TreatmentOutcome:
    """Detailed treatment outcome assessment"""
    medication: str
    start_date: datetime
    assessment_date: datetime
    seizure_reduction_percent: float  # 0-100
    seizure_frequency_reduction: float
    side_effects: List[str]
    side_effect_severity: float  # 0-10 scale
    quality_of_life_impact: float  # -10 to +10
    patient_satisfaction: float  # 1-10 scale
    overall_status: TreatmentStatus
    continuing_treatment: bool
    reasons: List[str]


@dataclass
class DoseOptimization:
    """Dose optimization recommendation"""
    medication: str
    current_dose: float
    recommended_dose: float
    rationale: str
    expected_improvement: str
    monitoring_needs: List[str]
    timeline: str


@dataclass
class CombinationTherapy:
    """Rational combination therapy plan"""
    primary_medication: str
    secondary_medication: str
    primary_dose: float
    secondary_dose: float
    rationale: str
    expected_synergy: str
    monitoring_requirements: List[str]
    potential_interactions: List[str]


class RealWorldEffectivenessTracker:
    """
    Tracks real-world treatment effectiveness and outcomes.

    Aggregates patient-reported outcomes to inform treatment decisions.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.treatment_history = []
        self.outcome_database = {}
        self.effectiveness_metrics = {}

    def record_treatment_outcome(self, outcome: TreatmentOutcome) -> Dict[str, Any]:
        """Record comprehensive treatment outcome"""
        self.treatment_history.append(outcome)

        analysis = {
            'timestamp': datetime.now().isoformat(),
            'medication': outcome.medication,
            'treatment_duration_days': (outcome.assessment_date - outcome.start_date).days,
            'seizure_reduction': outcome.seizure_reduction_percent,
            'side_effects': outcome.side_effects,
            'overall_status': outcome.overall_status.value,
            'should_continue': outcome.continuing_treatment,
            'optimization_recommendations': self._generate_optimization_recommendations(outcome)
        }

        return analysis

    def _generate_optimization_recommendations(self, outcome: TreatmentOutcome) -> List[str]:
        """Generate treatment optimization recommendations"""
        recommendations = []

        # Check treatment status
        if outcome.overall_status == TreatmentStatus.TREATMENT_FAILURE:
            recommendations.extend([
                "Consider discontinuation",
                "Evaluate alternative medications",
                "Reconsider diagnosis"
            ])

        elif outcome.overall_status == TreatmentStatus.POOR:
            recommendations.extend([
                "Consider dose optimization",
                "Evaluate for side effects",
                "Consider alternative medications"
            ])

        elif outcome.overall_status == TreatmentStatus.FAIR:
            recommendations.extend([
                "Consider dose adjustment",
                "Evaluate side effect management",
                "Monitor closely for improvement"
            ])

        # Side effect management
        if outcome.side_effect_severity >= 7:
            recommendations.append("Address significant side effects - dose reduction or change")

        # Patient satisfaction
        if outcome.patient_satisfaction <= 4:
            recommendations.append("Address patient concerns about treatment")

        return recommendations

    def get_treatment_summary(self) -> Dict[str, Any]:
        """Get summary of all treatments"""
        if not self.treatment_history:
            return {'status': 'no_treatments_recorded'}

        summary = {
            'total_treatments': len(self.treatment_history),
            'current_treatments': [t.medication for t in self.treatment_history if t.continuing_treatment],
            'successful_treatments': [t.medication for t in self.treatment_history if t.overall_status in [TreatmentStatus.EXCELLENT, TreatmentStatus.GOOD]],
            'failed_treatments': [t.medication for t in self.treatment_history if t.overall_status == TreatmentStatus.TREATMENT_FAILURE]
        }

        return summary


class DoseOptimizationEngine:
    """
    Algorithmic dose optimization based on response and side effects.

    Uses patient-specific data to optimize medication dosing.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.optimization_algorithms = {}
        self.dose_response_curves = {}

    def optimize_dose(self, medication: str, current_dose: float,
                    response_data: Dict, side_effect_data: Dict) -> DoseOptimization:
        """Optimize medication dose based on response and side effects"""
        recommended_dose = current_dose
        rationale = ""
        expected_improvement = ""
        monitoring_needs = []

        # Calculate seizure response
        seizure_reduction = response_data.get('seizure_reduction_percent', 0)

        # Assess side effect burden
        side_effect_burden = side_effect_data.get('overall_burden', 0)

        # Optimization logic
        if seizure_reduction >= 70 and side_effect_burden <= 3:
            # Good response, minimal side effects - maintain
            rationale = "Excellent response with minimal side effects"
            recommended_dose = current_dose
            expected_improvement = "Maintain current control"

        elif seizure_reduction >= 70 and side_effect_burden > 6:
            # Good response but significant side effects
            rationale = "Good response but significant side effects - consider dose reduction"
            recommended_dose = current_dose * 0.8  # Reduce by 20%
            expected_improvement = "Maintain seizure control while reducing side effects"
            monitoring_needs.extend(["Monitor for seizure breakthrough", "Track side effect improvement"])

        elif 30 <= seizure_reduction < 70 and side_effect_burden <= 3:
            # Moderate response, minimal side effects - consider increase
            rationale = "Moderate response with room for improvement"
            recommended_dose = current_dose * 1.2  # Increase by 20%
            expected_improvement = "Improved seizure control"
            monitoring_needs.extend(["Monitor for increased side effects", "Therapeutic drug monitoring if applicable"])

        elif seizure_reduction < 30 and side_effect_burden <= 3:
            # Poor response, minimal side effects - significant increase or change
            rationale = "Poor response despite adequate trial - consider significant dose increase or medication change"
            recommended_dose = current_dose * 1.5  # Increase by 50%
            expected_improvement = "Potential for improved seizure control"
            monitoring_needs.extend(["Close monitoring for side effects", "Consider therapeutic drug monitoring"])

        else:
            # Poor response with significant side effects - change medication
            rationale = "Poor response with significant side effects - recommend medication change"
            recommended_dose = current_dose  # No change since recommending switch
            expected_improvement = "Better response with different medication"
            monitoring_needs.append("Plan transition to alternative medication")

        optimization = DoseOptimization(
            medication=medication,
            current_dose=current_dose,
            recommended_dose=recommended_dose,
            rationale=rationale,
            expected_improvement=expected_improvement,
            monitoring_needs=monitoring_needs,
            timeline="Reassess in 4-8 weeks"
        )

        return optimization


class CombinationTherapyPlanner:
    """
    Rational combination therapy planning.

    Designs evidence-based polytherapy combinations for
    treatment-resistant epilepsy.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.evidence_base = self._initialize_combination_evidence()

    def design_combination_therapy(self, failed_meds: List[str],
                                     current_meds: List[str],
                                     patient_factors: Dict) -> CombinationTherapy:
        """Design rational combination therapy"""
        # Select combination based on evidence
        combination = self._select_evidence_based_combination(failed_meds, current_meds, patient_factors)

        therapy = CombinationTherapy(
            primary_medication=combination['primary'],
            secondary_medication=combination['secondary'],
            primary_dose=combination['primary_dose'],
            secondary_dose=combination['secondary_dose'],
            rationale=combination['rationale'],
            expected_synergy=combination['synergy'],
            monitoring_requirements=combination['monitoring'],
            potential_interactions=combination['interactions']
        )

        return therapy

    def _select_evidence_based_combination(self, failed_meds: List[str],
                                         current_meds: List[str],
                                         patient_factors: Dict) -> Dict:
        """Select evidence-based combination"""
        # Evidence-based combinations
        combinations = {
            'levetiracetam_lamotrigine': {
                'primary': 'levetiracetam',
                'secondary': 'lamotrigine',
                'primary_dose': 1000,
                'secondary_dose': 200,
                'rationale': 'Complementary mechanisms - SV2A and sodium channel',
                'synergy': 'Broad-spectrum coverage',
                'monitoring': ['Seizure frequency', 'Mood monitoring', 'Skin rash'],
                'interactions': ['Minimal pharmacokinetic interaction']
            },
            'levetiracetam_valproate': {
                'primary': 'levetiracetam',
                'secondary': 'valproate',
                'primary_dose': 1000,
                'secondary_dose': 1000,
                'rationale': 'Dual mechanisms - SV2A and histone deacetylase inhibition',
                'synergy': 'Effective for generalized and focal seizures',
                'monitoring': ['Liver function', 'Platelet count', 'Drug levels'],
                'interactions': ['Minimal interaction']
            },
            'lamotrigine_valproate': {
                'primary': 'lamotrigine',
                'secondary': 'valproate',
                'primary_dose': 200,
                'secondary_dose': 1000,
                'rationale': 'Multiple mechanisms - sodium channel and GABA enhancement',
                'synergy': 'Valproate inhibits lamotrigine metabolism - adjust doses',
                'monitoring': ['Skin rash', 'Lamotrigine levels', 'Liver function'],
                'interactions': ['Valproate doubles lamotrigine levels - slow titration essential']
            }
        }

        # Select appropriate combination
        if patient_factors.get('seizure_type') == 'generalized':
            return combinations['levetiracetam_valproate']
        elif patient_factors.get('gender') == 'female' and patient_factors.get('childbearing_age', False):
            return combinations['levetiracetam_lamotrigine']  # Avoid valproate
        else:
            return combinations['levetiracetam_lamotrigine']

    def _initialize_combination_evidence(self) -> Dict:
        """Initialize evidence base for combination therapy"""
        return {
            'synergistic_mechanisms': [
                'SV2A + Sodium channel',
                'SV2A + GABA enhancement',
                'Multiple sodium channels',
                'Calcium channel + GABA'
            ],
            'effective_combinations': [
                'Levetiracetam + Lamotrigine',
                'Levetiracetam + Valproate',
                'Lamotrigine + Valproate',
                'Carbamazepine + Lamotrigine'
            ]
        }


class TreatmentOptimizationEngine:
    """
    Main engine for dynamic treatment optimization.

    Integrates real-world effectiveness tracking, dose optimization,
    and combination therapy planning for personalized treatment.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.effectiveness_tracker = RealWorldEffectivenessTracker(patient_id)
        self.dose_optimizer = DoseOptimizationEngine(patient_id)
        self.combination_planner = CombinationTherapyPlanner(patient_id)
        self.optimization_history = []

    def comprehensive_optimization(self, patient_data: Dict,
                                 treatment_history: List[Dict]) -> Dict[str, Any]:
        """Comprehensive treatment optimization analysis"""

        # Analyze current treatment effectiveness
        effectiveness_analysis = {}
        for treatment in treatment_history:
            outcome = TreatmentOutcome(
                medication=treatment.get('medication'),
                start_date=datetime.fromisoformat(treatment.get('start_date')),
                assessment_date=datetime.fromisoformat(treatment.get('assessment_date')),
                seizure_reduction_percent=treatment.get('seizure_reduction', 0),
                seizure_frequency_reduction=treatment.get('frequency_reduction', 0),
                side_effects=treatment.get('side_effects', []),
                side_effect_severity=treatment.get('side_effect_severity', 0),
                quality_of_life_impact=treatment.get('qol_impact', 0),
                patient_satisfaction=treatment.get('satisfaction', 5),
                overall_status=TreatmentStatus(treatment.get('status', 'fair')),
                continuing_treatment=treatment.get('continuing', True),
                reasons=[]
            )

            analysis = self.effectiveness_tracker.record_treatment_outcome(outcome)
            effectiveness_analysis[treatment.get('medication')] = analysis

        # Generate dose optimization recommendations
        dose_recommendations = []
        for treatment in treatment_history:
            if treatment.get('continuing', True):
                optimization = self.dose_optimizer.optimize_dose(
                    treatment.get('medication'),
                    treatment.get('current_dose', 0),
                    treatment.get('response_data', {}),
                    treatment.get('side_effect_data', {})
                )
                dose_recommendations.append({
                    'medication': optimization.medication,
                    'current_dose': optimization.current_dose,
                    'recommended_dose': optimization.recommended_dose,
                    'rationale': optimization.rationale,
                    'monitoring': optimization.monitoring_needs
                })

        # Check for combination therapy needs
        combination_recommendation = None
        if patient_data.get('treatment_resistant', False):
            failed_meds = patient_data.get('failed_medications', [])
            current_meds = patient_data.get('current_medications', [])

            if len(failed_meds) >= 2 and len(current_meds) == 1:
                combination = self.combination_planner.design_combination_therapy(
                    failed_meds, current_meds, patient_data
                )
                combination_recommendation = {
                    'primary': combination.primary_medication,
                    'secondary': combination.secondary_medication,
                    'primary_dose': combination.primary_dose,
                    'secondary_dose': combination.secondary_dose,
                    'rationale': combination.rationale,
                    'monitoring': combination.monitoring_requirements,
                    'interactions': combination.potential_interactions
                }

        # Generate overall optimization plan
        optimization_plan = {
            'continue_current': [],
            'dose_changes': dose_recommendations,
            'medication_changes': [],
            'add_combination': combination_recommendation,
            'monitoring_priorities': [],
            'timeline': 'Reassess in 8-12 weeks'
        }

        # Categorize recommendations
        for analysis in effectiveness_analysis.values():
            if analysis.get('should_continue'):
                optimization_plan['continue_current'].append(analysis['medication'])
            else:
                optimization_plan['medication_changes'].append({
                    'medication': analysis['medication'],
                    'reason': analysis.get('optimization_recommendations', []),
                    'next_steps': self._generate_next_steps_for_change(analysis)
                })

        # Add monitoring priorities
        optimization_plan['monitoring_priorities'] = [
            'Seizure frequency monitoring',
            'Side effect tracking',
            'Medication adherence',
            'Quality of life assessment'
        ]

        return {
            'patient_id': self.patient_id,
            'optimization_date': datetime.now().isoformat(),
            'effectiveness_analysis': effectiveness_analysis,
            'optimization_plan': optimization_plan,
            'expected_outcomes': self._generate_expected_outcomes(optimization_plan),
            'recommendations': self._generate_integrated_recommendations(optimization_plan)
        }

    def _generate_next_steps_for_change(self, analysis: Dict) -> List[str]:
        """Generate next steps for medication change"""
        steps = []

        if not analysis.get('should_continue'):
            steps.append("Plan gradual transition to alternative medication")
            steps.append("Discuss change with neurologist")
            steps.append("Consider tapering schedule")

        return steps

    def _generate_expected_outcomes(self, plan: Dict) -> List[str]:
        """Generate expected outcomes from optimization plan"""
        outcomes = []

        if plan['dose_changes']:
            outcomes.append("Improved seizure control with dose optimization")

        if plan['add_combination']:
            outcomes.append("Enhanced seizure control from synergistic combination")

        outcomes.append("Better side effect profile")
        outcomes.append("Improved quality of life")

        return outcomes

    def _generate_integrated_recommendations(self, plan: Dict) -> List[str]:
        """Generate integrated treatment recommendations"""
        recommendations = []

        if plan['medication_changes']:
            recommendations.append("Review medication alternatives with neurologist")

        if plan['dose_changes']:
            recommendations.append("Implement dose adjustments with monitoring")

        if plan['add_combination']:
            recommendations.append("Consider rational combination therapy for enhanced control")

        recommendations.append("Schedule follow-up in 8-12 weeks")
        recommendations.append("Continue seizure diary throughout transition")

        return recommendations


# Convenience functions
def create_therapeutic_optimization_system(patient_id: str) -> TreatmentOptimizationEngine:
    """Create comprehensive therapeutic optimization system"""
    return TreatmentOptimizationEngine(patient_id)
