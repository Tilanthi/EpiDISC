"""
EPIDISC Women's Health and Pregnancy Epilepsy Care
==================================================

Comprehensive women's epilepsy care system including pregnancy,
teratogenicity, contraception, catamenial epilepsy, and menopause.

Based on:
- Pregnancy registries and safety data
- ILAE women's epilepsy guidelines
- UK Epilepsy and Pregnancy register
- FDA/EMA pregnancy categories
- Current teratogenicity evidence (2024-2026)

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class PregnancyTrimester(Enum):
    """Pregnancy trimesters for ASM management"""
    PRE_CONCEPTION = "pre_conception"              # Planning pregnancy
    FIRST_TRIMESTER = "first_trimester"          # Weeks 1-12 (organogenesis)
    SECOND_TRIMESTER = "second_trimester"        # Weeks 13-26
    THIRD_TRIMESTER = "third_trimester"          # Weeks 27-40
    POSTPARTUM = "postpartum"                    # Post-delivery
    LACTATION = "lactation"                      # Breastfeeding


class ContraceptionCategory(Enum):
    """Contraception categories for ASM interactions"""
    NO_INTERACTION = "no_interaction"            # No effect on contraception
    REDUCED_EFFICACY = "reduced_efficacy"        # Decreases contraceptive efficacy
    ALTERNATIVE_NEEDED = "alternative_needed"    # Requires alternative contraception


class TeratogenicityRisk(Enum):
    """ASM teratogenicity risk categories"""
    HIGH = "high"                                # Major teratogen (Category D/X)
    MODERATE = "moderate"                        # Moderate risk (Category C/D)
    LOW = "low"                                  # Low risk (Category B/C)
    UNKNOWN = "unknown"                          # Insufficient data


@dataclass
class WomenEpilepsyCare:
    """
    Complete women's epilepsy care assessment

    Includes pregnancy planning, ASM selection, teratogenicity
    counseling, and comprehensive care recommendations.
    """

    pregnancy_stage: Optional[PregnancyTrimester]
    current_medications: List[str]
    teratogenicity_assessment: Dict[str, TeratogenicityRisk]
    pregnancy_recommendations: List[str]
    contraception_recommendations: List[str]
    asm_adjustments: List[str]
    monitoring_requirements: List[str]
    breastfeeding_guidance: List[str]
    risk_counseling: List[str]


class WomenHealthEpilepsy:
    """
    Comprehensive women's health epilepsy care system

    Evidence-based approach to epilepsy in women including
    pregnancy, contraception, teratogenicity, and hormonal
    considerations.
    """

    # ASM teratogenicity data (based on pregnancy registries)
    ASM_TERATOGENICITY = {
        "valproate": {
            "risk": TeratogenicityRisk.HIGH,
            "major_malformations": "10% risk (vs 2-3% background)",
            "specific_defects": [
                "Neural tube defects (1-2%)",
                "Cleft lip/palate",
                "Cardiac defects",
                "Skeletal abnormalities",
                "Hypospadias",
                "Autism spectrum disorder (8% vs 1% background)"
            ],
            "neurodevelopmental": "IQ reduction 8-10 points (dose-dependent)",
            "recommendation": "⚠️ AVOID IN PREGNANCY IF POSSIBLE",
            "alternative": "Use lamotrigine or levetiracetam instead"
        },
        "phenobarbital": {
            "risk": TeratogenicityRisk.HIGH,
            "major_malformations": "6-7% risk",
            "specific_defects": [
                "Cardiac defects",
                "Cleft lip/palate",
                "Microcephaly"
            ],
            "neurodevelopmental": "Possible cognitive effects",
            "recommendation": "⚠️ AVOID IN PREGNANCY IF POSSIBLE",
            "alternative": "Use levetiracetam or lamotrigine"
        },
        "phenytoin": {
            "risk": TeratogenicityRisk.HIGH,
            "major_malformations": "5-10% risk",
            "specific_defects": [
                "Fetal hydantoin syndrome",
                "Facial dysmorphism",
                "Hypoplasia of digits/nails",
                "Growth retardation",
                "Developmental delay"
            ],
            "neurodevelopmental": "Cognitive effects reported",
            "recommendation": "⚠️ AVOID IN PREGNANCY IF POSSIBLE",
            "alternative": "Use levetiracetam or lamotrigine"
        },
        "carbamazepine": {
            "risk": TeratogenicityRisk.MODERATE,
            "major_malformations": "3-5% risk",
            "specific_defects": [
                "Neural tube defects (increased risk)",
                "Craniofacial defects",
                "Skeletal abnormalities"
            ],
            "neurodevelopmental": "Possible minor cognitive effects",
            "recommendation": "⚠️ USE WITH CAUTION, RISK-BENEFIT ASSESSMENT",
            "alternative": "Consider lamotrigine or levetiracetam"
        },
        "topiramate": {
            "risk": TeratogenicityRisk.MODERATE,
            "major_malformations": "2-4% risk",
            "specific_defects": [
                "Cleft lip/palate (2-3% risk)",
                "Low birth weight",
                "Growth restriction"
            ],
            "neurodevelopmental": "Limited data",
            "recommendation": "⚠️ AVOID IN FIRST TRIMESTER IF POSSIBLE",
            "alternative": "Use levetiracetam or lamotrigine"
        },
        "lamotrigine": {
            "risk": TeratogenicityRisk.LOW,
            "major_malformations": "2-3% risk (similar to background)",
            "specific_defects": [
                "Slightly increased cleft lip/palate (0.5% increase)"
            ],
            "neurodevelopmental": "No significant neurodevelopmental effects",
            "recommendation": "✅ PREFERRED IN PREGNANCY",
            "advantages": "Low teratogenicity, effective for broad spectrum epilepsy"
        },
        "levetiracetam": {
            "risk": TeratogenicityRisk.LOW,
            "major_malformations": "2-3% risk (similar to background)",
            "specific_defects": [
                "No consistent pattern identified"
            ],
            "neurodevelopmental": "Limited data but no major concerns",
            "recommendation": "✅ PREFERRED IN PREGNANCY",
            "advantages": "Low teratogenicity, rapid titration, no enzyme induction"
        },
        "oxcarbazepine": {
            "risk": TeratogenicityRisk.LOW,
            "major_malformations": "2-3% risk (similar to background)",
            "specific_defects": [
                "Limited data available"
            ],
            "neurodevelopmental": "Limited data",
            "recommendation": "✅ REASONABLE ALTERNATIVE",
            "considerations": "Structurally similar to carbamazepine but lower risk"
        },
        "benzodiazepines": {
            "risk": TeratogenicityRisk.MODERATE,
            "major_malformations": "Possible small increase",
            "specific_defects": [
                "Cleft lip/palate (possible)",
                "Floppy infant syndrome (postnatal)"
            ],
            "neurodevelopmental": "Possible withdrawal symptoms",
            "recommendation": "⚠️ AVOID IF POSSIBLE, USE LOWEST EFFECTIVE DOSE",
            "considerations": "Risk-benefit assessment needed for rescue use"
        }
    }

    # Contraception interactions
    CONTRACEPTION_INTERACTIONS = {
        "enzyme_inducers": {
            "medications": ["carbamazepine", "phenytoin", "phenobarbital", "topiramate", "oxcarbazepine"],
            "effect": "Decrease hormonal contraceptive efficacy",
            "recommendation": "⚠️ USE ADDITIONAL/ALTERNATIVE CONTRACEPTION",
            "alternatives": [
                "Higher dose combined oral contraceptive (50mcg estrogen)",
                "Depot progestin injection",
                "Intrauterine device (IUD)",
                "Barrier methods (condoms)"
            ]
        },
        "lamotrigine": {
            "medications": ["lamotrigine"],
            "effect": "Hormonal contraceptives decrease lamotrigine levels",
            "recommendation": "⚠️ MONITOR LAMOTRIGINE LEVELS",
            "considerations": [
                "May need dose increase when starting hormonal contraception",
                "May need dose decrease when stopping hormonal contraception",
                "Monitor for seizure control and lamotrigine side effects"
            ]
        },
        "no_interaction": {
            "medications": ["levetiracetam", "valproate", "brivaracetam", "perampanel", "lacosamide"],
            "effect": "No significant interaction",
            "recommendation": "✅ NO CONTRACEPTION ADJUSTMENT NEEDED"
        }
    }

    # Catamenial epilepsy patterns
    CATAMENIAL_EPILEPSY = {
        "definition": "Seizure patterns related to menstrual cycle",
        "patterns": {
            "perimenstrual": {
                "timing": "Days -3 to +3 from menstruation",
                "mechanism": "Progesterone withdrawal",
                "treatment": [
                    "Increase ASM dose perimenstrually",
                    "Consider progesterone supplementation",
                    "Consider acetazolamide"
                ]
            },
            "ovulation": {
                "timing": "Mid-cycle (days 10-16)",
                "mechanism": "Estrogen surge",
                "treatment": [
                    "Mid-cycle ASM increase",
                    "Consider hormonal manipulation"
                ]
            },
            "entire_cycle": {
                "timing": "Throughout luteal phase",
                "mechanism": "Hormonal fluctuation",
                "treatment": [
                    "Natural progesterone supplementation",
                    "Consider hormonal contraception to stabilize cycle"
                ]
            }
        }
    }

    @classmethod
    def assess_pregnancy_care(
        cls,
        pregnancy_stage: str,
        current_medications: List[str],
        clinical_context: Optional[Dict] = None
    ) -> WomenEpilepsyCare:
        """
        Comprehensive pregnancy epilepsy care assessment

        Args:
            pregnancy_stage: Current pregnancy stage
            current_medications: List of current ASMs
            clinical_context: Additional clinical information

        Returns:
            WomenEpilepsyCare with complete care recommendations
        """
        # Determine pregnancy stage
        stage = cls._determine_pregnancy_stage(pregnancy_stage)

        # Assess teratogenicity
        teratogenicity = {}
        for med in current_medications:
            med_lower = med.lower()
            if med_lower in cls.ASM_TERATOGENICITY:
                teratogenicity[med] = cls.ASM_TERATOGENICITY[med_lower]["risk"]

        # Generate recommendations
        recommendations = []
        asm_adjustments = []
        contraception_guidance = []

        # Pre-conception counseling
        if stage == PregnancyTrimester.PRE_CONCEPTION:
            recommendations.extend([
                "🤰 PRE-CONCEPTION COUNSELING:",
                "• Ideally plan pregnancy when seizure-free for 9-12 months",
                "• Optimize ASM regimen before conception",
                "• High-dose folic acid (5mg daily) START 3 MONTHS BEFORE CONCEPTION",
                "• Review all ASMs for teratogenicity",
                "• Consider lowest effective ASM dose",
                "• Aim for monotherapy if possible"
            ])

            # Check for high-risk ASMs
            for med in current_medications:
                med_lower = med.lower()
                if med_lower in ["valproate", "phenobarbital", "phenytoin"]:
                    asm_adjustments.append(
                        f"⚠️ CRITICAL: {med} HIGH TERATOGENIC RISK - "
                        f"CONSIDER DISCONTINUATION BEFORE PREGNANCY"
                    )
                elif med_lower == "topiramate":
                    asm_adjustments.append(
                        f"⚠️ {med} has moderate teratogenic risk - "
                        f"consider alternative if possible"
                    )

        # First trimester (organogenesis)
        elif stage == PregnancyTrimester.FIRST_TRIMESTER:
            recommendations.extend([
                "🤰 FIRST TRIMESTER CARE:",
                "• Continue high-dose folic acid (5mg daily)",
                "• Avoid valproate if possible (especially neural tube defects)",
                "• Consider switching high-risk ASMs",
                "• Monitor ASM levels (pharmacokinetic changes)",
                "• Detailed anatomy scan at 18-20 weeks",
                "• Maternal medicine follow-up"
            ])

        # Second trimester
        elif stage == PregnancyTrimester.SECOND_TRIMESTER:
            recommendations.extend([
                "🤰 SECOND TRIMESTER CARE:",
                "• Continue folic acid",
                "• Monitor ASM levels (volume changes)",
                "• Regular obstetric care",
                "• Fetal growth monitoring",
                "• Seizure frequency monitoring"
            ])

        # Third trimester
        elif stage == PregnancyTrimester.THIRD_TRIMESTER:
            recommendations.extend([
                "🤰 THIRD TRIMESTER CARE:",
                "• Continue ASM monitoring",
                "• Plan for delivery (seizure precautions)",
                "• Vitamin K supplementation (10mg PO daily) in last month",
                "• Plan for neonatal care (if high-risk ASMs)",
                "• Breastfeeding planning"
            ])

        # Postpartum
        elif stage == PregnancyTrimester.POSTPARTUM:
            recommendations.extend([
                "🤰 POSTPARTUM CARE:",
                "• Continue folic acid while breastfeeding",
                "• Monitor for postpartum seizures (hormonal changes)",
                "• ASM dose may need readjustment",
                "• Sleep deprivation prevention",
                "• Monitor for postpartum depression",
                "• Infant vitamin K if on enzyme-inducing ASMs"
            ])

        # Contraception guidance
        if clinical_context and clinical_context.get("need_contraception", False):
            contraception_guidance.extend(
                cls._get_contraception_recommendations(current_medications)
            )

        # Breastfeeding guidance
        breastfeeding_guidance = cls._get_breastfeeding_guidance(current_medications)

        # Risk counseling
        risk_counseling = cls._get_risk_counseling(current_medications)

        # Monitoring requirements
        monitoring = [
            "📋 MONITORING:",
            "• ASM levels each trimester",
            "• Seizure frequency monitoring",
            "• Obstetric ultrasounds (detailed anatomy scan 18-20 weeks)",
            "• Fetal growth monitoring",
            "• Maternal health monitoring"
        ]

        return WomenEpilepsyCare(
            pregnancy_stage=stage,
            current_medications=current_medications,
            teratogenicity_assessment=teratogenicity,
            pregnancy_recommendations=recommendations,
            contraception_recommendations=contraception_guidance,
            asm_adjustments=asm_adjustments,
            monitoring_requirements=monitoring,
            breastfeeding_guidance=breastfeeding_guidance,
            risk_counseling=risk_counseling
        )

    @classmethod
    def _determine_pregnancy_stage(cls, pregnancy_stage: str) -> PregnancyTrimester:
        """Determine pregnancy stage from input"""
        stage_lower = pregnancy_stage.lower()

        if "pre" in stage_lower or "planning" in stage_lower:
            return PregnancyTrimester.PRE_CONCEPTION
        elif "first" in stage_lower or "trimester1" in stage_lower:
            return PregnancyTrimester.FIRST_TRIMESTER
        elif "second" in stage_lower or "trimester2" in stage_lower:
            return PregnancyTrimester.SECOND_TRIMESTER
        elif "third" in stage_lower or "trimester3" in stage_lower:
            return PregnancyTrimester.THIRD_TRIMESTER
        elif "postpartum" in stage_lower or "post" in stage_lower:
            return PregnancyTrimester.POSTPARTUM
        elif "breastfeeding" in stage_lower or "lactation" in stage_lower:
            return PregnancyTrimester.LACTATION
        else:
            return PregnancyTrimester.PRE_CONCEPTION  # Default

    @classmethod
    def _get_contraception_recommendations(cls, medications: List[str]) -> List[str]:
        """Get contraception recommendations based on ASMs"""
        recommendations = [
            "💊 CONTRACEPTION RECOMMENDATIONS:"
        ]

        for med in medications:
            med_lower = med.lower()

            # Check if enzyme inducer
            if med_lower in cls.CONTRACEPTION_INTERACTIONS["enzyme_inducers"]["medications"]:
                recommendations.extend([
                    "",
                    f"⚠️ {med.upper()} REDUCES HORMONAL CONTRACEPTIVE EFFICACY",
                    "• Additional or alternative contraception required",
                    "• Consider IUD (most effective non-hormonal)",
                    "• Consider depot progestin injection",
                    "• If oral contraceptive: use 50mcg estrogen formulation"
                ])

            # Check lamotrigine specifically
            elif med_lower == "lamotrigine":
                recommendations.extend([
                    "",
                    f"⚠️ {med.upper()} LEVELS AFFECTED BY HORMONAL CONTRACEPTION",
                    "• Hormonal contraception decreases lamotrigine levels",
                    "• May need lamotrigine dose adjustment",
                    "• Monitor lamotrigine levels and seizure control"
                ])

        if len(medications) == 1 and medications[0].lower() in ["levetiracetam", "lamotrigine"]:
            recommendations.extend([
                "",
                "✅ Current ASMs do not significantly affect hormonal contraception"
            ])

        return recommendations

    @classmethod
    def _get_breastfeeding_guidance(cls, medications: List[str]) -> List[str]:
        """Get breastfeeding guidance for ASMs"""
        guidance = [
            "🤱 BREASTFEEDING GUIDANCE:",
            ""
        ]

        safe_medications = []
        caution_medications = []
        avoid_medications = []

        for med in medications:
            med_lower = med.lower()

            if med_lower in ["levetiracetam", "lamotrigine", "oxcarbazepine"]:
                safe_medications.append(med)
            elif med_lower in ["valproate", "carbamazepine", "phenytoin"]:
                caution_medications.append(med)
            elif med_lower in ["phenobarbital", "primidone"]:
                avoid_medications.append(med)

        if safe_medications:
            guidance.append("✅ GENERALLY SAFE DURING BREASTFEEDING:")
            for med in safe_medications:
                guidance.append(f"• {med.title()} - minimal excretion in breast milk")

        if caution_medications:
            guidance.append("")
            guidance.append("⚠️ USE WITH CAUTION DURING BREASTFEEDING:")
            for med in caution_medications:
                guidance.append(f"• {med.title()} - monitor infant for sedation")

        if avoid_medications:
            guidance.append("")
            guidance.append("⚠️ AVOID OR ALTERNATIVE PREFERRED:")
            for med in avoid_medications:
                guidance.append(f"• {med.title()} - may cause significant infant sedation")

        guidance.extend([
            "",
            "💡 GENERAL PRINCIPLES:",
            "• Breastfeeding generally encouraged",
            "• Monitor infant for sedation or feeding difficulties",
            "• Time feeds to minimize infant exposure",
            "• Discuss benefits/risks with patient"
        ])

        return guidance

    @classmethod
    def _get_risk_counseling(cls, medications: List[str]) -> List[str]:
        """Get comprehensive risk counseling"""
        counseling = [
            "⚠️ PREGNANCY RISK COUNSELING:",
            "",
            "BACKGROUND RISKS (All pregnancies):",
            "• Major malformations: 2-3% (background)",
            "• Spontaneous miscarriage: 15-20%",
            "• Stillbirth: 0.5%",
            "",
            "EPILEPSY-SPECIFIC RISKS:",
            "• Seizure complications during pregnancy",
            "• ASM-related teratogenicity",
            "• Uncontrolled seizures pose risk to mother and fetus"
        ])

        # Check for high-risk medications
        for med in medications:
            med_lower = med.lower()
            if med_lower in cls.ASM_TERATOGENICITY:
                asm_data = cls.ASM_TERATOGENICITY[med_lower]

                counseling.extend([
                    "",
                    f"{med.upper()} SPECIFIC RISKS:",
                    f"• Malformation risk: {asm_data['major_malformations']}",
                    f"• Risk category: {asm_data['risk'].value}"
                ])

                if asm_data.get("neurodevelopmental"):
                    counseling.append(f"• Neurodevelopmental: {asm_data['neurodevelopmental']}")

        counseling.extend([
            "",
            "💡 BENEFITS OF PLANNED PREGNANCY:",
            "• Optimize ASM regimen before conception",
            "• High-dose folic acid reduces neural tube defects",
            "• Most women with epilepsy have healthy babies",
            "• Seizure freedom reduces pregnancy complications"
        ])

        return counseling

    @classmethod
    def get_catamenial_epilepsy_guidance(cls) -> List[str]:
        """Get catamenial epilepsy assessment and treatment guidance"""
        return [
            "🔄 CATAMENIAL EPILEPSY:",
            "",
            "DEFINITION:",
            "• Seizures linked to menstrual cycle",
            "• Types: Perimenstrual, Ovulatory, Entire luteal phase",
            "",
            "ASSESSMENT:",
            "• Detailed seizure diary (3+ months)",
            "• Record menstrual cycles",
            "• Identify seizure pattern",
            "",
            "TREATMENT APPROACHES:",
            "• Perimenstrual ASM dose increase",
            "• Cyclic use of benzodiazepines (clonazepam)",
            "• Acetazolamide (carbonic anhydrase inhibitor)",
            "• Natural progesterone supplementation",
            "• Hormonal contraception (cycle stabilization)",
            "",
            "💡 CLINICAL PEARLS:",
            "• Diagnosis often missed (take detailed history)",
            "• Treatment can be very effective",
            "• Consider endocrinology referral"
        ]

    @classmethod
    def get_menopause_guidance(cls) -> List[str]:
        """Get menopause and epilepsy guidance"""
        return [
            "🌙 MENOPAUSE AND EPILEPSY:",
            "",
            "MENOPAUSE EFFECTS:",
            "• Hormonal changes can affect seizure frequency",
            "• Perimenopause: often increased seizures",
            "• Postmenopause: variable effects",
            "",
            "HORMONE REPLACEMENT THERAPY (HRT):",
            "• Generally safe for epilepsy patients",
            "• Avoid progesterone-only if provoking seizures",
            "• Transdermal estrogen preferred",
            "• Monitor seizure frequency",
            "",
            "ASM CONSIDERATIONS:",
            "• May need dose adjustments",
            "• Monitor for bone health (enzyme inducers)",
            "• Consider osteoporosis prevention",
            "",
            "💡 CLINICAL PEARLS:",
            "• Individualized approach needed",
            "• Discuss benefits/risks of HRT",
            "• Bone health important (enzyme inducers decrease bone density)"
        ]


__all__ = [
    'PregnancyTrimester',
    'ContraceptionCategory',
    'TeratogenicityRisk',
    'WomenEpilepsyCare',
    'WomenHealthEpilepsy'
]
