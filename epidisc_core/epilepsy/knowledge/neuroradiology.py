"""
EPIDISC Neuroradiology and Epilepsy Imaging
============================================

Comprehensive epilepsy imaging interpretation system with MRI protocol,
lesion recognition, and clinical correlation capabilities.

Based on:
- ILAE neuroimaging commission recommendations
- Epilepsy imaging protocols (2022)
- Evidence-based imaging yield data
- Neuroimaging criteria for common epileptogenic lesions

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class ImagingModality(Enum):
    """Neuroimaging modalities for epilepsy evaluation"""
    MRI_EPILEPSY_PROTOCOL = "mri_epilepsy_protocol"    # High-resolution MRI
    CT_BRAIN = "ct_brain"                             # CT head
    PET_FDG = "pet_fdg"                               # FDG-PET
    SPECT_ICTAL = "spect_ictal"                       # Ictal SPECT
    SPECT_INTERICTAL = "spect_interictal"            # Interictal SPECT
    FMRI = "fmri"                                    # Functional MRI
    DTI = "dti"                                      # Diffusion tensor imaging


class LesionType(Enum):
    """Common epileptogenic lesion types"""
    MESIAL_TEMPORAL_SCLEROSIS = "mesial_temporal_sclerosis"
    FOCAL_CORTICAL_DYSPLASIA = "focal_cortical_dysplasia"
    LOW_GRADE_TUMOR = "low_grade_tumor"
    CAVERNOMA = "cavernoma"
    ARTERIOVENOUS_MALFORMATION = "arteriovenous_malformation"
    POST_TRAUMATIC = "post_traumatic"
    STROKE_RELATED = "stroke_related"
    PERINATAL_INJURY = "perinatal_injury"
    HIPPOCAMPAL_SCLEROSIS = "hippocampal_sclerosis"
    NONE = "none_identified"


@dataclass
class ImagingFindings:
    """
    Complete imaging interpretation findings

    Includes structural findings, lesion characteristics,
    clinical correlation, and investigation recommendations.
    """

    modality: ImagingModality
    findings_description: str
    lesion_identified: bool
    lesion_type: Optional[LesionType]
    lesion_location: Optional[str]
    lesion_lateralization: Optional[str]
    additional_findings: List[str]
    normal_variants: List[str]
    clinical_correlation: str
    diagnostic_impression: str
    recommended_followup: List[str]
    confidence: float


class EpilepsyMRIProtocol:
    """
    Epilepsy MRI protocol specifications and interpretation

    Evidence-based MRI protocol for epilepsy evaluation
    with lesion detection optimization.
    """

    # Recommended epilepsy MRI protocol
    MRI_PROTOCOL = {
        "sequences": {
            "3D_T1_weighted": {
                "description": "High-resolution 3D T1-weighted imaging",
                "parameters": "1 mm isotropic voxels",
                "purpose": "Structural analysis, cortical thickness"
            },
            "T2_weighted": {
                "description": "T2-weighted imaging",
                "parameters": "2 mm slice thickness",
                "purpose": "Lesion detection, hippocampal assessment"
            },
            "FLAIR": {
                "description": "Fluid-attenuated inversion recovery",
                "parameters": "2 mm slice thickness, no gap",
                "purpose": "Cortical signal abnormality, hippocampal sclerosis"
            },
            "T2_star_GRE": {
                "description": "T2* gradient echo",
                "parameters": "Susceptibility-weighted imaging",
                "purpose": "Cavernoma detection, hemosiderin"
            },
            "DWI_ADC": {
                "description": "Diffusion-weighted imaging",
                "parameters": "Trace and ADC maps",
                "purpose": "Acute lesions, tumor characterization"
            },
            "hippocampal_protocol": {
                "description": "High-resolution hippocampal imaging",
                "parameters": "Perpendicular to hippocampal axis",
                "purpose": "Mesial temporal sclerosis detection"
            }
        },
        "indications": [
            "New-onset focal epilepsy",
            "Drug-resistant focal epilepsy",
            "Pre-surgical evaluation",
            "Post-stroke epilepsy",
            "Traumatic brain injury with epilepsy"
        ],
        "diagnostic_yield": {
            "new_onset_focal": "34% lesions identified",
            "drug_resistant": "70-80% lesions identified",
            "presurgical_evaluation": "85-90% lesions identified"
        }
    }

    # Mesial temporal sclerosis criteria
    MTS_CRITERIA = {
        "hippocampal_atrophy": {
            "description": "Reduced hippocampal volume",
            "measurement": "Visual assessment or volumetry",
            "significance": " hallmark finding"
        },
        "increased_T2_signal": {
            "description": "T2/FLAIR hyperintensity",
            "location": "Hippocampus proper",
            "significance": "Key diagnostic feature"
        },
        "loss_of_internal_architecture": {
            "description": "Blurring of hippocampal internal architecture",
            "structures_affected": ["CA1", "CA3", "CA4", "dentate gyrus"],
            "significance": "Supports MTS diagnosis"
        },
        "temporal_horn_enlargement": {
            "description": "Dilated temporal horn of lateral ventricle",
            "significance": "Secondary sign of atrophy"
        },
        "amygdala_changes": {
            "description": "Amygdala volume or signal changes",
            "significance": "Variable in MTS"
        }
    }

    # Focal cortical dysplasia features
    FCD_FEATURES = {
        "cortical_thickening": {
            "description": "Abnormal cortical thickness",
            "significance": "Focal cortical dysplasia Type I/II"
        },
        "blurred_grey_white_matter_interface": {
            "description": "Indistinct cortical-white matter junction",
            "significance": "Focal cortical dysplasia Type I"
        },
        "transmantle_sign": {
            "description": "Abnormal signal from cortex to ventricle",
            "significance": "Focal cortical dysplasia Type IIb"
        },
        "increased_T2_FLAIR_signal": {
            "description": "Abnormal T2/FLAIR signal in cortex",
            "significance": "Focal cortical dysplasia"
        }
    }

    # Other common epileptogenic lesions
    LESION_FEATURES = {
        "low_grade_tumor": {
            "description": "Low-grade glioma (DNET, ganglioglioma)",
            "typical_locations": ["Temporal lobe", "Frontal lobe"],
            "imaging_characteristics": [
                "Well-circumscribed mass",
                "Minimal surrounding edema",
                "Possible calcification",
                "Variable enhancement"
            ],
            "common_types": ["DNET", "Ganglioglioma", "Low-grade astrocytoma"]
        },
        "cavernoma": {
            "description": "Cerebral cavernous malformation",
            "imaging_characteristics": [
                "Popcorn-like appearance",
                "Hemosiderin rim on T2*",
                "Mixed signal due to blood products",
                "No significant edema"
            ]
        },
        "arteriovenous_malformation": {
            "description": "AVM",
            "imaging_characteristics": [
                "Serpiginous flow voids",
                "Feeding arteries, draining veins",
                "Possible hemosiderin",
                "Possible hemorrhage"
            ]
        },
        "post_traumatic": {
            "description": "Post-traumatic gliosis/encephalomalacia",
            "imaging_characteristics": [
                "Focal cortical atrophy",
                "Encephalomalacia at injury site",
                "Possible hemosiderin",
                "Possible gliosis"
            ]
        },
        "stroke_related": {
            "description": "Post-stroke cortical injury",
            "imaging_characteristics": [
                "Cortical laminar necrosis",
                "Encephalomalacia in vascular territory",
                "Possible hemosiderin",
                "Gliosis"
            ]
        }
    }


class EpilepsyImagingInterpreter:
    """
    Comprehensive epilepsy imaging interpretation system

    Provides consultant-level imaging analysis with clinical
    correlation and lesion detection capabilities.
    """

    @classmethod
    def interpret_mri(
        cls,
        imaging_description: str,
        clinical_context: Optional[Dict] = None
    ) -> ImagingFindings:
        """
        Interpret epilepsy MRI findings

        Args:
            imaging_description: Text description of MRI findings
            clinical_context: Clinical information for correlation

        Returns:
            ImagingFindings with complete interpretation
        """
        desc_lower = imaging_description.lower()

        # Assess for specific lesion types
        lesion_type = cls._identify_lesion_type(desc_lower)
        lesion_location = cls._identify_lesion_location(desc_lower)
        lesion_lateralization = cls._identify_lateralization(desc_lower)

        # Additional findings
        additional_findings = cls._extract_additional_findings(desc_lower)

        # Normal variants
        normal_variants = cls._identify_normal_variants(desc_lower)

        # Clinical correlation
        clinical_correlation = cls._provide_clinical_correlation(
            lesion_type, lesion_location, clinical_context
        )

        # Diagnostic impression
        diagnostic_impression = cls._form_diagnostic_impression(
            lesion_type, lesion_location, additional_findings
        )

        # Recommendations
        recommendations = cls._provide_recommendations(
            lesion_type, imaging_description
        )

        # Calculate confidence
        confidence = cls._calculate_confidence(lesion_type, imaging_description)

        return ImagingFindings(
            modality=ImagingModality.MRI_EPILEPSY_PROTOCOL,
            findings_description=imaging_description,
            lesion_identified=lesion_type is not None and lesion_type != LesionType.NONE,
            lesion_type=lesion_type,
            lesion_location=lesion_location,
            lesion_lateralization=lesion_lateralization,
            additional_findings=additional_findings,
            normal_variants=normal_variants,
            clinical_correlation=clinical_correlation,
            diagnostic_impression=diagnostic_impression,
            recommended_followup=recommendations,
            confidence=confidence
        )

    @classmethod
    def _identify_lesion_type(cls, description: str) -> Optional[LesionType]:
        """Identify lesion type from imaging description"""
        if "mesial temporal sclerosis" in description or "mts" in description or "hippocampal sclerosis" in description:
            return LesionType.MESIAL_TEMPORAL_SCLEROSIS
        elif "cortical dysplasia" in description or "fcd" in description:
            return LesionType.FOCAL_CORTICAL_DYSPLASIA
        elif "dnet" in description or "ganglioglioma" in description or "low grade tumor" in description:
            return LesionType.LOW_GRADE_TUMOR
        elif "cavernoma" in description or "cavernous malformation" in description:
            return LesionType.CAVERNOVA
        elif "avm" in description or "arteriovenous malformation" in description:
            return LesionType.ARTERIOVENOUS_MALFORMATION
        elif "post-traumatic" in description or "encephalomalacia" in description:
            return LesionType.POST_TRAUMATIC
        elif "stroke" in description or "infarct" in description:
            return LesionType.STROKE_RELATED
        elif "normal" in description and "no significant" in description:
            return LesionType.NONE
        elif "no lesion" in description or "unremarkable" in description:
            return LesionType.NONE
        else:
            return None

    @classmethod
    def _identify_lesion_location(cls, description: str) -> Optional[str]:
        """Identify lesion location from imaging description"""
        locations = ["temporal", "frontal", "parietal", "occipital", "insula", "hippocampus", "amygdala"]

        for location in locations:
            if location in description:
                return location

        return None

    @classmethod
    def _identify_lateralization(cls, description: str) -> Optional[str]:
        """Identify lesion lateralization from imaging description"""
        if "right" in description and "left" not in description:
            return "right"
        elif "left" in description and "right" not in description:
            return "left"
        elif "bilateral" in description:
            return "bilateral"
        else:
            return None

    @classmethod
    def _extract_additional_findings(cls, description: str) -> List[str]:
        """Extract additional findings from imaging description"""
        findings = []

        if "white matter" in description and "hyperintensity" in description:
            findings.append("White matter hyperintensities - may be nonspecific")

        if "atrophy" in description:
            findings.append("Generalized atrophy - nonspecific")

        if "ventricular_enlargement" in description or "ventriculomegaly" in description:
            findings.append("Ventricular enlargement - possible chronic changes")

        if "enhancement" in description:
            findings.append("Contrast enhancement present - consider neoplastic etiology")

        return findings

    @classmethod
    def _identify_normal_variants(cls, description: str) -> List[str]:
        """Identify normal variants from imaging description"""
        variants = []

        if "perivascular" in description and "space" in description:
            variants.append("Perivascular spaces - normal variant")

        if "pacz" in description or "pineal cyst" in description:
            variants.append("Pineal cyst - usually incidental")

        if "lipoma" in description:
            variants.append("Intracranial lipoma - usually asymptomatic")

        return variants

    @classmethod
    def _provide_clinical_correlation(
        cls,
        lesion_type: Optional[LesionType],
        lesion_location: Optional[str],
        clinical_context: Optional[Dict]
    ) -> str:
        """Provide clinical correlation of imaging findings"""
        correlation = []

        if lesion_type:
            correlation.append(f"Lesion identified: {lesion_type.value.replace('_', ' ')}")

            if lesion_location:
                correlation.append(f"Location: {lesion_location} region")

            # Specific correlations
            if lesion_type == LesionType.MESIAL_TEMPORAL_SCLEROSIS:
                correlation.append("Classic finding for mesial temporal lobe epilepsy")
                correlation.append("Consider temporal lobectomy evaluation")

            elif lesion_type == LesionType.FOCAL_CORTICAL_DYSPLASIA:
                correlation.append("Common cause of drug-resistant focal epilepsy")
                correlation.append("Consider presurgical evaluation")

            elif lesion_type == LesionType.LOW_GRADE_TUMOR:
                correlation.append("Low-grade tumors often epileptogenic")
                correlation.append("Surgical resection often curative")

        else:
            correlation.append("No epileptogenic lesion identified")
            correlation.append("MRI does not rule out epilepsy (30-40% sensitivity)")

            if clinical_context and clinical_context.get("drug_resistance"):
                correlation.append("Consider PET/SPECT for lesion detection")
                correlation.append("Consider repeat MRI with epilepsy protocol")
                correlation.append("Consider advanced imaging techniques")

        return "\n".join(correlation)

    @classmethod
    def _form_diagnostic_impression(
        cls,
        lesion_type: Optional[LesionType],
        lesion_location: Optional[str],
        additional_findings: List[str]
    ) -> str:
        """Form diagnostic impression from imaging findings"""
        impression = []

        if lesion_type and lesion_type != LesionType.NONE:
            impression.append(f"🧠 Lesion identified: {lesion_type.value.replace('_', ' ').title()}")

            if lesion_type == LesionType.MESIAL_TEMPORAL_SCLEROSIS:
                impression.append("Classic imaging for mesial TLE")
                impression.append("Excellent surgical candidate (70-80% seizure-free)")
                impression.append("Consider presurgical evaluation")

            elif lesion_type == LesionType.FOCAL_CORTICAL_DYSPLASIA:
                impression.append("Cortical dysplasia identified")
                impression.append("Common cause of drug-resistant epilepsy")
                impression.append("Surgical resection often successful")

            elif lesion_type == LesionType.LOW_GRADE_TUMOR:
                impression.append("Low-grade tumor identified")
                impression.append("Often highly epileptogenic")
                impression.append("Surgical resection often curative for seizures")

            elif lesion_type == LesionType.CAVERNOVA:
                impression.append("Cavernous malformation identified")
                impression.append("Risk of recurrent hemorrhage")
                impression.append("Consider surgical evaluation")

        else:
            impression.append("✓ MRI brain normal/epilepsy protocol")
            impression.append("No structural lesion identified")
            impression.append("Important: Normal MRI does NOT rule out epilepsy")

            if additional_findings:
                impression.append("\nAdditional findings:")
                impression.extend(additional_findings)

        return "\n".join(impression)

    @classmethod
    def _provide_recommendations(
        cls,
        lesion_type: Optional[LesionType],
        imaging_description: str
    ) -> List[str]:
        """Provide evidence-based recommendations"""
        recommendations = []

        if lesion_type and lesion_type != LesionType.NONE:
            recommendations.extend([
                "🎯 PRE-SURGICAL EVALUATION RECOMMENDED",
                "• Video-EEG monitoring for seizure localization",
                "• Neuropsychological testing",
                "• Wada test or fMRI for language/memory mapping",
                "• Consider SEEG if non-lesional epilepsy"
            ])

        else:
            recommendations.extend([
                "📝 ADDITIONAL EVALUATION CONSIDERATIONS:",
                "• Repeat MRI with epilepsy protocol if not already done",
                "• Consider FDG-PET for ictal/interictal assessment",
                "• Consider SPECT if frequent seizures",
                "• Consider advanced imaging techniques"
            ])

        return recommendations

    @classmethod
    def _calculate_confidence(cls, lesion_type: Optional[LesionType], description: str) -> float:
        """Calculate confidence in imaging interpretation"""
        if lesion_type and lesion_type != LesionType.NONE:
            return 0.9
        elif "normal" in description.lower() or "unremarkable" in description.lower():
            return 0.7  # Normal findings have good specificity
        else:
            return 0.6  # Uncertain findings


class AdvancedImagingModalities:
    """
    Advanced epilepsy imaging modalities and indications

    Evidence-based recommendations for PET, SPECT, fMRI, DTI
    in epilepsy evaluation.
    """

    MODALITY_INDICATIONS = {
        "FDG-PET": {
            "indications": [
                "Non-lesional MRI with drug-resistant epilepsy",
                "Pre-surgical localization",
                "Differentiating temporal vs extratemporal epilepsy",
                "MRI-negative focal epilepsy"
            ],
            "findings": [
                "Hypometabolism in epileptogenic zone (interictal)",
                "Hypermetabolism (ictal - rare)",
                "Helpful for surgical planning"
            ],
            "sensitivity": "60-90% (higher with temporal lobe epilepsy)",
            "limitations": [
                "Requires seizure-free interval >24 hours",
                "Limited spatial resolution",
                "Can be normal in some epilepsies"
            ]
        },
        "Ictal_SPECT": {
            "indications": [
                "Frequent seizures suitable for ictal injection",
                "Pre-surgical localization",
                "Non-lesional epilepsy"
            ],
            "findings": [
                "Hyperperfusion in epileptogenic zone (ictal)",
                "Subtraction ictal SPECT co-registered to MRI (SISCOM)"
            ],
            "sensitivity": "70-90% for seizure localization",
            "limitations": [
                "Requires injection during seizure",
                "Logistically challenging",
                "Radiation exposure"
            ]
        },
        "Interictal_SPECT": {
            "indications": [
                "Complement to ictal SPECT",
                "Perfusion assessment"
            ],
            "findings": [
                "Hypoperfusion in epileptogenic zone"
            ],
            "sensitivity": "Lower than ictal SPECT",
            "limitations": [
                "Lower sensitivity",
                "Often non-diagnostic"
            ]
        },
        "fMRI": {
            "indications": [
                "Language mapping pre-surgery",
                "Memory mapping pre-surgery",
                "Motor cortex mapping",
                "Visual cortex mapping"
            ],
            "findings": [
                "Functional activation maps",
                "Eloquent cortex identification"
            ],
            "sensitivity": "High for functional mapping",
            "limitations": [
                "Requires patient cooperation",
                "Movement artifact can be problematic"
            ]
        },
        "DTI": {
            "indications": [
                "White matter tract assessment",
                "Pre-surgical planning",
                "Epilepsy network analysis"
            ],
            "findings": [
                "White matter integrity",
                "Tract displacement",
                "Network abnormalities"
            ],
            "sensitivity": "Emerging technique",
            "limitations": [
                "Limited clinical validation",
                "Technical challenges"
            ]
        }
    }

    @classmethod
    def recommend_advanced_imaging(
        cls,
        mri_findings: str,
        seizure_frequency: str,
        surgical_candidate: bool
    ) -> List[str]:
        """Recommend appropriate advanced imaging based on clinical scenario"""
        recommendations = []

        # If MRI negative and drug-resistant
        if "normal" in mri_findings.lower() and "drug resistant" in seizure_frequency.lower():
            recommendations.extend([
                "🔍 ADVANCED IMAGING RECOMMENDED FOR MRI-NEGATIVE EPILEPSY:",
                "• FDG-PET (first-line advanced imaging)",
                "• Consider SPECT if frequent seizures",
                "• Consider repeat MRI with epilepsy protocol"
            ])

        # If surgical candidate
        if surgical_candidate:
            recommendations.extend([
                "",
                "🎯 PRE-SURGICAL IMAGING RECOMMENDED:",
                "• fMRI for language/memory mapping (if temporal lobe)",
                "• Consider DTI for tract mapping",
                "• Ictal SPECT if localizing uncertainty"
            ])

        # If frequent seizures
        if "frequent" in seizure_frequency.lower() or "daily" in seizure_frequency.lower():
            recommendations.extend([
                "",
                "🎺 ICTAL SPECT CONSIDERED:",
                "• High diagnostic yield with ictal injection",
                "• Requires seizure monitoring setup",
                "• Consider if other imaging non-diagnostic"
            ])

        return recommendations


class ImagingDiagnosticYield:
    """
    Evidence-based imaging diagnostic yield data

    Sensitivity, specificity, and yield data for various imaging
    modalities in epilepsy evaluation.
    """

    DIAGNOSTIC_YIELD = {
        "epilepsy_protocol_mri": {
            "yield": "70-80%",
            "context": "drug-resistant focal epilepsy",
            "sensitivity": "34% new onset, 70-80% drug-resistant",
            "specificity": "High (>95%)",
            "gold_standard": True
        },
        "ct_brain": {
            "yield": "10-20%",
            "context": "acute seizures or MRI contraindicated",
            "sensitivity": "Low for epilepsy",
            "specificity": "High for acute hemorrhage",
            "indications": ["Acute presentation", "MRI contraindication", "Calification detection"]
        },
        "fdg_pet": {
            "yield": "60-90%",
            "context": "MRI-negative drug-resistant epilepsy",
            "sensitivity": "60-90%",
            "specificity": "80-90%",
            "indications": ["MRI-negative epilepsy", "Pre-surgical planning"]
        },
        "ictal_spect": {
            "yield": "70-90%",
            "context": "With successful ictal injection",
            "sensitivity": "70-90%",
            "specificity": "70-90%",
            "limitations": ["Requires ictal injection", "Logistically complex"]
        },
        "fmri": {
            "yield": "High for functional mapping",
            "context": "Pre-surgical language/memory mapping",
            "sensitivity": "High for activation detection",
            "specificity": "High",
            "indications": ["Pre-surgical planning", "Eloquent cortex mapping"]
        }
    }

    @classmethod
    def get_imaging_algorithm(cls) -> List[str]:
        """Get evidence-based imaging algorithm for epilepsy"""
        return [
            "📋 EPILEPSY IMAGING ALGORITHM:",
            "",
            "1️⃣ FIRST-LINE (All focal epilepsy):",
            "   • MRI brain with epilepsy protocol (HIGH PRIORITY)",
            "   • Consider CT if MRI contraindicated or acute presentation",
            "",
            "2️⃣ SECOND-LINE (Drug-resistant, MRI-negative):",
            "   • Repeat MRI with epilepsy protocol (if not optimal)",
            "   • FDG-PET for localizing information",
            "   • Consider ictal SPECT if frequent seizures",
            "",
            "3️⃣ PRE-SURGICAL EVALUATION:",
            "   • fMRI for functional mapping",
            "   • Consider DTI for white matter assessment",
            "   • Consider SEEG for precise localization",
            "",
            "💡 KEY PRINCIPLES:",
            "• MRI epilepsy protocol is essential for focal epilepsy",
            "• Normal MRI does NOT rule out epilepsy",
            "• Advanced imaging increases diagnostic yield",
            "• Imaging must be correlated with EEG and clinical data"
        ]


__all__ = [
    'ImagingModality',
    'LesionType',
    'ImagingFindings',
    'EpilepsyMRIProtocol',
    'EpilepsyImagingInterpreter',
    'AdvancedImagingModalities',
    'ImagingDiagnosticYield'
]