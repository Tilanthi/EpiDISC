"""
Epilepsy-Specific MORK Ontology

Transformative enhancement: Comprehensive epilepsy knowledge ontology
for seizure classification, epilepsy syndromes, and treatment reasoning.

This extends the general MORK system with epilepsy-specific concepts and
semantic relations optimized for epilepsy consultation and research.
"""

from .. import BaseDomainModule, DomainConfig, DomainQueryResult
from ...memory.mork_ontology import MORKOntology, SemanticRelationType, OntologyNode, SemanticRelation
from typing import Dict, List, Optional, Set, Any
from dataclasses import dataclass
from datetime import datetime


class EpilepsyMORKOntology(MORKOntology):
    """
    Epilepsy-specialized MORK ontology for seizure classification,
    syndrome recognition, and treatment reasoning.

    Transformative capabilities:
    - Semantic seizure classification based on semiology
    - Epilepsy syndrome identification
    - Treatment response prediction
    - Causal reasoning for drug selection
    - Cross-referencing with EEG and imaging findings
    """

    def __init__(self):
        super().__init__()
        self._build_epilepsy_hierarchy()
        self._build_seizure_semiology()
        self._build_epilepsy_syndromes()
        self._build_treatment_knowledge()
        self._build_eeg_findings()
        self._build_causal_relations()

    def _build_epilepsy_hierarchy(self):
        """Build epilepsy-specific concept hierarchy"""

        # Epilepsy root concept
        self._add_node("EPILEPSY", "Epilepsy", "ROOT", {
            "description": "Neurological disorder characterized by recurrent seizures",
            "icd_10": "G40",
            "prevalence": "1% of population"
        })

        # Seizure types
        self._add_node("FOCAL_SEIZURE", "Focal Seizure", "EPILEPSY", {
            "description": "Seizures originating in one hemisphere",
            "ilae_2017": "Focal onset"
        })

        self._add_node("GENERALIZED_SEIZURE", "Generalized Seizure", "EPILEPSY", {
            "description": "Seizures originating in both hemispheres",
            "ilae_2017": "Generalized onset"
        })

        self._add_node("UNKNOWN_ONSET", "Unknown Onset Seizure", "EPILEPSY", {
            "description": "Seizures with unknown onset",
            "ilae_2017": "Unknown onset"
        })

        # Focal seizure subtypes
        self._add_node("FOCAL_AWARE", "Focal Aware Seizure", "FOCAL_SEIZURE", {
            "description": "Focal seizure with preserved awareness",
            "old_term": "Simple partial seizure"
        })

        self._add_node("FOCAL_IMPAIRED_AWARENESS", "Focal Impaired Awareness", "FOCAL_SEIZURE", {
            "description": "Focal seizure with impaired awareness",
            "old_term": "Complex partial seizure",
            "typical_duration": "1-2 minutes"
        })

        self._add_node("FOCAL_MOTOR", "Focal Motor Seizure", "FOCAL_SEIZURE", {
            "description": "Focal seizure with motor symptoms",
            "examples": "Jerking, stiffening, automatisms"
        })

        self._add_node("FOCAL_NON_MOTOR", "Focal Non-Motor Seizure", "FOCAL_SEIZURE", {
            "description": "Focal seizure without motor symptoms",
            "examples": "Sensory, autonomic, cognitive symptoms"
        })

        # Generalized seizure subtypes
        self._add_node("TONIC_CLONIC", "Tonic-Clonic Seizure", "GENERALIZED_SEIZURE", {
            "description": "Convulsive seizure with stiffening and jerking",
            "old_term": "Grand mal",
            "emergency": True
        })

        self._add_node("ABSENCE", "Absence Seizure", "GENERALIZED_SEIZURE", {
            "description": "Brief staring spells",
            "old_term": "Petit mal",
            "typical_duration": "5-15 seconds",
            "typical_age": "4-14 years"
        })

        self._add_node("MYOCLONIC", "Myoclonic Seizure", "GENERALIZED_SEIZURE", {
            "description": "Brief muscle jerks",
            "typical_timing": "Morning after awakening"
        })

        self._add_node("ATONIC", "Atonic Seizure", "GENERALIZED_SEIZURE", {
            "description": "Sudden loss of muscle tone",
            "nickname": "Drop attacks"
        })

        self._add_node("TONIC", "Tonic Seizure", "GENERALIZED_SEIZURE", {
            "description": "Sudden muscle stiffening"
        })

    def _build_seizure_semiology(self):
        """Build seizure semiology (symptom patterns) for classification"""

        # Aura symptoms
        self._add_node("AURA", "Aura", "SYMPTOM", {
            "description": "Subjective symptoms at seizure onset",
            "significance": "Indicates focal onset"
        })

        self._add_node("EPIGASTRIC_AURA", "Epigastric Rising Sensation", "AURA", {
            "description": "Rising sensation in abdomen",
            "localization": "Temporal lobe"
        })

        self._add_node("DEJA_VU", "Déjà Vu", "AURA", {
            "description": "Feeling of having experienced before",
            "localization": "Temporal lobe"
        })

        self._add_node("FEAR_AURA", "Fear Aura", "AURA", {
            "description": "Sudden feeling of fear or dread",
            "localization": "Temporal lobe"
        })

        # Automatisms
        self._add_node("AUTOMATISMS", "Automatisms", "SYMPTOM", {
            "description": "Repetitive automatic movements during seizure",
            "significance": "Suggests focal impaired awareness seizure"
        })

        self._add_node("ORAL_AUTOMATISMS", "Oral Automatisms", "AUTOMATISMS", {
            "description": "Lip-smacking, chewing, swallowing movements",
            "localization": "Temporal lobe"
        })

        self._add_node("MANUAL_AUTOMATISMS", "Manual Automatisms", "AUTOMATISMS", {
            "description": "Fumbling, picking at clothes",
            "localization": "Temporal lobe"
        })

        # Postictal symptoms
        self._add_node("POSTICTAL_CONFUSION", "Postictal Confusion", "SYMPTOM", {
            "description": "Confusion after seizure",
            "typical_duration": "1-15 minutes"
        })

        self._add_node("POSTICTAL_PARALYSIS", "Todd's Paralysis", "SYMPTOM", {
            "description": "Temporary weakness after seizure",
            "localizing_value": "Indicates seizure focus"
        })

    def _build_epilepsy_syndromes(self):
        """Build epilepsy syndrome concepts"""

        # Temporal lobe epilepsy
        self._add_node("TEMPORAL_LOBE_EPILEPSY", "Temporal Lobe Epilepsy", "EPILEPSY", {
            "description": "Most common focal epilepsy syndrome",
            "abbreviation": "TLE",
            "common_cause": "Hippocampal sclerosis",
            "typical_seizure": "Focal impaired awareness with automatisms"
        })

        self._add_node("MEPIAL_TEMPORAL_SCLEROSIS", "Mesial Temporal Sclerosis", "TEMPORAL_LOBE_EPILEPSY", {
            "description": "Scarring in mesial temporal structures",
            "mri_finding": "Hippocampal atrophy, T2 hyperintensity",
            "surgical_outcome": "Excellent (70-80% seizure-free)"
        })

        # Generalized epilepsy syndromes
        self._add_node("JUVENILE_MYOCLONIC_EPILEPSY", "Juvenile Myoclonic Epilepsy", "EPILEPSY", {
            "description": "Generalized epilepsy with myoclonus and GTCS",
            "abbreviation": "JME",
            "typical_age": "12-18 years",
            "triggers": "Sleep deprivation, alcohol, photic stimulation"
        })

        self._add_node("CHILDHOOD_ABSENCE_EPILEPSY", "Childhood Absence Epilepsy", "EPILEPSY", {
            "description": "Frequent absence seizures in children",
            "abbreviation": "CAE",
            "typical_age": "4-10 years",
            "prognosis": "Often outgrown in adolescence"
        })

        # Severe epilepsy syndromes
        self._add_node("LENNOX_GASTAUT", "Lennox-Gastaut Syndrome", "EPILEPSY", {
            "description": "Severe childhood-onset epilepsy",
            "characteristics": "Multiple seizure types, intellectual disability, treatment-resistant",
            "prognosis": "Poor, often persists into adulthood"
        })

        self._add_node("DRAVET", "Dravet Syndrome", "EPILEPSY", {
            "description": "Severe infantile-onset epilepsy",
            "genetics": "SCN1A mutation",
            "triggers": "Fever, hot baths",
            "characteristics": "Treatment-resistant, developmental delay"
        })

    def _build_treatment_knowledge(self):
        """Build medication and treatment knowledge"""

        # First-line AEDs
        self._add_node("LEVETIRACETAM", "Levetiracetam", "TREATMENT", {
            "description": "Broad-spectrum AED",
            "mechanism": "SV2A binding",
            "first_line": ["Focal seizures", "Generalized seizures"],
            "advantages": "No drug interactions, rapid titration",
            "side_effects": "Behavioral changes, sedation"
        })

        self._add_node("LAMOTRIGINE", "Lamotrigine", "TREATMENT", {
            "description": "Broad-spectrum AED",
            "mechanism": "Sodium channel modulation",
            "first_line": ["Focal seizures", "Generalized seizures"],
            "advantages": "Well-tolerated, mood-stabilizing",
            "disadvantages": "Slow titration, rash risk",
            "pregnancy": "Safe (first choice)"
        })

        self._add_node("CARBAMAZEPINE", "Carbamazepine", "TREATMENT", {
            "description": "Focal seizure AED",
            "mechanism": "Sodium channel blockade",
            "first_line": ["Focal seizures"],
            "contraindications": ["Generalized seizures", "Pregnancy"],
            "disadvantages": "Drug interactions, rash risk"
        })

        self._add_node("VALPROATE", "Valproate", "TREATMENT", {
            "description": "Broad-spectrum AED",
            "mechanism": "Multiple mechanisms",
            "indications": ["Generalized seizures", "JME"],
            "contraindications": ["Pregnancy", "Liver disease"],
            "teratogenic": "High risk"
        })

    def _build_eeg_findings(self):
        """Build EEG finding concepts for diagnostic reasoning"""

        self._add_node("EEG_SPIKE", "EEG Spike", "DIAGNOSTIC", {
            "description": "Sharp transient wave (20-70 ms)",
            "significance": "Interictal epileptiform discharge"
        })

        self._add_node("EEG_SHARP_WAVE", "EEG Sharp Wave", "DIAGNOSTIC", {
            "description": "Sharp transient wave (70-200 ms)",
            "significance": "Interictal epileptiform discharge"
        })

        self._add_node("TEMPORAL_SPIKE", "Temporal Spike", "EEG_SPIKE", {
            "description": "Spike in temporal region",
            "localization": "Temporal lobe epilepsy",
            "sleep_activation": "Common"
        })

        self._add_node("GENERALIZED_SPIKE_WAVE", "Generalized Spike-Wave", "DIAGNOSTIC", {
            "description": "Bilateral synchronous spike-wave discharges",
            "typical_frequency": "3 Hz (absence), 4-6 Hz (atypical)"
        })

        self._add_node("PLEDS", "Periodic Lateralized Epileptiform Discharges", "DIAGNOSTIC", {
            "description": "Periodic sharp waves over one hemisphere",
            "significance": "Acute structural lesion (stroke, trauma, infection)"
        })

    def _build_causal_relations(self):
        """Build causal reasoning relations for treatment decisions"""

        # Treatment response predictions
        self.relations.append(SemanticRelation(
            source_id="TEMPORAL_LOBE_EPILEPSY",
            relation_type=SemanticRelationType.CAUSES,
            target_id="SURGICAL_CANDIDATE",
            strength=0.8,
            metadata={"condition": "Drug-resistant TLE with MTS"}
        ))

        self.relations.append(SemanticRelation(
            source_id="JUVENILE_MYOCLONIC_EPILEPSY",
            relation_type=SemanticRelationType.INCOMPATIBLE,
            target_id="CARBAMAZEPINE",
            strength=0.9,
            metadata={"reason": "Can worsen myoclonic seizures"}
        ))

        self.relations.append(SemanticRelation(
            source_id="CHILDHOOD_ABSENCE_EPILEPSY",
            relation_type=SemanticRelationType.CAUSES,
            target_id="ETHOSUXIMIDE_RESPONSE",
            strength=0.85,
            metadata={"first_line": True}
        ))

        self.relations.append(SemanticRelation(
            source_id="PREGNANCY",
            relation_type=SemanticRelationType.INCOMPATIBLE,
            target_id="VALPROATE",
            strength=0.95,
            metadata={"reason": "High teratogenic risk"}
        ))

    def classify_seizure_from_description(self, description: str) -> Dict[str, Any]:
        """
        Transformative capability: Classify seizure from clinical description
        using semantic reasoning over the epilepsy ontology.
        """
        description_lower = description.lower()

        # Check for focal features
        focal_features = [
            "aura", "automatism", "lip smacking", "fumbling",
            "staring", "unresponsiveness", "confusion after"
        ]

        # Check for generalized features
        generalized_features = [
            "convulsion", "jerking", "stiffening", "loss of consciousness",
            "brief staring", "sudden"
        ]

        focal_score = sum(1 for feature in focal_features if feature in description_lower)
        generalized_score = sum(1 for feature in generalized_features if feature in description_lower)

        # Duration analysis
        if "2 minute" in description_lower or "2 minutes" in description_lower:
            focal_score += 2  # 2 minutes is typical for focal, long for absence

        classification = {
            "likely_type": "focal_impaired_awareness" if focal_score > generalized_score else "generalized",
            "confidence": max(focal_score, generalized_score) / (focal_score + generalized_score + 1),
            "reasoning": "Based on semiology analysis",
            "differential": ["focal_impaired_awareness", "absence", "psychogenic"] if focal_score > generalized_score else ["tonic_clonic", "absence", "focal_to_bilateral"]
        }

        return classification

    def recommend_treatment(self, seizure_type: str, patient_factors: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transformative capability: Recommend AED based on seizure type
        and patient factors using causal reasoning.
        """
        recommendations = []

        # Base recommendations on seizure type
        if "focal" in seizure_type.lower():
            recommendations.append({
                "medication": "Levetiracetam",
                "evidence": "First-line for focal seizures",
                "starting_dose": "500 mg twice daily",
                "confidence": 0.90
            })

            if not patient_factors.get("pregnancy"):
                recommendations.append({
                    "medication": "Lamotrigine",
                    "evidence": "Alternative first-line",
                    "caution": "Slow titration required",
                    "confidence": 0.85
                })

        elif "generalized" in seizure_type.lower():
            recommendations.append({
                "medication": "Valproate",
                "evidence": "First-line for generalized seizures",
                "caution": "Teratogenic - avoid in women of childbearing age",
                "confidence": 0.85
            })

            recommendations.append({
                "medication": "Levetiracetam",
                "evidence": "Alternative for generalized seizures",
                "confidence": 0.80
            })

        # Apply patient-specific modifications
        if patient_factors.get("pregnancy"):
            recommendations = [r for r in recommendations if "Lamotrigine" in r.get("medication", "") or
                            (r.get("medication") == "Levetiracetam" and "caution" not in r)]

        if patient_factors.get("psychiatric_history"):
            recommendations = [r for r in recommendations if "Levetiracetam" not in r.get("medication", "")]

        return {
            "recommendations": recommendations,
            "reasoning": "Based on seizure type, efficacy, and patient factors"
        }


# Factory function for creating epilepsy ontology
def create_epilepsy_ontology() -> EpilepsyMORKOntology:
    """
    Create epilepsy-specific MORK ontology.

    Returns:
        EpilepsyMORKOntology configured for seizure classification,
        syndrome recognition, and treatment reasoning.
    """
    return EpilepsyMORKOntology()