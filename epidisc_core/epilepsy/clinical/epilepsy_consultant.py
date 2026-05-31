"""
EPIDISC Comprehensive Epilepsy Consultation System
====================================================

Integrated epilepsy consultation system combining all knowledge modules
with consultant-level clinical reasoning and decision-making capabilities.

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class ConsultationComplexity(Enum):
    """Complexity levels for epilepsy consultations"""
    ROUTINE = "routine"                        # Straightforward case
    MODERATE = "moderate"                      # Some complexity
    COMPLEX = "complex"                        # Multiple factors
    HIGHLY_COMPLEX = "highly_complex"          # Severe complexity, multiple comorbidities


class ConsultationFocus(Enum):
    """Primary focus of epilepsy consultation"""
    DIAGNOSTIC_EVALUATION = "diagnostic_evaluation"
    TREATMENT_OPTIMIZATION = "treatment_optimization"
    PRE_SURGICAL_EVALUATION = "pre_surgical_evaluation"
    PREGNANCY_CONSULTATION = "pregnancy_consultation"
    DRUG_RESISTANCE_EVALUATION = "drug_resistance_evaluation"
    SECOND_OPINION = "second_opinion"
    EMERGENCY_GUIDANCE = "emergency_guidance"


@dataclass
class ConsultationResult:
    """
    Complete epilepsy consultation result

    Comprehensive assessment with diagnosis, treatment recommendations,
    and follow-up plan for epilepsy patient management.
    """

    patient_summary: str
    diagnostic_impression: str
    seizure_classification: str
    epilepsy_classification: str
    differential_diagnosis: List[str]
    treatment_recommendations: List[str]
    medication_recommendations: List[str]
    investigation_recommendations: List[str]
    safety_concerns: List[str]
    prognosis: str
    follow_up_plan: List[str]
    red_flags: List[str]
    quality_of_life_considerations: List[str]
    driving_assessment: str
    confidence: float


class EpilepsyConsultant:
    """
    Comprehensive epilepsy consultation system

    Integrates all epilepsy knowledge modules for consultant-level
    clinical reasoning and treatment recommendations.
    """

    def __init__(self):
        """Initialize epilepsy consultant with all knowledge modules"""
        # Import all knowledge modules
        from ..knowledge.classification import ILAEClassification, SeizureSemiology
        from ..knowledge.pharmacology import ASMDatabase, TreatmentGuidelines
        from ..knowledge.differential_diagnosis import DifferentialDiagnosisEngine, PNESDiagnosis
        from ..knowledge.neurophysiology import EEGInterpreter, EEGDiagnosticYield
        from ..knowledge.neuroradiology import EpilepsyImagingInterpreter
        from ..knowledge.genetics import GeneticEpilepsies, GeneticTestingGuidance

        self.classification = ILAEClassification
        self.semiology = SeizureSemiology
        self.asmdb = ASMDatabase
        self.guidelines = TreatmentGuidelines
        self.differential_engine = DifferentialDiagnosisEngine
        self.pnes_diagnosis = PNESDiagnosis
        self.eeg_interpreter = EEGInterpreter
        self.eeg_yield = EEGDiagnosticYield
        self.imaging_interpreter = EpilepsyImagingInterpreter
        self.genetics = GeneticEpilepsies
        self.genetic_testing = GeneticTestingGuidance

    def comprehensive_consultation(
        self,
        patient_data: Dict,
        clinical_context: Dict
    ) -> ConsultationResult:
        """
        Perform comprehensive epilepsy consultation

        Args:
            patient_data: Patient information (age, gender, medical history)
            clinical_context: Clinical information (seizure description, EEG, MRI, medications)

        Returns:
            ConsultationResult with complete assessment and recommendations
        """
        # Extract key information
        age = patient_data.get("age", "unknown")
        gender = patient_data.get("gender", "unknown")
        seizure_description = clinical_context.get("seizure_description", "")
        eeg_findings = clinical_context.get("eeg_findings", "")
        mri_findings = clinical_context.get("mri_findings", "")
        current_medications = clinical_context.get("current_medications", [])
        medical_history = clinical_context.get("medical_history", "")
        family_history = clinical_context.get("family_history", "")

        # Initialize result components
        diagnostic_impression = ""
        seizure_classification = ""
        epilepsy_classification = ""
        differential_diagnosis = []
        treatment_recommendations = []
        medication_recommendations = []
        investigation_recommendations = []
        safety_concerns = []
        prognosis = ""
        follow_up_plan = []
        red_flags = []
        quality_of_life_considerations = []
        driving_assessment = ""
        confidence = 0.8

        # 1. Seizure Classification
        if seizure_description:
            classification = self.classification.classify_seizure(seizure_description)
            seizure_classification = classification.get_classification_path()
            differential_diagnosis = classification.get_differential_diagnosis()

        # 2. Epilepsy Classification
        if seizure_classification:
            epilepsy_type = self._determine_epilepsy_type(seizure_description, eeg_findings)
            epilepsy_classification = epilepsy_type

            # Add treatment guidance based on classification
            treatment_guidance = self.guidelines.get_first_line_recommendation(
                epilepsy_type,
                self._get_patient_factors(patient_data)
            )
            treatment_recommendations.extend(treatment_guidance.get("recommended", []))

        # 3. Differential Diagnosis
        differential = self.differential_engine.evaluate_case({
            "history": clinical_context.get("history", ""),
            "semiology": clinical_context.get("semiology", seizure_description),
            "timing": clinical_context.get("timing", ""),
            "frequency": clinical_context.get("frequency", "")
        })

        # Add differential diagnosis to red flags
        if differential.red_flags:
            red_flags.extend([f"{flag[0]} ({flag[1].value})" for flag in differential.red_flags])

        # 4. EEG Analysis
        if eeg_findings:
            eeg_result = self.eeg_interpreter.interpret_eeg(
                eeg_findings,
                self._get_age_group(age),
                seizure_description
            )
            investigation_recommendations.extend([
                f"EEG Analysis: {eeg_result.diagnostic_impression}",
                f"Confidence: {eeg_result.confidence:.0%}"
            ])

            # Check if video-EEG recommended
            if clinical_context.get("seizure_frequency", "") == "frequent":
                investigation_recommendations.extend(
                    self.eeg_yield.recommend_eeg_strategy(
                        clinical_context.get("seizure_frequency", ""),
                        "high",
                        0
                    )
                )

        # 5. MRI Analysis
        if mri_findings:
            imaging_result = self.imaging_interpreter.interpret_mri(
                mri_findings,
                clinical_context
            )
            investigation_recommendations.extend([
                f"Imaging: {imaging_result.diagnostic_impression}"
            ])

            if imaging_result.lesion_identified:
                investigation_recommendations.extend([
                    f"Lesion identified: {imaging_result.lesion_type.value}",
                    "Consider presurgical evaluation"
                ])

        # 6. Medication Assessment
        if current_medications:
            for med in current_medications:
                # Check for drug interactions
                for other_med in current_medications:
                    if med != other_med:
                        interaction = self.asmdb.get_drug_interactions(med, other_med)
                        if interaction:
                            safety_concerns.append(f"⚠️ {interaction}")

                # Check for appropriateness
                warnings = self.asmdb.check_contraindications(
                    med.lower(),
                    epilepsy_classification,
                    self._get_patient_factors(patient_data)
                )
                safety_concerns.extend(warnings)

        # 7. Treatment Optimization
        if not current_medications or clinical_context.get("new_onset", False):
            # New-onset treatment recommendations
            if epilepsy_classification:
                recommendations = self.asmdb.recommend_first_line(
                    epilepsy_classification,
                    self._get_patient_factors(patient_data)
                )
                for med, considerations in recommendations:
                    medication_recommendations.append(f"• {med.title()}")
                    if considerations:
                        medication_recommendations.extend([f"  {c}" for c in considerations])

        # 8. Genetic Testing Considerations
        if self._should_consider_genetic_testing(patient_data, clinical_context):
            genetic_recommendations = self.genetic_testing.recommend_testing_strategy(
                patient_data.get("age_of_onset", ""),
                epilepsy_classification,
                clinical_context.get("developmental_status", ""),
                family_history,
                clinical_context.get("drug_resistance", False)
            )
            investigation_recommendations.extend(genetic_recommendations)

        # 9. Safety Considerations
        safety_concerns.extend(self._assess_safety_concerns(
            patient_data, clinical_context
        ))

        # 10. Driving Assessment
        driving_assessment = self._assess_driving_fitness(
            epilepsy_classification,
            clinical_context
        )

        # 11. Prognosis
        prognosis = self._assess_prognosis(
            epilepsy_classification,
            clinical_context,
            imaging_result if mri_findings else None
        )

        # 12. Follow-up Plan
        follow_up_plan.extend(self._generate_follow_up_plan(
            epilepsy_classification,
            clinical_context
        ))

        # 13. Quality of Life Considerations
        quality_of_life_considerations.extend(self._assess_quality_of_life(
            epilepsy_classification,
            clinical_context
        ))

        # Calculate overall confidence
        confidence = self._calculate_consultation_confidence(
            seizure_classification, eeg_findings, mri_findings
        )

        # Generate patient summary
        patient_summary = self._generate_patient_summary(
            patient_data, clinical_context, seizure_classification
        )

        # Form final diagnostic impression
        diagnostic_impression = self._form_diagnostic_impression(
            seizure_classification, epilepsy_classification, differential
        )

        return ConsultationResult(
            patient_summary=patient_summary,
            diagnostic_impression=diagnostic_impression,
            seizure_classification=seizure_classification,
            epilepsy_classification=epilepsy_classification,
            differential_diagnosis=differential_diagnosis,
            treatment_recommendations=treatment_recommendations,
            medication_recommendations=medication_recommendations,
            investigation_recommendations=investigation_recommendations,
            safety_concerns=safety_concerns,
            prognosis=prognosis,
            follow_up_plan=follow_up_plan,
            red_flags=red_flags,
            quality_of_life_considerations=quality_of_life_considerations,
            driving_assessment=driving_assessment,
            confidence=confidence
        )

    def _determine_epilepsy_type(self, seizure_description: str, eeg_findings: str) -> str:
        """Determine epilepsy type from clinical information"""
        description_lower = seizure_description.lower()
        eeg_lower = eeg_findings.lower()

        # Check for generalized features
        generalized_indicators = [
            "generalized", "bilaterally", "both sides", "from onset",
            "absence", "myoclonic", "tonic-clonic"
        ]

        focal_indicators = [
            "aura", "focal", "partial", "one side", "unilateral",
            "automatisms", "lip smacking"
        ]

        # Check EEG for guidance
        if "generalized spike" in eeg_lower or "generalized spike-wave" in eeg_lower:
            return "generalized"
        elif "focal spike" in eeg_lower or "temporal spike" in eeg_lower:
            return "focal"

        # Check description
        generalized_score = sum(1 for ind in generalized_indicators if ind in description_lower)
        focal_score = sum(1 for ind in focal_indicators if ind in description_lower)

        if generalized_score > focal_score:
            return "generalized"
        elif focal_score > generalized_score:
            return "focal"
        else:
            return "unknown"

    def _get_age_group(self, age: str) -> str:
        """Convert age to age group for EEG interpretation"""
        if isinstance(age, int):
            if age < 1:
                return "infant"
            elif age < 12:
                return "child"
            elif age < 18:
                return "adolescent"
            elif age < 65:
                return "adult"
            else:
                return "elderly"
        return "adult"  # Default

    def _get_patient_factors(self, patient_data: Dict) -> Dict[str, bool]:
        """Extract patient factors for ASM consideration"""
        return {
            "pregnancy": patient_data.get("pregnancy", False),
            "elderly": int(patient_data.get("age", 0)) > 65,
            "renal_impairment": patient_data.get("renal_impairment", False),
            "hepatic_impairment": patient_data.get("hepatic_impairment", False),
            "oral_contraceptives": patient_data.get("oral_contraceptives", False)
        }

    def _should_consider_genetic_testing(self, patient_data: Dict, clinical_context: Dict) -> bool:
        """Determine if genetic testing should be recommended"""
        age_of_onset = patient_data.get("age_of_onset", "")
        developmental_status = clinical_context.get("developmental_status", "")
        drug_resistance = clinical_context.get("drug_resistance", False)

        # High priority for genetic testing
        if age_of_onset in ["infancy", "neonatal"]:
            return True
        if drug_resistance and int(patient_data.get("age", 99)) < 40:
            return True
        if "intellectual disability" in developmental_status.lower():
            return True
        if "autism" in developmental_status.lower():
            return True

        return False

    def _assess_safety_concerns(self, patient_data: Dict, clinical_context: Dict) -> List[str]:
        """Assess safety concerns for epilepsy patient"""
        concerns = []

        # SUDEP risk factors
        if clinical_context.get("gtcs", False):
            concerns.append("⚠️ SUDEP risk: Generalized tonic-clonic seizures present")
            concerns.append("• Optimize seizure control to reduce SUDEP risk")
            concerns.append("• Discuss nocturnal supervision")

        # Seizure frequency
        frequency = clinical_context.get("seizure_frequency", "")
        if "daily" in frequency.lower():
            concerns.append("⚠️ High seizure frequency - increased safety risks")

        # Pregnancy considerations
        if patient_data.get("pregnancy", False):
            concerns.extend([
                "🤰 PREGNANCY SAFETY:",
                "• Review all ASMs for teratogenicity",
                "• Avoid valproate if possible (major teratogen)",
                "• Folic acid supplementation recommended",
                "• MDT obstetric-neurology management"
            ])

        # Driving considerations
        concerns.append(self._assess_driving_fitness(
            clinical_context.get("epilepsy_type", ""),
            clinical_context
        ))

        return concerns

    def _assess_driving_fitness(self, epilepsy_type: str, clinical_context: Dict) -> str:
        """Assess driving fitness (UK regulations)"""
        # This is based on UK DVLA regulations
        if not epilepsy_type or epilepsy_type == "unknown":
            return "🚗 DRIVING: Requires seizure-free period (usually 12 months)"

        seizure_free = clinical_context.get("seizure_free_period", "")
        controlled = clinical_context.get("well_controlled", False)

        if controlled and "year" in seizure_free.lower():
            return "✅ DRIVING: May be eligible if 12-month seizure-free period met"

        return "🚗 DRIVING: Not driving until 12-month seizure-free period"

    def _assess_prognosis(
        self,
        epilepsy_type: str,
        clinical_context: Dict,
        imaging_result: Optional[object] = None
    ) -> str:
        """Assess epilepsy prognosis"""
        prognostic_factors = []

        # Epilepsy type
        if epilepsy_type == "generalized":
            prognostic_factors.append("Generalized epilepsy: Often lifelong treatment")
        elif epilepsy_type == "focal":
            prognostic_factors.append("Focal epilepsy: Variable prognosis")

        # Drug resistance
        if clinical_context.get("drug_resistance", False):
            prognostic_factors.append("Drug-resistant epilepsy: Lower remission rate")

        # Lesional epilepsy
        if imaging_result and hasattr(imaging_result, 'lesion_identified') and imaging_result.lesion_identified:
            prognostic_factors.append("Lesional epilepsy: Better surgical prognosis")

        # Age factors
        age = clinical_context.get("age", 0)
        if isinstance(age, int) and age > 60:
            prognostic_factors.append("Late-onset epilepsy: Often requires lifelong treatment")

        return "\n".join(prognostic_factors) if prognostic_factors else "Generally favorable prognosis"

    def _generate_follow_up_plan(
        self,
        epilepsy_type: str,
        clinical_context: Dict
    ) -> List[str]:
        """Generate follow-up plan"""
        follow_up = []

        follow_up.extend([
            "📋 FOLLOW-UP PLAN:",
            "• Review in 3-6 months",
            "• Seizure diary review",
            "• ASM side effect assessment",
            "• Consider ASM level monitoring if appropriate"
        ])

        # Specific follow-up based on clinical situation
        if clinical_context.get("drug_resistance", False):
            follow_up.extend([
                "",
                "DRUG-RESISTANT EPILEPSY:",
                "• Refer to epilepsy specialist",
                "• Consider presurgical evaluation",
                "• Consider neuromodulation options"
            ])

        if clinical_context.get("new_onset", False):
            follow_up.extend([
                "",
                "NEW-ONSET EPILEPSY:",
                "• Patient education about epilepsy",
                "• Safety counseling (SUDEP, driving)",
                "• Provide seizure action plan"
            ])

        return follow_up

    def _assess_quality_of_life(
        self,
        epilepsy_type: str,
        clinical_context: Dict
    ) -> List[str]:
        """Assess quality of life considerations"""
        qol_considerations = []

        qol_considerations.extend([
            "💛 QUALITY OF LIFE CONSIDERATIONS:",
            "• Discuss epilepsy impact on daily life",
            "• Sleep hygiene importance",
            "• Alcohol in moderation",
            "• Stress management",
            "• Regular exercise encouraged"
        ])

        # Work considerations
        qol_considerations.extend([
            "",
            "💼 WORK CONSIDERATIONS:",
            "• Discuss epilepsy disclosure with employer",
            "• Safety-critical work considerations",
            "• Disability discrimination protections"
        ])

        # Mental health
        qol_considerations.extend([
            "",
            "🧠 MENTAL HEALTH:",
            "• Screen for depression and anxiety",
            "• Provide psychological support referral if needed",
            "• Consider epilepsy support groups"
        ])

        return qol_considerations

    def _calculate_consultation_confidence(
        self,
        seizure_classification: str,
        eeg_findings: str,
        mri_findings: str
    ) -> float:
        """Calculate overall confidence in consultation"""
        confidence = 0.5  # Base confidence

        if seizure_classification:
            confidence += 0.2

        if eeg_findings and "epileptiform" in eeg_findings.lower():
            confidence += 0.2

        if mri_findings and ("lesion" in mri_findings.lower() or "sclerosis" in mri_findings.lower()):
            confidence += 0.1

        return min(confidence, 1.0)

    def _generate_patient_summary(
        self,
        patient_data: Dict,
        clinical_context: Dict,
        seizure_classification: str
    ) -> str:
        """Generate patient summary"""
        summary = [
            f"Patient Summary: {patient_data.get('age', 'Unknown')} year old {patient_data.get('gender', 'Unknown')}",
            f"Seizure classification: {seizure_classification if seizure_classification else 'Pending classification'}",
            f"Seizure frequency: {clinical_context.get('seizure_frequency', 'Unknown')}",
            f"Drug resistance: {clinical_context.get('drug_resistance', False)}"
        ]

        return "\n".join(summary)

    def _form_diagnostic_impression(
        self,
        seizure_classification: str,
        epilepsy_classification: str,
        differential: object
    ) -> str:
        """Form comprehensive diagnostic impression"""
        impression = [
            "🧠 DIAGNOSTIC IMPRESSION:",
            ""
        ]

        if seizure_classification:
            impression.append(f"Seizure Classification: {seizure_classification}")

        if epilepsy_classification:
            impression.append(f"Epilepsy Type: {epilepsy_classification}")

        if differential and differential.primary_diagnosis:
            impression.append(f"Primary Consideration: {differential.primary_diagnosis}")

        impression.extend([
            "",
            "This impression is based on clinical information and available investigations.",
            "Diagnosis may be revised with additional information."
        ])

        return "\n".join(impression)


def create_epilepsy_consultant() -> EpilepsyConsultant:
    """Factory function to create epilepsy consultation system"""
    return EpilepsyConsultant()


__all__ = [
    'ConsultationComplexity',
    'ConsultationFocus',
    'ConsultationResult',
    'EpilepsyConsultant',
    'create_epilepsy_consultant'
]