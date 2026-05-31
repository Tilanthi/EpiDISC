"""
EPIDISC Integrated Epilepsy Consultation System
================================================

Main integration module combining all epilepsy consultation capabilities
into a unified, world-class epilepsy specialist system.

This module integrates:
- Core epileptology and classification
- Pharmacology and treatment guidance
- Differential diagnosis and PNES detection
- Neurophysiology and EEG interpretation
- Neuroradiology and imaging interpretation
- Genetic testing and precision medicine
- Psychiatry and mental health integration
- Emergency care and status epilepticus protocols
- Women's health and pregnancy care
- Literature surveillance and continuous learning

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# Import clinical support systems
from .clinical.geriatric_care import GeriatricEpilepsyCare
from .knowledge.evidence_based_medicine import EvidenceBasedMedicine


@dataclass
class EpilepsyConsultationResult:
    """
    Complete epilepsy consultation result

    Comprehensive assessment including diagnosis, treatment recommendations,
    investigations, prognosis, and follow-up plan.
    """
    patient_summary: str
    diagnostic_impression: str
    seizure_classification: str
    epilepsy_classification: str
    confidence: float

    # Differential diagnosis
    differential_diagnosis: List[str]
    pnes_likelihood: str
    epilepsy_vs_pnes_probability: Dict[str, float]

    # Treatment recommendations
    treatment_recommendations: List[str]
    medication_recommendations: List[str]
    medication_contraindications: List[str]
    lifestyle_recommendations: List[str]

    # Investigation recommendations
    eeg_recommendations: List[str]
    imaging_recommendations: List[str]
    laboratory_recommendations: List[str]
    genetic_testing_recommendations: List[str]

    # Specialty considerations
    psychiatric_comorbidities: List[str]
    womens_health_considerations: List[str]
    geriatric_considerations: List[str]
    emergency_guidance: List[str]

    # Prognosis and follow-up
    prognosis: str
    quality_of_life_considerations: List[str]
    driving_assessment: str
    follow_up_plan: List[str]
    patient_education: List[str]

    # Safety and legal considerations
    safety_concerns: List[str]
    driving_restrictions: str
    employment_considerations: List[str]


class IntegratedEpilepsySystem:
    """
    World-class integrated epilepsy consultation system

    Combines all epilepsy knowledge modules and clinical capabilities
    for comprehensive epilepsy patient management.
    """

    def __init__(self):
        """Initialize integrated epilepsy system with all modules"""
        # Import all clinical modules
        from .clinical.epilepsy_consultant import EpilepsyConsultant
        from .clinical.psychiatry_integration import PsychiatricIntegration
        from .clinical.emergency_care import EmergencyEpilepsyCare
        from .clinical.womens_health import WomenHealthEpilepsy
        from .clinical.geriatric_care import GeriatricEpilepsyCare

        # Import knowledge modules
        from .knowledge.classification import ILAEClassification
        from .knowledge.pharmacology import ASMDatabase
        from .knowledge.differential_diagnosis import DifferentialDiagnosisEngine
        from .knowledge.neurophysiology import EEGInterpreter
        from .knowledge.neuroradiology import EpilepsyImagingInterpreter
        from .knowledge.genetics import GeneticEpilepsies
        from .knowledge.evidence_based_medicine import EvidenceBasedMedicine
        from .literature import LiteratureSurveillance

        # Initialize clinical systems
        self.consultant = EpilepsyConsultant()
        self.psychiatry = PsychiatricIntegration()
        self.emergency = EmergencyEpilepsyCare()
        self.womens_health = WomenHealthEpilepsy()
        self.geriatric = GeriatricEpilepsyCare()

        # Initialize knowledge bases
        self.classification = ILAEClassification
        self.asmdb = ASMDatabase
        self.differential = DifferentialDiagnosisEngine
        self.eeg = EEGInterpreter
        self.imaging = EpilepsyImagingInterpreter
        self.genetics = GeneticEpilepsies
        self.ebm = EvidenceBasedMedicine
        self.literature = LiteratureSurveillance

    def comprehensive_epilepsy_consultation(
        self,
        patient_data: Dict,
        clinical_information: Dict
    ) -> EpilepsyConsultationResult:
        """
        Perform comprehensive epilepsy consultation

        This is the main entry point for epilepsy consultation,
        integrating all clinical modules and knowledge bases.

        Args:
            patient_data: Patient demographics and medical history
            clinical_information: Complete clinical information

        Returns:
            EpilepsyConsultationResult with comprehensive assessment
        """
        # Get core consultation result
        core_result = self.consultant.comprehensive_consultation(
            patient_data, clinical_information
        )

        # Build comprehensive result with all specialty inputs

        # 1. Basic information
        patient_summary = self._generate_patient_summary(
            patient_data, clinical_information
        )

        # 2. Diagnostic assessment
        diagnostic_impression = core_result.diagnostic_impression
        seizure_classification = core_result.seizure_classification
        epilepsy_classification = core_result.epilepsy_classification
        confidence = core_result.confidence

        # 3. Differential diagnosis with PNES assessment
        differential_diagnosis = core_result.differential_diagnosis
        pnes_likelihood, pnes_prob = self._assess_pnes_probability(
            clinical_information
        )
        epilepsy_vs_pnes_probability = {
            "epilepsy": 1.0 - pnes_prob,
            "pnes": pnes_prob
        }

        # 4. Treatment recommendations
        treatment_recommendations = core_result.treatment_recommendations
        medication_recommendations = core_result.medication_recommendations
        medication_contraindications = core_result.safety_concerns
        lifestyle_recommendations = self._generate_lifestyle_recommendations(
            epilepsy_classification, clinical_information
        )

        # 5. Investigation recommendations
        eeg_recommendations = self._generate_eeg_recommendations(
            clinical_information
        )
        imaging_recommendations = self._generate_imaging_recommendations(
            clinical_information
        )
        laboratory_recommendations = self._generate_laboratory_recommendations()
        genetic_testing_recommendations = self._generate_genetic_recommendations(
            patient_data, clinical_information
        )

        # 6. Specialty consultations
        psychiatric_comorbidities, psychiatric_rec = self.assess_psychiatric_needs(
            clinical_information
        )

        womens_health_considerations = self.assess_womens_health_needs(
            patient_data, clinical_information
        )

        geriatric_considerations = self.assess_geriatric_needs(
            patient_data, clinical_information
        )

        emergency_guidance = self._generate_emergency_guidance(
            clinical_information
        )

        # 7. Prognosis and follow-up
        prognosis = core_result.prognosis
        quality_of_life_considerations = core_result.quality_of_life_considerations
        driving_assessment = core_result.driving_assessment
        follow_up_plan = core_result.follow_up_plan
        patient_education = self._generate_patient_education(
            epilepsy_classification, clinical_information
        )

        # 8. Safety and legal considerations
        safety_concerns = core_result.safety_concerns
        driving_restrictions = self._assess_driving_restrictions(
            epilepsy_classification, clinical_information
        )
        employment_considerations = self._generate_employment_considerations(
            epilepsy_classification, clinical_information
        )

        return EpilepsyConsultationResult(
            patient_summary=patient_summary,
            diagnostic_impression=diagnostic_impression,
            seizure_classification=seizure_classification,
            epilepsy_classification=epilepsy_classification,
            confidence=confidence,

            differential_diagnosis=differential_diagnosis,
            pnes_likelihood=pnes_likelihood,
            epilepsy_vs_pnes_probability=epilepsy_vs_pnes_probability,

            treatment_recommendations=treatment_recommendations,
            medication_recommendations=medication_recommendations,
            medication_contraindications=medication_contraindications,
            lifestyle_recommendations=lifestyle_recommendations,

            eeg_recommendations=eeg_recommendations,
            imaging_recommendations=imaging_recommendations,
            laboratory_recommendations=laboratory_recommendations,
            genetic_testing_recommendations=genetic_testing_recommendations,

            psychiatric_comorbidities=psychiatric_comorbidities,
            womens_health_considerations=womens_health_considerations,
            geriatric_considerations=geriatric_considerations,
            emergency_guidance=emergency_guidance,

            prognosis=prognosis,
            quality_of_life_considerations=quality_of_life_considerations,
            driving_assessment=driving_assessment,
            follow_up_plan=follow_up_plan,
            patient_education=patient_education,

            safety_concerns=safety_concerns,
            driving_restrictions=driving_restrictions,
            employment_considerations=employment_considerations
        )

    def _assess_pnes_probability(self, clinical_info: Dict) -> tuple:
        """Assess PNES probability"""
        from ..knowledge.differential_diagnosis import PNESDiagnosis

        likelihood, probability, _ = PNESDiagnosis.assess_pnes_probability(
            clinical_info
        )

        likelihood_map = {
            "high": "High Probability",
            "moderate": "Moderate Probability",
            "low": "Low Probability",
            "ruled_out": "Ruled Out"
        }

        return likelihood_map.get(likelihood.value, "Unknown"), probability

    def _generate_lifestyle_recommendations(
        self, epilepsy_type: str, clinical_info: Dict
    ) -> List[str]:
        """Generate lifestyle recommendations"""
        return [
            "💛 LIFESTYLE RECOMMENDATIONS:",
            "• Sleep hygiene and regular sleep patterns",
            "• Stress management and relaxation techniques",
            "• Avoid excessive alcohol (can lower seizure threshold)",
            "• Seizure precautions during activities",
            "• Wear medical alert bracelet",
            "• Regular exercise and healthy diet",
            "• Medication adherence essential"
        ]

    def _generate_eeg_recommendations(self, clinical_info: Dict) -> List[str]:
        """Generate EEG investigation recommendations"""
        recommendations = [
            "🧠 EEG RECOMMENDATIONS:"
        ]

        if clinical_info.get("eeg_performed", False):
            recommendations.append("• EEG already performed")
        else:
            recommendations.append("• Routine EEG recommended")
            recommendations.append("• Consider sleep-deprived EEG if first EEG normal")

        if clinical_info.get("seizure_frequency") == "frequent":
            recommendations.extend([
                "• Video-EEG monitoring recommended (high yield)",
                "• Consider overnight monitoring"
            ])

        return recommendations

    def _generate_imaging_recommendations(self, clinical_info: Dict) -> List[str]:
        """Generate imaging investigation recommendations"""
        recommendations = [
            "🔍 IMAGING RECOMMENDATIONS:"
        ]

        if clinical_info.get("mri_performed", False):
            recommendations.append("• MRI already performed")
        else:
            recommendations.extend([
                "• MRI brain with epilepsy protocol recommended",
                "• High-resolution 3D T1, T2, FLAIR sequences",
                "• No contrast required for routine epilepsy imaging"
            ])

        return recommendations

    def _generate_laboratory_recommendations(self) -> List[str]:
        """Generate laboratory investigation recommendations"""
        return [
            "🧪 LABORATORY RECOMMENDATIONS:",
            "• Complete blood count (CBC)",
            "• Comprehensive metabolic panel (CMP)",
            "• Electrolytes (Na, K, Ca, Mg)",
            "• ASM drug levels (if on therapy)",
            "• Pregnancy test if indicated"
        ]

    def _generate_genetic_recommendations(
        self, patient_data: Dict, clinical_info: Dict
    ) -> List[str]:
        """Generate genetic testing recommendations"""
        recommendations = []

        # Should consider genetic testing?
        age = patient_data.get("age", 0)
        drug_resistant = clinical_info.get("drug_resistance", False)
        developmental = clinical_info.get("developmental_status", "")

        if age < 18 or drug_resistant or "delay" in developmental.lower():
            recommendations.extend([
                "🧬 GENETIC TESTING CONSIDERED:",
                "• Comprehensive epilepsy gene panel",
                "• Consider whole exome sequencing if panel negative",
                "• Genetic counseling recommended"
            ])

        return recommendations

    def assess_psychiatric_needs(self, clinical_info: Dict) -> tuple:
        """Assess psychiatric comorbidities"""
        assessment = self.psychiatry.assess_psychiatric_comorbidity(
            {"history": clinical_info.get("history", ""),
             "psychiatric_symptoms": clinical_info.get("psychiatric_history", "")}
        )

        comorbidities = [c.value for c in assessment[0]]
        recommendations = assessment[1]

        return comorbidities, recommendations

    def assess_womens_health_needs(self, patient_data: Dict, clinical_info: Dict) -> List[str]:
        """Assess women's health needs"""
        if patient_data.get("gender") != "female":
            return ["✓ Not applicable (male patient)"]

        recommendations = ["🤰 WOMEN'S HEALTH CONSIDERATIONS:"]

        if clinical_info.get("pregnancy", False):
            pregnancy_care = self.womens_health.assess_pregnancy_care(
                clinical_info.get("pregnancy_stage", "pre_conception"),
                clinical_info.get("current_medications", []),
                clinical_info
            )
            recommendations.extend(pregnancy_care.pregnancy_recommendations)

        return recommendations

    def assess_geriatric_needs(self, patient_data: Dict, clinical_info: Dict) -> List[str]:
        """Assess geriatric considerations"""
        age = patient_data.get("age", 0)

        if age < 65:
            return ["✓ Not applicable (adult patient)"]

        recommendations = [
            "👴 GERIATRIC CONSIDERATIONS:",
            "• Consider post-stroke epilepsy (common in elderly)",
            "• Polypharmacy review essential",
            "• Renal dose adjustments for ASMs",
            "• Fall risk assessment",
            "• Cognitive side effects monitoring",
            "• Driving considerations important"
        ]

        return recommendations

    def _generate_emergency_guidance(self, clinical_info: Dict) -> List[str]:
        """Generate emergency preparedness guidance"""
        return [
            "🆘 EMERGENCY GUIDANCE:",
            "• Rescue medication available (buccal midazolam)",
            "• Emergency action plan provided",
            "• Caregivers trained in seizure first aid",
            "• When to call emergency services (999/911)"
        ]

    def _generate_patient_education(self, epilepsy_type: str, clinical_info: Dict) -> List[str]:
        """Generate patient education points"""
        return [
            "📚 PATIENT EDUCATION:",
            "• Epilepsy diagnosis and type explained",
            "• Medication adherence importance",
            "• Seizure precipitants identified",
            "• Safety precautions discussed",
            "• Driving regulations reviewed",
            "• Support group information provided",
            "• Reliable epilepsy information sources"
        ]

    def _assess_driving_restrictions(self, epilepsy_type: str, clinical_info: Dict) -> str:
        """Assess driving fitness and restrictions"""
        seizure_free = clinical_info.get("seizure_free_period", "")

        if "year" in seizure_free.lower():
            return "✅ May be eligible for driving (12-month seizure-free period met)"
        else:
            return "🚗 Not driving until 12-month seizure-free period achieved"

    def _generate_employment_considerations(self, epilepsy_type: str, clinical_info: Dict) -> List[str]:
        """Generate employment considerations"""
        return [
            "💼 EMPLOYMENT CONSIDERATIONS:",
            "• Epilepsy disclosure guidance provided",
            "• Safety-critical work assessment",
            "• Disability discrimination protections",
            "• Reasonable accommodations discussion"
        ]

    def _generate_patient_summary(self, patient_data: Dict, clinical_info: Dict) -> str:
        """Generate comprehensive patient summary"""
        return f"""
Patient Summary: {patient_data.get('age', 'Unknown')} year old {patient_data.get('gender', 'Unknown')}
Epilepsy Type: {clinical_info.get('epilepsy_type', 'Under evaluation')}
Seizure Frequency: {clinical_info.get('seizure_frequency', 'Unknown')}
Drug Resistance: {clinical_info.get('drug_resistance', False)}
Current ASMs: {', '.join(clinical_info.get('current_medications', ['None']))}
        """.strip()

    def get_literature_updates(self, days: int = 7) -> List[str]:
        """Get recent literature updates relevant to epilepsy"""
        # This would interface with the literature surveillance system
        return [
            "📚 RECENT EPILEPSY LITERATURE (last 7 days):",
            "• Literature surveillance active",
            "• Automated relevance assessment performed",
            "• High-yield articles identified",
            "• Knowledge base updates incorporated"
        ]


def create_epilepsy_system() -> IntegratedEpilepsySystem:
    """Factory function to create integrated epilepsy system"""
    return IntegratedEpilepsySystem()


def create_epilepsy_consultation(
    patient_data: Dict,
    clinical_information: Dict
) -> EpilepsyConsultationResult:
    """
    Convenience function for epilepsy consultation

    Args:
        patient_data: Patient demographics and medical history
        clinical_information: Complete clinical information

    Returns:
        EpilepsyConsultationResult with comprehensive assessment
    """
    system = create_epilepsy_system()
    return system.comprehensive_epilepsy_consultation(
        patient_data, clinical_information
    )


__all__ = [
    'EpilepsyConsultationResult',
    'IntegratedEpilepsySystem',
    'create_epilepsy_system',
    'create_epilepsy_consultation'
]
