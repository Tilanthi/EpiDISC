"""
EPIDISC Neurophysiology and EEG Interpretation
==============================================

Comprehensive EEG interpretation system with normal variants,
epileptiform discharges, and clinical correlation capabilities.

Based on:
- ILAE EEG terminology commission
- Standardized EEG terminology (2023)
- Clinical EEG interpretation standards
- Evidence-based EEG diagnostic yield

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class EEGBackgroundActivity(Enum):
    """EEG background activity patterns"""
    NORMAL = "normal"                          # Normal awake background
    SLOWED = "slowed"                          # Generalized slowing
    POSTERIOR_SLOWING = "posterior_slowing"    # Posterior rhythm slowing
    ASYMMETRY = "asymmetry"                    # Hemispheric asymmetry
    ATTENUATION = "attenuation"                # Background attenuation
    BURST_SUPPRESSION = "burst_suppression"   # Burst-suppression pattern


class EpileptiformPattern(Enum):
    """Types of epileptiform discharges"""
    SPIKE = "spike"                            # <70ms duration
    SHARP_WAVE = "sharp_wave"                 # 70-200ms duration
    SHARP_SLOW = "sharp_slow"                # Sharp wave followed by slow wave
    SPIKE_WAVE = "spike_wave"                # Spike followed by slow wave
    POLYSPIKE = "polyspike"                  # Multiple spikes
    POLYSPIKE_WAVE = "polyspike_wave"        # Polyspike followed by slow wave


class EEGLocalization(Enum):
    """EEG localization patterns"""
    GENERALIZED = "generalized"                # Bilateral synchronous
    FOCAL = "focal"                           # Single region
    MULTIFOCAL = "multifocal"                # Independent foci
    LATERALIZED = "lateralized"              # One hemisphere
    INDEPENDENT_BILATERAL = "independent_bilateral"  # Independent bilateral spikes


@dataclass
class EEGFindings:
    """
    Complete EEG interpretation findings

    Includes background activity, epileptiform discharges,
    normal variants, artifacts, and clinical correlation.
    """

    background: EEGBackgroundActivity
    background_frequency: Optional[float]  # Hz (alpha frequency)
    epileptiform_discharges: List[Tuple[EpileptiformPattern, EEGLocalization, str]]
    normal_variants: List[str]
    artifacts: List[str]
    focal_slowing: Optional[Dict[str, str]]  # location, description
    generalized_abnormalities: List[str]
    activation_procedures: List[str]  # HV, photic stimulation, sleep
    sleep_achieved: bool
    clinical_correlation: str
    diagnostic_impression: str
    confidence: float


class EEGInterpreter:
    """
    Comprehensive EEG interpretation system

    Provides consultant-level EEG analysis with clinical
    correlation and diagnostic recommendations.
    """

    # Normal EEG background by age
    NORMAL_BACKGROUND = {
        "adult": {
            "alpha_frequency": "9-11 Hz",
            "alpha_distribution": "posterior dominant",
            "reactivity": "present to eye opening",
            "anterior rhythm": "low-amplitude beta",
            "sleep_spindles": "present in stage N2"
        },
        "adolescent": {
            "alpha_frequency": "9-11 Hz",
            "alpha_distribution": "posterior dominant",
            "reactivity": "present",
            "anterior rhythm": "beta mixed with alpha"
        },
        "child": {
            "alpha_frequency": "8-10 Hz",
            "alpha_distribution": "posterior dominant",
            "reactivity": "present",
            "background": "more posterior slow activity"
        },
        "elderly": {
            "alpha_frequency": "8-9 Hz",
            "alpha_distribution": "posterior dominant but slower",
            "reactivity": "may be reduced",
            "background": "more slow activity"
        }
    }

    # Epileptiform discharge characteristics
    EPILEPTIFORM_FEATURES = {
        "spike": {
            "duration": "<70ms",
            "morphology": "sharp, pointed",
            "aftergoing_slow_wave": "often present",
            "field": "limited distribution",
            "significance": "highly suggestive of epilepsy"
        },
        "sharp_wave": {
            "duration": "70-200ms",
            "morphology": "sharp but less pointed than spike",
            "aftergoing_slow_wave": "typically present",
            "field": "limited distribution",
            "significance": "suggestive of epilepsy"
        },
        "spike_wave": {
            "pattern": "spike followed by slow wave",
            "duration": "spike <70ms, slow wave 200-500ms",
            "morphology": "complex morphology",
            "significance": "characteristic of generalized epilepsy"
        }
    }

    # Normal variants (can be mistaken for epileptiform)
    NORMAL_VARIANTS = {
        "benign_epileptiform_transients_of_sleep": {
            "description": "BETS - sharp transients in temporal regions during sleep",
            "location": "temporal",
            "timing": "sleep",
            "significance": "normal variant, not epileptiform"
        },
        "wicket_spikes": {
            "description": "Arch-shaped waves in temporal regions",
            "location": "temporal",
            "morphology": "wicket-like",
            "significance": "normal variant"
        },
        "rhythmic_midtemporal_theta": {
            "description": "RMTT - rhythmic theta bursts in temporal regions",
            "location": "midtemporal",
            "frequency": "5-7 Hz",
            "significance": "normal variant in adults"
        },
        "small_sharp_spikes": {
            "description": "Small sharp spikes - biphasic sharp transients",
            "location": "frontopolar or temporal",
            "duration": "<50ms",
            "significance": "normal variant"
        },
        "psychomotor_variant": {
            "description": "Rhythmic theta bursts",
            "location": "frontal/temporal",
            "frequency": "5-7 Hz",
            "significance": "normal variant"
        },
        "subclinical_rhythmic_discharge": {
            "description": "Rhythmic delta in adults",
            "location": "frontal",
            "frequency": "1-2 Hz",
            "significance": "normal variant, not epileptiform"
        },
        "vertex_sharp": {
            "description": "Vertex sharp transients in sleep",
            "location": "vertex (Cz, Fz, Pz)",
            "timing": "stage N1/N2 sleep",
            "significance": "normal sleep finding"
        },
        "sleep_spindles": {
            "description": "Bursts of 12-14 Hz activity",
            "location": "centroparietal",
            "timing": "stage N2 sleep",
            "significance": "normal sleep finding"
        },
        "k_complexes": {
            "description": "Sharp wave followed by slow wave complex",
            "location": "vertex",
            "timing": "stage N2 sleep",
            "significance": "normal sleep finding"
        }
    }

    # Artifacts that can be mistaken for epileptiform
    COMMON_ARTIFACTS = {
        "eye_blinks": {
            "description": "High-amplitude frontal potentials",
            "location": "FP1, FP2",
            "characteristics": "biphasic, synchronous",
            "identification": "correlate with observed blinking"
        },
        "eye_movements": {
            "description": "Slow lateral eye movements",
            "location": "Fp, F channels",
            "characteristics": "out-of-phase between hemispheres"
        },
        "muscle_artifact": {
            "description": "High-frequency EMG activity",
            "characteristics": "broadband, high amplitude",
            "location": "cranial muscles, neck"
        },
        "movement_artifact": {
            "description": "Slow wave-like activity from movement",
            "characteristics": "rhythmic, variable",
            "identification": "correlate with observed movement"
        },
        "ecg_artifact": {
            "description": "EKG artifact in EEG channels",
            "characteristics": "regular rhythm, EKG frequency",
            "location": "channels near heart"
        },
        "glossokinetic": {
            "description": "Tongue movement artifact",
            "characteristics": "low-frequency rhythmic",
            "location": "T1, T2, F7, F8"
        },
        "sweat_artifact": {
            "description": "Slow potential changes from sweating",
            "characteristics": "very slow, widespread"
        },
        "electrode_pop": {
            "description": "Sudden high-amplitude transients",
            "characteristics": "restricted to one electrode",
            "identification": "impedance check reveals poor contact"
        }
    }

    @classmethod
    def interpret_eeg(
        cls,
        eeg_description: str,
        age_group: str = "adult",
        clinical_context: Optional[str] = None
    ) -> EEGFindings:
        """
        Interpret EEG findings with clinical correlation

        Args:
            eeg_description: Text description of EEG findings
            age_group: Age group for normal background expectations
            clinical_context: Clinical information for correlation

        Returns:
            EEGFindings object with complete interpretation
        """
        eeg_lower = eeg_description.lower()

        # Assess background
        background = cls._assess_background(eeg_lower, age_group)
        background_frequency = cls._extract_alpha_frequency(eeg_lower)

        # Identify epileptiform discharges
        epileptiform = cls._identify_epileptiform(eeg_lower)

        # Identify normal variants
        normal_variants = cls._identify_normal_variants(eeg_lower)

        # Identify artifacts
        artifacts = cls._identify_artifacts(eeg_lower)

        # Assess focal slowing
        focal_slowing = cls._assess_focal_slowing(eeg_lower)

        # Assess generalized abnormalities
        generalized_abnormalities = cls._assess_generalized_abnormalities(eeg_lower)

        # Clinical correlation
        clinical_correlation = cls._provide_clinical_correlation(
            epileptiform, focal_slowing, clinical_context
        )

        # Diagnostic impression
        diagnostic_impression = cls._form_diagnostic_impression(
            background, epileptiform, focal_slowing, clinical_correlation
        )

        # Calculate confidence
        confidence = cls._calculate_confidence(epileptiform, focal_slowing)

        return EEGFindings(
            background=background,
            background_frequency=background_frequency,
            epileptiform_discharges=epileptiform,
            normal_variants=normal_variants,
            artifacts=artifacts,
            focal_slowing=focal_slowing,
            generalized_abnormalities=generalized_abnormalities,
            activation_procedures=cls._extract_activation_procedures(eeg_lower),
            sleep_achieved="sleep" in eeg_lower,
            clinical_correlation=clinical_correlation,
            diagnostic_impression=diagnostic_impression,
            confidence=confidence
        )

    @classmethod
    def _assess_background(
        cls,
        eeg_description: str,
        age_group: str
    ) -> EEGBackgroundActivity:
        """Assess EEG background activity"""
        if "normal background" in eeg_description:
            return EEGBackgroundActivity.NORMAL
        elif "generalized slowing" in eeg_description:
            return EEGBackgroundActivity.SLOWED
        elif "posterior slowing" in eeg_description:
            return EEGBackgroundActivity.POSTERIOR_SLOWING
        elif "asymmetric" in eeg_description:
            return EEGBackgroundActivity.ASYMMETRY
        elif "burst suppression" in eeg_description:
            return EEGBackgroundActivity.BURST_SUPPRESSION
        else:
            return EEGBackgroundActivity.NORMAL

    @classmethod
    def _extract_alpha_frequency(cls, eeg_description: str) -> Optional[float]:
        """Extract alpha frequency from EEG description"""
        # Look for patterns like "9-10 Hz", "alpha 9-11 Hz", etc.
        import re
        freq_pattern = r'(\d+[.-]?\d*)\s*hz'
        matches = re.findall(freq_pattern, eeg_description)

        if matches:
            return float(matches[0])
        return None

    @classmethod
    def _identify_epileptiform(cls, eeg_description: str) -> List[Tuple]:
        """Identify epileptiform discharges"""
        epileptiform = []

        # Check for spikes
        if "spike" in eeg_description and "normal" not in eeg_description:
            # Determine localization
            localization = cls._determine_localization(eeg_description)
            epileptiform.append((EpileptiformPattern.SPIKE, localization, "spike"))

        # Check for sharp waves
        if "sharp wave" in eeg_description:
            localization = cls._determine_localization(eeg_description)
            epileptiform.append((EpileptiformPattern.SHARP_WAVE, localization, "sharp wave"))

        # Check for spike-wave complexes
        if "spike and wave" in eeg_description or "spike-wave" in eeg_description:
            localization = cls._determine_localization(eeg_description)
            epileptiform.append((EpileptiformPattern.SPIKE_WAVE, localization, "spike-wave"))

        # Check for polyspikes
        if "polyspike" in eeg_description:
            localization = cls._determine_localization(eeg_description)
            epileptiform.append((EpileptiformPattern.POLYSPIKE, localization, "polyspike"))

        return epileptiform

    @classmethod
    def _determine_localization(cls, eeg_description: str) -> EEGLocalization:
        """Determine localization of epileptiform activity"""
        if "generalized" in eeg_description or "bilateral synchronous" in eeg_description:
            return EEGLocalization.GENERALIZED
        elif "multifocal" in eeg_description or "independent bilateral" in eeg_description:
            return EEGLocalization.MULTIFOCAL
        elif "right" in eeg_description and "left" not in eeg_description:
            return EEGLocalization.LATERALIZED
        elif "left" in eeg_description and "right" not in eeg_description:
            return EEGLocalization.LATERALIZED
        elif "temporal" in eeg_description or "frontal" in eeg_description:
            return EEGLocalization.FOCAL
        else:
            return EEGLocalization.GENERALIZED

    @classmethod
    def _identify_normal_variants(cls, eeg_description: str) -> List[str]:
        """Identify normal variants in EEG"""
        variants = []

        for variant_name, details in cls.NORMAL_VARIANTS.items():
            variant_keywords = [
                variant_name.replace("_", " "),
                details.get("description", ""),
                details.get("location", "")
            ]

            for keyword in variant_keywords:
                if keyword.lower() in eeg_description:
                    variants.append(f"{variant_name.replace('_', ' ').title()}: {details['significance']}")
                    break

        return variants

    @classmethod
    def _identify_artifacts(cls, eeg_description: str) -> List[str]:
        """Identify artifacts in EEG"""
        artifacts = []

        for artifact_name, details in cls.COMMON_ARTIFACTS.items():
            if any(keyword in eeg_description for keyword in [
                artifact_name.replace("_", " "),
                details.get("location", "")
            ]):
                artifacts.append(f"{artifact_name.replace('_', ' ').title()}")

        return artifacts

    @classmethod
    def _assess_focal_slowing(cls, eeg_description: str) -> Optional[Dict[str, str]]:
        """Assess focal slowing in EEG"""
        if "focal slowing" in eeg_description or "focal slow" in eeg_description:

            # Determine location
            location = "unknown"
            for region in ["temporal", "frontal", "occipital", "parietal", "left", "right"]:
                if region in eeg_description:
                    location = region
                    break

            return {
                "location": location,
                "description": "Focal slowing present - may indicate structural abnormality",
                "significance": "Consider MRI brain if not already done"
            }

        return None

    @classmethod
    def _assess_generalized_abnormalities(cls, eeg_description: str) -> List[str]:
        """Assess generalized abnormalities in EEG"""
        abnormalities = []

        if "generalized slowing" in eeg_description:
            abnormalities.append("Generalized background slowing - encephalopathic pattern")

        if "burst suppression" in eeg_description:
            abnormalities.append("Burst suppression - severe encephalopathy")

        if "triphasic" in eeg_description:
            abnormalities.append("Triphasic waves - metabolic/toxic encephalopathy")

        return abnormalities

    @classmethod
    def _extract_activation_procedures(cls, eeg_description: str) -> List[str]:
        """Extract activation procedures performed"""
        procedures = []

        if "hyperventilation" in eeg_description or "hv" in eeg_description:
            procedures.append("Hyperventilation")

        if "photic" in eeg_description or "photic stimulation" in eeg_description:
            procedures.append("Photic stimulation")

        if "sleep" in eeg_description or "drowsy" in eeg_description:
            procedures.append("Sleep deprivation")

        if "photoparoxysmal" in eeg_description:
            procedures.append("Photosensitivity demonstrated")

        return procedures

    @classmethod
    def _provide_clinical_correlation(
        cls,
        epileptiform: List,
        focal_slowing: Optional[Dict],
        clinical_context: Optional[str]
    ) -> str:
        """Provide clinical correlation of EEG findings"""
        correlation = []

        if epileptiform:
            pattern_types = [pattern[0].value for pattern in epileptiform]
            correlation.append(f"Epileptiform discharges ({', '.join(set(pattern_types))}) present")

            if len(epileptiform) > 1:
                correlation.append("Multiple epileptiform patterns suggest epileptogenic zone")
        else:
            correlation.append("No epileptiform discharges identified")

        if focal_slowing:
            correlation.append(f"Focal slowing in {focal_slowing['location']} region - may indicate underlying structural abnormality")

        if clinical_context:
            correlation.append(f"\nClinical correlation: {clinical_context}")

        return "\n".join(correlation)

    @classmethod
    def _form_diagnostic_impression(
        cls,
        background: EEGBackgroundActivity,
        epileptiform: List,
        focal_slowing: Optional[Dict],
        clinical_correlation: str
    ) -> str:
        """Form diagnostic impression"""
        impression = []

        if epileptiform:
            impression.append("🧠 EEG shows epileptiform activity - supports diagnosis of epilepsy")

            # Determine if focal or generalized
            localizations = [pattern[1] for pattern in epileptiform]
            if all(loc == EEGLocalization.GENERALIZED for loc in localizations):
                impression.append("Generalized epileptiform discharges suggest generalized epilepsy")
            elif all(loc != EEGLocalization.GENERALIZED for loc in localizations):
                impression.append("Focal epileptiform discharges suggest focal epilepsy")

        elif focal_slowing:
            impression.append("⚠️ EEG shows focal slowing without epileptiform discharges")
            impression.append("Consider structural abnormality - MRI brain recommended")
            impression.append("Indeterminate for epilepsy - clinical correlation required")

        else:
            impression.append("✓ Normal EEG - does not rule out epilepsy")
            impression.append("Sensitivity: Single routine EEG ~29-50%")
            impression.append("Consider repeat EEG, sleep-deprived EEG, or video-EEG monitoring")

        return "\n".join(impression)

    @classmethod
    def _calculate_confidence(cls, epileptiform: List, focal_slowing: Optional[Dict]) -> float:
        """Calculate confidence in EEG interpretation"""
        if epileptiform:
            return 0.9  # High confidence with epileptiform discharges
        elif focal_slowing:
            return 0.7  # Moderate confidence with focal slowing
        else:
            return 0.5  # Low confidence with normal EEG (can't rule out)


class EEGDiagnosticYield:
    """
    EEG diagnostic yield data and recommendations

    Evidence-based guidance on EEG utility and optimization.
    """

    DIAGNOSTIC_YIELD = {
        "first_routine_eeg": {
            "yield": "29-50%",
            "factors_affecting": ["Timing since event", "Sleep deprivation", "Medications"],
            "optimization": "Consider sleep deprivation increases yield by ~30%"
        },
        "repeat_routine_eeg": {
            "yield": "Additional 10-15%",
            "indication": "First EEG normal but high clinical suspicion",
            "timing": "Within 1 week of first EEG"
        },
        "sleep_deprived_eeg": {
            "yield": "60-70%",
            "indication": "High suspicion despite normal routine EEG",
            "protocol": "Partial sleep deprivation (4-6 hours)"
        },
        "ambulatory_eeg": {
            "yield": "70-80%",
            "indication": "Events occurring several times per week",
            "duration": "24-72 hours"
        },
        "video_eeg": {
            "yield": "85-95%",
            "indication": "Diagnostic uncertainty, presurgical evaluation",
            "gold_standard": True
        }
    }

    @classmethod
    def recommend_eeg_strategy(
        cls,
        event_frequency: str,
        clinical_suspicion: str,
        previous_eegs: int = 0
    ) -> List[str]:
        """Recommend optimal EEG strategy based on clinical scenario"""
        recommendations = []

        if clinical_suspicion == "high":
            if event_frequency == "daily":
                recommendations.extend([
                    "🎺 VIDEO-EEG MONITORING RECOMMENDED",
                    "• Gold standard for diagnosis",
                    "• Capture typical events with clinical correlation",
                    "• Diagnostic yield: 85-95%"
                ])

            elif event_frequency == "weekly":
                recommendations.extend([
                    "🎺 AMBULATORY EEG RECOMMENDED",
                    "• 24-72 hour monitoring",
                    "• Diagnostic yield: 70-80%",
                    "• Consider if video-EEG not available"
                ])

            else:  # less frequent
                recommendations.extend([
                    "📝 SLEEP-DEPRIVED EEG RECOMMENDED",
                    "• Partial sleep deprivation (4-6 hours)",
                    "• Increases yield by ~30%",
                    "• Repeat EEG if first normal"
                ])

        elif clinical_suspicion == "moderate":
            recommendations.extend([
                "📝 ROUTINE EEG FIRST",
                "• Consider sleep deprivation",
                "• Repeat if high suspicion persists",
                "• Consider video-EEG if diagnostic uncertainty"
            ])

        else:  # low suspicion
            recommendations.extend([
                "✓ ROUTINE EEG APPROPRIATE",
                "• Consider alternative diagnoses",
                "• May not be necessary if low suspicion",
                "• Clinical correlation essential"
            ])

        return recommendations

    @classmethod
    def get_interictal_eeg_significance(cls) -> Dict[str, str]:
        """Get significance of interictal epileptiform discharges"""
        return {
            "generalized_spike_wave": {
                "significance": "Strongly suggests generalized epilepsy",
                "typical_syndromes": [
                    "Childhood absence epilepsy",
                    "Juvenile absence epilepsy",
                    "Juvenile myoclonic epilepsy"
                ],
                "localization_value": "Less specific - generalized from onset"
            },
            "focal_spikes": {
                "significance": "Suggests focal epilepsy",
                "localization_value": "Indicates region of epileptogenesis",
                "correlation": "Correlate with clinical semiology and imaging"
            },
            "independent_bilateral_spikes": {
                "significance": "Suggests multifocal epilepsy or generalized epilepsy",
                "considerations": [
                    "Multiple focal epileptogenic zones",
                    "Generalized epilepsy with focal expression",
                    "Need clinical correlation for accurate classification"
                ]
            }
        }


__all__ = [
    'EEGBackgroundActivity',
    'EpileptiformPattern',
    'EEGLocalization',
    'EEGFindings',
    'EEGInterpreter',
    'EEGDiagnosticYield'
]