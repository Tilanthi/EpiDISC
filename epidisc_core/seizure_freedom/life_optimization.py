"""
EPIDISC Seizure Freedom Ecosystem
Comprehensive life management for epilepsy patients beyond seizure control
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import json


@dataclass
class SUDEPRiskAssessment:
    """SUDEP risk assessment"""
    overall_risk: str  # low, moderate, high
    risk_factors: List[str]
    protective_factors: List[str]
    mitigation_strategies: List[str]
    night_monitoring_needs: str
    emergency_preparedness: List[str]


@dataclass
class DrivingAssessment:
    """Driving capability assessment"""
    can_drive: bool
    state_requirements: Dict
    seizure_free_requirement: Dict
    recommended_restrictions: List[str]
    reevaluation_timeline: str
    alternative_transportation: List[str]


@dataclass
class ReproductivePlan:
    """Reproductive health planning"""
    pre_conception_optimization: List[str]
    medication_adjustments: Dict
    pregnancy_risk_assessment: Dict
    breastfeeding_guidance: Dict
    genetic_counseling_needs: List[str]
    pregnancy_monitoring: List[str]


@dataclass
class LifeCoursePlan:
    """Life course planning for epilepsy"""
    school_accommodations: List[str]
    work_considerations: List[str]
    independent_living_assessment: Dict
    long_term_care_needs: List[str]
    transition_points: List[Dict]


class SUDEPPreventionSpecialist:
    """
    SUDEP (Sudden Unexpected Death in Epilepsy) prevention specialist.

    Provides comprehensive risk assessment and mitigation strategies.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.risk_assessments = []
        self.prevention_plans = {}

    def comprehensive_risk_assessment(self, patient_data: Dict) -> SUDEPRiskAssessment:
        """Comprehensive SUDEP risk assessment"""
        risk_factors = self._identify_risk_factors(patient_data)
        protective_factors = self._identify_protective_factors(patient_data)

        overall_risk = self._calculate_overall_risk(risk_factors, protective_factors)
        mitigation_strategies = self._generate_mitigation_strategies(risk_factors, overall_risk)
        night_monitoring = self._assess_night_monitoring_needs(risk_factors)
        emergency_preparedness = self._generate_emergency_preparedness(overall_risk)

        assessment = SUDEPRiskAssessment(
            overall_risk=overall_risk,
            risk_factors=risk_factors,
            protective_factors=protective_factors,
            mitigation_strategies=mitigation_strategies,
            night_monitoring_needs=night_monitoring,
            emergency_preparedness=emergency_preparedness
        )

        self.risk_assessments.append(assessment)
        return assessment

    def _identify_risk_factors(self, patient_data: Dict) -> List[str]:
        """Identify SUDEP risk factors"""
        factors = []

        if patient_data.get('generalized_tonic_clonic', False):
            factors.append("Generalized tonic-clonic seizures")

        if patient_data.get('nocturnal_seizures', False):
            factors.append("Nocturnal seizures")

        if patient_data.get('seizure_frequency', 0) >= 3:
            factors.append("High seizure frequency (3+/month)")

        if not patient_data.get('seizure_free', False):
            factors.append("Not seizure-free")

        if patient_data.get('medication_adherence', 1.0) < 0.8:
            factors.append("Poor medication adherence")

        if patient_data.get('aeds_count', 0) >= 3:
            factors.append("Polytherapy (3+ AEDs)")

        if patient_data.get('early_onset', False):
            factors.append("Early epilepsy onset")

        if patient_data.get('developmental_delay', False):
            factors.append("Developmental delay")

        return factors

    def _identify_protective_factors(self, patient_data: Dict) -> List[str]:
        """Identify protective factors against SUDEP"""
        protective = []

        if patient_data.get('seizure_free', True):
            protective.append("Seizure-free")

        if patient_data.get('supervised_night', True):
            protective.append("Night supervision")

        if patient_data.get('device_therapy', False):
            protective.append("Device therapy (VNS/DBS)")

        if patient_data.get('medication_adherence', 1.0) >= 0.9:
            protective.append("Excellent medication adherence")

        if patient_data.get('seizure_frequency', 0) == 0:
            protective.append("No recent seizures")

        return protective

    def _calculate_overall_risk(self, risk_factors: List[str], protective_factors: List[str]) -> str:
        """Calculate overall SUDEP risk"""
        risk_score = len(risk_factors) * 2
        protective_score = len(protective_factors)

        net_risk = risk_score - protective_score

        if net_risk >= 6:
            return "high"
        elif net_risk >= 3:
            return "moderate"
        else:
            return "low"

    def _generate_mitigation_strategies(self, risk_factors: List[str], overall_risk: str) -> List[str]:
        """Generate SUDEP mitigation strategies"""
        strategies = []

        # Core strategies for all risk levels
        strategies.append("Optimize seizure control")
        strategies.append("Improve medication adherence")
        strategies.append("Regular follow-up with neurologist")

        if "nocturnal_seizures" in risk_factors:
            strategies.extend([
                "Night supervision recommended",
                "Consider seizure detection devices",
                "Bedroom safety modifications"
            ])

        if "high seizure frequency" in risk_factors or overall_risk == "high":
            strategies.extend([
                "Supervision during sleep",
                "Rescue medication available",
                "Emergency response plan"
            ])

        if "poor medication adherence" in risk_factors:
            strategies.extend([
                "Medication reminder system",
                "Pill organizer or smart bottle",
                "Family supervision of adherence"
            ])

        return strategies

    def _assess_night_monitoring_needs(self, risk_factors: List[str]) -> str:
        """Assess night monitoring needs"""
        high_risk_indicators = ["nocturnal_seizures", "high seizure_frequency", "generalized_tonic_clonic"]

        if any(indicator in risk_factors for indicator in high_risk_indicators):
            return "Night supervision strongly recommended"
        elif len(risk_factors) >= 3:
            return "Consider night monitoring"
        else:
            return "Routine precautions sufficient"

    def _generate_emergency_preparedness(self, overall_risk: str) -> List[str]:
        """Generate emergency preparedness recommendations"""
        preparedness = []

        # Core preparedness for all patients
        preparedness.append("Family and caregivers trained in seizure first aid")
        preparedness.append("Rescue medication accessible")

        if overall_risk == "high":
            preparedness.extend([
                "Emergency response plan in place",
                "Rescue medication at bedside",
                "Emergency contacts informed",
                "Medical alert bracelet/necklace",
                "Night-time supervision arrangements"
            ])
        elif overall_risk == "moderate":
            preparedness.extend([
                "Emergency response plan recommended",
                "Consider medical alert identification"
            ])

        return preparedness


