"""
EPIDISC Women's Health Module - Epilepsy and Pregnancy
======================================================

Comprehensive women's epilepsy care including pregnancy planning,
teratogenicity risk assessment, breastfeeding considerations, and
hormonal influences on seizure control.

Based on:
- NICE NG217 Epilepsies in pregnancy (2024)
- ILAE pregnancy task force recommendations (2024)
- EURAP epilepsy and pregnancy registry data (2025)
- AAN pregnancy guidelines update (2025)

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class PregnancyStage(Enum):
    """Stages of pregnancy for AED management"""
    PRE_CONCEPTION = "pre_conception"
    FIRST_TRIMESTER = "first_trimester"      # Weeks 1-12 (highest teratogenic risk)
    SECOND_TRIMESTER = "second_trimester"    # Weeks 13-26
    THIRD_TRIMESTER = "third_trimester"      # Weeks 27-40
    POSTPARTUM = "postpartum"
    BREASTFEEDING = "breastfeeding"


class TeratogenicityRisk(Enum):
    """Teratogenicity risk categories for AEDs"""
    HIGH = "high"              # >10% major malformations
    MODERATE = "moderate"      # 5-10% major malformations
    LOW = "low"                # <5% major malformations
    MINIMAL = "minimal"        # <1% major malformations
    UNKNOWN = "unknown"        # Insufficient data


class HormonalInfluence(Enum):
    """Types of hormonal influence on seizures"""
    CATAMENIAL_EPILEPSY = "catamenial_epilepsy"
    OCP_INTERACTIONS = "ocp_interactions"
    PREGNANCY_EFFECTS = "pregnancy_effects"
    MENOPAUSE_EFFECTS = "menopause_effects"


@dataclass
class PregnancyRiskAssessment:
    """
    Complete pregnancy risk assessment for AEDs

    Includes teratogenicity risk, monitoring recommendations,
    dose adjustments, and alternative medication options.
    """

    current_aed: str
    teratogenicity_risk: TeratogenicityRisk
    major_malformation_types: List[str]
    recommended_alternatives: List[str]
    folic_acid_recommendation: str
    monitoring_requirements: List[str]
    breastfeeding_safety: str
    neonatal_risk: str
    counseling_points: List[str]
    confidence: float


@dataclass
class PreConceptionConsultation:
    """
    Complete pre-conception consultation for women with epilepsy

    Includes AED optimization, folate supplementation, risk assessment,
    and pregnancy planning recommendations.
    """

    current_regimen: List[str]
    optimization_recommendations: List[str]
    teratogenicity_assessment: Dict[str, TeratogenicityRisk]
    folic_acid_guidance: str
    timing_conception: str
    genetic_counseling: List[str]
    prognosis: str
    confidence: float


class WomensHealthIntegration:
    """
    Comprehensive women's epilepsy care

    Evidence-based pregnancy management, teratogenicity assessment,
    hormonal influences, and breastfeeding safety.
    """

    # AED Teratogenicity Data (from EURAP and other registries)
    AED_TERATOGENICITY = {
        "valproate": {
            "risk": TeratogenicityRisk.HIGH,
            "malformation_rate": "10-11% major malformations",
            "dose_response": "Risk increases with dose (>1000 mg/day highest)",
            "specific_risks": [
                "Neural tube defects (spina bifida)",
                "Cleft lip/palate",
                "Cardiac defects",
                "Hypospadias",
                "Neurodevelopmental delay",
                "Lower IQ (8-10 points lower than other AEDs)",
                "Autism spectrum disorder risk (4-5x increased)",
                "ADHD risk increased"
            ],
            "recommendation": "CONTRAINDICATED in pregnancy unless absolutely essential",
            "alternatives": ["Lamotrigine", "Levetiracetam", "Carbamazepine (monotherapy)"],
            "breastfeeding": "Compatible with breastfeeding"
        },
        "phenobarbital": {
            "risk": TeratogenicityRisk.MODERATE,
            "malformation_rate": "6-7% major malformations",
            "specific_risks": [
                "Cardiac defects",
                "Cleft lip/palate",
                "Neurodevelopmental effects"
            ],
            "recommendation": "Avoid in pregnancy if possible",
            "alternatives": ["Lamotrigine", "Levetiracetam"],
            "breastfeeding": "Caution - may cause sedation in infant"
        },
        "phenytoin": {
            "risk": TeratogenicityRisk.MODERATE,
            "malformation_rate": "5-7% major malformations",
            "specific_risks": [
                "Fetal hydantoin syndrome",
                "Facial dysmorphism",
                "Cleft lip/palate",
                "Cardiac defects",
                "Growth restriction",
                "Neurodevelopmental delay"
            ],
            "recommendation": "Avoid in pregnancy if possible",
            "alternatives": ["Lamotrigine", "Levetiracetam"],
            "breastfeeding": "Compatible with breastfeeding"
        },
        "carbamazepine": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "3-5% major malformations (slightly above background)",
            "specific_risks": [
                "Neural tube defects (spina bifida)",
                "Cleft lip/palate",
                "Slight neurodevelopmental effects"
            ],
            "dose_response": "Risk increases with dose (>700 mg/day higher)",
            "recommendation": "Acceptable in pregnancy if effective",
            "note": "Better than valproate, but lamotrigine/levetiracetam preferred",
            "breastfeeding": "Compatible with breastfeeding"
        },
        "lamotrigine": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "2-3% major malformations (similar to background)",
            "specific_risks": [
                "Cleft lip/palate (slight increase)"
            ],
            "dose_response": "No clear dose-response relationship",
            "recommendation": "PREFERRED in pregnancy",
            "advantages": [
                "Lowest teratogenic risk",
                "Effective for many seizure types",
                "Breastfeeding compatible"
            ],
            "pregnancy_considerations": [
                "Clearance increases 2-3x in pregnancy",
                "Therapeutic drug monitoring essential",
                "Frequent dose adjustments often needed",
                "Postpartum dose reduction needed"
            ],
            "breastfeeding": "SAFE - preferred AED for breastfeeding"
        },
        "levetiracetam": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "2-3% major malformations (similar to background)",
            "specific_risks": [
                "No consistent pattern identified"
            ],
            "dose_response": "No clear dose-response",
            "recommendation": "PREFERRED in pregnancy",
            "advantages": [
                "Low teratogenic risk",
                "No significant drug interactions",
                "Therapeutic drug monitoring less critical"
            ],
            "pregnancy_considerations": [
                "Clearance increases in pregnancy (less than lamotrigine)",
                "May need dose increase in pregnancy",
                "Postpartum dose reduction often needed"
            ],
            "breastfeeding": "SAFE - preferred AED for breastfeeding"
        },
        "topiramate": {
            "risk": TeratogenicityRisk.MODERATE,
            "malformation_rate": "4-5% major malformations",
            "specific_risks": [
                "Cleft lip/palate",
                "Oral clefts",
                "Growth restriction",
                "Possible neurodevelopmental effects"
            ],
            "dose_response": "Risk increases with dose (>200 mg/day)",
            "recommendation": "Use only if benefits outweigh risks",
            "alternatives": ["Lamotrigine", "Levetiracetam"],
            "breastfeeding": "Compatible with breastfeeding"
        },
        "oxcarbazepine": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "2-3% major malformations",
            "recommendation": "Acceptable alternative in pregnancy",
            "breastfeeding": "Compatible with breastfeeding"
        },
        "zonisamide": {
            "risk": TeratogenicityRisk.MODERATE,
            "malformation_rate": "3-4% major malformations (limited data)",
            "recommendation": "Use only if necessary",
            "breastfeeding": "Limited data, caution"
        },
        "brivaracetam": {
            "risk": TeratogenicityRisk.UNKNOWN,
            "malformation_rate": "Insufficient data",
            "recommendation": "Use only if necessary, avoid if possible",
            "breastfeeding": "Insufficient data"
        },
        "perampanel": {
            "risk": TeratogenicityRisk.UNKNOWN,
            "malformation_rate": "Insufficient data",
            "recommendation": "Use only if necessary, avoid if possible",
            "breastfeeding": "Insufficient data"
        },
        "lacosamide": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "2-3% major malformations (limited data)",
            "recommendation": "Appears safe, use if necessary",
            "breastfeeding": "Compatible with breastfeeding"
        },
        "clobazam": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "2-3% major malformations (limited data)",
            "recommendation": "Acceptable in pregnancy",
            "caution": "Neonatal withdrawal possible with high doses",
            "breastfeeding": "Caution - may cause sedation"
        },
        "clonazepam": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "2-3% major malformations",
            "recommendation": "Acceptable in pregnancy",
            "caution": "Neonatal withdrawal possible with high doses",
            "breastfeeding": "Caution - may cause sedation in infant"
        },
        "ethosuximide": {
            "risk": TeratogenicityRisk.MODERATE,
            "malformation_rate": "3-4% major malformations",
            "recommendation": "Acceptable if necessary for absence seizures",
            "breastfeeding": "Compatible with breastfeeding"
        },
        "gabapentin": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "2-3% major malformations (limited data)",
            "recommendation": "Acceptable in pregnancy",
            "breastfeeding": "Compatible with breastfeeding"
        },
        "pregabalin": {
            "risk": TeratogenicityRisk.LOW,
            "malformation_rate": "2-3% major malformations (limited data)",
            "recommendation": "Acceptable in pregnancy",
            "breastfeeding": "Compatible with breastfeeding"
        }
    }

    # Folic Acid Recommendations
    FOLIC_ACID_GUIDANCE = {
        "general_recommendation": "All women of childbearing age should take folic acid",
        "epilepsy_specific": {
            "dose": "5 mg daily (high dose)",
            "timing": "Start at least 3 months before conception",
            "continue_throughout": "Continue throughout pregnancy",
            "rationale": [
                "Reduces neural tube defect risk by 70-80%",
                "High dose (5 mg) for women on AEDs",
                "Particularly important for valproate, carbamazepine",
                "Also reduces cardiac defect risk"
            ]
        }
    }

    # Hormonal Influences on Seizures
    HORMONAL_INFLUENCES = {
        "catamenial_epilepsy": {
            "definition": "Seizure clustering related to menstrual cycle",
            "types": {
                "perimenstrual": "Day -3 to +3 of menses (most common)",
                "ovulatory": "Around ovulation (day +10 to +14)",
                "entire_cycle": "Throughout luteal phase"
            },
            "mechanism": [
                "Estrogen: Proconvulsant (lowers seizure threshold)",
                "Progesterone: Anticonvulsant (raises seizure threshold)",
                "Perimenstrual progesterone withdrawal → seizures"
            ],
            "treatment": [
                "Optimize AEDs (may need perimenstrual dose increase)",
                "Consider catamenial-specific treatments:",
                "- Progesterone supplementation",
                "- Acetazolamide (carbonic anhydrase inhibitor)",
                "- Clobazam (intermittent use)"
            ],
            "prevalence": "10-30% of women with epilepsy"
        },
        "contraception_interactions": {
            "enzyme_inducers": [
                "Carbamazepine",
                "Phenytoin",
                "Phenobarbital",
                "Primidone",
                "Topiramate (high dose)",
                "Oxcarbazepine (weak)"
            ],
            "effect": "Reduce oral contraceptive pill efficacy",
            "mechanism": "Induce hepatic enzymes → increased hormone metabolism",
            "management": [
                "Use higher dose OCP (50 mcg estrogen)",
                "OR use non-hormonal contraception",
                "OR use levonorgestrel IUD (local hormone)",
                "Counsel about reduced OCP efficacy",
                "Consider alternative AEDs (lamotrigine, levetiracetam)"
            ],
            "lamotrigine_specific": [
                "OCP decreases lamotrigine levels",
                "Lamotrigine increases OCP hormone levels",
                "Bidirectional interaction",
                "Need to monitor lamotrigine levels"
            ]
        },
        "pregnancy_effects": {
            "seizure_frequency_changes": {
                "no_change": "50-60% no change",
                "decrease": "20-30% decrease (especially in generalized epilepsy)",
                "increase": "15-20% increase (especially in focal epilepsy)"
            },
            "factors_influencing_seizure_control": [
                "AED levels decrease in pregnancy",
                "Sleep deprivation (pregnancy-related)",
                "Hormonal changes",
                "Stress and anxiety",
                "Medication non-adherence (due to concerns about baby)"
            ],
            "risk_factors_for_seizure_during_pregnancy": [
                "History of frequent seizures pre-pregnancy",
                "Incomplete AED adherence during pregnancy",
                "Sleep deprivation",
                "Not adjusting AED doses during pregnancy"
            ]
        },
        "postpartum_considerations": {
            "seizure_risk": [
                "Increased risk in postpartum period",
                "Sleep deprivation",
                "Stress of newborn care",
                "AED levels may fluctuate postpartum"
            ],
            "medication_adjustments": [
                "AED doses increased during pregnancy need postpartum reduction",
                "Particularly important for lamotrigine",
                "Monitor AED levels postpartum",
                "Avoid toxicity (mother and infant if breastfeeding)"
            ],
            "neonatal_risks": {
                "aeds_at_delivery": "May cause neonatal sedation",
                "withdrawal": "Neonatal withdrawal if high-dose benzodiazepines",
                "vitamin_k": "Consider vitamin K for neonate if enzyme inducers"
            }
        },
        "menopause": {
            "seizure_frequency": [
                "Variable - may increase, decrease, or no change",
                "Perimenopause may worsen seizure control",
                "Hormone replacement therapy may influence seizures"
            ],
            "hrt_considerations": [
                "Estrogen may increase seizures",
                "Progesterone may decrease seizures",
                "Use lowest effective HRT dose",
                "Consider non-hormonal alternatives for menopausal symptoms"
            ]
        }
    }

    @classmethod
    def assess_pregnancy_risk(
        cls,
        current_aeds: List[str],
        pregnancy_stage: PregnancyStage = PregnancyStage.PRE_CONCEPTION
    ) -> Dict[str, PregnancyRiskAssessment]:
        """
        Assess pregnancy risk for current AED regimen

        Args:
            current_aeds: List of current AEDs
            pregnancy_stage: Current pregnancy stage

        Returns:
            Dict mapping each AED to its PregnancyRiskAssessment
        """
        assessments = {}

        for aed in current_aeds:
            aed_lower = aed.lower()
            teratogenicity_info = cls.AED_TERATOGENICITY.get(aed_lower, {
                "risk": TeratogenicityRisk.UNKNOWN,
                "malformation_rate": "Insufficient data",
                "recommendation": "Insufficient data, discuss with specialist",
                "breastfeeding": "Insufficient data"
            })

            # Build risk assessment
            assessment = PregnancyRiskAssessment(
                current_aed=aed,
                teratogenicity_risk=teratogenicity_info["risk"],
                major_malformation_types=teratogenicity_info.get("specific_risks", []),
                recommended_alternatives=teratogenicity_info.get("alternatives", []),
                folic_acid_recommendation="5 mg daily starting 3 months pre-conception",
                monitoring_requirements=cls._get_pregnancy_monitoring(aed, pregnancy_stage),
                breastfeeding_safety=teratogenicity_info.get("breastfeeding", "Unknown"),
                neonatal_risk=cls._assess_neonatal_risk(aed),
                counseling_points=cls._get_pregnancy_counseling_points(aed, teratogenicity_info),
                confidence=0.90
            )

            assessments[aed] = assessment

        return assessments

    @classmethod
    def _get_pregnancy_monitoring(cls, aed: str, stage: PregnancyStage) -> List[str]:
        """Get pregnancy monitoring requirements for specific AED"""
        monitoring = [
            "**General Pregnancy Monitoring**:",
            "- Detailed anomaly scan at 18-20 weeks",
            "- Fetal echocardiogram if indicated",
            "- Regular obstetric reviews"
        ]

        aed_lower = aed.lower()

        if aed_lower in ["lamotrigine", "levetiracetam", "oxcarbazepine"]:
            monitoring.extend([
                "",
                "**AED-Specific Monitoring**:",
                "- Therapeutic drug monitoring (especially lamotrigine)",
                "- Monthly AED level checks in 2nd/3rd trimester",
                "- Dose adjustment as needed",
                "- Postpartum dose reduction planning"
            ])

        if aed_lower in ["carbamazepine", "phenytoin", "phenobarbital"]:
            monitoring.extend([
                "",
                "**Enzyme Inducer Monitoring**:",
                "- Vitamin K supplementation in last month",
                "- Neonatal vitamin K at delivery",
                "- Monitor maternal folate levels",
                "- Monitor for maternal anemia"
            ])

        return monitoring

    @classmethod
    def _assess_neonatal_risk(cls, aed: str) -> str:
        """Assess neonatal risks from AED exposure"""
        aed_lower = aed.lower()

        if aed_lower in ["clonazepam", "clobazam", "diazepam"]:
            return "⚠️ Neonatal sedation and withdrawal possible if high-dose benzodiazepine use in late pregnancy. Monitor neonate for withdrawal symptoms."

        elif aed_lower in ["phenobarbital", "primidone"]:
            return "⚠️ Neonatal sedation and withdrawal possible. Monitor neonate for withdrawal symptoms. Consider vitamin K for neonate."

        elif aed_lower == "valproate":
            return "⚠️ HIGH RISK: Neonatal hepatic toxicity, sedation, withdrawal. NICU monitoring recommended. Avoid valproate in pregnancy if possible."

        else:
            return "✅ Generally low neonatal risk. Routine monitoring as per standard obstetric care."

    @classmethod
    def _get_pregnancy_counseling_points(cls, aed: str, teratogenicity_info: Dict) -> List[str]:
        """Get key counseling points for AED in pregnancy"""
        points = [
            f"**Current Medication**: {aed}",
            "",
            f"**Teratogenicity Risk**: {teratogenicity_info['risk'].value.upper()}",
            f"**Malformation Rate**: {teratogenicity_info.get('malformation_rate', 'Unknown')}",
            ""
        ]

        points.extend([
            f"**Recommendation**: {teratogenicity_info['recommendation']}",
            ""
        ])

        if teratogenicity_info.get("specific_risks"):
            points.extend([
                "**Specific Risks**:",
            ])
            for risk in teratogenicity_info["specific_risks"]:
                points.append(f"- {risk}")
            points.append("")

        return points

    @classmethod
    def generate_pre_conception_consultation(
        cls,
        current_aeds: List[str],
        seizure_frequency: str,
        pregnancy_plans: str
    ) -> PreConceptionConsultation:
        """
        Generate comprehensive pre-conception consultation

        Args:
            current_aeds: Current AED regimen
            seizure_frequency: Seizure frequency (well-controlled, occasional, frequent)
            pregnancy_plans: Timing of pregnancy planning

        Returns:
            PreConceptionConsultation with complete guidance
        """
        optimization_recommendations = []

        # Assess each AED
        teratogenicity_assessment = {}
        for aed in current_aeds:
            aed_lower = aed.lower()
            if aed_lower in cls.AED_TERATOGENICITY:
                teratogenicity_assessment[aed] = cls.AED_TERATOGENICITY[aed_lower]["risk"]

        # Optimization recommendations
        for aed in current_aeds:
            aed_lower = aed.lower()

            if aed_lower == "valproate":
                optimization_recommendations.extend([
                    f"🔴 CRITICAL: {aed} (valproate) has HIGH teratogenicity risk",
                    "- STRONGLY consider discontinuation before pregnancy",
                    "- Switch to lamotrigine or levetiracetam if possible",
                    "- If valproate essential: Use lowest effective dose",
                    "- Split dosing (avoid sustained release)",
                    "- High-dose folic acid (5 mg) essential",
                    "- Detailed counseling required"
                ])

            elif aed_lower in ["phenobarbital", "phenytoin"]:
                optimization_recommendations.extend([
                    f"⚠️ {aed} has MODERATE teratogenicity risk",
                    "- Consider switching to lamotrigine or levetiracetam",
                    "- If continuing: Use lowest effective dose",
                    "- High-dose folic acid (5 mg) essential"
                ])

            elif aed_lower in ["lamotrigine", "levetiracetam"]:
                optimization_recommendations.extend([
                    f"✅ {aed} is LOW risk - preferred in pregnancy",
                    "- Continue if seizures well-controlled",
                    "- High-dose folic acid (5 mg) still recommended"
                ])

        # Seizure frequency considerations
        if seizure_frequency == "frequent":
            optimization_recommendations.extend([
                "",
                "**Important**: Seizure frequency must be optimized before pregnancy",
                "- Frequent seizures pose risks to mother and baby",
                "- Work with epilepsy specialist before conceiving",
                "- Goal: Best possible seizure control prior to pregnancy"
            ])

        # Genetic counseling
        genetic_counseling = [
            "**Genetic Counseling Considerations**:",
            "- Most epilepsy cases are not inherited",
            "- Discuss family history of epilepsy",
            "- Consider genetic testing if indicated",
            "- Counsel about recurrence risk (usually low)",
            "- Pre-conception folic acid reduces risk"
        ]

        # Timing
        if "immediate" in pregnancy_plans.lower():
            timing = "Urgent pre-conception consultation needed"
        elif "next year" in pregnancy_plans.lower():
            timing = "Adequate time for AED optimization - good planning"
        else:
            timing = "Discuss optimal timing with neurologist"

        # Prognosis
        if all(risk in [TeratogenicityRisk.LOW, TeratogenicityRisk.MINIMAL] for risk in teratogenicity_assessment.values()):
            prognosis = "Good prognosis for pregnancy with low-risk AED regimen. Continue current planning."
        elif any(risk == TeratogenicityRisk.HIGH for risk in teratogenicity_assessment.values()):
            prognosis = "High teratogenicity risk present. Urgent AED optimization recommended before pregnancy."
        else:
            prognosis = "Moderate teratogenicity risk. Discuss AED optimization with epilepsy specialist."

        return PreConceptionConsultation(
            current_regimen=current_aeds,
            optimization_recommendations=optimization_recommendations,
            teratogenicity_assessment=teratogenicity_assessment,
            folic_acid_guidance="Start high-dose folic acid (5 mg daily) at least 3 months before conception. Continue throughout pregnancy.",
            timing_conception=timing,
            genetic_counseling=genetic_counseling,
            prognosis=prognosis,
            confidence=0.90
        )

    @classmethod
    def get_breastfeeding_guidance(cls, aeds: List[str]) -> List[str]:
        """Get breastfeeding guidance for AED regimen"""
        guidance = [
            "## BREASTFEEDING WITH EPILEPSY MEDICATIONS",
            "",
            "**General Principle**:",
            "- Breastfeeding is generally encouraged for women with epilepsy",
            "- Most AEDs are compatible with breastfeeding",
            "- Benefits of breastfeeding usually outweigh risks",
            "- Monitor infant for sedation or poor feeding",
            "",
            "**Specific Medication Guidance**:",
            ""
        ]

        for aed in aeds:
            aed_lower = aed.lower()
            if aed_lower in cls.AED_TERATOGENICITY:
                bf_safety = cls.AED_TERATOGENICITY[aed_lower].get("breastfeeding", "Unknown")
                guidance.extend([
                    f"**{aed}**: {bf_safety}",
                ])

        guidance.extend([
            "",
            "**Monitoring**:",
            "- Monitor infant for sedation, poor feeding, weight gain",
            "- Seek medical advice if concerns about infant",
            "- Report any infant concerns to pediatrician",
            "",
            "**Advantages of Breastfeeding**:",
            "- Optimal nutrition for baby",
            "- Bonding benefits",
            "- Reduced maternal stress",
            "- No additional cost",
            "",
            "**⚠️ Precautions**:",
            "- Avoid breastfeeding if infant sedated",
            "- Time breastfeeding relative to AED doses if possible",
            "- Monitor infant closely if high-dose benzodiazepines",
            "- Discuss with pediatrician and neurologist"
        ])

        return guidance


__all__ = [
    'PregnancyStage',
    'TeratogenicityRisk',
    'HormonalInfluence',
    'PregnancyRiskAssessment',
    'PreConceptionConsultation',
    'WomensHealthIntegration'
]
