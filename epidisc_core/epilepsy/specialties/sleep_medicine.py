"""
EPIDISC Sleep Medicine Integration Module
==========================================

Comprehensive sleep-epilepsy overlap management including parasomnia
differentiation, sleep-related epilepsy syndromes, and sleep disorder
effects on seizure control.

Based on:
- AASM sleep medicine guidelines
- ILAE sleep-epilepsy consensus statements
- Sleep-wake epilepsy research (2024-2026)

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class SleepDisorderType(Enum):
    """Types of sleep disorders relevant to epilepsy"""
    OBSTRUCTIVE_SLEEP_APNEA = "obstructive_sleep_apnea"
    NARCOLEPSY = "narcolepsy"
    REM_SLEEP_BEHAVIOR_DISORDER = "rem_sleep_behavior_disorder"
    SLEEP_PARALYSIS = "sleep_paralysis"
    INSOMNIA = "insomnia"
    RESTLESS_LEG_SYNDROME = "restless_leg_syndrome"
    PERIODIC_LIMB_MOVEMENT = "periodic_limb_movement"
    CIRCADIAN_RHYTHM_DISORDER = "circadian_rhythm_disorder"


class ParasomniaType(Enum):
    """Types of parasomnias to differentiate from seizures"""
    CONFUSIONAL_AROUSALS = "confusional_arousals"
    SLEEPWALKING = "sleepwalking"
    SLEEP_TERRORS = "sleep_terrors"
    SLEEP_TALKING = "sleep_talking"
    REM_SLEEP_BEHAVIOR_DISORDER = "rem_sleep_behavior_disorder"
    SLEEP_PARALYSIS = "sleep_paralysis"
    NOCTURNAL_EATING_DISORDER = "nocturnal_eating_disorder"


class SleepRelatedEpilepsy(Enum):
    """Sleep-related epilepsy syndromes"""
    SLEEP_TEMPERATURE_LOBE_EPILEPSY = "sleep_related_tle"
    NOCTURNAL_FRONTAL_LOBE_EPILEPSY = "nocturnal_frontal_lobe_epilepsy"
    JUVENILE_MYOCLONIC_EPILEPSY = "juvenile_myoclonic_epilepsy"
    LANDAU_KLEFFNER = "landau_kleffner"
    ESES = "electrical_status_epilepticus_sleep"


@dataclass
class SleepEpilepsyAssessment:
    """
    Complete sleep-epilepsy overlap assessment

    Includes sleep disorder identification, parasomnia differential,
    epilepsy-sleep interaction analysis, and treatment recommendations.
    """

    sleep_disorders: List[SleepDisorderType]
    parasomnia_differential: List[ParasomniaType]
    sleep_related_epilepsy: Optional[SleepRelatedEpilepsy]
    seizure_sleep_timing: str  # Sleep-related, awakening, random
    sleep_quality_impact: str
    treatment_recommendations: List[str]
    diagnostic_recommendations: List[str]
    confidence: float


class SleepMedicineIntegration:
    """
    Comprehensive sleep medicine integration for epilepsy

    Evidence-based sleep-epilepsy overlap management with
    parasomnia differentiation and sleep disorder effects.
    """

    # Parasomnia vs Seizure Differentiation
    PARASOMNIA_FEATURES = {
        ParasomniaType.CONFUSIONAL_AROUSALS: {
            "age_group": "Children (2-12 years)",
            "timing": "First third of night (N3 sleep)",
            "duration": "1-10 minutes",
            "appearance": "Confused, disoriented",
            "memory": "No memory of event",
            "motor": "Purposeless movements, may sit up",
            "response": "Minimal to stimulation",
            "post_event": "Returns to sleep easily",
            "distinguishing_features": [
                "No stereotyped movements",
                "No tonic-clonic activity",
                "Occurs from deep sleep (N3)",
                "No postictal phase"
            ]
        },
        ParasomniaType.SLEEPWALKING: {
            "age_group": "Children (4-12 years), can persist",
            "timing": "First third of night (N3 sleep)",
            "duration": "5-15 minutes (can be longer)",
            "appearance": "Blank staring, purposeful movements",
            "memory": "No memory of event",
            "motor": "Walking, complex behaviors",
            "response": "Difficult to awaken, confused if awakened",
            "post_event": "Returns to sleep easily",
            "distinguishing_features": [
                "Can navigate environment (though clumsily)",
                "May perform routine tasks",
                "No stereotyped seizure activity",
                "Safety concerns (falling, leaving house)"
            ]
        },
        ParasomniaType.SLEEP_TERRORS: {
            "age_group": "Children (3-12 years)",
            "timing": "First third of night (N3 sleep)",
            "duration": "1-10 minutes",
            "appearance": "Terrified, screaming, autonomic arousal",
            "memory": "No memory of event",
            "motor": "Sitting up, thrashing, attempts to escape",
            "response": "Difficult to console, no recognition",
            "post_event": "Returns to sleep, no memory",
            "distinguishing_features": [
                "Blood-curdling scream (characteristic)",
                "Intense autonomic symptoms (tachycardia, sweating)",
                "No stereotyped motor activity",
                "No postictal confusion"
            ]
        },
        ParasomniaType.REM_SLEEP_BEHAVIOR_DISORDER: {
            "age_group": "Older adults (60+ years)",
            "timing": "Second half of night (REM sleep)",
            "duration": "Minutes to longer",
            "appearance": "Acting out dreams",
            "memory": "May recall dream content",
            "motor": "Punching, kicking, yelling (often violent)",
            "response": "Can be awakened",
            "post_event": "Alert, oriented immediately",
            "distinguishing_features": [
                "Dream enactment behavior",
                "Violent movements matching dream content",
                "No postictal phase",
                "Often precedes Parkinson's disease (alpha-synucleinopathy)",
                "Strong association with neurodegenerative disease"
            ]
        },
        ParasomniaType.SLEEP_PARALYSIS: {
            "age_group": "Adolescents and adults",
            "timing": "Sleep onset or offset (REM transitions)",
            "duration": "Seconds to minutes",
            "appearance": "Unable to move, conscious",
            "memory": "Full awareness and memory",
            "motor": "Eye movements possible, otherwise paralyzed",
            "response": "Full consciousness, often terrifying",
            "post_event": "Immediate recovery, may fear recurrence",
            "distinguishing_features": [
                "Conscious awareness throughout",
                "No motor activity (paralysis)",
                "Often hallucinations (hypnagogic/hypnopompic)",
                "No postictal confusion",
                "Associated with narcolepsy"
            ]
        },
        ParasomniaType.NOCTURNAL_EATING_DISORDER: {
            "age_group": "Adults",
            "timing": "During sleep (partial arousal)",
            "duration": "Variable",
            "appearance": "Eating while asleep",
            "memory": "No or partial memory",
            "motor": "Preparing/consuming food",
            "response": "Minimal response during episode",
            "post_event": "May find evidence in morning",
            "distinguishing_features": [
                "Inappropriate eating behaviors",
                "May consume dangerous items",
                "Weight gain concerns",
                "Link to zolpidem use"
            ]
        }
    }

    # Sleep Disorders and Seizure Control
    SLEEP_DISORDER_EFFECTS = {
        SleepDisorderType.OBSTRUCTIVE_SLEEP_APNEA: {
            "prevalence_in_epilepsy": "15-20% (higher than general population)",
            "epilepsy_impact": [
                "Sleep fragmentation → lower seizure threshold",
                "Hypoxia → cortical irritability",
                "Poor sleep quality → increased seizure frequency",
                "ADEs may be less effective with poor sleep"
            ],
            "treatment_benefit": [
                "CPAP therapy can significantly reduce seizures",
                "Some patients achieve seizure freedom with OSA treatment",
                "Improved sleep quality → better seizure control",
                "Reduction in AED dosing possible in some cases"
            ],
            "screening_recommendations": [
                "Screen all epilepsy patients with poor seizure control",
                "High suspicion if: snoring, daytime sleepiness, obesity",
                "STOP-BANG questionnaire screening",
                "Formal sleep study if high suspicion"
            ],
            "red_flags": [
                "Loud snoring with witnessed apneas",
                "Excessive daytime sleepiness",
                "Morning headaches",
                "Poor seizure control despite appropriate AEDs",
                "Obesity (BMI >30)"
            ]
        },
        SleepDisorderType.NARCOLEPSY: {
            "epilepsy_interaction": [
                "Narcolepsy with epilepsy: complex differential",
                "Both conditions involve sleep-wake dysregulation",
                "Shared genetic susceptibility (HLA-DQB1*06:02)",
                "Cataplexy vs seizure distinction important"
            ],
            "differential_features": {
                "cataplexy_vs_seizure": [
                    "Cataplexy: Triggered by emotions (laughter, surprise)",
                    "Cataplexy: Conscious during episode",
                    "Cataplexy: No postictal phase",
                    "Cataplexy: Seconds to minutes duration",
                    "Seizure: Often stereotyped",
                    "Seizure: May have postictal confusion"
                ]
            },
            "treatment_considerations": [
                "Sodium oxybate: Reduces both narcolepsy and seizures",
                "Stimulants: May lower seizure threshold",
                "AEDs: Some may worsen daytime sleepiness",
                "Need coordinated treatment approach"
            ]
        },
        SleepDisorderType.INSOMNIA: {
            "epilepsy_impact": [
                "Sleep deprivation is potent seizure precipitant",
                "Poor sleep quality → increased seizure frequency",
                "Vicious cycle: seizures → anxiety → insomnia → seizures",
                "ADE side effects may include insomnia"
            ],
            "treatment_approach": [
                "Sleep hygiene optimization",
                "CBT-I (cognitive behavioral therapy for insomnia)",
                "Caution with hypnotics (may worsen OSA)",
                "Consider timing of AED dosing"
            ]
        }
    }

    # Sleep-Related Epilepsy Syndromes
    SLEEP_RELATED_EPILEPSIES = {
        SleepRelatedEpilepsy.NOCTURNAL_FRONTAL_LOBE_EPILEPSY: {
            "characteristics": [
                "Seizures exclusively or predominantly during sleep",
                "Brief, stereotyped hyperkinetic seizures",
                "Often mistaken for parasomnias",
                "May have sudden arousals from sleep",
                "Motor: thrashing, kicking, bicycling movements"
            ],
            "differential_diagnosis": [
                "Parasomnias (especially sleep terrors, confusional arousals)",
                "REM sleep behavior disorder",
                "Sleep walking",
                "Nocturnal panic attacks"
            ],
            "key_distinguishing_features": [
                "Stereotyped nature (vs variable parasomnias)",
                "Multiple seizures per night (vs single parasomnia)",
                "Can occur from any sleep stage (not just N3)",
                "May have interictal EEG abnormalities",
                "Video-EEG diagnostic"
            ],
            "treatment": [
                "Carbamazepine often effective",
                "Consider genetic testing (CHRNA2, CHRNB2 mutations)",
                "AEDs typically effective (unlike parasomnias)"
            ]
        },
        SleepRelatedEpilepsy.SLEEP_TEMPERATURE_LOBE_EPILEPSY: {
            "characteristics": [
                "Temporal lobe seizures during sleep",
                "May have auras (even during sleep)",
                "Automatisms common",
                "Secondary generalization possible"
            ],
            "clinical_significance": [
                "Often lesional (MRI abnormalities)",
                "Surgery may be considered if drug-resistant",
                "Sleep seizures may be only manifestation"
            ]
        },
        SleepRelatedEpilepsy.JUVENILE_MYOCLONIC_EPILEPSY: {
            "characteristics": [
                "Myoclonic jerks on awakening",
                "Strong sleep-wake relationship",
                "Sleep deprivation major trigger",
                "Generalized tonic-clonic on awakening"
            ],
            "management_considerations": [
                "Emphasize sleep hygiene",
                "Avoid sleep deprivation",
                "Morning dosing considerations",
                "Valproate, levetiracetam, lamotrigine effective"
            ]
        }
    }

    @classmethod
    def assess_sleep_epilepsy_overlap(
        cls,
        seizure_description: str,
        sleep_history: Dict,
        epilepsy_context: Dict
    ) -> SleepEpilepsyAssessment:
        """
        Assess sleep-epilepsy overlap and parasomnia differential

        Args:
            seizure_description: Description of nocturnal events
            sleep_history: Sleep history (snoring, apneas, daytime sleepiness)
            epilepsy_context: Epilepsy diagnosis and seizure timing

        Returns:
            SleepEpilepsyAssessment with complete evaluation
        """
        sleep_disorders = []
        parasomnia_differential = []
        sleep_related_epilepsy = None
        recommendations = []

        # Check for sleep disorders
        if sleep_history.get("snoring") and sleep_history.get("witnessed_apneas"):
            sleep_disorders.append(SleepDisorderType.OBSTRUCTIVE_SLEEP_APNEA)
            recommendations.extend([
                "Screen for obstructive sleep apnea",
                "Consider formal sleep study (polysomnography)",
                "CPAP therapy may improve seizure control"
            ])

        if sleep_history.get("daytime_sleepiness") and sleep_history.get("sleep_attacks"):
            sleep_disorders.append(SleepDisorderType.NARCOLEPSY)
            recommendations.extend([
                "Consider narcolepsy evaluation",
                "Multiple sleep latency testing indicated",
                "Distinguish cataplexy from seizures"
            ])

        # Parasomnia differential
        description_lower = seizure_description.lower()

        if any(term in description_lower for term in ["sleep walking", "somnambulism", "walking during sleep"]):
            parasomnia_differential.append(ParasomniaType.SLEEPWALKING)

        if any(term in description_lower for term in ["scream", "terror", "blood-curdling", "crying out"]):
            parasomnia_differential.append(ParasomniaType.SLEEP_TERRORS)

        if any(term in description_lower for term in ["acting out dream", "punching", "kicking", "dream enactment"]):
            parasomnia_differential.append(ParasomniaType.REM_SLEEP_BEHAVIOR_DISORDER)

        if "paralyzed" in description_lower or "can't move" in description_lower:
            parasomnia_differential.append(ParasomniaType.SLEEP_PARALYSIS)

        # Determine if likely epilepsy vs parasomnia
        epilepsy_features = [
            "stereotyped", "rhythmic", "tonic-clonic", "postictal",
            "confusion after", "automatism", "aura"
        ]
        parasomnia_features = [
            "scream", "terrified", "walking", "thrashing", "no memory",
            "confused arousal", "sitting up", "blank stare"
        ]

        epilepsy_score = sum(1 for feature in epilepsy_features if feature in description_lower)
        parasomnia_score = sum(1 for feature in parasomnia_features if feature in description_lower)

        # Sleep-related epilepsy assessment
        if epilepsy_context.get("seizure_timing") == "during sleep":
            if "frontal" in epilepsy_context.get("epilepsy_type", "").lower():
                sleep_related_epilepsy = SleepRelatedEpilepsy.NOCTURNAL_FRONTAL_LOBE_EPILEPSY
                recommendations.extend([
                    "Consider nocturnal frontal lobe epilepsy",
                    "Video-EEG monitoring during sleep",
                    "MRI brain (epilepsy protocol)",
                    "Trial of carbamazepine"
                ])
            elif "temporal" in epilepsy_context.get("epilepsy_type", "").lower():
                sleep_related_epilepsy = SleepRelatedEpilepsy.SLEEP_TEMPERATURE_LOBE_EPILEPSY

        # General recommendations
        recommendations.extend([
            "Comprehensive sleep history essential",
            "Consider video-EEG monitoring for diagnosis",
            "Sleep hygiene optimization recommended",
            "Screen for OSA in refractory cases"
        ])

        return SleepEpilepsyAssessment(
            sleep_disorders=sleep_disorders,
            parasomnia_differential=parasomnia_differential,
            sleep_related_epilepsy=sleep_related_epilepsy,
            seizure_sleep_timing=epilepsy_context.get("seizure_timing", "unknown"),
            sleep_quality_impact=cls._assess_sleep_impact(sleep_disorders),
            treatment_recommendations=recommendations,
            diagnostic_recommendations=cls._get_sleep_diagnostic_recommendations(
                sleep_disorders, parasomnia_differential
            ),
            confidence=0.85 if (parasomnia_differential or sleep_disorders) else 0.75
        )

    @classmethod
    def _assess_sleep_impact(cls, sleep_disorders: List[SleepDisorderType]) -> str:
        """Assess impact of sleep disorders on epilepsy"""
        if not sleep_disorders:
            return "No specific sleep disorder identified, sleep hygiene optimization recommended"

        impacts = []
        for disorder in sleep_disorders:
            if disorder == SleepDisorderType.OBSTRUCTIVE_SLEEP_APNEA:
                impacts.append("⚠️ OSA: Significantly worsens seizure control, CPAP therapy may improve seizures")
            elif disorder == SleepDisorderType.NARCOLEPSY:
                impacts.append("⚠️ Narcolepsy: Complex management required, coordinate treatment")
            elif disorder == SleepDisorderType.INSOMNIA:
                impacts.append("⚠️ Insomnia: Sleep deprivation worsens seizures, sleep hygiene essential")

        return "\n".join(impacts)

    @classmethod
    def _get_sleep_diagnostic_recommendations(
        cls,
        sleep_disorders: List[SleepDisorderType],
        parasomnia_differential: List[ParasomniaType]
    ) -> List[str]:
        """Get diagnostic recommendations based on assessment"""
        recommendations = []

        if SleepDisorderType.OBSTRUCTIVE_SLEEP_APNEA in sleep_disorders:
            recommendations.extend([
                "**Polysomnography (Sleep Study)**",
                "- Overnight sleep study with EEG monitoring",
                "- AHI assessment for OSA severity",
                "- CPAP titration if OSA confirmed"
            ])

        if parasomnia_differential:
            recommendations.extend([
                "**Video-EEG Polysomnography**",
                "- Capture typical event with video and EEG",
                "- Gold standard for distinguishing parasomnia vs seizure",
                "- May require multiple nights if events infrequent"
            ])

        if sleep_disorders or parasomnia_differential:
            recommendations.extend([
                "**Sleep Diary**",
                "- Document timing and characteristics of events",
                "- Record sleep patterns and quality",
                "- Track seizure/parasomnia frequency"
            ])

        return recommendations

    @classmethod
    def get_parasomnia_differential_table(cls) -> List[str]:
        """Get formatted parasomnia vs seizure differential table"""
        return [
            "## PARASOMNIA VS SEIZURE DIFFERENTIAL DIAGNOSIS",
            "",
            "**Key Distinguishing Features**:",
            "",
            "| Feature | Parasomnia | Seizure |",
            "|---------|-----------|---------|",
            "| Timing | First 1/3 night (N3) or REM | Any stage, any time |",
            "| Duration | Variable (often >2 min) | Usually <2 min |",
            "| Stereotypy | Variable each episode | Stereotyped, consistent |",
            "| Memory | Amnesia for event | May have aura/memory |",
            "| Postictal | None, returns to sleep | Postictal confusion common |",
            "| Frequency | Usually single episode/night | Can be multiple |",
            "| Response | Minimal during event | May respond to stimulation |",
            "| EEG | Normal during event | May show epileptiform activity |",
            "",
            "**Video-EEG is Gold Standard for Diagnosis**",
            "",
            "**Specific Parasomnias**:",
            "",
            "**Sleep Terrors**:",
            "- Blood-curdling scream (characteristic)",
            "- Occurs from deep sleep (N3)",
            "- Terrified appearance, autonomic arousal",
            "- No memory, returns to sleep",
            "",
            "**Sleepwalking**:",
            "- Purposeful walking during sleep",
            "- Blank stare, clumsy movements",
            "- Safety concerns (falling, leaving house)",
            "- No memory, no postictal phase",
            "",
            "**REM Sleep Behavior Disorder**:",
            "- Dream enactment behavior",
            "- Violent movements matching dream content",
            "- Second half of night (REM)",
            "- Strong association with neurodegenerative disease",
            "",
            "**Sleep Paralysis**:",
            "- Conscious but unable to move",
            "- Occurs at sleep onset/offset",
            "- May have hallucinations",
            "- No motor activity",
            "",
            "**⚕️ Clinical Significance**:",
            "- Parasomnias: Benign, safety measures, reassure",
            "- Seizures: AED treatment, EEG monitoring",
            "- Some NFLE patients misdiagnosed as parasomnia"
        ]

    @classmethod
    def get_sleep_hygiene_recommendations(cls) -> List[str]:
        """Get sleep hygiene recommendations for epilepsy patients"""
        return [
            "## SLEEP HYGIENE FOR EPILEPSY PATIENTS",
            "",
            "**Why Sleep Hygiene Matters in Epilepsy**:",
            "- Sleep deprivation is potent seizure precipitant",
            "- Poor sleep quality worsens seizure control",
            "- Some epilepsy syndromes strongly sleep-related (JME, NFLE)",
            "- Sleep optimization improves seizure control",
            "",
            "**Essential Sleep Hygiene Measures**:",
            "",
            "**1. Regular Sleep Schedule**:",
            "- Consistent bedtime and wake time (even weekends)",
            "- Aim for 7-9 hours sleep per night",
            "- Avoid catching up on sleep on weekends (disrupts rhythm)",
            "",
            "**2. Sleep Environment**:",
            "- Dark, quiet, cool bedroom",
            "- Comfortable mattress and pillows",
            "- Remove electronics from bedroom",
            "- Use bed only for sleep (not work/TV)",
            "",
            "**3. Pre-Sleep Routine**:",
            "- Wind down 1 hour before bed",
            "- Avoid screens (blue light suppresses melatonin)",
            "- Relaxation techniques (reading, warm bath)",
            "- Avoid stimulating activities",
            "",
            "**4. Daytime Habits**:",
            "- Regular exercise (not within 3 hours of bed)",
            "- Morning sunlight exposure (regulates circadian rhythm)",
            "- Limit caffeine after 2 PM",
            "- Avoid naps (or limit to 20 min, early afternoon)",
            "",
            "**5. Sleep-Deprived EEG Preparation**:",
            "- Only when medically indicated",
            "- Should be supervised",
            "- Consider driving restrictions",
            "- Discuss seizure risk with neurologist",
            "",
            "**Specific Epilepsy Considerations**:",
            "",
            "**Juvenile Myoclonic Epilepsy (JME)**:",
            "- EXTREMELY SENSITIVE to sleep deprivation",
            "- Missing sleep is common seizure trigger",
            "- Strict sleep hygiene essential",
            "- ADE compliance plus sleep optimization",
            "",
            "**Nocturnal Seizures**:",
            "- Optimize sleep to reduce nocturnal events",
            "- Consider timing of AED dosing",
            "- Safety measures (padding bed, seizure alarms)",
            "",
            "**⚕️ Clinical Recommendations**:",
            "- Sleep hygiene as adjunct to AED treatment",
            "- Discuss sleep problems at epilepsy reviews",
            "- Screen for OSA in refractory epilepsy",
            "- Refer to sleep specialist if indicated"
        ]


__all__ = [
    'SleepDisorderType',
    'ParasomniaType',
    'SleepRelatedEpilepsy',
    'SleepEpilepsyAssessment',
    'SleepMedicineIntegration'
]