class IndependenceSpecialist:
    """
    Independence and driving assessment specialist.

    Helps patients maintain autonomy while ensuring safety.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.driving_assessments = []
        self.independence_plans = {}

    def driving_capability_assessment(self, patient_data: Dict, location: str) -> DrivingAssessment:
        """Comprehensive driving capability assessment"""
        seizure_free_months = patient_data.get('seizure_free_months', 0)
        seizure_type = patient_data.get('seizure_type', '')
        physician_clearance = patient_data.get('physician_clearance', False)

        # Determine if patient can drive
        can_drive = self._determine_driving_eligibility(seizure_free_months, seizure_type, physician_clearance)

        # Get state requirements
        state_requirements = self._get_state_requirements(location)

        # Calculate seizure-free requirement
        seizure_free_requirement = self._calculate_seizure_free_requirement(seizure_type, location)

        # Generate recommendations
        restrictions = self._generate_driving_restrictions(can_drive, patient_data, state_requirements)
        reevaluation = self._determine_reevaluation_timeline(can_drive, patient_data)
        alternatives = self._suggest_alternative_transportation(can_drive, patient_data)

        assessment = DrivingAssessment(
            can_drive=can_drive,
            state_requirements=state_requirements,
            seizure_free_requirement=seizure_free_requirement,
            recommended_restrictions=restrictions,
            reevaluation_timeline=reevaluation,
            alternative_transportation=alternatives
        )

        self.driving_assessments.append(assessment)
        return assessment

    def _determine_driving_eligibility(self, seizure_free_months: int, seizure_type: str, clearance: bool) -> bool:
        """Determine if patient can drive"""
        if not clearance:
            return False

        # Typical requirements
        if seizure_free_months >= 6 and seizure_type != "generalized":
            return True
        elif seizure_free_months >= 12:
            return True
        else:
            return False

    def _get_state_requirements(self, location: str) -> Dict:
        """Get state-specific driving requirements"""
        # Simplified - in production would use actual state regulations
        return {
            'state': location,
            'seizure_free_months': 6,
            'physician_clearance_required': True,
            'reporting_requirements': 'Physician certification required'
        }

    def _calculate_seizure_free_requirement(self, seizure_type: str, location: str) -> Dict:
        """Calculate required seizure-free period"""
        requirements = {
            'focal_seizures': '6-12 months',
            'generalized_seizures': '12-24 months',
            'status_epilepticus_history': '24+ months'
        }

        return {
            'required_period': requirements.get(seizure_type, '12 months'),
            'currently_met': seizure_type == 'focal',
            'next_milestone': '6 months seizure-free'
        }

    def _generate_driving_restrictions(self, can_drive: bool, patient_data: Dict, state_req: Dict) -> List[str]:
        """Generate driving restrictions"""
        restrictions = []

        if not can_drive:
            restrictions.append("No driving until seizure-free requirement met")
            restrictions.append("No driving during medication changes")
            return restrictions

        # Restrictions even if cleared to drive
        if patient_data.get('recent_medication_change', False):
            restrictions.append("No driving for 1-2 weeks after medication change")

        if patient_data.get('seizure_frequency', 0) > 0:
            restrictions.append("Consider limiting driving during treatment optimization")

        return restrictions

    def _determine_reevaluation_timeline(self, can_drive: bool, patient_data: Dict) -> str:
        """Determine reevaluation timeline"""
        if can_drive:
            return "Reevaluate annually or after medication changes"
        else:
            seizure_free = patient_data.get('seizure_free_months', 0)
            months_until_eligible = max(6 - seizure_free, 1)
            return f"Reevaluate in {months_until_eligible} month(s)"

    def _suggest_alternative_transportation(self, can_drive: bool, patient_data: Dict) -> List[str]:
        """Suggest alternative transportation options"""
        alternatives = []

        if not can_drive:
            alternatives.extend([
                "Public transportation",
                "Rideshare services (Uber, Lyft)",
                "Family/friend assistance",
                "Community transportation services",
                "Consider relocation closer to work/school"
            ])

        return alternatives


class ReproductiveHealthSpecialist:
    """
    Reproductive health specialist for women with epilepsy.

    Comprehensive guidance from pre-conception through parenting.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.reproductive_plans = []

    def comprehensive_reproductive_planning(self, patient_data: Dict) -> ReproductivePlan:
        """Comprehensive reproductive health planning"""
        # Pre-conception optimization
        pre_conception = self._generate_pre_conception_plan(patient_data)

        # Medication adjustments
        medication_adjustments = self._generate_medication_adjustments(patient_data)

        # Pregnancy risk assessment
        pregnancy_risk = self._assess_pregnancy_risk(patient_data)

        # Breastfeeding guidance
        breastfeeding_guidance = self._generate_breastfeeding_guidance(patient_data)

        # Genetic counseling needs
        genetic_needs = self._assess_genetic_counseling_needs(patient_data)

        # Pregnancy monitoring
        pregnancy_monitoring = self._generate_pregnancy_monitoring(patient_data)

        plan = ReproductivePlan(
            pre_conception_optimization=pre_conception,
            medication_adjustments=medication_adjustments,
            pregnancy_risk_assessment=pregnancy_risk,
            breastfeeding_guidance=breastfeeding_guidance,
            genetic_counseling_needs=genetic_needs,
            pregnancy_monitoring=pregnancy_monitoring
        )

        self.reproductive_plans.append(plan)
        return plan

    def _generate_pre_conception_plan(self, patient_data: Dict) -> List[str]:
        """Generate pre-conception optimization recommendations"""
        recommendations = []

        recommendations.append("Schedule pre-conception consultation with neurologist")
        recommendations.append("Review current AED regimen")
        recommendations.append("Achieve optimal seizure control before conception")
        recommendations.append("Start folic acid supplementation (1-5 mg daily)")
        recommendations.append("Review vitamin D levels")

        return recommendations

    def _generate_medication_adjustments(self, patient_data: Dict) -> Dict[str, str]:
        """Generate medication adjustment recommendations"""
        current_meds = patient_data.get('current_medications', [])

        adjustments = {}

        for med in current_meds:
            if med == 'valproate':
                adjustments[med] = "STRONGLY CONSIDER CHANGING - high teratogenic risk"
            elif med == 'phenytoin':
                adjustments[med] = "CONSIDER ALTERNATIVE - teratogenic risk"
            elif med == 'phenobarbital':
                adjustments[med] = "CONSIDER ALTERNATIVE - teratogenic risk"
            elif med == 'topiramate':
                adjustments[med] = "May increase risk of oral clefts - discuss"
            elif med == 'lamotrigine':
                adjustments[med] = "Generally safe - may require dose adjustment during pregnancy"
            elif med == 'levetiracetam':
                adjustments[med] = "Generally safe - limited pregnancy data"

        return adjustments

    def _assess_pregnancy_risk(self, patient_data: Dict) -> Dict:
        """Assess pregnancy-related risks"""
        risks = {
            'maternal_risks': [],
            'fetal_risks': [],
            'seizure_risk': '',
            'medication_risks': []
        }

        seizure_frequency = patient_data.get('seizure_frequency', 0)
        if seizure_frequency >= 1:
            risks['seizure_risk'] = "Continued seizures during pregnancy risk maternal and fetal harm"
        else:
            risks['seizure_risk'] = "Well-controlled seizures - lower risk"

        current_meds = patient_data.get('current_medications', [])
        if 'valproate' in current_meds:
            risks['fetal_risks'].append("Valproate: Neural tube defects, cognitive effects, developmental delay")
            risks['medication_risks'].append("Valproate: High teratogenic risk - STRONGLY recommend changing")

        return risks

    def _generate_breastfeeding_guidance(self, patient_data: Dict) -> Dict:
        """Generate breastfeeding guidance"""
        current_meds = patient_data.get('current_medications', [])

        guidance = {
            'general_recommendation': 'Breastfeeding generally encouraged with epilepsy',
            'medication_guidance': {},
            'monitoring': 'Monitor infant for sedation and feeding difficulties'
        }

        for med in current_meds:
            if med == 'levetiracetam':
                guidance['medication_guidance'][med] = "Generally compatible with breastfeeding"
            elif med == 'lamotrigine':
                guidance['medication_guidance'][med] = "Compatible with breastfeeding - monitor infant"
            elif med == 'carbamazepine':
                guidance['medication_guidance'][med] = "Compatible with breastfeeding - monitor infant for sedation"
            elif med == 'phenobarbital':
                guidance['medication_guidance'][med] = "Excreted in breast milk - may cause sedation, monitor infant"

        return guidance

    def _assess_genetic_counseling_needs(self, patient_data: Dict) -> List[str]:
        """Assess genetic counseling needs"""
        needs = []

        needs.append("Discuss genetic epilepsy risks with genetic counselor")
        needs.append("Review recurrence risk for offspring")

        if patient_data.get('genetic_epilepsy', False):
            needs.append("Specific genetic counseling for inherited epilepsy")
            needs.append("Consider prenatal testing options")

        return needs

    def _generate_pregnancy_monitoring(self, patient_data: Dict) -> List[str]:
        """Generate pregnancy monitoring recommendations"""
        monitoring = [
            "Monthly neurologist visits during pregnancy",
            "AED level monitoring each trimester",
            "Dose adjustments as pregnancy progresses",
            "Detailed fetal ultrasound (anomaly scan)",
            "Seizure diary throughout pregnancy",
            "Postpartum medication adjustment planning"
        ]

        return monitoring


