"""
EPIDISC Differential Diagnosis Engine
=====================================

Comprehensive differential diagnosis system for distinguishing epilepsy
from common mimics with consultant-level clinical reasoning.

Based on:
- Clinical epilepsy diagnostic criteria
- Literature on epilepsy mimics (PNES, syncope, migraine)
- Evidence-based diagnostic approaches

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class DiagnosisLikelihood(Enum):
    """Likelihood categories for differential diagnosis"""
    HIGH = "high"                    # >70% probability
    MODERATE = "moderate"            # 30-70% probability
    LOW = "low"                     # <30% probability
    RULED_OUT = "ruled_out"          # <5% probability
    CONFIRMED = "confirmed"          # >95% probability


class RedFlagSeverity(Enum):
    """Severity levels for diagnostic red flags"""
    CRITICAL = "critical"            # Requires immediate evaluation
    SIGNIFICANT = "significant"      # Strongly suggests alternative diagnosis
    MODERATE = "moderate"            # Warrants consideration
    MILD = "mild"                   # Minor consideration


@dataclass
class DifferentialDiagnosis:
    """
    Complete differential diagnosis for epilepsy evaluation

    Provides Bayesian probability assessment for epilepsy vs mimics
    with clinical reasoning and investigation recommendations.
    """

    primary_diagnosis: str
    likelihood: DiagnosisLikelihood
    confidence: float  # 0-1
    differential_list: List[Tuple[str, DiagnosisLikelihood, float]]
    key_distinguishing_features: Dict[str, List[str]]
    red_flags: List[Tuple[str, RedFlagSeverity]]
    recommended_investigations: List[str]
    clinical_pearls: List[str]
    follow_up_recommendations: List[str]


class PNESDiagnosis:
    """
    Psychogenic Non-Epileptic Seizures (PNES) Diagnostic System

    Evidence-based approach to distinguishing PNES from epilepsy
    with sensitivity and specificity optimization.
    """

    # High-yield PNES indicators (based on systematic reviews)
    PNES_FAVORING_FEATURES = {
        "history": [
            ("High frequency of daily seizures", 2.5),
            ("Seizures clustered in time", 2.0),
            ("Occur in presence of others", 2.0),
            ("Rarely occur during sleep", 2.0),
            ("No postictal confusion", 1.8),
            ("Long duration (>2 minutes)", 1.5),
            ("Gradual onset", 1.5),
            ("Prolonged recovery", 1.5),
            ("Emotional triggers reported", 1.3),
            ("History of trauma/abuse", 1.2),
            ("Multiple seizure types", 1.0),
            ("Suggestions/inductions possible", 0.8),
            ("Comorbidity with other functional disorders", 0.8),
            ("History of psychiatric illness", 0.5)
        ],
        "semiology": [
            ("Asynchronous limb movements", 2.5),
            ("Side-to-side head movement", 2.0),
            ("Pelvic thrusting", 2.0),
            ("Bilateral limb movements with preserved awareness", 1.8),
            ("Weeping during event", 1.5),
            ("Vocalization during 'unconsciousness'", 1.5),
            ("Eyes closed during event", 1.3),
            ("Resistance to eye opening", 1.3),
            ("Variable semiology between events", 1.0),
            ("Forced closure of eyes", 1.0),
            ("Speech during 'unconsciousness'", 0.8)
        ]
    }

    # Epilepsy favoring features
    EPILEPSY_FAVORING_FEATURES = {
        "history": [
            ("Stereotyped events", 2.5),
            ("Clear postictal phase", 2.0),
            ("Occurs during sleep", 2.0),
            ("Tongue biting", 1.5),
            ("Urinary incontinence", 1.3),
            ("Injury during event", 1.2),
            ("Brief duration (<2 minutes)", 1.0),
            ("Morning occurrence", 0.5)
        ],
        "semiology": [
            ("Focal onset with march", 2.5),
            ("Automatisms (lip smacking, picking)", 2.0),
            ("Dystonic posturing", 1.5),
            ("Head version", 1.3),
            ("Unilateral limb movements", 1.3),
            ("Eye deviation", 1.0),
            ("Stereotyped semiology", 2.0)
        ]
    }

    # Diagnostic test utility
    TEST_UTILITY = {
        "video_eeg": {
            "sensitivity": 0.85,
            "specificity": 0.95,
            "gold_standard": True,
            "indications": [
                "Frequent events (≥1 per week)",
                "Diagnostic uncertainty",
                "Presurgical evaluation",
                "Medication adjustment needed"
            ],
            "limitations": [
                "May miss events if infrequent",
                "Expensive",
                "Requires hospitalization"
            ]
        },
        "routine_eeg": {
            "sensitivity": 0.29,
            "specificity": 0.80,
            "gold_standard": False,
            "indications": [
                "Initial evaluation",
                "Seizure characterization",
                "Syndrome identification"
            ],
            "limitations": [
                "Low sensitivity for single routine EEG",
                "Normal EEG doesn't rule out epilepsy",
                "Can be normal in PNES"
            ]
        },
        "serum_prolactin": {
            "sensitivity": 0.60,
            "specificity": 0.90,
            "gold_standard": False,
            "indications": [
                "Differentiating GTCS from PNES",
                "Postictal measurement (10-20 minutes)"
            ],
            "limitations": [
                "Only for GTCS",
                "False positives with syncope",
                "Timing critical"
            ]
        }
    }

    @classmethod
    def assess_pnes_probability(
        cls,
        clinical_features: Dict[str, str]
    ) -> Tuple[DiagnosisLikelihood, float, List[str]]:
        """
        Assess probability of PNES vs epilepsy

        Args:
            clinical_features: Dictionary with clinical information

        Returns:
            (Likelihood, probability, reasoning_points)
        """
        pnes_score = 0.0
        epilepsy_score = 0.0
        reasoning = []

        # Score PNES favoring features
        for feature, weight in cls.PNES_FAVORING_FEATURES["history"]:
            if feature.lower() in clinical_features.get("history", "").lower():
                pnes_score += weight
                reasoning.append(f"+{weight}: {feature} favors PNES")

        for feature, weight in cls.PNES_FAVORING_FEATURES["semiology"]:
            if feature.lower() in clinical_features.get("semiology", "").lower():
                pnes_score += weight
                reasoning.append(f"+{weight}: {feature} favors PNES")

        # Score epilepsy favoring features
        for feature, weight in cls.EPILEPSY_FAVORING_FEATURES["history"]:
            if feature.lower() in clinical_features.get("history", "").lower():
                epilepsy_score += weight
                reasoning.append(f"-{weight}: {feature} favors epilepsy")

        for feature, weight in cls.EPILEPSY_FAVORING_FEATURES["semiology"]:
            if feature.lower() in clinical_features.get("semiology", "").lower():
                epilepsy_score += weight
                reasoning.append(f"-{weight}: {feature} favors epilepsy")

        # Calculate probability
        total_score = pnes_score + epilepsy_score
        if total_score == 0:
            pnes_probability = 0.5  # Uncertain
        else:
            pnes_probability = pnes_score / total_score

        # Determine likelihood category
        if pnes_probability > 0.85:
            likelihood = DiagnosisLikelihood.HIGH
        elif pnes_probability > 0.70:
            likelihood = DiagnosisLikelihood.MODERATE
        elif pnes_probability > 0.30:
            likelihood = DiagnosisLikelihood.MODERATE
        elif pnes_probability > 0.15:
            likelihood = DiagnosisLikelihood.LOW
        else:
            likelihood = DiagnosisLikelihood.RULED_OUT

        return likelihood, pnes_probability, reasoning

    @classmethod
    def get_diagnostic_approach(
        cls,
        pnes_probability: float,
        event_frequency: str
    ) -> List[str]:
        """Get evidence-based diagnostic approach recommendations"""
        recommendations = []

        if event_frequency == "frequent (≥1 per week)":
            recommendations.append("🎯 Video-EEG monitoring is GOLD STANDARD")
            recommendations.append("Admit for video-EEG telemetry")
            recommendations.append("Target: Capture 2-3 typical events")
            recommendations.append("Sensitivity: 85%, Specificity: 95%")

        elif event_frequency == "occasional (1 per month)":
            recommendations.append("Consider ambulatory EEG")
            recommendations.append("Induction techniques if appropriate")
            recommendations.append("May require prolonged monitoring")

        else:  # Rare events
            recommendations.append("Consider home video recording")
            recommendations.append("Detailed semiology analysis")
            recommendations.append("Induction techniques if appropriate")

        # Add serum prolactin if GTCS suspected
        if "gtcs" in event_frequency.lower() or "generalized" in event_frequency.lower():
            recommendations.append("Serum prolactin 10-20 minutes post-event")
            recommendations.append("Elevated prolactin suggests GTCS (sensitivity 60%, specificity 90%)")

        return recommendations

    @classmethod
    def get_communication_guidance(cls) -> List[str]:
        """Get evidence-based communication approach for PNES"""
        return [
            "🗣️ COMMUNICATION APPROACH:",
            "• Use clear, compassionate language",
            "• Explain diagnosis positively ('functional' not 'fake')",
            "• Emphasize treatability and good prognosis",
            "• Avoid confrontation - events are real, not faked",
            "• Explain stress-response model",
            "• Emphasize multidisciplinary treatment approach",
            "",
            "💛 KEY MESSAGES:",
            "• 'Your seizures are real and distressing'",
            "• 'The cause is different from epilepsy'",
            "• 'The good news is that seizures are treatable'",
            "• 'We have a clear treatment pathway'",
            "",
            "🔄 FOLLOW-UP:",
            "• Refer to psychology/psychiatry",
            "• CBT is first-line treatment",
            "• Gradual ASM withdrawal if epilepsy ruled out",
            "• Prognosis: 50-70% improve with treatment"
        ]


class SyncopeDifferentiation:
    """
    Syncope vs Seizure Differentiation System

    Evidence-based approach to distinguishing syncope from seizures,
    particularly convulsive syncope which mimics epilepsy.
    """

    SYNCOPE_FAVORING_FEATURES = {
        "provoking_factors": [
            ("Prolonged standing", 2.0),
            ("Painful stimulus", 1.5),
            ("Fear/emotional distress", 1.0),
            ("Dehydration", 1.0),
            ("Crowded/hot environment", 1.0),
            ("Medical procedure", 1.0)
        ],
        "symptoms": [
            ("Lightheadedness/dizziness preceding event", 2.5),
            ("Visual grayout/tunnel vision", 2.0),
            ("Hearing changes", 1.5),
            ("Nausea/feeling hot", 1.5),
            ("Brief loss of consciousness (<1 minute)", 2.0),
            ("Rapid recovery", 2.0),
            ("No postictal confusion", 2.0),
            ("Pale appearance", 1.5),
            ("Sweating", 1.0)
        ],
        "semiology": [
            ("Atonus then brief myoclonic jerks", 2.5),
            ("Brief bilateral jerks (<10 seconds)", 2.0),
            ("No automatisms", 2.0),
            ("No tongue biting", 1.5),
            ("No urinary incontinence", 1.5),
            ("Eye closure", 1.0)
        ]
    }

    SEIZURE_FAVORING_FEATURES = {
        "symptoms": [
            ("Aura/epigastric rising", 2.5),
            ("Clear postictal confusion", 2.0),
            ("Prolonged event (>2 minutes)", 1.5),
            ("Tongue biting (lateral)", 2.0),
            ("Urinary incontinence", 1.5),
            ("Injury during event", 1.5)
        ],
        "semiology": [
            ("Stereotyped motor patterns", 2.5),
            ("Automatisms", 2.0),
            ("Focal onset with march", 2.0),
            ("Dystonic posturing", 1.5),
            ("Head deviation", 1.5)
        ]
    }

    @classmethod
    def assess_syncope_probability(
        cls,
        clinical_features: Dict[str, str]
    ) -> Tuple[DiagnosisLikelihood, float, List[str]]:
        """Assess probability of syncope vs seizure"""
        syncope_score = 0.0
        seizure_score = 0.0
        reasoning = []

        # Score syncope favoring features
        for category, features in cls.SYNCOPE_FAVORING_FEATURES.items():
            for feature, weight in features:
                if feature.lower() in clinical_features.get(category, "").lower():
                    syncope_score += weight
                    reasoning.append(f"+{weight}: {feature} favors syncope")

        # Score seizure favoring features
        for category, features in cls.SEIZURE_FAVORING_FEATURES.items():
            for feature, weight in features:
                if feature.lower() in clinical_features.get(category, "").lower():
                    seizure_score += weight
                    reasoning.append(f"-{weight}: {feature} favors seizure")

        # Calculate probability
        total_score = syncope_score + seizure_score
        if total_score == 0:
            syncope_probability = 0.5
        else:
            syncope_probability = syncope_score / total_score

        # Determine likelihood
        if syncope_probability > 0.75:
            likelihood = DiagnosisLikelihood.HIGH
        elif syncope_probability > 0.60:
            likelihood = DiagnosisLikelihood.MODERATE
        elif syncope_probability > 0.40:
            likelihood = DiagnosisLikelihood.MODERATE
        elif syncope_probability > 0.25:
            likelihood = DiagnosisLikelihood.LOW
        else:
            likelihood = DiagnosisLikelihood.RULED_OUT

        return likelihood, syncope_probability, reasoning

    @classmethod
    def get_cardiac_evaluation(cls) -> List[str]:
        """Get cardiac evaluation recommendations when syncope suspected"""
        return [
            "💓 CARDIAC EVALUATION:",
            "• ECG (critical - can identify arrhythmias)",
            "• Cardiac monitoring (Holter, event monitor, or loop recorder)",
            "• Echocardiogram if structural disease suspected",
            "• Tilt table test if vasovagal syncope suspected",
            "",
            "⚠️ RED FLAGS for cardiac syncope:",
            "• Family history of sudden cardiac death",
            "• Syncope during exercise",
            "• Abnormal ECG",
            "• Structural heart disease",
            "",
            "🚨 EMERGENCY INDICATIONS:",
            "• Syncope with chest pain",
            "• Syncope with palpitations",
            "• Family history of sudden death",
            "• Abnormal ECG",
            "• Multiple syncopal episodes"
        ]


class MigraineDifferentiation:
    """
    Migraine vs Seizure Differentiation System

    Distinguishing migraine with aura from focal seizures,
    particularly complex migraine vs temporal lobe epilepsy.
    """

    MIGRAINE_FAVORING_FEATURES = {
        "aura": [
            ("Gradual aura progression (>5 minutes)", 2.5),
            ("Visual aura (scintillations, fortification)", 2.0),
            ("Unilateral headache", 2.0),
            ("Nausea/vomiting", 1.5),
            ("Photophobia/phonophobia", 1.5),
            ("Prolonged aura (>30 minutes)", 1.5),
            ("Gradual resolution", 1.0),
            ("Positive visual phenomena", 1.0)
        ],
        "history": [
            ("Previous migraine attacks", 2.0),
            ("Family history of migraine", 1.5),
            ("Trigger factors (stress, food, hormones)", 1.0),
            ("Long duration events (>30 minutes)", 1.0)
        ]
    }

    SEIZURE_FAVORING_FEATURES = {
        "aura": [
            ("Brief aura (<60 seconds)", 2.5),
            ("Stereotyped aura", 2.0),
            ("Autonomic aura (epigastric rising)", 1.5),
            ("Olfactory/gustatory hallucinations", 1.5),
            ("Psychic aura (fear, déjà vu)", 1.0)
        ],
        "history": [
            ("Morning occurrence", 1.5),
            ("Brief duration (<2 minutes)", 1.5),
            ("Clear postictal phase", 1.5),
            ("Tongue biting", 1.0),
            ("Injury during event", 1.0)
        ]
    }

    @classmethod
    def assess_migraine_probability(
        cls,
        clinical_features: Dict[str, str]
    ) -> Tuple[DiagnosisLikelihood, float, List[str]]:
        """Assess probability of migraine vs seizure"""
        migraine_score = 0.0
        seizure_score = 0.0
        reasoning = []

        # Score features
        for category, features in cls.MIGRAINE_FAVORING_FEATURES.items():
            for feature, weight in features:
                if feature.lower() in clinical_features.get(category, "").lower():
                    migraine_score += weight
                    reasoning.append(f"+{weight}: {feature} favors migraine")

        for category, features in cls.SEIZURE_FAVORING_FEATURES.items():
            for feature, weight in features:
                if feature.lower() in clinical_features.get(category, "").lower():
                    seizure_score += weight
                    reasoning.append(f"-{weight}: {feature} favors seizure")

        # Calculate probability
        total_score = migraine_score + seizure_score
        if total_score == 0:
            migraine_probability = 0.5
        else:
            migraine_probability = migraine_score / total_score

        # Determine likelihood
        if migraine_probability > 0.75:
            likelihood = DiagnosisLikelihood.HIGH
        elif migraine_probability > 0.60:
            likelihood = DiagnosisLikelihood.MODERATE
        elif migraine_probability > 0.40:
            likelihood = DiagnosisLikelihood.MODERATE
        elif migraine_probability > 0.25:
            likelihood = DiagnosisLikelihood.LOW
        else:
            likelihood = DiagnosisLikelihood.RULED_OUT

        return likelihood, migraine_probability, reasoning

    @classmethod
    def get_treatment_considerations(cls) -> List[str]:
        """Get treatment considerations when migraine vs seizure uncertain"""
        return [
            "💊 TREATMENT CONSIDERATIONS:",
            "• Valproate effective for both migraine and epilepsy",
            "• Topiramate effective for both migraine and epilepsy",
            "• Some ASMs (levetiracetam) may worsen migraine",
            "• Triptans contraindicated if true epilepsy uncertain",
            "",
            "🔍 DIAGNOSTIC APPROACH:",
            "• Detailed semiology analysis (gradual vs sudden)",
            "• Consider prolonged EEG if uncertainty",
            "• MRI brain to exclude structural causes",
            "• Consider both conditions can coexist"
        ]


class SleepDisorderDifferentiation:
    """
    Sleep Disorder vs Seizure Differentiation System

    Distinguishing parasomnias, narcolepsy, and other sleep disorders
    from epilepsy.
    """

    SLEEP_DISORDER_FEATURES = {
        "parasomnias": [
            ("Occurs from sleep", 2.5),
            ("No memory recall", 2.0),
            ("Event occurs at specific sleep stage", 2.0),
            ("Stereotyped behaviors", 1.5),
            ("No postictal confusion", 1.5),
            ("Variable semiology", 1.0)
        ],
        "narcolepsy": [
            ("Sleep attacks", 2.5),
            ("Cataplexy (emotional trigger)", 2.5),
            ("Sleep paralysis", 1.5),
            ("Hypnagogic/hypnopompic hallucinations", 1.5),
            ("Excessive daytime sleepiness", 1.0)
        ],
        "rem_sleep_behavior_disorder": [
            ("Dream enactment", 2.5),
            ("Violent movements during sleep", 2.0),
            ("Occurs during REM sleep", 2.0),
            ("Older age onset", 1.0)
        ]
    }

    @classmethod
    def assess_sleep_disorder_probability(
        cls,
        clinical_features: Dict[str, str]
    ) -> Tuple[DiagnosisLikelihood, str, List[str]]:
        """Assess probability of sleep disorder vs seizure"""
        reasoning = []

        # Check for sleep occurrence
        if "during sleep" in clinical_features.get("timing", "").lower():
            reasoning.append("⚠️ Events during sleep - consider parasomnia")

        # Check for specific features
        if "cataplexy" in clinical_features.get("history", "").lower():
            return DiagnosisLikelihood.HIGH, "narcolepsy", [
                "Strong evidence for narcolepsy",
                "Refer for sleep study",
                "Consider MSLT (Multiple Sleep Latency Test)"
            ]

        if "dream enactment" in clinical_features.get("semiology", "").lower():
            return DiagnosisLikelihood.HIGH, "RBD", [
                "Strong evidence for REM Sleep Behavior Disorder",
                "Refer for PSG with EMG monitoring",
                "Consider neurodegenerative disease association"
            ]

        # General sleep disorder assessment
        sleep_score = 0
        for feature, weight in cls.SLEEP_DISORDER_FEATURES["parasomnias"]:
            if feature.lower() in str(clinical_features).lower():
                sleep_score += weight
                reasoning.append(f"+{weight}: {feature}")

        if sleep_score > 3:
            return DiagnosisLikelihood.MODERATE, "parasomnia", reasoning

        return DiagnosisLikelihood.LOW, "unlikely", reasoning

    @classmethod
    def get_sleep_evaluation(cls) -> List[str]:
        """Get sleep disorder evaluation recommendations"""
        return [
            "😴 SLEEP EVALUATION:",
            "• Detailed sleep history (timing, frequency, behaviors)",
            "• Overnight PSG (polysomnography)",
            "• Video-PSG if possible",
            "• Actigraphy if home monitoring needed",
            "",
            "🎯 SPECIFIC TESTS:",
            "• MSLT for narcolepsy",
            "• PSG with EMG for RBD",
            "• Home sleep study if OSA suspected",
            "",
            "💡 CLINICAL PEARLS:",
            "• Parasomnias often occur from specific sleep stages",
            "• Sleep-related seizures typically occur N2/N3",
            "• Frontal lobe seizures can mimic parasomnias",
            "• Consider both can coexist"
        ]


class DifferentialDiagnosisEngine:
    """
    Comprehensive Differential Diagnosis Engine

    Integrates all differentiation systems with Bayesian reasoning
    for consultant-level diagnostic accuracy.
    """

    @classmethod
    def evaluate_case(
        cls,
        clinical_features: Dict[str, str]
    ) -> DifferentialDiagnosis:
        """
        Comprehensive case evaluation for epilepsy vs mimics

        Args:
            clinical_features: Dictionary with complete clinical information

        Returns:
            DifferentialDiagnosis with full assessment
        """
        # Extract key information
        history = clinical_features.get("history", "")
        semiology = clinical_features.get("semiology", "")
        timing = clinical_features.get("timing", "")
        frequency = clinical_features.get("frequency", "")

        # Assess differentials
        pnes_likelihood, pnes_prob, pnes_reasoning = PNESDiagnosis.assess_pnes_probability(
            clinical_features
        )

        syncope_likelihood, syncope_prob, syncope_reasoning = SyncopeDifferentiation.assess_syncope_probability(
            clinical_features
        )

        migraine_likelihood, migraine_prob, migraine_reasoning = MigraineDifferentiation.assess_migraine_probability(
            clinical_features
        )

        sleep_likelihood, sleep_type, sleep_reasoning = SleepDisorderDifferentiation.assess_sleep_disorder_probability(
            clinical_features
        )

        # Build differential list
        differential_list = [
            ("Psychogenic NES", pnes_likelihood, pnes_prob),
            ("Syncope", syncope_likelihood, syncope_prob),
            ("Migraine", migraine_likelihood, migraine_prob),
            ("Sleep Disorder", sleep_likelihood, 0.5)  # Placeholder probability
        ]

        # Sort by probability
        differential_list.sort(key=lambda x: x[2], reverse=True)

        # Determine primary diagnosis
        if pnes_prob > 0.7:
            primary = "Psychogenic Non-Epileptic Seizures (PNES)"
            primary_likelihood = pnes_likelihood
        elif syncope_prob > 0.7:
            primary = "Syncope"
            primary_likelihood = syncope_likelihood
        elif migraine_prob > 0.7:
            primary = "Migraine"
            primary_likelihood = migraine_likelihood
        else:
            primary = "Epilepsy (vs mimics)"
            primary_likelihood = DiagnosisLikelihood.MODERATE

        # Calculate confidence
        highest_prob = max(pnes_prob, syncope_prob, migraine_prob, 0.5)
        confidence = abs(highest_prob - 0.5) * 2  # Convert to 0-1 scale

        # Build reasoning
        all_reasoning = []
        all_reasoning.extend([f"PNES: {r}" for r in pnes_reasoning])
        all_reasoning.extend([f"Syncope: {r}" for r in syncope_reasoning])
        all_reasoning.extend([f"Migraine: {r}" for r in migraine_reasoning])

        # Get recommended investigations
        investigations = cls._get_investigation_recommendations(
            pnes_prob, syncope_prob, migraine_prob, frequency
        )

        return DifferentialDiagnosis(
            primary_diagnosis=primary,
            likelihood=primary_likelihood,
            confidence=confidence,
            differential_list=differential_list,
            key_distinguishing_features={
                "epilepsy_favors": ["Stereotyped events", "Postictal confusion", "Sleep occurrence"],
                "pnes_favors": ["High frequency", "Long duration", "Emotional triggers"],
                "syncope_favors": ["Lightheadedness", "Brief duration", "Rapid recovery"],
                "migraine_favors": ["Gradual onset", "Visual symptoms", "Headache"]
            },
            red_flags=cls._get_red_flags(clinical_features),
            recommended_investigations=investigations,
            clinical_pearls=cls._get_clinical_pearls(),
            follow_up_recommendations=cls._get_follow_up_recommendations(
                pnes_prob, syncope_prob, migraine_prob
            )
        )

    @classmethod
    def _get_investigation_recommendations(
        cls,
        pnes_prob: float,
        syncope_prob: float,
        migraine_prob: float,
        frequency: str
    ) -> List[str]:
        """Get evidence-based investigation recommendations"""
        investigations = []

        # Core investigations for all cases
        investigations.extend([
            "🧪 CORE INVESTIGATIONS:",
            "• Routine EEG (all cases)",
            "• MRI brain epilepsy protocol",
            "• ECG (cardiac syncope assessment)"
        ])

        # Video-EEG if high PNES probability
        if pnes_prob > 0.5:
            investigations.extend([
                "",
                "🎺 VIDEO-EEG RECOMMENDED:",
                "• Admit for video-EEG monitoring",
                "• Capture 2-3 typical events",
                "• Gold standard for PNES diagnosis"
            ])

        # Cardiac monitoring if high syncope probability
        if syncope_prob > 0.5:
            investigations.extend([
                "",
                "💓 CARDIAC MONITORING:",
                "• Holter monitor (24-48 hours)",
                "• Event recorder (longer monitoring)",
                "• Consider loop recorder if recurrent syncope"
            ])

        # Sleep studies if sleep-related
        if "sleep" in frequency.lower():
            investigations.extend([
                "",
                "😴 SLEEP STUDIES:",
                "• Polysomnography (PSG)",
                "• Video-PSG if possible",
                "• Consider MSLT if narcolepsy suspected"
            ])

        return investigations

    @classmethod
    def _get_red_flags(cls, features: Dict[str, str]) -> List[Tuple[str, RedFlagSeverity]]:
        """Get clinical red flags"""
        red_flags = []

        # Critical red flags
        if "chest pain" in features.get("semiology", "").lower():
            red_flags.append(("Cardiac syncope - requires ECG", RedFlagSeverity.CRITICAL))

        if "family history" in features.get("family", "").lower() and "sudden death" in features.get("family", "").lower():
            red_flags.append(("Family history of sudden death - cardiac evaluation", RedFlagSeverity.CRITICAL))

        if "multiple" in features.get("frequency", "").lower() and "daily" in features.get("frequency", "").lower():
            red_flags.append(("Very frequent events - consider PNES", RedFlagSeverity.SIGNIFICANT))

        # Significant red flags
        if "injury" in features.get("complications", "").lower():
            red_flags.append(("Injury during events - favors epilepsy", RedFlagSeverity.SIGNIFICANT))

        if "no memory" in features.get("history", "").lower():
            red_flags.append(("No memory recall - favors PNES or syncope", RedFlagSeverity.SIGNIFICANT))

        return red_flags

    @classmethod
    def _get_clinical_pearls(cls) -> List[str]:
        """Get clinical pearls for differential diagnosis"""
        return [
            "💡 CLINICAL PEARLS:",
            "• PNES is 2-3x more common in epilepsy clinics than realized",
            "• Video-EEG is gold standard - aim for diagnostic yield",
            "• PNES and epilepsy can coexist (10-30% of cases)",
            "• Don't make PNES diagnosis without video-EEG confirmation",
            "• Convulsive syncope can mimic epilepsy - always consider cardiac",
            "• Migraine aura is gradual (>5 min) vs seizure aura (<60 sec)",
            "• Sleep disorders are common epilepsy mimics",
            "• Always consider dual diagnosis"
        ]

    @classmethod
    def _get_follow_up_recommendations(
        cls,
        pnes_prob: float,
        syncope_prob: float,
        migraine_prob: float
    ) -> List[str]:
        """Get evidence-based follow-up recommendations"""
        recommendations = []

        if pnes_prob > 0.7:
            recommendations.extend([
                "🔄 PNES FOLLOW-UP:",
                "• Refer to psychology/psychiatry",
                "• CBT is first-line treatment",
                "• Gradual ASM withdrawal if epilepsy ruled out",
                "• Prognosis: 50-70% improve with treatment"
            ])

        if syncope_prob > 0.7:
            recommendations.extend([
                "💓 SYNCOPE FOLLOW-UP:",
                "• Cardiology referral",
                "• Repeat ECG and cardiac monitoring",
                "• Review medications",
                "• Driving restrictions per local regulations"
            ])

        if migraine_prob > 0.7:
            recommendations.extend([
                "🧠 MIGRAINE FOLLOW-UP:",
                "• Consider preventive medications",
                "• Trigger avoidance strategies",
                "• Both conditions may require treatment"
            ])

        return recommendations


__all__ = [
    'DiagnosisLikelihood',
    'RedFlagSeverity',
    'DifferentialDiagnosis',
    'PNESDiagnosis',
    'SyncopeDifferentiation',
    'MigraineDifferentiation',
    'SleepDisorderDifferentiation',
    'DifferentialDiagnosisEngine'
]