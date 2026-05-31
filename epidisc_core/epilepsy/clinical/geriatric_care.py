"""
EPIDISC Geriatric Epilepsy Care System
=====================================

Comprehensive epilepsy care for elderly patients including post-stroke
epilepsy, polypharmacy considerations, and age-specific management.

Based on:
- Geriatric epilepsy clinical guidelines (2022-2024)
- Post-stroke epilepsy studies
- Elderly-specific ASM considerations
- Falls and safety in elderly epilepsy patients

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class GeriatricEpilepsyType(Enum):
    """Common epilepsy types in elderly"""
    POST_STROKE = "post_stroke"                    # Most common
    DEGENERATIVE = "degenerative"                # Dementia-related
    METABOLIC = "metabolic"                      # Systemic causes
    NEOPLASTIC = "neoplastic"                    # Brain tumors
    TRAUMATIC = "traumatic"                      # Post-traumatic
    UNKNOWN = "unknown"                          # Cryptogenic


class ElderlyRiskFactor(Enum):
    """Risk factors specific to elderly epilepsy"""
    FALL_RISK = "fall_risk"                      # Seizure-related falls
    COGNITIVE_DECLINE = "cognitive_decline"      # ASM cognitive effects
    POLYPHARMACY = "polypharmacy"                # Drug interactions
    RENAL_IMPAIRMENT = "renal_impairment"      # Reduced clearance
    FRAILTY = "frailty"                          # General vulnerability


@dataclass
class GeriatricEpilepsyAssessment:
    """
    Complete geriatric epilepsy assessment

    Elderly-specific evaluation including post-stroke epilepsy,
    polypharmacy review, cognitive considerations, and fall prevention.
    """

    epilepsy_type: Optional[GeriatricEpilepsyType]
    etiology: str
    fall_risk_assessment: str
    cognitive_status: str
    polypharmacy_review: List[str]
    asm_recommendations: List[str]
    dose_adjustments: List[str]
    safety_recommendations: List[str]
    driving_assessment: str
    quality_of_life_considerations: List[str]


class GeriatricEpilepsyCare:
    """
    Comprehensive geriatric epilepsy care system

    Evidence-based approach to epilepsy in elderly patients
    with age-specific considerations and management.
    """

    # Post-stroke epilepsy (most common elderly epilepsy)
    POST_STROKE_EPILEPSY = {
        "incidence": "5-20% of stroke survivors develop epilepsy",
        "time_course": [
            "Early seizures (within 1 week): 2-5%",
            "Late seizures (after 1 week): 3-10%",
            "Highest risk: Large cortical strokes, hemorrhagic strokes"
        ],
        "risk_factors": [
            "Cortical involvement",
            "Large stroke size",
            "Hemorrhagic stroke",
            "Early post-stroke seizures"
        ],
        "prophylaxis": "Controversial, but consider if high risk",
        "treatment": "Standard ASM selection (avoid enzyme inducers with warfarin)"
    }

    # Elderly-specific ASM considerations
    ELDERLY_ASM_CONSIDERATIONS = {
        "levetiracetam": {
            "advantages": [
                "No enzyme induction (good for warfarin)",
                "Renally excreted (dose adjustment needed)",
                "Few drug interactions",
                "Well tolerated overall"
            ],
            "disadvantages": [
                "Behavioral side effects common",
                "Can worsen psychiatric conditions",
                "Requires renal dose adjustment"
            ],
            "elderly_dosing": "Start 250mg BID, titrate slowly, monitor renal function",
            "recommendation": "✅ GOOD CHOICE FOR ELDERLY (watch behavioral effects)"
        },
        "lamotrigine": {
            "advantages": [
                "No enzyme induction",
                "Cognitive-friendly",
                "Few drug interactions",
                "Good tolerability"
            ],
            "disadvantages": [
                "Slow titration (weeks to therapeutic dose)",
                "Rash risk ( Stevens-Johnson rare in elderly)",
                "Renally excreted (dose adjustment needed)"
            ],
            "elderly_dosing": "Start 25mg daily, titrate slowly every 2-4 weeks",
            "recommendation": "✅ EXCELLENT CHOICE FOR ELDERLY (cognitive profile)"
        },
        "carbamazepine": {
            "advantages": [
                "Inexpensive",
                "Well-studied",
                "Effective for focal epilepsy"
            ],
            "disadvantages": [
                "⚠️ ENZYME INDUCER (major drug interactions)",
                "⚠️ Worsens warfarin anticoagulation",
                "⚠️ Cognitive side effects (drowsiness, dizziness)",
                "⚠️ Hyponatremia risk",
                "⚠️ Cardiac conduction effects"
            ],
            "elderly_dosing": "Start 100mg BID, titrate slowly",
            "recommendation": "⚠️ USE WITH CAUTION IN ELDERLY (many disadvantages)"
        },
        "valproate": {
            "advantages": [
                "Broad-spectrum",
                "No enzyme induction",
                "Well-studied"
            ],
            "disadvantages": [
                "⚠️ Tremor common (elderly especially sensitive)",
                "⚠️ Weight gain",
                "⚠️ Thrombocytopenia risk",
                "⚠️ Hepatic metabolism (caution in liver disease)"
            ],
            "elderly_dosing": "Start 125mg BID, monitor liver function",
            "recommendation": "⚠️ USE WITH CAUTION (tremor and liver concerns)"
        },
        "brivaracetam": {
            "advantages": [
                "SV2A binder (similar to levetiracetam)",
                "Fewer behavioral side effects",
                "Rapid titration",
                "No enzyme induction"
            ],
            "disadvantages": [
                "Expensive",
                "Limited experience in elderly",
                "Renally excreted"
            ],
            "elderly_dosing": "Start 25mg BID, titrate to 50mg BID",
            "recommendation": "✅ GOOD CHOICE (fewer behavioral effects than levetiracetam)"
        },
        "lacosamide": {
            "advantages": [
                "No significant drug interactions",
                "Rapid titration",
                "IV formulation available"
            ],
            "disadvantages": [
                "⚠️ Can worsen generalized epilepsy",
                "⚠️ Cardiac conduction effects (PR prolongation)",
                "Renally excreted"
            ],
            "elderly_dosing": "Start 50mg BID, monitor ECG",
            "recommendation": "⚠️ USE WITH CAUTION (cardiac effects, focal only)"
        }
    }

    @classmethod
    def assess_geriatric_epilepsy(
        cls,
        patient_data: Dict,
        clinical_information: Dict
    ) -> GeriatricEpilepsyAssessment:
        """
        Comprehensive geriatric epilepsy assessment

        Args:
            patient_data: Elderly patient information
            clinical_information: Clinical details

        Returns:
            GeriatricEpilepsyAssessment with complete evaluation
        """
        age = patient_data.get("age", 0)
        if age < 65:
            return GeriatricEpilepsyAssessment(
                epilepsy_type=None,
                etiology="Not geriatric patient",
                fall_risk_assessment="Not applicable",
                cognitive_status="Not applicable",
                polypharmacy_review=["Not applicable"],
                asm_recommendations=[],
                dose_adjustments=[],
                safety_recommendations=[],
                driving_assessment="Not applicable",
                quality_of_life_considerations=[]
            )

        # Determine epilepsy type
        epilepsy_type = cls._determine_elderly_epilepsy_type(clinical_information)
        etiology = cls._determine_etiology(clinical_information)

        # Fall risk assessment
        fall_risk = cls._assess_fall_risk(clinical_information)

        # Cognitive status
        cognitive = cls._assess_cognitive_status(clinical_information)

        # Polypharmacy review
        polypharmacy = cls._review_polypharmacy(
            clinical_information.get("current_medications", []),
            clinical_information
        )

        # ASM recommendations
        asm_recommendations = cls._get_elderly_asm_recommendations(
            clinical_information
        )

        # Dose adjustments
        dose_adjustments = cls._get_elderly_dose_adjustments(
            patient_data, clinical_information
        )

        # Safety recommendations
        safety = cls._get_elderly_safety_recommendations(
            clinical_information
        )

        # Driving assessment
        driving = cls._assess_elderly_driving(
            clinical_information
        )

        # Quality of life
        qol = cls._get_elderly_qol_considerations()

        return GeriatricEpilepsyAssessment(
            epilepsy_type=epilepsy_type,
            etiology=etiology,
            fall_risk_assessment=fall_risk,
            cognitive_status=cognitive,
            polypharmacy_review=polypharmacy,
            asm_recommendations=asm_recommendations,
            dose_adjustments=dose_adjustments,
            safety_recommendations=safety,
            driving_assessment=driving,
            quality_of_life_considerations=qol
        )

    @classmethod
    def _determine_elderly_epilepsy_type(cls, clinical_info: Dict) -> GeriatricEpilepsyType:
        """Determine epilepsy type in elderly patient"""
        if "stroke" in clinical_info.get("etiology", "").lower():
            return GeriatricEpilepsyType.POST_STROKE
        elif "dementia" in clinical_info.get("comorbidities", "").lower():
            return GeriatricEpilepsyType.DEGENERATIVE
        elif "tumor" in clinical_info.get("etiology", "").lower():
            return GeriatricEpilepsyType.NEOPLASTIC
        elif "trauma" in clinical_info.get("etiology", "").lower():
            return GeriatricEpilepsyType.TRAUMATIC
        else:
            return GeriatricEpilepsyType.UNKNOWN

    @classmethod
    def _determine_etiology(cls, clinical_info: Dict) -> str:
        """Determine likely etiology"""
        etiology = clinical_info.get("etiology", "").lower()

        if "stroke" in etiology:
            return "Post-stroke epilepsy (most common in elderly)"
        elif "degenerative" in etiology or "dementia" in etiology:
            return "Neurodegenerative disease (Alzheimer's, vascular dementia)"
        elif "metabolic" in etiology:
            return "Metabolic cause (electrolytes, renal failure, liver disease)"
        elif "tumor" in etiology:
            return "Brain tumor (primary or metastatic)"
        elif "trauma" in etiology:
            return "Traumatic brain injury sequelae"
        elif "alcohol" in etiology:
            return "Alcohol-related seizures"
        else:
            return "Cryptogenic (unknown etiology)"

    @classmethod
    def _assess_fall_risk(cls, clinical_info: Dict) -> str:
        """Assess fall risk in elderly epilepsy patient"""
        risk_factors = []

        seizure_frequency = clinical_info.get("seizure_frequency", "").lower()
        if "gtcs" in seizure_frequency or "convulsive" in seizure_frequency:
            risk_factors.append("Convulsive seizures")

        if "daily" in seizure_frequency or "frequent" in seizure_frequency:
            risk_factors.append("Frequent seizures")

        if "unsteady" in clinical_info.get("mobility", "").lower():
            risk_factors.append("Mobility problems")

        if "weakness" in clinical_info.get("examination", "").lower():
            risk_factors.append("Muscle weakness")

        if len(risk_factors) >= 2:
            return f"🚨 HIGH FALL RISK: {', '.join(risk_factors)}"
        elif len(risk_factors) == 1:
            return f"⚠️ MODERATE FALL RISK: {risk_factors[0]}"
        else:
            return "✓ Low fall risk (with appropriate precautions)"

    @classmethod
    def _assess_cognitive_status(cls, clinical_info: Dict) -> str:
        """Assess cognitive status"""
        cognitive = clinical_info.get("cognitive_status", "").lower()

        if "dementia" in cognitive:
            return "🧠 DEMENTIA PRESENT - ASM selection critical (avoid cognitive impairment)"
        elif "mci" in cognitive:
            return "🧠 MILD COGNITIVE IMPAIRMENT - cognitive-friendly ASMs preferred"
        elif "normal" in cognitive:
            return "✓ Normal cognition"
        else:
            return "⚠️ Cognitive assessment recommended"

    @classmethod
    def _review_polypharmacy(cls, medications: List[str], clinical_info: Dict) -> List[str]:
        """Review polypharmacy and drug interactions"""
        review = [
            "💊 POLYPHARMACY REVIEW:"
        ]

        if len(medications) > 5:
            review.append(f"⚠️ HIGH POLYPHARMACY ({len(medications)} medications)")
            review.append("• Review all medications for necessity")
            review.append("• Consider deprescribing where possible")

        # Check for drug interactions
        from ..knowledge.pharmacology import ASMDatabase
        interactions = ASMDatabase.get_all_interactions(medications)

        if interactions:
            review.extend([
                "",
                "⚠️ DRUG INTERACTIONS IDENTIFIED:"
            ])
            review.extend(interactions)

        # Check for fall-risk medications
        fall_risk_meds = ["benzodiazepines", "z-drugs", "antipsychotics", "antidepressants"]
        for med in medications:
            if any(fall_type in med.lower() for fall_type in fall_risk_meds):
                review.append(f"⚠️ {med} increases fall risk")

        return review if review and len(review) > 1 else ["✓ Polypharmacy review complete"]

    @classmethod
    def _get_elderly_asm_recommendations(cls, clinical_info: Dict) -> List[str]:
        """Get ASM recommendations specific to elderly"""
        recommendations = [
            "💊 ELDERLY ASM RECOMMENDATIONS:",
            "",
            "✅ PREFERRED CHOICES:",
            "• Lamotrigine (cognitive-friendly, well-tolerated)",
            "• Levetiracetam (watch behavioral side effects)",
            "• Brivaracetam (fewer behavioral effects)",
            "",
            "⚠️ USE WITH CAUTION:",
            "• Carbamazepine (enzyme inducer, cognitive effects)",
            "• Valproate (tremor, liver concerns)",
            "• Phenytoin (cognitive effects, ataxia)",
            "",
            "💡 ELDERLY-SPECIFIC CONSIDERATIONS:",
            "• Start low, go slow",
            "• Monitor renal function (dose adjustment)",
            "• Monitor for cognitive side effects",
            "• Fall prevention essential",
            "• Drug interaction review critical"
        ]

        return recommendations

    @classmethod
    def _get_elderly_dose_adjustments(cls, patient_data: Dict, clinical_info: Dict) -> List[str]:
        """Get dose adjustment recommendations for elderly"""
        adjustments = []

        renal = patient_data.get("renal_impairment", False)
        hepatic = patient_data.get("hepatic_impairment", False)

        if renal:
            adjustments.extend([
                "🚨 RENAL DOSE ADJUSTMENTS:",
                "• Levetiracetam: reduce dose (renally excreted)",
                "• Lamotrigine: reduce dose (renally excreted)",
                "• Pregabalin: reduce dose",
                "• Avoid gabapentin (renally excreted)",
                "• Monitor renal function"
            ])

        if hepatic:
            adjustments.extend([
                "🚨 HEPATIC DOSE ADJUSTMENTS:",
                "• Valproate: reduce dose (hepatic metabolism)",
                "• Avoid carbamazepine (hepatic metabolism)",
                "• Avoid phenytoin (hepatic metabolism)",
                "• Monitor liver function"
            ])

        if not adjustments:
            adjustments.append("✓ No specific dose adjustments required")

        return adjustments

    @classmethod
    def _get_elderly_safety_recommendations(cls, clinical_info: Dict) -> List[str]:
        """Get elderly-specific safety recommendations"""
        return [
            "👴 ELDERLY SAFETY RECOMMENDATIONS:",
            "",
            "FALL PREVENTION:",
            "• Home safety assessment",
            "• Remove hazards (rugs, loose carpets)",
            "• Install grab bars in bathroom",
            "• Night lights recommended",
            "• Consider hip protector if high risk",
            "",
            "SEIZURE PRECAUTIONS:",
            "• Avoid heights (stairs, ladders)",
            "• Supervised bathing if frequent seizures",
            "• Seizure alarm if nocturnal seizures",
            "• Caregiver education essential",
            "",
            "COGNITIVE MONITORING:",
            "• Regular cognitive assessment",
            "• Monitor for ASM cognitive effects",
            "• Assess for depression and anxiety",
            "• Screen for delirium risk",
            "",
            "💡 QUALITY OF LIFE:",
            "• Maintain independence as appropriate",
            "• Social engagement important",
            "• Physical activity (with precautions)",
            "• Regular review of medication necessity"
        ]

    @classmethod
    def _assess_elderly_driving(cls, clinical_info: Dict) -> str:
        """Assess driving fitness in elderly"""
        seizure_free = clinical_info.get("seizure_free_period", "").lower()

        # Additional considerations for elderly
        vision = clinical_info.get("vision", "")
        reaction_time = clinical_info.get("reaction_time", "")
        mobility = clinical_info.get("mobility", "")

        concerns = []
        if "impaired" in vision:
            concerns.append("vision impairment")
        if "slowed" in reaction_time:
            concerns.append("slowed reaction time")
        if "impaired" in mobility:
            concerns.append("mobility impairment")

        if "year" in seizure_free:
            base = "✅ May be eligible for driving (12-month seizure-free period met)"
        else:
            base = "🚗 Not driving until 12-month seizure-free period"

        if concerns:
            return f"{base} (Additional considerations: {', '.join(concerns)})"
        else:
            return base

    @classmethod
    def _get_elderly_qol_considerations(cls) -> List[str]:
        """Get quality of life considerations for elderly"""
        return [
            "💛 ELDERLY QUALITY OF LIFE:",
            "",
            "INDEPENDENCE:",
            "• Maintain independence where safe",
            "• Assistive devices if needed",
            "• Balance autonomy with safety",
            "",
            "SOCIAL ENGAGEMENT:",
            "• Social activities important",
            "• Seizure precautions discussed",
            "• Support groups available",
            "",
            "PHYSICAL ACTIVITY:",
            "• Exercise within safe limits",
            "• Fall prevention program",
            "• Physical therapy if needed",
            "",
            "COGNITIVE HEALTH:",
            "• Cognitive stimulation important",
            "• Mental health screening",
            "• Social engagement",
            "",
            "💡 CARRGIVER SUPPORT:",
            "• Family education essential",
            "• Respite care options",
            "• Support for caregivers"
        ]

    @classmethod
    def get_post_stroke_epilepsy_guidance(cls) -> List[str]:
        """Get post-stroke epilepsy management guidance"""
        return [
            "🧠 POST-STROKE EPILEPSY:",
            "",
            "RISK FACTORS:",
            "• Large cortical strokes",
            "Hemorrhagic strokes",
            "• Early post-stroke seizures",
            "• Cortical involvement",
            "",
            "INCIDENCE:",
            "• 5-20% of stroke survivors develop epilepsy",
            "• Highest risk in first year post-stroke",
            "• Risk remains elevated for years",
            "",
            "PROPHYLAXIS:",
            "• Controversial - not routinely recommended",
            "• Consider high-risk patients",
            "• Weigh benefits vs ASM risks",
            "",
            "TREATMENT:",
            "• Standard ASM selection when seizures occur",
            "• Avoid enzyme inducers (warfarin interaction)",
            "• Consider levetiracetam or lamotrigine",
            "• Monitor for drug interactions",
            "",
            "💡 CLINICAL PEARLS:",
            "• Early post-stroke seizures don't always mean epilepsy",
            "• Late seizures more predictive of epilepsy",
            "• ASM prophylaxis controversial",
            "• Individualized treatment approach"
        ]


__all__ = [
    'GeriatricEpilepsyType',
    'ElderlyRiskFactor',
    'GeriatricEpilepsyAssessment',
    'GeriatricEpilepsyCare'
]
