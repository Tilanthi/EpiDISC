"""
EPIDISC Psychiatry Integration Module
======================================

Comprehensive psychiatry-epilepsy overlap management including
PNES diagnosis, psychiatric comorbidities, and psychotropic
medication interactions with antiepileptic drugs.

Based on:
- ILAE PNES task force recommendations (2024)
- NICE guidelines on PNES (2022)
- Epilepsy-psychiatry comorbidity research (2024-2026)

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class PsychiatricComorbidity(Enum):
    """Psychiatric comorbidities in epilepsy"""
    DEPRESSION = "depression"
    ANXIETY = "anxiety"
    PSYCHOSIS = "psychosis"
    BIPOLAR_DISORDER = "bipolar_disorder"
    ADHD = "adhd"
    AUTISM_SPECTRUM = "autism_spectrum"
    PTSD = "ptsd"
    PERSONALITY_DISORDER = "personality_disorder"
    SUBSTANCE_USE_DISORDER = "substance_use_disorder"


class PNESType(Enum):
    """Types of Psychogenic Non-Epileptic Seizures"""
    HYPERMOTOR_PNES = "hypermotor_pnes"
    CATATONIC_PNES = "catatonic_pnes"
    SUBTLE_PNES = "subtle_pnes"
    MIXED_PNES = "mixed_pnes"


class PsychiatricMedicationInteraction(Enum):
    """Types of interactions between psychotropics and AEDs"""
    PHARMACOKINETIC = "pharmacokinetic"      # Metabolism interactions
    PHARMACODYNAMIC = "pharmacodynamic"      # Additive effects
    CONGENITAL = "contraindicated"           # Should not be combined
    CAUTION = "caution_required"             # Use with monitoring


@dataclass
class PNESAssessment:
    """
    Complete PNES assessment

    Includes diagnostic likelihood, differentiating features,
    comorbidities, and treatment recommendations.
    """

    pnes_likelihood: str  # High, moderate, low
    key_features_suggesting_pnes: List[str]
    epilepsy_features_present: List[str]
    psychiatric_comorbidities: List[PsychiatricComorbidity]
    trauma_history: List[str]
    treatment_recommendations: List[str]
    diagnostic_recommendations: List[str]
    prognosis: str
    confidence: float


@dataclass
class PsychotropicInteractionAssessment:
    """
    Assessment of psychotropic-AED interactions

    Includes interaction type, severity, and management recommendations.
    """

    psychotropic_medication: str
    aed_medication: str
    interaction_type: PsychiatricMedicationInteraction
    severity: str  # Severe, moderate, mild
    clinical_significance: str
    management_recommendations: List[str]
    monitoring_requirements: List[str]
    alternative_options: List[str]


class PsychiatryIntegration:
    """
    Comprehensive psychiatry-epilepsy overlap management

    Evidence-based PNES diagnosis and psychiatric comorbidity
    management with medication interaction assessment.
    """

    # PNES Diagnostic Features
    PNES_DIAGNOSTIC_FEATURES = {
        "strong_pnes_indicators": {
            "clinical_features": [
                "**Duration**: Often >2 minutes (epilepsy typically <2 min)",
                "**Variability**: Different semiology between episodes",
                "**Asynchronous movements**: Non-rhythmic, out-of-phase limb movements",
                "**Pelvic thrusting**: Characteristic of PNES",
                "**Side-to-side head movements**: Rotational head movements",
                "**Talking during events**: Words or sentences during motor activity",
                "**Weeping**: Crying during event",
                "**Gradual onset**: Progressive build-up vs sudden seizure onset",
                "**Gradual offset**: Gradual return to baseline vs postictal phase",
                "**Recall preservation**: Partial or full memory of event",
                "**Eye closure**: Eyes closed during event (vs open in epilepsy)",
                "**Co-occurring**: Events can occur during interictal EEG discharges",
                "**Suggestibility**: Events triggered by suggestion/induction"
            ],
            "historical_features": [
                "**High frequency**: Daily or multiple daily events",
                "**Psychiatric history**: High comorbidity (depression, anxiety, PTSD)",
                "**Trauma history**: Physical, sexual, emotional trauma common",
                "**Multiple conversion symptoms**: Other functional symptoms",
                "**AED resistance**: Poor response to appropriate AEDs",
                "**Normal EEG**: Repeated normal EEGs despite frequent events",
                "**Normal MRI**: No epileptogenic lesion identified",
                "**Female predominance**: 70-80% female (in adult series)",
                "**Age of onset**: Can occur at any age, peaks 20s-30s"
            ]
        },
        "epilepsy_features_suggesting_seizures": {
            "clinical_features": [
                "**Stereotyped**: Same pattern each time",
                "**Rhythmic**: Regular, rhythmic motor activity",
                "**Tonic-clonic**: Bilateral tonic-clonic activity",
                "**Automatisms**: Purposeless, stereotyped automatisms",
                "**Postictal confusion**: Post-event confusion and fatigue",
                "**Injury**: Tongue biting, falls, injuries",
                "**Incontinence**: Urinary (or fecal) incontinence",
                "**Sudden onset**: Abrupt beginning without build-up",
                "**Sudden offset**: Abrupt ending, rapid postictal"
            ],
            "historical_features": [
                "**Aura**: Pre-seizure warning symptoms",
                "**Sleep-related**: Events from sleep (highly specific for epilepsy)",
                "**AED response**: Good response to appropriate AEDs",
                "**EEG abnormalities**: Epileptiform discharges on EEG",
                "**MRI lesion**: Structural lesion on imaging",
                "**Family history**: Family history of epilepsy"
            ]
        },
        "diagnostic_challenges": {
            "overlap_features": [
                "**Both can have**: Automatisms, vocalizations",
                "**Both can have**: Stereotyped features (some PNES)",
                "**Both can have**: Post-event confusion (some PNES)",
                "**Both can coexist**: 10-40% have epilepsy + PNES"
            ],
            "red_flags_for_pnes": [
                "**Normal EEG despite frequent events**",
                "**Poor AED response despite appropriate trials**",
                "**Multiple psychiatric comorbidities**",
                "**History of trauma or abuse**",
                "**Multiple conversion symptoms**",
                "**Events suggestible by stress/emotion**"
            ],
            "red_flags_for_epilepsy": [
                "**Events from sleep** (very specific for epilepsy)",
                "**Tongue biting (lateral edge)**",
                "**Significant injury from events**",
                "**Urinary incontinence**",
                "**Clear postictal phase**",
                "**EEG epileptiform abnormalities**"
            ]
        }
    }

    # Psychiatric Comorbidities in Epilepsy
    PSYCHIATRIC_COMORBIDITIES = {
        PsychiatricComorbidity.DEPRESSION: {
            "prevalence": "20-30% (3-4x general population)",
            "risk_factors": [
                "Temporal lobe epilepsy",
                "Frequent seizures",
                "Drug-resistant epilepsy",
                "Left-sided seizure focus",
                "Vagus nerve stimulation (may cause/worsen depression)"
            ],
            "clinical_implications": [
                "Worsens seizure control",
                "Increases suicide risk",
                "Reduces quality of life",
                "Worsens AED side effects",
                "Increases healthcare utilization"
            ],
            "treatment_considerations": [
                "SSRIs generally safe (seizure risk low)",
                "Avoid bupropion (lowers seizure threshold)",
                "Psychotherapy (CBT) effective",
                "Combined epilepsy-psychiatry management essential"
            ],
            "screening": [
                "PHQ-9 at epilepsy clinic visits",
                "Direct questioning about mood",
                "Suicide risk assessment in high-risk patients"
            ]
        },
        PsychiatricComorbidity.ANxiety: {
            "prevalence": "15-25%",
            "subtypes": [
                "Generalized anxiety disorder",
                "Panic disorder",
                "Social anxiety disorder",
                "Seizure phobia (fear of having seizures)"
            ],
            "clinical_implications": [
                "Anxiety can trigger seizures",
                "Seizure anticipation anxiety",
                "Avoidance behaviors",
                "Reduced independence",
                "Worsened quality of life"
            ],
            "treatment_considerations": [
                "SSRIs generally safe",
                "Benzodiazepines caution (dependence, withdrawal)",
                "CBT highly effective",
                "Relaxation techniques helpful"
            ]
        },
        PsychiatricComorbidity.PSYCHOSIS: {
            "prevalence": "2-7%",
            "types": [
                "Interictal psychosis",
                "Postictal psychosis",
                "AED-induced psychosis",
                "Schizophrenia-like illness"
            ],
            "postictal_psychosis": {
                "timing": "Hours to days after cluster of seizures",
                "duration": "Days to weeks",
                "features": "Delusions, hallucinations, disorganized thinking",
                "treatment": "Antipsychotics, prevent clusters"
            },
            "aed_induced_psychosis": {
                "causative_aeds": [
                    "Levetiracetam (most common)",
                    "Zonisamide",
                    "Topiramate",
                    "Perampanel"
                ],
                "management": "Reduce or discontinue offending AED"
            }
        },
        PsychiatricComorbidity.BIPOLAR_DISORDER: {
            "prevalence": "2-7%",
            "clinical_implications": [
                "Mood instability can worsen seizure control",
                "Sleep disruption from mania triggers seizures",
                "AEDs can cause mood symptoms (valproate exception)",
                "High suicide risk"
            ],
            "treatment_considerations": [
                "Valproate treats both epilepsy and bipolar",
                "Lamotrigine treats both (watch for SJS titration)",
                "Avoid antidepressants that may induce mania",
                "Mood stabilizers may help seizure control"
            ]
        },
        PsychiatricComorbidity.ADHD: {
            "prevalence": "10-30% in pediatric epilepsy",
            "clinical_implications": [
                "Poor medication adherence",
                "Academic difficulties",
                "Behavioral problems",
                "Increased seizure risk (possibly from poor adherence)"
            ],
            "treatment_considerations": [
                "Stimulants may lower seizure threshold",
                "Atomoxetine generally safe",
                "Non-pharmacological approaches first line",
                "Combined treatment often necessary"
            ]
        }
    }

    # Psychotropic-AED Interactions
    PSYCHOTROPIC_INTERACTIONS = {
        "antidepressants": {
            "ssris": {
                "general": "Generally safe, minimal seizure risk",
                "fluoxetine": {
                    "interaction": "Inhibits CYP2D6/3A4",
                    "aeds_affected": "Carbamazepine, phenytoin metabolism",
                    "recommendation": "Monitor levels, dose adjust if needed"
                },
                "paroxetine": {
                    "interaction": "Inhibits CYP2D6",
                    "aeds_affected": "Minimal AED interactions",
                    "recommendation": "Generally safe"
                },
                "sertraline": {
                    "interaction": "Mild CYP inhibition",
                    "aeds_affected": "Minimal interactions",
                    "recommendation": "Good choice in epilepsy"
                },
                "citalopram_escitalopram": {
                    "interaction": "Minimal CYP interactions",
                    "aeds_affected": "Generally safe",
                    "recommendation": "Preferred SSRI in epilepsy"
                }
            },
            "avoid_in_epilepsy": {
                "clomipramine": "Lowers seizure threshold",
                "bupropion": "Significantly lowers seizure threshold",
                "amoxapine": "Lowers seizure threshold",
                "maprotiline": "Lowers seizure threshold"
            },
            "use_with_caution": {
                "tcas": "All TCAs lower seizure threshold (dose-dependent)",
                "venlafaxine": "May lower seizure threshold at high doses",
                "mirtazapine": "Generally safe but monitor"
            }
        },
        "antipsychotics": {
            "generally_safe": [
                "Risperidone",
                "Olanzapine",
                "Quetiapine",
                "Aripiprazole"
            ],
            "caution_required": {
                "clozapine": "Lowers seizure threshold (dose-dependent)",
                "quetiapine_high_dose": "Seizure risk at high doses",
                "olanzapine_high_dose": "Seizure risk at high doses"
            },
            "aed_interactions": {
                "carbamazepine": "Induces antipsychotic metabolism (lower levels)",
                "phenytoin": "Induces antipsychotic metabolism",
                "valproate": "May increase some antipsychotic levels",
                "recommendation": "Monitor clinical response, adjust doses"
            }
        },
        "anxiolytics": {
            "benzodiazepines": {
                "benefits": [
                    "Reduce seizure threshold (anticonvulsant)",
                    "Treat anxiety",
                    "Acute seizure treatment"
                ],
                "risks": [
                    "Dependence risk",
                    "Withdrawal seizures",
                    "Tolerance development",
                    "Cognitive side effects"
                ],
                "recommendation": "Short-term use only, avoid abrupt withdrawal"
            },
            "buspirone": {
                "safety": "No known seizure risk",
                "interaction": "Minimal AED interactions",
                "recommendation": "Good long-term anxiolytic option"
            }
        },
        "mood_stabilizers": {
            "valproate": {
                "efficacy": "Effective for epilepsy and bipolar",
                "benefits": "Treats both conditions, single medication",
                "risks": "Teratogenic, weight gain, tremor"
            },
            "lamotrigine": {
                "efficacy": "Effective for epilepsy and bipolar depression",
                "benefits": "Treats both conditions",
                "risks": "SJS risk (slow titration essential)",
                "note": "May precipitate mania in bipolar patients"
            },
            "lithium": {
                "interaction": "Minimal AED interactions",
                "safety": "No seizure risk",
                "monitoring": "Levels, renal, thyroid",
                "recommendation": "Generally safe in epilepsy"
            }
        }
    }

    @classmethod
    def assess_pnes(
        cls,
        event_description: str,
        psychiatric_history: Dict,
        seizure_history: Dict,
        eeg_results: str = "",
        mri_results: str = ""
    ) -> PNESAssessment:
        """
        Comprehensive PNES assessment

        Args:
            event_description: Description of typical events
            psychiatric_history: Psychiatric diagnosis, trauma, comorbidities
            seizure_history: Known epilepsy, AED trials, event frequency
            eeg_results: EEG findings
            mri_results: MRI findings

        Returns:
            PNESAssessment with complete evaluation
        """
        description_lower = event_description.lower()

        # Identify PNES features
        pnes_features = []
        epilepsy_features = []

        # Check for strong PNES indicators
        if any(term in description_lower for term in [
            "pelvic thrust", "thrusting", "side to side", "rotational",
            "talking during", "weeping", "crying during", "gradual onset",
            "gradual offset", "eyes closed"
        ]):
            pnes_features.extend([
                "Strong PNES features present (pelvic thrusting, side-to-side movements, talking during event, etc.)"
            ])

        # Check for epilepsy features
        if any(term in description_lower for term in [
            "stereotyped", "rhythmic", "tonic-clonic", "postictal",
            "tongue biting", "incontinence", "from sleep"
        ]):
            epilepsy_features.append("Strong epilepsy features present")

        # Duration assessment
        if ">2 minute" in description_lower or "long duration" in description_lower:
            pnes_features.append("Long duration favors PNES")

        # Variability assessment
        if "variable" in description_lower or "different each" in description_lower:
            pnes_features.append("Variable semiology favors PNES")

        # Postictal assessment
        if "postictal" in description_lower:
            epilepsy_features.append("Postictal phase suggests epilepsy")

        # Historical features
        historical_pnes_indicators = []
        if psychiatric_history.get("trauma_history"):
            historical_pnes_indicators.append("Trauma history")

        if psychiatric_history.get("multiple_psychiatric_comorbidities"):
            historical_pnes_indicators.append("Multiple psychiatric comorbidities")

        if not seizure_history.get("aed_response") and seizure_history.get("aed_trials", 0) >= 2:
            historical_pnes_indicators.append("Poor AED response despite adequate trials")

        if seizure_history.get("normal_eeg_count", 0) >= 2:
            historical_pnes_indicators.append(f"{seizure_history['normal_eeg_count']} normal EEGs")

        # Sleep events strongly suggest epilepsy
        if "from sleep" in description_lower or "during sleep" in description_lower:
            epilepsy_features.append("Events from sleep strongly suggest epilepsy")

        # Determine PNES likelihood
        pnes_score = len(pnes_features) + len(historical_pnes_indicators)
        epilepsy_score = len(epilepsy_features)

        if pnes_score >= 3 and epilepsy_score == 0:
            likelihood = "High likelihood of PNES"
        elif pnes_score >= 2 and epilepsy_score <= 1:
            likelihood = "Moderate likelihood of PNES"
        elif epilepsy_score >= 2:
            likelihood = "Low likelihood of PNES (epilepsy more likely)"
        else:
            likelihood = "Indeterminate - requires video-EEG"

        # Identify psychiatric comorbidities
        comorbidities = []
        for comorbidity in PsychiatricComorbidity:
            if psychiatric_history.get(comorbidity.value):
                comorbidities.append(comorbidity)

        # Treatment recommendations
        treatment_recommendations = []

        if "High" in likelihood or "Moderate" in likelihood:
            treatment_recommendations.extend([
                "**Video-EEG monitoring is diagnostic gold standard**",
                "**Psychiatric evaluation recommended**",
                "**Consider psychological interventions (CBT, EMDR)**",
                "**Communicate diagnosis clearly and compassionately**",
                "**Avoid labeling as \"fake\" or \"not real\"",
                "**Multidisciplinary management (neurology + psychiatry)**"
            ])

        if comorbidities:
            treatment_recommendations.extend([
                "**Treat identified psychiatric comorbidities**",
                "**Consider trauma-focused therapy if trauma history**"
            ])

        # Diagnostic recommendations
        diagnostic_recommendations = [
            "**Video-EEG telemetry** (gold standard)",
            "**Psychiatric assessment**",
            "**Detailed event description (eyewitness account crucial)**"
        ]

        # Prognosis
        if "High" in likelihood:
            prognosis = "With appropriate diagnosis and psychological treatment, many patients experience significant reduction in PNES frequency. Early diagnosis associated with better outcomes."
        else:
            prognosis = "Prognosis depends on definitive diagnosis. Video-EEG essential for accurate diagnosis and appropriate treatment planning."

        return PNESAssessment(
            pnes_likelihood=likelihood,
            key_features_suggesting_pnes=pnes_features,
            epilepsy_features_present=epilepsy_features,
            psychiatric_comorbidities=comorbidities,
            trauma_history=psychiatric_history.get("trauma_types", []),
            treatment_recommendations=treatment_recommendations,
            diagnostic_recommendations=diagnostic_recommendations,
            prognosis=prognosis,
            confidence=0.85
        )

    @classmethod
    def assess_psychotropic_interactions(
        cls,
        psychotropic_medication: str,
        aed_medication: str
    ) -> PsychotropicInteractionAssessment:
        """Assess interactions between psychotropics and AEDs"""
        psych_lower = psychotropic_medication.lower()
        aed_lower = aed_medication.lower()

        # Default assessment
        interaction_type = PsychiatricMedicationInteraction.CAUTION
        severity = "Mild"
        clinical_significance = "Minimal clinical significance"
        management = []
        monitoring = []
        alternatives = []

        # Antidepressant interactions
        if "bupropion" in psych_lower:
            interaction_type = PsychiatricMedicationInteraction.CONGENITAL
            severity = "Severe"
            clinical_significance = "Bupropion significantly lowers seizure threshold"
            management = ["Avoid bupropion in epilepsy patients", "Consider alternative antidepressants"]
            alternatives = ["SSRIs (sertraline, citalopram)", "SNRIs (duloxetine)", "Mirtazapine"]

        elif any(tca in psych_lower for tca in ["amitriptyline", "nortriptyline", "imipramine"]):
            interaction_type = PsychiatricMedicationInteraction.CAUTION
            severity = "Moderate"
            clinical_significance = "TCAs lower seizure threshold (dose-dependent)"
            management = ["Use lowest effective dose", "Monitor seizure frequency", "Consider alternative antidepressant"]
            alternatives = ["SSRIs", "SNRIs", "Mirtazapine"]

        elif any(ssri in psych_lower for ssri in ["sertraline", "citalopram", "escitalopram"]):
            interaction_type = PsychiatricMedicationInteraction.CAUTION
            severity = "Mild"
            clinical_significance = "SSRIs generally safe in epilepsy"
            management = ["Standard dosing", "Monitor mood and seizure frequency"]
            alternatives = ["Other SSRIs generally acceptable"]

        # Antipsychotic interactions
        elif "clozapine" in psych_lower:
            interaction_type = PsychiatricMedicationInteraction.CAUTION
            severity = "Moderate"
            clinical_significance = "Clozapine lowers seizure threshold (dose-dependent)"
            management = ["Use lowest effective dose", "Monitor seizure frequency", "Consider alternative antipsychotic"]
            alternatives = ["Risperidone", "Olanzapine", "Quetiapine", "Aripiprazole"]

        elif any(antipsych in psych_lower for antipsych in ["risperidone", "olanzapine", "quetiapine", "aripiprazole"]):
            interaction_type = PsychiatricMedicationInteraction.CAUTION
            severity = "Mild"
            clinical_significance = "Second-generation antipsychotics generally safe"

        # Carbamazepine interactions with psychotropics
        if "carbamazepine" in aed_lower:
            if "olanzapine" in psych_lower or "quetiapine" in psych_lower:
                clinical_significance = "Carbamazepine induces metabolism, reduces antipsychotic levels"
                management.extend([
                    "Monitor antipsychotic levels if available",
                    "May need higher antipsychotic doses",
                    "Monitor for reduced efficacy"
                ])

        return PsychotropicInteractionAssessment(
            psychotropic_medication=psychotropic_medication,
            aed_medication=aed_medication,
            interaction_type=interaction_type,
            severity=severity,
            clinical_significance=clinical_significance,
            management_recommendations=management,
            monitoring_requirements=monitoring,
            alternative_options=alternatives
        )

    @classmethod
    def get_psychiatric_screening_recommendations(cls) -> List[str]:
        """Get psychiatric screening recommendations for epilepsy patients"""
        return [
            "## PSYCHIATRIC SCREENING IN EPILEPSY",
            "",
            "**Why Screen?**",
            "- Psychiatric comorbidities 3-4x more common in epilepsy",
            "- Worsen seizure control",
            "- Reduce quality of life",
            "- Increase suicide risk",
            "- Effective treatments available",
            "",
            "**What to Screen For**:",
            "",
            "**Depression**:",
            "- Prevalence: 20-30%",
            "- Screen: PHQ-9 at clinic visits",
            "- Ask: \"Over the past 2 weeks, have you felt down, depressed, hopeless?\"",
            "- Suicide risk assessment in depressed patients",
            "",
            "**Anxiety**:",
            "- Prevalence: 15-25%",
            "- Screen: GAD-7",
            "- Ask about worry, panic, seizure phobia",
            "",
            "**PNES (Psychogenic Non-Epileptic Seizures)**:",
            "- Consider in: Drug-resistant epilepsy, normal EEGs, trauma history",
            "- Gold standard: Video-EEG monitoring",
            "- High suspicion if: Variable events, psychiatric comorbidity",
            "",
            "**Suicide Risk**:",
            "- Elevated in epilepsy (3-5x general population)",
            "- Risk factors: Depression, drug-resistant epilepsy, young age",
            "- Assess: Direct questioning about suicidal thoughts",
            "- Act: If suicidal ideation, urgent mental health referral",
            "",
            "**Screening Frequency**:",
            "- At diagnosis",
            "- Annually",
            "- After medication changes",
            "- When mood symptoms suspected",
            "- After status epilepticus or seizure clusters",
            "",
            "**Collaborative Care**:",
            "- Integrated epilepsy-psychiatry management optimal",
            "- Address both neurological and psychiatric needs",
            "- Improve quality of life and seizure control"
        ]


__all__ = [
    'PsychiatricComorbidity',
    'PNESType',
    'PsychiatricMedicationInteraction',
    'PNESAssessment',
    'PsychotropicInteractionAssessment',
    'PsychiatryIntegration'
]