class LifeCoursePlanner:
    """
    Life course planning for epilepsy patients.

    Comprehensive planning from school through aging.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.life_plans = {}

    def comprehensive_life_plan(self, patient_data: Dict) -> LifeCoursePlan:
        """Create comprehensive life course plan"""
        school_accommodations = self._plan_school_accommodations(patient_data)
        work_considerations = self._plan_work_considerations(patient_data)
        independent_living = self._assess_independent_living(patient_data)
        long_term_care = self._identify_long_term_needs(patient_data)
        transitions = self._plan_life_transitions(patient_data)

        plan = LifeCoursePlan(
            school_accommodations=school_accommodations,
            work_considerations=work_considerations,
            independent_living_assessment=independent_living,
            long_term_care_needs=long_term_care,
            transition_points=transitions
        )

        return plan

    def _plan_school_accommodations(self, patient_data: Dict) -> List[str]:
        """Plan school accommodations"""
        accommodations = []

        accommodations.append("504 plan or IEP for epilepsy accommodations")
        accommodations.append("Seizure action plan for school staff")
        accommodations.append("Modified testing schedule if needed")
        accommodations.append("Safe environment during physical activities")
        accommodations.append("Accommodations for medication timing and side effects")
        accommodations.append("Cognitive support if needed")

        return accommodations

    def _plan_work_considerations(self, patient_data: Dict) -> List[str]:
        """Plan work/occupational considerations"""
        considerations = []

        if not patient_data.get('driving_eligible', True):
            considerations.append("Consider jobs not requiring driving")
            considerations.append("Remote work options")
            considerations.append("Public transportation access")

        considerations.append("Workplace epilepsy disclosure decisions")
        considerations.append("Workplace safety planning")
        considerations.append("Schedule accommodations if needed")
        considerations.append("ADA accommodations if applicable")

        return considerations

    def _assess_independent_living(self, patient_data: Dict) -> Dict:
        """Assess independent living needs and capabilities"""
        assessment = {
            'living_independently': patient_data.get('living_independently', True),
            'capabilities': [],
            'needs': [],
            'recommendations': []
        }

        if patient_data.get('seizure_controlled', False):
            assessment['needs'].append("Seizure monitoring and safety planning")
        else:
            assessment['capabilities'].append("Good seizure control supports independent living")

        assessment['recommendations'].extend([
            "Home safety modifications",
            "Emergency alert system",
            "Regular check-in system"
        ])

        return assessment

    def _identify_long_term_needs(self, patient_data: Dict) -> List[str]:
        """Identify long-term care needs"""
        needs = []

        if patient_data.get('treatment_resistant', False):
            needs.append("Ongoing epilepsy management")
            needs.append("Regular neurologist follow-up")

        if patient_data.get('cognitive_impairment', False):
            needs.append("Cognitive support services")
            needs.append("Memory and planning assistance")

        if patient_data.get('psychiatric_comorbidities', False):
            needs.append("Mental health services")
            needs.append("Therapy and counseling")

        return needs

    def _plan_life_transitions(self, patient_data: Dict) -> List[Dict]:
        """Plan key life transition points"""
        transitions = []

        age = patient_data.get('age', 0)

        # Upcoming transitions
        if age < 18:
            transitions.append({
                'transition': 'School to adulthood',
                'timing': 'Age 18-21',
                'planning_needed': ['Adult healthcare transition', 'Independent living skills', 'Vocational planning']
            })
        elif age < 30:
            transitions.append({
                'transition': 'Career establishment',
                'timing': 'Age 20-30',
                'planning_needed': ['Career planning with epilepsy considerations', 'Insurance and benefits planning']
            })

        return transitions


class SeizureFreedomEcosystem:
    """
    Main ecosystem for comprehensive seizure freedom and life optimization.

    Integrates SUDEP prevention, independence planning, reproductive
    health, and life course management.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.sudep_specialist = SUDEPPreventionSpecialist(patient_id)
        self.independence_specialist = IndependenceSpecialist(patient_id)
        self.reproductive_specialist = ReproductiveHealthSpecialist(patient_id)
        self.life_planner = LifeCoursePlanner(patient_id)

    def comprehensive_life_optimization(self, patient_data: Dict, location: str = 'US') -> Dict[str, Any]:
        """Comprehensive life optimization assessment and planning"""

        # SUDEP risk assessment
        sudep_assessment = self.sudep_specialist.comprehensive_risk_assessment(patient_data)

        # Driving assessment
        driving_assessment = self.independence_specialist.driving_capability_assessment(patient_data, location)

        # Reproductive planning
        reproductive_plan = None
        if patient_data.get('reproductive_age', False) or patient_data.get('planning_pregnancy', False):
            reproductive_plan = self.reproductive_specialist.comprehensive_reproductive_planning(patient_data)

        # Life course planning
        life_plan = self.life_planner.comprehensive_life_plan(patient_data)

        return {
            'patient_id': self.patient_id,
            'assessment_date': datetime.now().isoformat(),
            'sudep_prevention': {
                'overall_risk': sudep_assessment.overall_risk,
                'risk_factors': sudep_assessment.risk_factors,
                'mitigation_strategies': sudep_assessment.mitigation_strategies,
                'night_monitoring': sudep_assessment.night_monitoring_needs
            },
            'independence_planning': {
                'driving': {
                    'can_drive': driving_assessment.can_drive,
                    'restrictions': driving_assessment.recommended_restrictions,
                    'alternatives': driving_assessment.alternative_transportation,
                    'reevaluation': driving_assessment.reevaluation_timeline
                },
                'life_course': {
                    'school_accommodations': life_plan.school_accommodations,
                    'work_considerations': life_plan.work_considerations,
                    'independent_living': life_plan.independent_living_assessment
                }
            },
            'reproductive_health': {
                'pre_conception': reproductive_plan.pre_conception_optimization if reproductive_plan else [],
                'medication_adjustments': reproductive_plan.medication_adjustments if reproductive_plan else {},
                'pregnancy_monitoring': reproductive_plan.pregnancy_monitoring if reproductive_plan else []
            },
            'overall_recommendations': self._generate_life_recommendations(sudep_assessment, driving_assessment, life_plan)
        }

    def _generate_life_recommendations(self, sudep: SUDEPRiskAssessment, driving: DrivingAssessment, life: LifeCoursePlan) -> List[str]:
        """Generate integrated life recommendations"""
        recommendations = []

        # SUDEP prevention
        if sudep.overall_risk in ['moderate', 'high']:
            recommendations.append("Implement comprehensive SUDEP prevention strategies")

        # Driving
        if not driving.can_drive:
            recommendations.append("Plan alternative transportation options")
            recommendations.append("Work toward seizure-free driving requirement")

        # Overall recommendations
        recommendations.append("Regular life planning reviews")
        recommendations.append("Maintain open communication with healthcare team")

        return recommendations


# Convenience function
def create_seizure_freedom_ecosystem(patient_id: str) -> SeizureFreedomEcosystem:
    """Create comprehensive seizure freedom ecosystem"""
    return SeizureFreedomEcosystem(patient_id)
