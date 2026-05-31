"""
EPIDISC Evidence-Based Medicine and Critical Appraisal Framework
=============================================================

Comprehensive evidence-based medicine system with critical appraisal,
guideline evaluation, statistical reasoning, and clinical decision support.

Based on:
- Evidence-based medicine principles (Sackett, 1996)
- Clinical epidemiology frameworks
- Statistical reasoning for clinicians
- Guideline development and evaluation methods
- Study design and interpretation

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass
from enum import Enum


class StudyDesign(Enum):
    """Clinical study design types"""
    RANDOMIZED_CONTROLLED_TRIAL = "randomized_controlled_trial"
    SYSTEMATIC_REVIEW = "systematic_review"
    META_ANALYSIS = "meta_analysis"
    COHORT_STUDY = "cohort_study"
    CASE_CONTROL = "case_control"
    CASE_SERIES = "case_series"
    CASE_REPORT = "case_report"
    EXPERT_OPINION = "expert_opinion"
    ANIMAL_RESEARCH = "animal_research"
    BASIC_SCIENCE = "basic_science"


class EvidenceLevel(Enum):
    """Evidence quality levels (Oxford Centre for EBM)"""
    LEVEL_1A = "systematic_reviews_of_rcts"
    LEVEL_1B = "individual_rct"
    LEVEL_2A = "cohort_studies"
    LEVEL_2B = "case_control_studies"
    LEVEL_3A = "case_series"
    LEVEL_3B = "expert_opinion"
    LEVEL_4 = "mechanism_based_reasoning"
    LEVEL_5 = "anecdote"


class StatisticalSignificance(Enum):
    """Statistical interpretation categories"""
    STATISTICALLY_SIGNIFICANT = "statistically_significant"
    CLINICALLY_SIGNIFICANT = "clinically_significant"
    BOTH = "both_significant"
    NEITHER = "neither_significant"
    INSUFFICIENT_DATA = "insufficient_data"


@dataclass
class CriticalAppraisal:
    """
    Complete critical appraisal of clinical evidence

    Includes study quality assessment, bias evaluation, statistical
    interpretation, and clinical applicability.
    """

    study_design: StudyDesign
    evidence_level: EvidenceLevel
    sample_size: int
    methodology_score: str
    bias_assessment: List[str]
    statistical_analysis: List[str]
    results_summary: str
    clinical_significance: str
    applicability: str
    limitations: List[str]
    strengths: List[str]
    overall_quality: str
    confidence_interval: Optional[str]
    absolute_risk_reduction: Optional[str]
    number_needed_to_treat: Optional[float]


class EvidenceBasedMedicine:
    """
    Comprehensive evidence-based medicine framework

    Critical appraisal, guideline evaluation, and statistical
    reasoning capabilities for consultant-level decision-making.
    """

    # Evidence hierarchy for clinical questions
    EVIDENCE_HIERARCHY = {
        "therapy": {
            "highest": [
                "Systematic review of RCTs",
                "Individual RCT with narrow confidence interval"
            ],
            "moderate": [
                "Cohort studies",
                "Case-control studies"
            ],
            "lower": [
                "Case series",
                "Expert opinion",
                "Animal research",
                "Mechanism-based reasoning"
            ]
        },
        "diagnosis": {
            "highest": [
                "Systematic review of clinical trials",
                "Clinical decision rules validated in different populations"
            ],
            "moderate": [
                "Cohort studies",
                "Case-control studies"
            ],
            "lower": [
                "Case series",
                "Expert opinion",
                "Pathophysiological studies"
            ]
        },
        "prognosis": {
            "highest": [
                "Systematic review of inception cohort studies",
                "Individual inception cohort study with >80% follow-up"
            ],
            "moderate": [
                "Case-control studies",
                "Retrospective cohort studies"
            ],
            "lower": [
                "Case series",
                "Expert opinion",
                "Mechanism-based studies"
            ]
        }
    }

    # Critical appraisal tools
    CRITICAL_APPRAISAL_CHECKLISTS = {
        "rct_checklist": {
            "randomization": "Was randomization truly random?",
            "allocation_concealment": "Was allocation concealed?",
            "blinding": "Were participants and clinicians blinded?",
            "follow_up": "Was follow-up complete?",
            "intention_to_treat": "Was intention-to-treat analysis performed?",
            "baseline_comparison": "Were groups similar at baseline?",
            "co_interventions": "Were co-interventions avoided?",
            "outcomes": "Were outcomes predefined and measured appropriately?",
            "sample_size": "Was sample size adequate?",
            "statistical_methods": "Were statistical methods appropriate?"
        },
        "cohort_checklist": {
            "cohort_definition": "Was cohort definition clear?",
            "selection": "Was selection bias minimized?",
            "exposure": "Was exposure measured reliably?",
            "outcome": "Was outcome measured reliably?",
            "confounders": "Were important confounders accounted for?",
            "follow_up": "Was follow-up adequate?",
            "statistical_methods": "Were statistical methods appropriate?"
        },
        "case_control_checklist": {
            "case_definition": "Was case definition clear?",
            "control_selection": "Were controls appropriately selected?",
            "exposure": "Was exposure measurement reliable?",
            "blinding": "Was assessor blinded to exposure?",
            "confounders": "Were confounders appropriately controlled?",
            "statistical_methods": "Were statistical methods appropriate?"
        }
    }

    # Common biases in clinical research
    BIASES = {
        "selection_bias": {
            "description": "Systematic differences in baseline characteristics",
            "examples": ["Healthy user bias", "Attrition bias"],
            "detection": "Compare group characteristics, assess follow-up completeness"
        },
        "performance_bias": {
            "description": "Systematic differences in care delivery",
            "examples": ["Co-intervention bias", "Provider expertise bias"],
            "detection": "Standardized protocols, blinding of providers"
        },
        "detection_bias": {
            "description": "Systematic differences in outcome assessment",
            "examples": ["Observer bias", "Measurement bias"],
            "detection": "Blinded outcome assessment, objective measures"
        },
        "reporting_bias": {
            "description": "Selective reporting of outcomes",
            "examples": ["Publication bias", "Outcome switching"],
            "detection": "Trial registries, protocol registration"
        }
    }

    # Statistical concepts for clinicians
    STATISTICAL_CONCEPTS = {
        "p_value": {
            "definition": "Probability of observing results if null hypothesis true",
            "clinical_significance": "p < 0.05 doesn't equal clinical significance",
            "misconceptions": [
                "p < 0.05 = 'statistically significant' (but maybe not clinically important)",
                "p > 0.05 = 'negative' (but maybe underpowered)",
                "Multiple comparisons increase false positive rate"
            ],
            "better_alternatives": "Effect sizes, confidence intervals, clinical significance"
        },
        "confidence_interval": {
            "definition": "Range of values likely to contain true effect",
            "interpretation": "Range includes clinically important effect?",
            "clinical_use": "If CI excludes 1 for binary outcomes, likely real effect",
            "width": "Narrow CI = precise estimate, Wide CI = uncertainty"
        },
        "effect_size": {
            "definition": "Magnitude of treatment effect (independent of sample size)",
            "clinical_value": "Large effect sizes may be more important than statistical significance",
            "examples": {
                "binary_outcomes": {
                    "RR": "Relative risk",
                    "OR": "Odds ratio",
                    "ARR": "Absolute risk reduction",
                    "NNT": "Number needed to treat"
                },
                "continuous_outcomes": {
                    "Cohens_d": "Standardized mean difference",
                    "mean_difference": "Absolute difference"
                }
            }
        },
        "nnt": {
            "definition": "Number of patients needed to treat to prevent one bad outcome",
            "calculation": "1 / (Absolute Risk Reduction)",
            "interpretation": {
                "NNT 1-10": "Very effective treatment",
                "NNT 10-50": "Moderate effectiveness",
                "NNT 50-100": "Small benefit",
                "NNT >100": "Minimal benefit or harm"
            }
        },
        "type_i_error": {
            "definition": "False positive - concluding effect exists when it doesn't",
            "probability": "α level (typically 0.05)",
            "consequences": "Adopt ineffective treatment"
        },
        "type_ii_error": {
            "definition": "False negative - concluding no effect when one exists",
            "probability": "β level (related to power)",
            "consequences": "Miss effective treatment",
            "mitigation": "Adequate sample size"
        },
        "power": {
            "definition": "Ability to detect clinically significant effect",
            "adequate_power": "≥80% (0.8)",
            "low_power": "<80% increases false negative rate",
            "calculation": "1 - β"
        }
    }

    @classmethod
    def critical_appraise_study(cls, study_data: Dict) -> CriticalAppraisal:
        """
        Perform critical appraisal of clinical study

        Args:
            study_data: Study metadata and results

        Returns:
            CriticalAppraisal with complete assessment
        """
        # Determine study design
        design = cls._determine_study_design(study_data)

        # Determine evidence level
        evidence = cls._determine_evidence_level(study_data)

        # Assess methodology
        methodology = cls._assess_methodology(study_data)

        # Identify biases
        biases = cls._identify_biases(study_data)

        # Assess statistical analysis
        stats = cls._assess_statistical_analysis(study_data)

        # Clinical significance
        clinical = cls._assess_clinicial_significance(study_data)

        # Limitations and strengths
        limitations = cls._identify_limitations(study_data)
        strengths = cls._identify_strengths(study_data)

        # Overall quality
        quality = cls._assess_overall_quality(study_data, biases, limitations)

        return CriticalAppraisal(
            study_design=design,
            evidence_level=evidence,
            sample_size=study_data.get("sample_size", 0),
            methodology_score=methodology,
            bias_assessment=biases,
            statistical_analysis=stats,
            results_summary=study_data.get("results", ""),
            clinical_significance=clinical,
            applicability=cls._assess_applicability(study_data),
            limitations=limitations,
            strengths=strengths,
            overall_quality=quality,
            confidence_interval=study_data.get("confidence_interval"),
            absolute_risk_reduction=study_data.get("absolute_risk_reduction"),
            number_needed_to_treat=study_data.get("number_needed_to_treat")
        )

    @classmethod
    def _determine_study_design(cls, study: Dict) -> StudyDesign:
        """Determine study design type"""
        design = study.get("design", "").lower()

        if "randomized" in design and "controlled" in design:
            return StudyDesign.RANDOMIZED_CONTROLLED_TRIAL
        elif "systematic review" in design:
            return StudyDesign.SYSTEMATIC_REVIEW
        elif "meta-analysis" in design:
            return StudyDesign.META_ANALYSIS
        elif "cohort" in design:
            return StudyDesign.COHORT_STUDY
        elif "case control" in design:
            return StudyDesign.CASE_CONTROL
        elif "case series" in design:
            return StudyDesign.CASE_SERIES
        elif "case report" in design:
            return StudyDesign.CASE_REPORT
        else:
            return StudyDesign.OBSERVATIONAL

    @classmethod
    def _determine_evidence_level(cls, study: Dict) -> EvidenceLevel:
        """Determine evidence level"""
        design = cls._determine_study_design(study)

        if design == StudyDesign.SYSTEMATIC_REVIEW:
            return EvidenceLevel.LEVEL_1A
        elif design == StudyDesign.RANDOMIZED_CONTROLLED_TRIAL:
            return EvidenceLevel.LEVEL_1B
        elif design == StudyDesign.COHORT_STUDY:
            return EvidenceLevel.LEVEL_2A
        elif design == StudyDesign.CASE_CONTROL:
            return EvidenceLevel.LEVEL_2B
        elif design == StudyDesign.CASE_SERIES:
            return EvidenceLevel.LEVEL_3A
        else:
            return EvidenceLevel.LEVEL_3B

    @classmethod
    def _assess_methodology(cls, study: Dict) -> str:
        """Assess study methodology"""
        method_score = []

        # Key methodological features
        if study.get("randomization", False):
            method_score.append("✅ Randomized")
        else:
            method_score.append("❌ No randomization")

        if study.get("blinding", "") == "double":
            method_score.append("✅ Double-blinded")
        elif study.get("blinding", "") == "single":
            method_score.append("⚠️ Single-blinded")
        else:
            method_score.append("❌ No blinding")

        if study.get("allocation_concealment", False):
            method_score.append("✅ Allocation concealed")
        else:
            method_score.append("❌ Allocation not concealed")

        if study.get("intention_to_treat", False):
            method_score.append("✅ Intention-to-treat analysis")
        else:
            method_score.append("❌ No intention-to-treat analysis")

        if study.get("follow_up_complete", False):
            method_score.append("✅ Complete follow-up")
        else:
            method_score.append("⚠️ Incomplete follow-up (attrition bias)")

        # Calculate quality score
        positives = sum(1 for item in method_score if item.startswith("✅"))
        return f"Methodology quality: {positives}/7 features adequate"

    @classmethod
    def _identify_biases(cls, study: Dict) -> List[str]:
        """Identify potential biases in study"""
        biases = []

        # Selection bias
        if not study.get("randomized", False):
            biases.append("⚠️ Potential selection bias (non-randomized)")

        if not study.get("allocation_concealed", False):
            biases.append("⚠️ Potential selection bias (allocation not concealed)")

        # Performance bias
        if study.get("blinding") != "double":
            biases.append("⚠️ Potential performance bias (not double-blinded)")

        # Detection bias
        if study.get("blinded_assessment", False) == False:
            biases.append("⚠️ Potential detection bias (outcome assessor not blinded)")

        # Attrition bias
        if not study.get("follow_up_complete", False):
            biases.append("⚠️ Potential attrition bias (incomplete follow-up)")

        # Reporting bias
        if not study.get("all_outcomes_reported", False):
            biases.append("⚠️ Potential reporting bias (selective outcome reporting)")

        return biases

    @classmethod
    def _assess_statistical_analysis(cls, study: Dict) -> List[str]:
        """Assess statistical analysis"""
        stats = []

        if study.get("p_value", 1.0) < 0.05:
            stats.append("✓ Statistically significant (p < 0.05)")
        else:
            stats.append("✗ Not statistically significant (p ≥ 0.05)")

        if study.get("confidence_interval"):
            stats.append(f"✓ Confidence interval provided: {study['confidence_interval']}")

        if study.get("number_needed_to_treat"):
            nnt = study["number_needed_to_treat"]
            stats.append(f"NNT = {nnt} ({cls._interpret_nnt(nnt)})")

        # Check for appropriate tests
        if study.get("appropriate_tests", False):
            stats.append("✓ Appropriate statistical tests used")

        return stats

    @classmethod
    def _interpret_nnt(cls, nnt: float) -> str:
        """Interpret NNT value"""
        if nnt <= 10:
            return "Very effective"
        elif nnt <= 50:
            return "Moderate effectiveness"
        elif nnt <= 100:
            return "Small benefit"
        else:
            return "Minimal benefit"

    @classmethod
    def _assess_clinical_significance(cls, study: Dict) -> str:
        """Assess clinical significance of findings"""
        clinical = []

        # Check for clinically important effect
        arr = study.get("absolute_risk_reduction", 0)
        if arr > 0.05:  # 5% absolute risk reduction
            clinical.append("✓ Clinically significant (>5% ARR)")
        elif arr > 0.02:  # 2-5% absolute risk reduction
            clinical.append("⚠️ Possibly clinically significant (2-5% ARR)")
        else:
            clinical.append("✗ Not clinically significant (<2% ARR)")

        # Check NNT
        nnt = study.get("number_needed_to_treat")
        if nnt:
            if nnt < 25:
                clinical.append("✓ Clinically meaningful (NNT < 25)")
            elif nnt < 100:
                clinical.append("⚠️ May be clinically meaningful (NNT 25-100)")
            else:
                clinical.append("✗ Not clinically meaningful (NNT > 100)")

        # Check for safety concerns
        if study.get("serious_adverse_events", 0) > 0:
            clinical.append("⚠️ Safety concerns may limit clinical utility")

        return "\n".join(clinical)

    @classmethod
    def _assess_applicability(cls, study: Dict) -> str:
        """Assess applicability to clinical practice"""
        applicability = []

        # Check population similarity
        if study.get("population", "") == "epilepsy":
            applicability.append("✓ Relevant population")
        else:
            applicability.append("⚠️ Different population (extrapolation required)")

        # Check intervention availability
        if study.get("intervention_available", True):
            applicability.append("✓ Intervention clinically available")
        else:
            applicability.append("⚠️ Intervention not standardly available")

        # Check outcome relevance
        if study.get("patient_outcomes", False):
            applicability.append("✓ Patient-important outcomes")
        else:
            applicability.append("⚠️ Surrogate outcomes (clinical relevance uncertain)")

        return "\n".join(applicability)

    @classmethod
    def _identify_limitations(cls, study: Dict) -> List[str]:
        """Identify study limitations"""
        limitations = []

        if study.get("sample_size", 0) < 100:
            limitations.append(f"⚠️ Small sample size (n={study['sample_size']}) - may be underpowered")

        if not study.get("randomized", False):
            limitations.append("❌ Non-randomized design")

        if study.get("blinding") != "double":
            limitations.append("⚠️ Lack of double-blinding")

        if not study.get("follow_up_complete", False):
            limitations.append("⚠️ Incomplete follow-up")

        if study.get("single_center", False):
            limitations.append("⚠️ Single-center study (limited generalizability)")

        if study.get("industry_funded", False):
            limitations.append("⚠️ Industry funding (potential bias)")

        if study.get("short_follow_up", False):
            limitations.append("⚠️ Short follow-up duration")

        return limitations

    @classmethod
    def _identify_strengths(cls, study: Dict) -> List[str]:
        """Identify study strengths"""
        strengths = []

        if study.get("randomized", False):
            strengths.append("✅ Randomized design")

        if study.get("blinding") == "double":
            strengths.append("✅ Double-blinded")

        if study.get("sample_size", 0) > 200:
            strengths.append(f"✅ Adequate sample size (n={study['sample_size']})")

        if study.get("intention_to_treat", False):
            strengths.append("✅ Intention-to-treat analysis")

        if study.get("multicenter", False):
            strengths.append("✅ Multicenter design")

        if study.get("long_term_follow_up", False):
            strengths.append("✅ Long-term follow-up")

        if study.get("patient_outcomes", False):
            strengths.append("✅ Patient-important outcomes")

        return strengths

    @classmethod
    def _assess_overall_quality(cls, study: Dict, biases: List, limitations: List) -> str:
        """Assess overall study quality"""
        # Count biases and limitations
        bias_count = len(biases)
        limitation_count = len(limitations)

        if bias_count == 0 and limitation_count <= 1:
            return "HIGH QUALITY"
        elif bias_count <= 1 and limitation_count <= 2:
            return "GOOD QUALITY"
        elif bias_count <= 2 and limitation_count <= 3:
            return "FAIR QUALITY"
        else:
            return "POOR QUALITY"

    @classmethod
    def get_guideline_evaluation(cls, guideline: Dict) -> List[str]:
        """Evaluate clinical guideline quality"""
        evaluation = [
            "📋 GUIDELINE QUALITY ASSESSMENT:",
            ""
        ]

        # Check for AGREE criteria
        evaluation.extend([
            "AGREE II CRITERIA:",
            "• Stakeholder involvement",
            "• Systematic literature review",
            "• Evidence quality assessment",
            "• Clear recommendations",
            "• Benefit vs harm consideration",
            "• Patient preferences considered",
            "• External review",
            "• Regular updates planned"
        ])

        return evaluation

    @classmethod
    def get_statistical_guidance(cls) -> List[str]:
        """Get statistical guidance for clinicians"""
        return [
            "📊 STATISTICAL CONCEPTS FOR CLINICIANS:",
            "",
            "P-VALUE:",
            "• Probability of results if null hypothesis true",
            "• p < 0.05 = 'statistically significant'",
            "• But p < 0.05 ≠ 'clinically important'",
            "• Large samples can detect tiny, unimportant effects",
            "",
            "CONFIDENCE INTERVAL:",
            "• Range likely to contain true effect",
            "• Width indicates precision (narrow = precise)",
            "• If CI includes 1: may not be real effect",
            "• If CI excludes 1: likely real effect",
            "",
            "EFFECT SIZE:",
            "• Magnitude of treatment effect (sample size independent)",
            "• More important than p-value for clinical decisions",
            "• Relative vs absolute risk",
            "",
            "NUMBER NEEDED TO TREAT (NNT):",
            "• Patients needed to treat to prevent 1 bad outcome",
            "• NNT 1-10: Very effective",
            "• NNT 10-50: Moderately effective",
            "• NNT 50-100: Small benefit",
            "• NNT >100: Minimal benefit",
            "",
            "TYPE I AND TYPE II ERRORS:",
            "• Type I: False positive (reject true null hypothesis)",
            "• Type II: False negative (fail to detect real effect)",
            "• Power: Ability to detect clinically significant effect",
            "• Adequate power: ≥80% (0.8)"
        ]

    @classmethod
    def get_ebm_principles(cls) -> List[str]:
        """Get EBM principles and philosophy"""
        return [
            "🎯 EVIDENCE-BASED MEDICINE PRINCIPLES:",
            "",
            "DEFINITION:",
            "• 'Conscientious, explicit, and judicious use of current best evidence'",
            "• Integration with clinical expertise",
            "• Consideration of patient values and preferences",
            "",
            "THE EBM TRIAD:",
            "1. Best Available Research Evidence",
            "2. Clinical Expertise and Experience",
            "3. Patient Values and Circumstances",
            "",
            "EVIDENCE HIERARCHY (Highest to Lowest):",
            "1. Systematic reviews of RCTs",
            "2. Individual RCTs",
            "3. Cohort studies",
            "4. Case-control studies",
            "5. Case series",
            "6. Expert opinion",
            "",
            "STEPS OF EBM:",
            "1. Formulate clinical question",
            "2. Search for best evidence",
            "3. Critically appraise evidence",
            "4. Integrate with clinical expertise",
            "5. Consider patient preferences",
            "6. Apply findings to patient care",
            "7. Evaluate outcomes",
            "",
            "💡 KEY PRINCIPLES:",
            "• Evidence alone is never enough",
            "• Clinical experience is crucial",
            "• Patient values must guide decisions",
            "• Not all questions have good evidence",
            "• Guidelines don't replace clinical judgment",
            "• Uncertainty is inevitable in medicine"
        ]


__all__ = [
    'StudyDesign',
    "EvidenceLevel",
    "StatisticalSignificance",
    "CriticalAppraisal",
    "EvidenceBasedMedicine"
]
