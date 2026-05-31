"""
EPIDISC Psychiatry and PNES Integration
==========================================

Comprehensive psychiatric comorbidity and psychogenic non-epileptic
seizure (PNES) integration system for epilepsy consultation.

Based on:
- Evidence-based PNES diagnosis and management
- Psychiatric comorbidity in epilepsy literature
- Multidisciplinary treatment approaches
- Integrated epilepsy-psychiatry care models

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class PsychiatricComorbidity(Enum):
    """Common psychiatric comorbidities in epilepsy"""
    DEPRESSION = "depression"
    ANXIETY = "anxiety"
    BIPOLAR_DISORDER = "bipolar_disorder"
    PSYCHOSIS = "psychosis"
    PTSD = "ptsd"
    ADHD = "adhd"
    AUTISM = "autism"
    PERSONALITY_DISORDER = "personality_disorder"


class PNESLikelihood(Enum):
    """PNES likelihood categories"""
    DEFINITE = "definite"                      # Video-EEG confirmed
    HIGH_PROBABILITY = "high_probability"      # Strong clinical suspicion
    MODERATE_PROBABILITY = "moderate_probability"  # Possible PNES
    LOW_PROBABILITY = "low_probability"        # Unlikely PNES
    RULED_OUT = "ruled_out"                    # Epilepsy confirmed


@dataclass
class PNESDiagnosisResult:
    """
    Complete PNES diagnostic assessment

    Includes likelihood assessment, diagnostic confidence,
    treatment recommendations, and multidisciplinary approach.
    """

    likelihood: PNESLikelihood
    confidence: float
    pnes_features: List[str]
    epilepsy_features: List[str]
    diagnostic_recommendations: List[str]
    treatment_approach: str
    prognosis: str
    multidisciplinary_team: List[str]
    communication_guidance: List[str]


class PsychiatricIntegration:
    """
    Comprehensive psychiatric integration for epilepsy

    Evidence-based approach to psychiatric comorbidities and
    PNES with multidisciplinary treatment planning.
    """

    # Depression in epilepsy
    DEPRESSION_IN_EPILEPSY = {
        "prevalence": "30-50% (vs 10-15% general population)",
        "risk_factors": [
            "Drug-resistant epilepsy",
            "Temporal lobe epilepsy",
            "Frequent seizures",
            "Earlier age of onset"
        ],
        "symptoms": [
            "Low mood",
            "Anhedonia",
            "Sleep disturbance",
            "Fatigue",
            "Worthlessness",
            "Suicidal ideation"
        ],
        "asm_effects": [
            "Levetiracetam → depression risk",
            "Barbiturates → depression risk",
            "Topiramate → cognitive effects mimicking depression"
        ],
        "treatment": [
            "SSRIs generally safe with ASMs",
            "Monitor drug interactions (enzyme inducers)",
            "Consider psychotherapy (CBT)",
            "Screen for suicidality regularly"
        ],
        "screening": [
            "PHQ-9 (9-item depression scale)",
            "Regular mood assessment",
            "Suicide risk assessment"
        ]
    }

    # Anxiety in epilepsy
    ANXIETY_IN_EPILEPSY = {
        "prevalence": "20-40%",
        "types": [
            "Anticipatory anxiety (seizure occurrence)",
            "Interictal anxiety",
            "Periictal anxiety",
            "Social anxiety"
        ],
        "symptoms": [
            "Worry about seizures",
            "Avoidance behaviors",
            "Panic symptoms",
            "Sleep disturbance",
            "Concentration difficulties"
        ],
        "treatment": [
            "SSRIs first-line",
            "CBT effective",
            "Relaxation techniques",
            "Psychoeducation about epilepsy"
        ],
        "screening": [
            "GAD-7 (7-item anxiety scale)",
            "Seizure worry questionnaire",
            "Anxiety severity assessment"
        ]
    }

    # PNES clinical features
    PNES_DIAGNOSTIC_CRITERIA = {
        "definite": {
            "description": "Video-EEG documented PNES",
            "requirements": [
                "Typical event captured on video-EEG",
                "EEG shows no epileptiform activity during event",
                "Event is stereotyped to reported events"
            ],
            "specificity": "95-100%",
            "sensitivity": "Depends on event capture"
        },
        "probable": {
            "description": "High clinical suspicion without video-EEG confirmation",
            "requirements": [
                "Multiple PNES-favoring features",
                "Low epilepsy likelihood",
                "Inconsistent semiology"
            ],
            "diagnostic_yield": "70-80% with video-EEG"
        }
    }

    @classmethod
    def assess_psychiatric_comorbidity(
        cls,
        clinical_features: Dict[str, str]
    ) -> Tuple[List[PsychiatricComorbidity], List[str]]:
        """
        Assess for psychiatric comorbidities in epilepsy patient

        Args:
            clinical_features: Clinical information

        Returns:
            (comorbidities, recommendations)
        """
        comorbidities = []
        recommendations = []

        history = clinical_features.get("history", "").lower()
        symptoms = clinical_features.get("psychiatric_symptoms", "").lower()

        # Depression screening
        depression_indicators = [
            "low mood", "anhedonia", "worthlessness", "guilt",
            "sleep disturbance", "fatigue", "suicidal", "hopeless"
        ]

        if any(indicator in history or indicator in symptoms for indicator in depression_indicators):
            comorbidities.append(PsychiatricComorbidity.DEPRESSION)
            recommendations.extend([
                "💊 DEPRESSION ASSESSMENT:",
                "• Administer PHQ-9 depression screening",
                "• Assess suicide risk (critical)",
                "• Review ASMs for mood effects (levetiracetam)",
                "• Consider psychiatry referral",
                "• SSRIs generally safe with most ASMs"
            ])

        # Anxiety screening
        anxiety_indicators = [
            "worry", "anxious", "panic", "avoidance", "nervous",
            "seizure worry", "anticipatory anxiety"
        ]

        if any(indicator in history or indicator in symptoms for indicator in anxiety_indicators):
            comorbidities.append(PsychiatricComorbidity.ANXIETY)
            recommendations.extend([
                "😰 ANXIETY ASSESSMENT:",
                "• Administer GAD-7 anxiety screening",
                "• Assess for panic disorder",
                "• Consider seizure-specific anxiety",
                "• CBT effective for anxiety disorders"
            ])

        # Psychosis screening
        psychosis_indicators = [
            "hallucination", "delusion", "paranoid", "psychosis",
            "schizophrenia", "thought disorder"
        ]

        if any(indicator in history or indicator in symptoms for indicator in psychosis_indicators):
            comorbidities.append(PsychiatricComorbidity.PSYCHOSIS)
            recommendations.extend([
                "🔮 PSYCHOSIS ASSESSMENT:",
                "• Urgent psychiatry referral",
                "• Consider ASM effects (levetiracetam psychosis)",
                "• Differentiate from postictal psychosis",
                "• Consider antipsychotic medication"
            ])

        return comorbidities, recommendations

    @classmethod
    def comprehensive_pnes_assessment(
        cls,
        clinical_features: Dict[str, str]
    ) -> PNESDiagnosisResult:
        """
        Comprehensive PNES diagnostic assessment

        Args:
            clinical_features: Complete clinical information

        Returns:
            PNESDiagnosisResult with complete assessment
        """
        from ..knowledge.differential_diagnosis import PNESDiagnosis

        # Use existing PNES diagnosis system
        likelihood, probability, reasoning = PNESDiagnosis.assess_pnes_probability(
            clinical_features
        )

        # Extract PNES and epilepsy features
        pnes_features = []
        epilepsy_features = []

        for reason in reasoning:
            if "favors PNES" in reason:
                feature = reason.replace("+", "").replace("favors PNES", "").strip()
                pnes_features.append(feature)
            elif "favors epilepsy" in reason:
                feature = reason.replace("-", "").replace("favors epilepsy", "").strip()
                epilepsy_features.append(feature)

        # Determine PNES likelihood category
        if probability > 0.85:
            pnes_category = PNESLikelihood.HIGH_PROBABILITY
        elif probability > 0.70:
            pnes_category = PNESLikelihood.HIGH_PROBABILITY
        elif probability > 0.40:
            pnes_category = PNESLikelihood.MODERATE_PROBABILITY
        elif probability > 0.20:
            pnes_category = PNESLikelihood.LOW_PROBABILITY
        else:
            pnes_category = PNESLikelihood.RULED_OUT

        # Generate diagnostic recommendations
        if pnes_category in [PNESLikelihood.HIGH_PROBABILITY, PNESLikelihood.MODERATE_PROBABILITY]:
            diagnostic_recommendations = [
                "🎺 VIDEO-EEG MONITORING RECOMMENDED:",
                "• Admit for video-EEG telemetry",
                "• Gold standard for PNES diagnosis",
                "• Aim to capture 2-3 typical events",
                "• Sensitivity: 85-95%, Specificity: 95-100%"
            ]

            if clinical_features.get("frequency", "") == "frequent":
                diagnostic_recommendations.append("✅ High event frequency → high diagnostic yield")
            else:
                diagnostic_recommendations.append("⏳ Consider induction techniques if events infrequent")

        elif pnes_category == PNESLikelihood.LOW_PROBABILITY:
            diagnostic_recommendations = [
                "✓ PNES unlikely - epilepsy more probable",
                "• Continue epilepsy evaluation",
                "• Consider PNES if clinical picture changes"
            ]

        else:
            diagnostic_recommendations = [
                "✓ Epilepsy confirmed - PNES ruled out",
                "• Continue epilepsy management",
                "• Video-EEG monitoring if diagnosis uncertain"
            ]

        # Treatment approach
        if pnes_category in [PNESLikelihood.HIGH_PROBABILITY, PNESLikelihood.MODERATE_PROBABILITY]:
            treatment_approach = """
            🧠 PNES TREATMENT APPROACH:

            FIRST-LINE: Cognitive Behavioral Therapy (CBT)
            • 70-80% show significant improvement
            • 12-16 sessions recommended
            • Includes psychoeducation, cognitive restructuring

            SECOND-LINE:
            • Psychiatric medication for comorbidities
            • Physical therapy for functional symptoms
            • Occupational therapy

            PROGNOSIS:
            • 50-70% achieve remission with treatment
            • Better outcomes with early diagnosis
            • Worse outcomes with delayed diagnosis
            """

            # Multidisciplinary team
            multidisciplinary_team = [
                "Psychiatrist (lead)",
                "Neurologist (rule out epilepsy)",
                "Clinical psychologist (CBT provider)",
                "Neuropsychologist (assessment)",
                "Epilepsy specialist nurse (education)"
            ]

            # Communication guidance
            communication_guidance = [
                "🗣️ COMMUNICATION APPROACH:",
                "• Use 'functional' not 'fake'",
                "• Emphasize 'events are real'",
                "• Explain stress-response model",
                "• Focus on treatability",
                "• Avoid confrontation",
                "• Include family in education"
            ]

            prognosis = "Good with appropriate treatment (50-70% improvement)"

        else:
            treatment_approach = "Continue epilepsy management"
            multidisciplinary_team = ["Neurologist", "Epilepsy nurse"]
            communication_guidance = []
            prognosis = "N/A (epilepsy confirmed)"

        return PNESDiagnosisResult(
            likelihood=pnes_category,
            confidence=probability,
            pnes_features=pnes_features,
            epilepsy_features=epilepsy_features,
            diagnostic_recommendations=diagnostic_recommendations,
            treatment_approach=treatment_approach,
            prognosis=prognosis,
            multidisciplinary_team=multidisciplinary_team,
            communication_guidance=communication_guidance
        )

    @classmethod
    def get_psychiatric_screening_protocol(cls) -> List[str]:
        """Get recommended psychiatric screening protocol for epilepsy clinic"""
        return [
            "🧠 PSYCHIATRIC SCREENING PROTOCOL:",
            "",
            "ROUTINE SCREENING (All epilepsy patients):",
            "• PHQ-9 (depression) - Every 6 months",
            "• GAD-7 (anxiety) - Every 6 months",
            "• Suicide risk assessment - At each visit",
            "",
            "HIGH-RISK GROUPS:",
            "• Drug-resistant epilepsy",
            "• Temporal lobe epilepsy",
            "• History of psychiatric illness",
            "• Recent ASM changes",
            "",
            "🎯 RED FLAGS (Immediate psychiatry referral):",
            "• Suicidal ideation",
            "• Psychotic symptoms",
            "• Severe depression",
            "• Manic symptoms",
            "",
            "💡 CLINICAL PEARLS:",
            "• Depression common but treatable",
            "• Anxiety often seizure-related",
            "• Psychosis can be ASM-induced",
            "• Psychiatric comorbidities affect quality of life",
            "• Treatment improves seizure outcomes"
        ]

    @classmethod
    def get_mental_health_integration(cls) -> List[str]:
        """Get mental health integration recommendations"""
        return [
            "🔗 MENTAL HEALTH INTEGRATION:",
            "",
            "COLLABORATIVE CARE MODEL:",
            "• Regular psychiatry input",
            "• Shared care protocols",
            "• Multidisciplinary team meetings",
            "• Integrated care pathways",
            "",
            "SCREENING PROTOCOLS:",
            "• Systematic mood assessment",
            "• Routine anxiety screening",
            "• Suicide risk monitoring",
            "• Quality of life assessment",
            "",
            "TREATMENT APPROACHES:",
            "• CBT for anxiety/depression",
            "• Medication management",
            "• Psychoeducation",
            "• Support groups",
            "• Family therapy (when indicated)",
            "",
            "💡 KEY PRINCIPLES:",
            "• Mental health affects seizure control",
            "• ASMs can affect mood",
            "• Integrated care improves outcomes",
            "• Quality of life optimization essential"
        ]


__all__ = [
    'PsychiatricComorbidity',
    'PNESLikelihood',
    'PNESDiagnosisResult',
    'PsychiatricIntegration'
]