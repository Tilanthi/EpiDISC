"""
EPIDISC Epilepsy Classification System
=======================================

Implementation of ILAE 2017 seizure and epilepsy classification systems
with consultant-level clinical reasoning capabilities.

Based on:
- ILAE Commission on Classification and Terminology (2017)
- "Operational classification of seizure types by the ILAE"
- "Seizure semiology and seizure classification" (2022)

Version: 1.0.0
ILAE Classification Version: 2017
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class SeizureOnset(Enum):
    """Primary seizure onset classification per ILAE 2017"""
    FOCAL = "focal"                    # Onset in one hemisphere
    GENERALIZED = "generalized"        # Onset in both hemispheres
    UNKNOWN = "unknown"                # Onset is unknown


class FocalAwareness(Enum):
    """Awareness level for focal seizures"""
    AWARE = "focal aware"              # Fully aware
    IMPAIRED = "focal impaired awareness"  # Impaired awareness
    UNKNOWN = "focal unknown awareness"  # Awareness unknown


class MotorFeatures(Enum):
    """Motor seizure features"""
    TONIC = "tonic"                    # Sustained muscle contraction
    CLONIC = "clonic"                  # Rhythmic jerking
    TONIC_CLONIC = "tonic-clonic"      # Tonic then clonic
    MYOCLONIC = "myoclonic"            # Brief muscle jerks
    ATONIC = "atonic"                   # Loss of muscle tone
    AUTOMATISMS = "automatisms"        # Repetitive purposeless movements
    HYPERKINETIC = "hyperkinetic"      # Excessive movement
    AKINETIC = "akinetic"              # Pauses movement
    NONE = "absent"                    # No motor features


class NonMotorFeatures(Enum):
    """Non-motor seizure features"""
    AURA = "aura"                      # Subjective sensory/psychological phenomena
    AUTONOMIC = "autonomic"            # Autonomic symptoms
    COGNITIVE = "cognitive"            # Cognitive disturbances
    BEHAVIORAL = "behavioral"         # Behavioral changes
    EMOTIONAL = "emotional"            # Emotional experiences
    SENSORY = "sensory"                # Sensory symptoms


@dataclass
class SeizureClassification:
    """
    Complete seizure classification according to ILAE 2017 operational classification

    Classification hierarchy:
    1. Seizure onset (Focal/Generalized/Unknown)
    2. Motor/Non-motor features
    3. Specific seizure type
    4. Awareness (if focal)
    """

    seizure_onset: SeizureOnset
    motor_features: Optional[List[MotorFeatures]] = None
    non_motor_features: Optional[List[NonMotorFeatures]] = None
    focal_awareness: Optional[FocalAwareness] = None
    specific_type: Optional[str] = None
    semiology: Optional[str] = None
    localization: Optional[str] = None
    lateralization: Optional[str] = None
    confidence: float = 0.8  # Confidence in classification (0-1)

    def get_classification_path(self) -> str:
        """Get full ILAE classification path"""
        path = []

        # Level 1: Onset
        path.append(self.seizure_onset.value)

        # Level 2: Awareness (if focal)
        if self.seizure_onset == SeizureOnset.FOCAL and self.focal_awareness:
            path.append(self.focal_awareness.value)

        # Level 3: Motor/Non-motor features
        if self.motor_features:
            for feature in self.motor_features:
                path.append(feature.value)

        if self.non_motor_features:
            for feature in self.non_motor_features:
                path.append(feature.value)

        # Level 4: Specific type
        if self.specific_type:
            path.append(self.specific_type)

        return " → ".join(path)

    def get_differential_diagnosis(self) -> List[str]:
        """Get differential diagnoses based on classification"""
        differentials = []

        if self.seizure_onset == SeizureOnset.FOCAL:
            differentials.extend([
                "Psychogenic Non-Epileptic Seizures (PNES)",
                "Migraine (especially with aura)",
                "Syncope (especially with myoclonic jerks)",
                "Sleep disorders (parasomnias, RBD)",
                "Movement disorders (tics, dystonia)",
                "Transient global amnesia"
            ])
        elif self.seizure_onset == SeizureOnset.GENERALIZED:
            differentials.extend([
                "Psychogenic Non-Epileptic Seizures (PNES)",
                "Syncope with convulsions",
                "Narcolepsy/cataplexy",
                "Movement disorders (myoclonus, chorea)",
                "Metabolic disturbances"
            ])

        return differentials


@dataclass
class EpilepsyClassification:
    """
    Epilepsy classification according to ILAE 2017

    Classification considers:
    1. Seizure type(s)
    2. Epilepsy type (Focal/Generalized/Unknown)
    3. Epilepsy syndrome (if identifiable)
    4. Etiology
    """

    epilepsy_type: str  # focal, generalized, combined generalized and focal, unknown
    seizure_types: List[SeizureClassification]
    epilepsy_syndrome: Optional[str] = None
    etiology: Optional[str] = None
    genetic_cause: Optional[str] = None
    structural_cause: Optional[str] = None
    metabolic_cause: Optional[str] = None
    immune_cause: Optional[str] = None
    infectious_cause: Optional[str] = None
    age_at_onset: Optional[int] = None
    severity: Optional[str] = None  # mild, moderate, severe
    drug_resistance: Optional[bool] = None

    def get_treatment_recommendations(self) -> List[str]:
        """Get initial treatment recommendations based on classification"""
        recommendations = []

        if self.epilepsy_type == "focal":
            recommendations.extend([
                "Consider carbamazepine, lamotrigine, or levetiracetam as first-line",
                "MRI brain epilepsy protocol indicated",
                "Routine EEG may be diagnostic (consider sleep deprivation)",
                "Consider video-EEG monitoring if diagnosis uncertain"
            ])
        elif self.epilepsy_type == "generalized":
            recommendations.extend([
                "Consider valproate, lamotrigine, or levetiracetam as first-line",
                "Avoid carbamazepine and phenytoin (may worsen generalized seizures)",
                "Routine EEG with hyperventilation and photic stimulation",
                "Genetic testing may be indicated"
            ])
        elif self.epilepsy_type == "combined generalized and focal":
            recommendations.extend([
                "Broad-spectrum ASMs preferred (levetiracetam, lamotrigine, valproate)",
                "Genetic testing strongly recommended",
                "Consider developmental and epileptic encephalopathies"
            ])

        if self.drug_resistance:
            recommendations.extend([
                "Re-evaluate diagnosis",
                "Consider ASM combination optimization",
                "Refer for presurgical evaluation if focal",
                "Consider neuromodulation (VNS, DBS, RNS)"
            ])

        return recommendations


class ILAEClassification:
    """
    ILAE 2017 Classification System Implementation

    Provides consultant-level seizure and epilepsy classification
    with clinical reasoning and differential diagnosis capabilities.
    """

    # Focal seizure types
    FOCAL_AWARE = "Focal aware seizure"
    FOCAL_IMPAIRED_AWARENESS = "Focal impaired awareness seizure"
    FOCAL_MOTOR = "Focal motor seizure"
    FOCAL_NON_MOTOR = "Focal non-motor seizure"

    # Generalized seizure types
    GENERALIZED_TONIC_CLONIC = "Generalized tonic-clonic seizure"
    ABSENCE = "Absence seizure"
    TYPICAL_ABSENCE = "Typical absence"
    ATYPICAL_ABSENCE = "Atypical absence"
    MYOCLONIC = "Myoclonic seizure"
    ATONIC = "Atonic seizure"
    CLONIC = "Clonic seizure"
    TONIC = "Tonic seizure"

    # Unknown onset seizure types
    UNKNOWN_MOTOR = "Unknown motor seizure"
    UNKNOWN_NON_MOTOR = "Unknown non-motor seizure"

    # Epilepsy types
    FOCAL_EPILEPSY = "Focal epilepsy"
    GENERALIZED_EPILEPSY = "Generalized epilepsy"
    COMBINED_EPILEPSY = "Combined generalized and focal epilepsy"
    UNKNOWN_EPILEPSY = "Unknown epilepsy"

    @classmethod
    def classify_seizure(cls, description: str) -> SeizureClassification:
        """
        Classify seizure based on clinical description

        Args:
            description: Clinical description of seizure

        Returns:
            SeizureClassification object with full classification
        """
        description_lower = description.lower()

        # Determine onset
        onset = cls._determine_onset(description_lower)

        # Determine features
        motor_features = cls._extract_motor_features(description_lower)
        non_motor_features = cls._extract_non_motor_features(description_lower)

        # Determine awareness (if focal)
        focal_awareness = cls._determine_focal_awareness(description_lower)

        # Determine specific type
        specific_type = cls._determine_specific_type(
            onset, motor_features, non_motor_features, description_lower
        )

        return SeizureClassification(
            seizure_onset=onset,
            motor_features=motor_features,
            non_motor_features=non_motor_features,
            focal_awareness=focal_awareness,
            specific_type=specific_type,
            semiology=description
        )

    @classmethod
    def _determine_onset(cls, description: str) -> SeizureOnset:
        """Determine seizure onset from description"""
        focal_indicators = [
            "aura", "focal", "focal onset", "partial", "local",
            "jerking one side", "one arm", "one leg", " unilateral",
            "temporal lobe", "frontal lobe", "focal motor"
        ]

        generalized_indicators = [
            "generalized", "bilaterally", "both sides", "whole body",
            "from the start", "immediately", "absence", "generalized onset",
            "tonic-clonic", "convulsion"
        ]

        for indicator in focal_indicators:
            if indicator in description:
                return SeizureOnset.FOCAL

        for indicator in generalized_indicators:
            if indicator in description:
                return SeizureOnset.GENERALIZED

        return SeizureOnset.UNKNOWN

    @classmethod
    def _extract_motor_features(cls, description: str) -> List[MotorFeatures]:
        """Extract motor features from description"""
        features = []

        if "tonic" in description:
            features.append(MotorFeatures.TONIC)
        if "clonic" in description or "jerking" in description or "shaking" in description:
            features.append(MotorFeatures.CLONIC)
        if "tonic-clonic" in description or "convulsion" in description:
            features.append(MotorFeatures.TONIC_CLONIC)
        if "myoclonic" in description or "jerk" in description and "brief" in description:
            features.append(MotorFeatures.MYOCLONIC)
        if "atonic" in description or "drop" in description or "fall" in description:
            features.append(MotorFeatures.ATONIC)
        if "automatisms" in description or "lip smacking" in description or "picking" in description:
            features.append(MotorFeatures.AUTOMATISMS)

        return features if features else None

    @classmethod
    def _extract_non_motor_features(cls, description: str) -> List[NonMotorFeatures]:
        """Extract non-motor features from description"""
        features = []

        if "aura" in description or "rising sensation" in description:
            features.append(NonMotorFeatures.AURA)
        if "autonomic" in description or "heart racing" in description or "sweating" in description:
            features.append(NonMotorFeatures.AUTONOMIC)
        if "confused" in description or "memory" in description:
            features.append(NonMotorFeatures.COGNITIVE)
        if "fear" in description or "panic" in description or "depression" in description:
            features.append(NonMotorFeatures.EMOTIONAL)
        if "tingling" in description or "numbness" in description or "visual" in description:
            features.append(NonMotorFeatures.SENSORY)

        return features if features else None

    @classmethod
    def _determine_focal_awareness(cls, description: str) -> Optional[FocalAwareness]:
        """Determine awareness level for focal seizures"""
        aware_indicators = [
            "aware", "remembered", "responsive", "could answer",
            "knew what was happening", "conscious"
        ]

        impaired_indicators = [
            "unaware", "unresponsive", "confused", "amnesia",
            "don't remember", "lost consciousness", "impaired awareness"
        ]

        for indicator in aware_indicators:
            if indicator in description:
                return FocalAwareness.AWARE

        for indicator in impaired_indicators:
            if indicator in description:
                return FocalAwareness.IMPAIRED

        return None

    @classmethod
    def _determine_specific_type(
        cls,
        onset: SeizureOnset,
        motor_features: Optional[List[MotorFeatures]],
        non_motor_features: Optional[List[NonMotorFeatures]],
        description: str
    ) -> Optional[str]:
        """Determine specific seizure type"""
        if onset == SeizureOnset.FOCAL:
            if motor_features and MotorFeatures.AUTOMATISMS in motor_features:
                return "Focal impaired awareness seizure with automatisms"
            elif motor_features:
                return "Focal motor seizure"
            elif non_motor_features:
                return "Focal non-motor seizure"

        elif onset == SeizureOnset.GENERALIZED:
            if motor_features:
                if MotorFeatures.TONIC_CLONIC in motor_features:
                    return "Generalized tonic-clonic seizure"
                elif MotorFeatures.MYOCLONIC in motor_features:
                    return "Myoclonic seizure"
                elif MotorFeatures.ATONIC in motor_features:
                    return "Atonic seizure"
                elif MotorFeatures.TONIC in motor_features:
                    return "Tonic seizure"

            if "absence" in description:
                if "atypical" in description:
                    return "Atypical absence seizure"
                else:
                    return "Typical absence seizure"

        return None

    @classmethod
    def get_class_red_flags(cls, classification: SeizureClassification) -> List[str]:
        """Get red flags suggesting alternative diagnosis"""
        red_flags = []

        # Red flags for all seizure types
        if "psychogenic" in classification.semiology.lower():
            red_flags.append("Psychogenic non-epileptic seizures - consider psychiatric evaluation")

        if classification.seizure_onset == SeizureOnset.FOCAL:
            # Focal seizure red flags
            if "gradual" in classification.semiology.lower():
                red_flags.append("Gradual onset suggests syncope rather than seizure")

            if "postictal" not in classification.semiology.lower():
                red_flags.append("Lack of postictal confusion - consider alternative diagnoses")

        elif classification.seizure_onset == SeizureOnset.GENERALIZED:
            # Generalized seizure red flags
            if "triggered by" in classification.semiology.lower():
                red_flags.append("Clear triggers suggest reflex seizures or alternative diagnosis")

        return red_flags


class SeizureSemiology:
    """
    Seizure semiology analysis for localization and lateralization

    Provides consultant-level interpretation of seizure symptoms
    with localization confidence and differential diagnosis.
    """

    # Temporal lobe semiology
    TEMPORAL_LOBE_FEATURES = [
        "epigastric rising sensation", "déjà vu", "jamais vu",
        "olfactory hallucinations", "gustatory hallucinations",
        "lip smacking", "chewing", "swallowing", "manual automatisms",
        "dystonic posturing (contralateral)", "memory impairment"
    ]

    # Frontal lobe semiology
    FRONTAL_LOBE_FEATURES = [
        "focal motor", "hyperkinetic", "bicycling movements",
        "asymmetric tonic posturing", "vocalization", "brief seizures",
        "cluster seizures", "no postictal confusion"
    ]

    # Parietal lobe semiology
    PARIETAL_LOBE_FEATURES = [
        "somatosensory aura", "tingling", "numbness",
        "pain", "thermal sensations", "visual distortion in visual field"
    ]

    # Occipital lobe semiology
    OCCIPITAL_LOBE_FEATURES = [
        "visual aura", "scintillations", "hemianopia",
        "blindness", "visual hallucinations", "eye movement sensations"
    ]

    @classmethod
    def localize_seizure(cls, semiology: str) -> Dict[str, float]:
        """
        Localize seizure onset based on semiology

        Returns:
            Dictionary with brain regions and confidence scores
        """
        semiology_lower = semiology.lower()
        localization_scores = {}

        # Check temporal lobe features
        temporal_score = sum(1 for feature in cls.TEMPORAL_LOBE_FEATURES
                           if feature in semiology_lower)
        if temporal_score > 0:
            localization_scores["temporal_lobe"] = min(0.95, 0.3 + temporal_score * 0.15)

        # Check frontal lobe features
        frontal_score = sum(1 for feature in cls.FRONTAL_LOBE_FEATURES
                          if feature in semiology_lower)
        if frontal_score > 0:
            localization_scores["frontal_lobe"] = min(0.95, 0.3 + frontal_score * 0.15)

        # Check parietal lobe features
        parietal_score = sum(1 for feature in cls.PARIETAL_LOBE_FEATURES
                           if feature in semiology_lower)
        if parietal_score > 0:
            localization_scores["parietal_lobe"] = min(0.95, 0.3 + parietal_score * 0.15)

        # Check occipital lobe features
        occipital_score = sum(1 for feature in cls.OCCIPITAL_LOBE_FEATURES
                            if feature in semiology_lower)
        if occipital_score > 0:
            localization_scores["occipital_lobe"] = min(0.95, 0.3 + occipital_score * 0.15)

        return localization_scores

    @classmethod
    def lateralize_seizure(cls, semiology: str) -> Optional[str]:
        """
        Lateralize seizure based on semiology

        Returns:
            "left", "right", or None if unable to lateralize
        """
        semiology_lower = semiology.lower()

        # Right hemisphere signs (usually left symptoms)
        right_indicators = [
            "left hand", "left arm", "left leg", "left face",
            "left hemibody", "left-sided"
        ]

        # Left hemisphere signs (usually right symptoms)
        left_indicators = [
            "right hand", "right arm", "right leg", "right face",
            "right hemibody", "right-sided"
        ]

        right_score = sum(1 for indicator in right_indicators
                         if indicator in semiology_lower)
        left_score = sum(1 for indicator in left_indicators
                        if indicator in semiology_lower)

        # Also check for speech arrest (usually left hemisphere)
        if "speech arrest" in semiology_lower or "dysphasia" in semiology_lower:
            left_score += 2

        # Also check for dystonic posturing (contralateral)
        if "right arm dystonic" in semiology_lower:
            left_score += 2
        if "left arm dystonic" in semiology_lower:
            right_score += 2

        if right_score > left_score:
            return "right"  # Right hemisphere focus
        elif left_score > right_score:
            return "left"   # Left hemisphere focus

        return None


class ElectroclinicalSyndromes:
    """
    Common electroclinical epilepsy syndromes

    Based on ILAE recognized syndromes with clinical features,
    EEG findings, and treatment considerations.
    """

    # Self-limited focal epilepsies
    SELF_LIMITED_FOCAL = {
        "rolandic_epilepsy": {
            "age_group": "childhood (3-13 years)",
            "seizure_type": "focal motor",
            "semiology": "face twitching, speech arrest, hypersalivation",
            "eeg": "centrotemporal spikes",
            "prognosis": "excellent (remits by adolescence)",
            "treatment": "may not need treatment, carbamazepine if needed"
        },
        "panayiotopoulos_syndrome": {
            "age_group": "childhood (3-6 years)",
            "seizure_type": "focal autonomic",
            "semiology": "nausea, vomiting, pupillary dilation, head deviation",
            "eeg": "occipital spikes",
            "prognosis": "excellent (remits by adolescence)",
            "treatment": "may not need treatment"
        }
    }

    # Generalized epilepsies
    GENERALIZED_EPILEPSIES = {
        "childhood_absence_epilepsy": {
            "age_group": "childhood (4-10 years)",
            "seizure_type": "typical absence",
            "semiology": "brief staring, unresponsive, multiple daily",
            "eeg": "3Hz generalized spike-wave",
            "prognosis": "good (80% remit)",
            "treatment": "ethosuximide or valproate"
        },
        "juvenile_absence_epilepsy": {
            "age_group": "adolescence (10-17 years)",
            "seizure_type": "absence + GTCS",
            "semiology": "longer absences, may have GTCS",
            "eeg": "generalized spike-wave",
            "prognosis": "lifelong treatment usually needed",
            "treatment": "valproate or lamotrigine"
        },
        "juvenile_myoclonic_epilepsy": {
            "age_group": "adolescence (12-18 years)",
            "seizure_type": "myoclonic + absence + GTCS",
            "semiology": "morning myoclonic jerks, GTCS on awakening",
            "eeg": "generalized spike-wave, photosensitivity",
            "prognosis": "lifelong treatment usually needed",
            "treatment": "valproate, levetiracetam, lamotrigine"
        }
    }

    # Developmental and epileptic encephalopathies
    ENCEPHALOPATHIES = {
        "dravet_syndrome": {
            "age_group": "infancy (first year)",
            "seizure_type": "multiple prolonged types",
            "semiology": "prolonged febrile seizures, hemiclonic seizures",
            "eeg": "generalized spike-wave, multifocal",
            "genetics": "SCN1A mutation",
            "prognosis": "poor (drug resistance, developmental delay)",
            "treatment": "avoid sodium channel blockers, use stiripentol, clobazam"
        },
        "lennox_gastaut_syndrome": {
            "age_group": "childhood (1-8 years)",
            "seizure_type": "multiple types (tonic, atonic, atypical absence)",
            "semiology": "drop attacks, intellectual disability",
            "eeg": "slow spike-wave, generalized paroxysmal fast activity",
            "prognosis": "poor (drug resistance, developmental delay)",
            "treatment": "multiple ASMs, consider ketogenic diet, surgery"
        },
        "west_syndrome": {
            "age_group": "infancy (3-12 months)",
            "seizure_type": "spasms",
            "semiology": "brief flexor/extensor spasms, clusters",
            "eeg": "hypsarrhythmia",
            "prognosis": "variable (depends on etiology)",
            "treatment": "adrenocorticotropic hormone (ACTH), vigabatrin"
        }
    }

    @classmethod
    def identify_syndrome(cls, clinical_features: Dict[str, str]) -> Optional[str]:
        """
        Identify epilepsy syndrome based on clinical features

        Args:
            clinical_features: Dictionary with 'age', 'seizure_type', 'semiology', 'eeg'

        Returns:
            Syndrome name or None
        """
        age = clinical_features.get('age', '').lower()
        seizure_type = clinical_features.get('seizure_type', '').lower()
        semiology = clinical_features.get('semiology', '').lower()
        eeg = clinical_features.get('eeg', '').lower()

        # Check for encephalopathies (highest priority due to severity)
        if 'infancy' in age or 'first year' in age:
            if 'prolonged febrile' in semiology or 'hemiclonic' in semiology:
                return 'dravet_syndrome'
            if 'spasm' in semiology or 'hypsarrhythmia' in eeg:
                return 'west_syndrome'

        if 'childhood' in age:
            if 'drop attack' in semiology or 'atonic' in seizure_type:
                return 'lennox_gastaut_syndrome'
            if 'staring' in semiology and '3hz' in eeg:
                return 'childhood_absence_epilepsy'
            if 'face twitching' in semiology or 'centrotemporal' in eeg:
                return 'rolandic_epilepsy'
            if 'vomiting' in semiology or 'occipital' in eeg:
                return 'panayiotopoulos_syndrome'

        if 'adolescence' in age or 'teenager' in age:
            if 'myoclonic' in semiology and 'morning' in semiology:
                return 'juvenile_myoclonic_epilepsy'
            if 'absence' in seizure_type and 'gtcs' in seizure_type:
                return 'juvenile_absence_epilepsy'

        return None

    @classmethod
    def get_treatment_guidance(cls, syndrome: str) -> List[str]:
        """Get treatment guidance for specific syndrome"""
        guidance = []

        if syndrome in cls.ENCEPHALOPATHIES:
            syndrome_data = cls.ENCEPHALOPATHIES[syndrome]
            guidance.append(f"⚠️ {syndrome} - severe epilepsy syndrome")
            guidance.append(f"Genetics: {syndrome_data.get('genetics', 'consider genetic testing')}")
            guidance.append(f"Treatment: {syndrome_data.get('treatment')}")
            guidance.append(f"Prognosis: {syndrome_data.get('prognosis')}")
            guidance.append("Refer to pediatric epilepsy specialist")

        elif syndrome in cls.GENERALIZED_EPILEPSIES:
            syndrome_data = cls.GENERALIZED_EPILEPSIES[syndrome]
            guidance.append(f"Age-appropriate generalized epilepsy syndrome")
            guidance.append(f"Treatment: {syndrome_data.get('treatment')}")
            guidance.append("Avoid sodium channel blockers for generalized epilepsy")

        elif syndrome in cls.SELF_LIMITED_FOCAL:
            syndrome_data = cls.SELF_LIMITED_FOCAL[syndrome]
            guidance.append(f"Age-appropriate focal epilepsy syndrome")
            guidance.append(f"Prognosis: {syndrome_data.get('prognosis')}")
            guidance.append("May not need long-term treatment")

        return guidance


__all__ = [
    'SeizureOnset',
    'FocalAwareness',
    'MotorFeatures',
    'NonMotorFeatures',
    'SeizureClassification',
    'EpilepsyClassification',
    'ILAEClassification',
    'SeizureSemiology',
    'ElectroclinicalSyndromes'
]