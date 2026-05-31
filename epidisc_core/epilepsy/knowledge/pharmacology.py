"""
EPIDISC Antiseizure Medication Database
========================================

Comprehensive antiseizure medication (ASM) knowledge system with
mechanisms, interactions, side effects, and clinical decision support.

Based on:
- NICE Clinical Guidelines (CG137, CG2)
- ILAE treatment guidelines
- BNF and formulary data
- FDA/EMA prescribing information
- Current clinical evidence (2024-2026)

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class ASMMechanism(Enum):
    """Primary mechanisms of action for antiseizure medications"""
    SODIUM_CHANNEL_BLOCKER = "sodium_channel_blocker"
    GABA_ENHANCER = "gaba_enhancer"
    GLUTAMATE_ANTAGONIST = "glutamate_antagonist"
    CALCIUM_CHANNEL_BLOCKER = "calcium_channel_blocker"
    SV2A_BINDER = "sv2a_binder"
    AMPA_RECEPTOR_ANTAGONIST = "ampa_receptor_antagonist"
    MULTIPLE_MECHANISMS = "multiple_mechanisms"
    UNKNOWN = "unknown"


class ASMCategory(Enum):
    """ASM categories based on spectrum and use"""
    BROAD_SPECTRUM = "broad_spectrum"           # Both focal and generalized
    FOCAL_ONLY = "focal_only"                    # Focal seizures only
    GENERALIZED_ONLY = "generalized_only"        # Generalized seizures only
    RESCUE = "rescue"                            # Acute rescue treatment
    ADJUNCTIVE = "adjunctive"                     # Add-on therapy


class SideEffectSeverity(Enum):
    """Severity levels for side effects"""
    MILD = "mild"                                # Tolerable, may not require intervention
    MODERATE = "moderate"                        # May require dose adjustment
    SEVERE = "severe"                            # Requires discontinuation
    LIFE_THREATENING = "life_threatening"        # Medical emergency


@dataclass
class ASMProfile:
    """
    Complete ASM profile for clinical decision-making

    Includes all essential information for safe and effective prescribing
    with evidence-based recommendations and safety monitoring.
    """

    # Basic information
    name: str
    brand_names: List[str]
    category: ASMCategory
    mechanism: ASMMechanism
    evidence_level: str  # A, B, C, D

    # Dosing information
    starting_dose_adult: str
    target_dose_adult: str
    maximum_dose_adult: str
    dosing_frequency: str
    titration_required: bool

    # Spectrum and indications
    effective_for: List[str]  # Focal, generalized, specific syndromes
    contraindicated_for: List[str]  # Seizure types that worsen

    # Side effects
    common_side_effects: List[str]
    serious_side_effects: List[str]
    black_box_warnings: List[str]

    # Drug interactions
    significant_interactions: List[str]
    enzyme_inducer: bool
    enzyme_inhibitor: bool
    protein_binding: str  # High, moderate, low

    # Special populations
    pregnancy_category: str  # FDA pregnancy categories
    breastfeeding: str      # Safe, caution, contraindicated
    renal_adjustment: bool
    hepatic_adjustment: bool
    elderly_considerations: str

    # Monitoring requirements
    required_monitoring: List[str]
    therapeutic_drug_monitoring: bool

    # Clinical considerations
    advantages: List[str]
    disadvantages: List[str]
    clinical_pearls: List[str]
    evidence_notes: str


class ASMDatabase:
    """
    Comprehensive ASM database with clinical decision support

    Evidence-based profiles for all commonly used antiseizure medications
    with interaction checking, safety monitoring, and treatment optimization.
    """

    # First-line ASM profiles (most commonly used)
    LEVETIRACETAM = ASMProfile(
        name="Levetiracetam",
        brand_names=["Keppra", "Elepsia XR"],
        category=ASMCategory.BROAD_SPECTRUM,
        mechanism=ASMMechanism.SV2A_BINDER,
        evidence_level="A",

        starting_dose_adult="250-500mg BID",
        target_dose_adult="1000-3000mg/day",
        maximum_dose_adult="3000mg/day",
        dosing_frequency="BID",
        titration_required=False,

        effective_for=["focal", "generalized", "myoclonic", "tonic-clonic"],
        contraindicated_for=[],

        common_side_effects=["sedation", "dizziness", "irritability", "behavioral changes"],
        serious_side_effects=["psychosis", "suicidal ideation", "severe depression"],
        black_box_warnings=["suicidal behavior and ideation"],

        significant_interactions=["none major", "may enhance CNS depressants"],
        enzyme_inducer=False,
        enzyme_inhibitor=False,
        protein_binding="Low (<10%)",

        pregnancy_category="C",
        breastfeeding="Safe - minimal excretion in breast milk",
        renal_adjustment=True,  # Renally excreted
        hepatic_adjustment=False,
        elderly_considerations="Renal dose adjustment, monitor behavior",

        required_monitoring=["renal function", "behavioral changes", "depression screening"],
        therapeutic_drug_monitoring=False,

        advantages=["no enzyme induction", "no significant drug interactions", "rapid titration", "IV/PO"],
        disadvantages=["behavioral side effects", "psychiatric effects", "expensive"],
        clinical_pearls=[
            "Rapid titration makes it good for acute situations",
            "Behavioral side effects more common in those with psychiatric history",
            "No hepatic metabolism - excellent for polytherapy",
            "Watch for irritability in children and elderly"
        ],
        evidence_notes="Level A evidence for focal and generalized seizures. First-line for most epilepsy types."
    )

    LAMOTRIGINE = ASMProfile(
        name="Lamotrigine",
        brand_names=["Lamictal"],
        category=ASMCategory.BROAD_SPECTRUM,
        mechanism=ASMMechanism.SODIUM_CHANNEL_BLOCKER,
        evidence_level="A",

        starting_dose_adult="25mg daily",
        target_dose_adult="100-200mg BID",
        maximum_dose_adult="500mg/day",
        dosing_frequency="BID",
        titration_required=True,  # Slow titration to avoid SJS/TEN

        effective_for=["focal", "generalized", "absence", "tonic-clonic"],
        contraindicated_for=[],

        common_side_effects=["dizziness", "headache", "nausea", "insomnia"],
        serious_side_effects=["Stevens-Johnson syndrome", "toxic epidermal necrolysis"],
        black_box_warnings=["serious rash requiring hospitalization"],

        significant_interactions=["valproate (doubles lamotrigine levels)", "carbamazepine (induces metabolism)"],
        enzyme_inducer=False,
        enzyme_inhibitor=False,
        protein_binding="Moderate (55%)",

        pregnancy_category="C",
        breastfeeding="Safe - excreted in breast milk at low levels",
        renal_adjustment=False,
        hepatic_adjustment=False,
        elderly_considerations="Slow titration, monitor for rash",

        required_monitoring=["rash", "liver function", "blood counts"],
        therapeutic_drug_monitoring=False,

        advantages=["excellent for mood stabilization", "broad spectrum", "cognitive friendly"],
        disadvantages=["slow titration", "rash risk", "drug interactions"],
        clinical_pearls=[
            "Slow titration is critical - rash risk increases with rapid titration",
            "Excellent for bipolar disorder comorbidity",
            "Valproate doubles levels, halve target dose",
            "Good cognitive profile - excellent for elderly"
        ],
        evidence_notes="Level A evidence for focal and generalized seizures. Excellent for mood disorders."
    )

    VALPROATE = ASMProfile(
        name="Valproate",
        brand_names=["Depakote", "Epilim"],
        category=ASMCategory.BROAD_SPECTRUM,
        mechanism=ASMMechanism.MULTIPLE_MECHANISMS,
        evidence_level="A",

        starting_dose_adult="250mg BID",
        target_dose_adult="1000-2000mg/day",
        maximum_dose_adult="3000mg/day",
        dosing_frequency="BID-TID",
        titration_required=False,

        effective_for=["generalized", "absence", "myoclonic", "tonic-clonic", "focal"],
        contraindicated_for=["mitochondrial disorders", "urea cycle disorders"],

        common_side_effects=["weight gain", "tremor", "hair loss", "GI upset"],
        serious_side_effects=["hepatotoxicity", "pancreatitis", "thrombocytopenia", "polycystic ovaries"],
        black_box_warnings=["hepatotoxicity", "teratogenicity", "pancreatitis"],

        significant_interactions=["many - enzyme inhibitor", "increases lamotrigine levels"],
        enzyme_inducer=False,
        enzyme_inhibitor=True,
        protein_binding="High (90-95%)",

        pregnancy_category="D",  # Major teratogen
        breastfeeding="Use with caution - excreted in breast milk",
        renal_adjustment=False,
        hepatic_adjustment=True,  # Hepatic metabolism
        elderly_considerations="Lower doses, monitor liver function, tremor",

        required_monitoring=["liver function", "ammonia levels", "platelets", "valproate level"],
        therapeutic_drug_monitoring=True,

        advantages=["excellent for generalized epilepsy", "migraine prophylaxis", "mood stabilization"],
        disadvantages=["teratogenic", "weight gain", "hair loss", "liver toxicity"],
        clinical_pearls=[
            "First-line for generalized epilepsy but avoid in pregnancy",
            "Excellent for JME and JAE",
            "Avoid in women of childbearing potential if possible",
            "Monitor ammonia levels if encephalopathy suspected"
        ],
        evidence_notes="Level A evidence for generalized seizures. Major teratogen - neural tube defects."
    )

    CARBAMAZEPINE = ASMProfile(
        name="Carbamazepine",
        brand_names=["Tegretol"],
        category=ASMCategory.FOCAL_ONLY,
        mechanism=ASMMechanism.SODIUM_CHANNEL_BLOCKER,
        evidence_level="A",

        starting_dose_adult="100-200mg BID",
        target_dose_adult="800-1200mg/day",
        maximum_dose_adult="2000mg/day",
        dosing_frequency="BID-TID",
        titration_required=True,

        effective_for=["focal", "tonic-clonic"],
        contraindicated_for=["generalized epilepsy", "absence", "myoclonic"],  # Can worsen

        common_side_effects=["dizziness", "diplopia", "GI upset", "hyponatremia"],
        serious_side_effects=["aplastic anemia", "agranulocytosis", "Stevens-Johnson", "hepatotoxicity"],
        black_box_warnings=["serious blood disorders", "severe skin reactions"],

        significant_interactions=["many - potent enzyme inducer", "decreases oral contraceptive efficacy"],
        enzyme_inducer=True,
        enzyme_inhibitor=False,
        protein_binding="High (75-90%)",

        pregnancy_category="D",
        breastfeeding="Safe - excreted in breast milk",
        renal_adjustment=False,
        hepatic_adjustment=True,
        elderly_considerations="Lower doses, monitor sodium, cardiac conduction",

        required_monitoring=["CBC", "serum sodium", "liver function", "carbamazepine level"],
        therapeutic_drug_monitoring=True,

        advantages=["first-line for focal epilepsy", " inexpensive", "long experience"],
        disadvantages=["enzyme induction", "can worsen generalized seizures", "many drug interactions"],
        clinical_pearls=[
            "Excellent for focal epilepsy but AVOID in generalized epilepsy",
            "Monitor sodium - hyponatremia common",
            "Enzyme inducer - affects many other medications",
            "Autoinduction - levels may decrease over time"
        ],
        evidence_notes="Level A evidence for focal seizures. Can worsen generalized seizures - avoid."
    )

    # Additional ASM profiles (continuing with comprehensive database)

    LACOSAMIDE = ASMProfile(
        name="Lacosamide",
        brand_names=["Vimpat"],
        category=ASMCategory.FOCAL_ONLY,
        mechanism=ASMMechanism.SODIUM_CHANNEL_BLOCKER,
        evidence_level="B",

        starting_dose_adult="50mg BID",
        target_dose_adult="200-400mg/day",
        maximum_dose_adult="600mg/day",
        dosing_frequency="BID",
        titration_required=True,

        effective_for=["focal"],
        contraindicated_for=["generalized epilepsy"],  # Can worsen

        common_side_effects=["dizziness", "headache", "nausea", "PR interval prolongation"],
        serious_side_effects=["cardiac conduction abnormalities", "suicidal ideation"],
        black_box_warnings=["suicidal behavior and ideation"],

        significant_interactions=["strong CYP3A4 inducers", "drugs affecting cardiac conduction"],
        enzyme_inducer=False,
        enzyme_inhibitor=False,
        protein_binding="Low (<15%)",

        pregnancy_category="C",
        breastfeeding="Caution - limited data",
        renal_adjustment=True,
        hepatic_adjustment=False,
        elderly_considerations="Monitor ECG in elderly, consider renal function",

        required_monitoring=["ECG (PR interval)", "cardiac conduction", "behavioral changes"],
        therapeutic_drug_monitoring=False,

        advantages=["IV/PO formulation", "no significant drug interactions", "can be used rapidly"],
        disadvantages=["can worsen generalized seizures", "cardiac conduction effects"],
        clinical_pearls=[
            "Excellent for acute treatment (IV formulation)",
            "Monitor PR interval, especially with other cardiac drugs",
            "Avoid in patients with conduction abnormalities",
            "Rapid titration possible"
        ],
        evidence_notes="Level B evidence for focal seizures. Useful for acute treatment with IV formulation."
    )

    BRIVARACETAM = ASMProfile(
        name="Brivaracetam",
        brand_names=["Briviact"],
        category=ASMCategory.BROAD_SPECTRUM,
        mechanism=ASMMechanism.SV2A_BINDER,
        evidence_level="B",

        starting_dose_adult="25mg BID",
        target_dose_adult="50-100mg BID",
        maximum_dose_adult="200mg/day",
        dosing_frequency="BID",
        titration_required=False,

        effective_for=["focal"],
        contraindicated_for=[],

        common_side_effects=["somnolence", "dizziness", "fatigue"],
        serious_side_effects=["suicidal ideation", "psychiatric reactions"],
        black_box_warnings=["suicidal behavior and ideation"],

        significant_interactions=["Rifampin decreases levels"],
        enzyme_inducer=False,
        enzyme_inhibitor=False,
        protein_binding="Low (<20%)",

        pregnancy_category="C",
        breastfeeding="Caution - limited data",
        renal_adjustment=True,
        hepatic_adjustment=True,
        elderly_considerations="No specific concerns, dose adjust if needed",

        required_monitoring=["behavioral changes", "psychiatric symptoms"],
        therapeutic_drug_monitoring=False,

        advantages=["less behavioral side effects than levetiracetam", "rapid titration", "IV/PO"],
        disadvantages=["expensive", "less experience than levetiracetam"],
        clinical_pearls=[
            "SV2A binder like levetiracetam but with fewer behavioral side effects",
            "Can be used rapidly without titration",
            "Good alternative if levetiracetam not tolerated",
            "Some patients respond to both levetiracetam and brivaracetam"
        ],
        evidence_notes="Level B evidence for focal seizures. Similar to levetiracetam with better tolerability."
    )

    PERAMPANEL = ASMProfile(
        name="Perampanel",
        brand_names=["Fycompa"],
        category=ASMCategory.FOCAL_ONLY,
        mechanism=ASMMechanism.AMPA_RECEPTOR_ANTAGONIST,
        evidence_level="B",

        starting_dose_adult="2mg daily",
        target_dose_adult="8-12mg/day",
        maximum_dose_adult="12mg/day",
        dosing_frequency="QD",
        titration_required=True,

        effective_for=["focal", "tonic-clonic"],
        contraindicated_for=[],

        common_side_effects=["dizziness", "somnolence", "ataxia", "behavioral changes"],
        serious_side_effects=["psychosis", "suicidal ideation", "severe aggression"],
        black_box_warnings=["suicidal behavior and ideation"],

        significant_interactions=["enzyme inducers decrease levels", "alcohol enhances effects"],
        enzyme_inducer=False,
        enzyme_inhibitor=False,
        protein_binding="High (95%)",

        pregnancy_category="C",
        breastfeeding="Caution - limited data",
        renal_adjustment=False,
        hepatic_adjustment=True,
        elderly_considerations="Monitor for behavioral changes and falls",

        required_monitoring=["behavioral changes", "aggression", "psychosis", "fall risk"],
        therapeutic_drug_monitoring=False,

        advantages=["novel mechanism", "once daily dosing", "effective for refractory focal epilepsy"],
        disadvantages=["behavioral and psychiatric side effects", "expensive"],
        clinical_pearls=[
            "First-in-class AMPA receptor antagonist",
            "Significant behavioral side effects - monitor closely",
            "Once daily dosing improves adherence",
            "Good for drug-resistant focal epilepsy"
        ],
        evidence_notes="Level B evidence for focal seizures. Novel mechanism with significant behavioral effects."
    )

    CENOBAMATE = ASMProfile(
        name="Cenobamate",
        brand_names=["Xcopri"],
        category=ASMCategory.FOCAL_ONLY,
        mechanism=ASMMechanism.MULTIPLE_MECHANISMS,
        evidence_level="B",

        starting_dose_adult="12.5mg daily",
        target_dose_adult="200-400mg/day",
        maximum_dose_adult="400mg/day",
        dosing_frequency="BID",
        titration_required=True,  # CRITICAL - slow titration to avoid SJS/TEN

        effective_for=["focal"],
        contraindicated_for=[],

        common_side_effects=["somnolence", "dizziness", "double vision", "headache"],
        serious_side_effects=["Stevens-Johnson syndrome", "cardiac conduction abnormalities", "shortened QT"],
        black_box_warnings=["serious rash", "cardiac conduction abnormalities", "suicidal behavior"],

        significant_interactions=["enzyme inhibitors", "drugs affecting cardiac conduction"],
        enzyme_inducer=False,
        enzyme_inhibitor=False,
        protein_binding="High (90%)",

        pregnancy_category="C",
        breastfeeding="Caution - limited data",
        renal_adjustment=False,
        hepatic_adjustment=True,
        elderly_considerations="Monitor ECG, watch for CNS side effects",

        required_monitoring=["ECG (PR, QRS, QT)", "rash", "behavioral changes"],
        therapeutic_drug_monitoring=False,

        advantages=["highly effective for refractory focal epilepsy", "novel mechanisms"],
        disadvantages=["slow titration required", "rash risk", "cardiac effects"],
        clinical_pearls=[
            "Very effective but slow titration is CRITICAL to avoid SJS/TEN",
            "Monitor ECG for conduction abnormalities",
            "Can be very effective for drug-resistant focal epilepsy",
            "Recent approval with growing experience"
        ],
        evidence_notes="Level B evidence for focal seizures. Highly effective but requires careful titration."
    )

    @classmethod
    def get_all_ASMS(cls) -> Dict[str, ASMProfile]:
        """Get all available ASM profiles"""
        return {
            "levetiracetam": cls.LEVETIRACETAM,
            "lamotrigine": cls.LAMOTRIGINE,
            "valproate": cls.VALPROATE,
            "carbamazepine": cls.CARBAMAZEPINE,
            "lacosamide": cls.LACOSAMIDE,
            "brivaracetam": cls.BRIVARACETAM,
            "perampanel": cls.PERAMPANEL,
            "cenobamate": cls.CENOBAMATE
        }

    @classmethod
    def get_first_line_focal(cls) -> List[str]:
        """Get first-line ASMs for focal epilepsy"""
        return [
            "levetiracetam",
            "lamotrigine",
            "carbamazepine",
            "lacosamide"
        ]

    @classmethod
    def get_first_line_generalized(cls) -> List[str]:
        """Get first-line ASMs for generalized epilepsy"""
        return [
            "valproate",
            "lamotrigine",
            "levetiracetam"
        ]

    @classmethod
    def check_contraindications(
        cls,
        asm_name: str,
        seizure_type: str,
        patient_factors: Dict[str, bool]
    ) -> List[str]:
        """
        Check for contraindications and warnings for ASM

        Args:
            asm_name: Name of ASM
            seizure_type: Type of seizures (focal, generalized, etc.)
            patient_factors: Patient characteristics (pregnancy, renal, hepatic, etc.)

        Returns:
            List of warnings and contraindications
        """
        warnings = []
        asm = cls.get_all_ASMS().get(asm_name)

        if not asm:
            warnings.append(f"⚠️ Unknown ASM: {asm_name}")
            return warnings

        # Check seizure type contraindications
        if seizure_type in asm.contraindicated_for:
            warnings.append(f"⚠️ CRITICAL: {asm_name} can worsen {seizure_type}")

        # Check pregnancy
        if patient_factors.get("pregnancy", False) and asm.pregnancy_category == "D":
            warnings.append(f"⚠️ CRITICAL: {asm_name} is teratogenic (Category D)")

        # Check renal function
        if patient_factors.get("renal_impairment", False) and not asm.renal_adjustment:
            warnings.append(f"⚠️ {asm_name} may require renal dose adjustment")

        # Check hepatic function
        if patient_factors.get("hepatic_impairment", False) and asm.hepatic_adjustment:
            warnings.append(f"⚠️ {asm_name} requires hepatic dose adjustment")

        # Check enzyme induction (affects many other drugs)
        if asm.enzyme_inducer and patient_factors.get("oral_contraceptives", False):
            warnings.append(f"⚠️ {asm_name} decreases oral contraceptive efficacy")

        # Check elderly considerations
        if patient_factors.get("elderly", False):
            warnings.append(f"ℹ️ Elderly: {asm.elderly_considerations}")

        return warnings

    @classmethod
    def get_drug_interactions(cls, asm1: str, asm2: str) -> Optional[str]:
        """Check for significant interactions between two ASMs"""
        interactions = {
            "valproate-lamotrigine": "⚠️ Valproate doubles lamotrigine levels - halve lamotrigine target dose",
            "carbamazepine-any": "⚠️ Carbamazepine induces metabolism of many ASMs - increase doses",
            "phenytoin-any": "⚠️ Phenytoin induces metabolism of many ASMs - increase doses",
            "enzyme_inducers-oral_contraceptives": "⚠️ Enzyme inducers decrease oral contraceptive efficacy"
        }

        # Create interaction key
        key1 = f"{asm1}-{asm2}"
        key2 = f"{asm2}-{asm1}"

        if key1 in interactions:
            return interactions[key1]
        elif key2 in interactions:
            return interactions[key2]
        elif asm1 == asm2:
            return None
        else:
            return None  # No major interaction

    @classmethod
    def recommend_first_line(
        cls,
        seizure_type: str,
        patient_factors: Optional[Dict[str, bool]] = None
    ) -> List[Tuple[str, List[str]]]:
        """
        Recommend first-line ASMs with considerations

        Args:
            seizure_type: Focal, generalized, etc.
            patient_factors: Patient characteristics

        Returns:
            List of (ASM, considerations) tuples
        """
        recommendations = []
        patient_factors = patient_factors or {}

        if seizure_type == "focal":
            for asm_name in cls.get_first_line_focal():
                asm = cls.get_all_ASMS()[asm_name]
                considerations = cls.check_contraindications(
                    asm_name, seizure_type, patient_factors
                )

                if not any("CRITICAL" in c for c in considerations):
                    recommendations.append((asm_name, considerations))

        elif seizure_type == "generalized":
            for asm_name in cls.get_first_line_generalized():
                asm = cls.get_all_ASMS()[asm_name]
                considerations = cls.check_contraindications(
                    asm_name, seizure_type, patient_factors
                )

                if not any("CRITICAL" in c for c in considerations):
                    recommendations.append((asm_name, considerations))

        return recommendations


class DrugInteractions:
    """
    ASM drug interaction checker and management

    Provides comprehensive drug interaction checking with
    clinical recommendations and management strategies.
    """

    # Major ASM interactions requiring intervention
    MAJOR_INTERACTIONS = {
        "valproate_lamotrigine": {
            "severity": "major",
            "effect": "Valproate inhibits lamotrigine glucuronidation → doubles lamotrigine levels",
            "action": "Halve lamotrigine target dose when adding valproate",
            "monitoring": "Monitor for lamotrigine toxicity (rash, dizziness, ataxia)"
        },
        "carbamazepine_lamotrigine": {
            "severity": "moderate",
            "effect": "Carbamazepine induces lamotrigine metabolism → decreases lamotrigine levels",
            "action": "May need to increase lamotrigine dose when adding carbamazepine",
            "monitoring": "Monitor seizure control, consider lamotrigine level"
        },
        "carbamazepine_oral_contraceptives": {
            "severity": "major",
            "effect": "Carbamazepine induces estrogen metabolism → decreases contraceptive efficacy",
            "action": "Use alternative contraception or higher-dose contraceptive",
            "monitoring": "Counsel on pregnancy risk, consider alternative ASM"
        },
        "phenytoin_warfarin": {
            "severity": "major",
            "effect": "Phenytoin induces warfarin metabolism → decreases INR",
            "action": "Monitor INR closely when starting/stopping phenytoin",
            "monitoring": "Frequent INR monitoring, adjust warfarin dose"
        }
    }

    @classmethod
    def check_interaction(
        cls,
        drug1: str,
        drug2: str
    ) -> Optional[Dict[str, str]]:
        """Check for interaction between two drugs"""
        key = f"{drug1}_{drug2}"
        return cls.MAJOR_INTERACTIONS.get(key)

    @classmethod
    def get_all_interactions(cls, medication_list: List[str]) -> List[Dict]:
        """Get all interactions in a medication list"""
        interactions_found = []
        medications_lower = [m.lower() for m in medication_list]

        for i, med1 in enumerate(medications_lower):
            for med2 in medications_lower[i+1:]:
                interaction = cls.check_interaction(med1, med2)
                if interaction:
                    interactions_found.append({
                        "drugs": f"{med1} + {med2}",
                        "severity": interaction["severity"],
                        "effect": interaction["effect"],
                        "action": interaction["action"],
                        "monitoring": interaction["monitoring"]
                    })

        return interactions_found


class SideEffectProfiles:
    """
    ASM side effect profiles with management strategies

    Comprehensive side effect information with monitoring
    recommendations and management approaches.
    """

    # Common side effect clusters
    BEHAVIORAL_EFFECTS = {
        "medications": ["levetiracetam", "brivaracetam", "perampanel", "zonisamide", "topiramate"],
        "symptoms": ["irritability", "aggression", "depression", "suicidal ideation", "psychosis"],
        "monitoring": "Behavioral screening at each visit, suicide risk assessment",
        "management": "Reduce dose, discontinue if severe, consider psychiatric evaluation"
    }

    COGNITIVE_EFFECTS = {
        "medications": ["topiramate", "phenobarbital", "benzodiazepines"],
        "symptoms": ["slowed thinking", "memory problems", "word-finding difficulties", "attention deficits"],
        "monitoring": "Cognitive assessment at baseline and periodically",
        "management": "Reduce dose, switch to cognitive-friendly ASM (levetiracetam, lamotrigine)"
    }

    DERMATOLOGICAL_EFFECTS = {
        "medications": ["lamotrigine", "carbamazepine", "phenytoin", "valproate"],
        "symptoms": ["rash", "Stevens-Johnson syndrome", "toxic epidermal necrolysis"],
        "monitoring": "Rash assessment at each visit, especially during titration",
        "management": "STOP immediately if rash present, seek emergency care for severe rash"
    }

    CARDIAC_EFFECTS = {
        "medications": ["lacosamide", "carbamazepine", "phenytoin"],
        "symptoms": ["PR prolongation", "QRS widening", "arrhythmias"],
        "monitoring": "ECG at baseline and after dose changes",
        "management": "Reduce dose or discontinue if significant conduction abnormalities"
    }

    METABOLIC_EFFECTS = {
        "medications": ["valproate", "carbamazepine", "phenytoin", "phenobarbital"],
        "symptoms": ["weight gain", "insulin resistance", "dyslipidemia", "bone health"],
        "monitoring": "Weight, BMI, fasting glucose, lipid panel, vitamin D",
        "management": "Lifestyle modifications, consider metabolic-friendly ASM alternatives"
    }

    @classmethod
    def get_side_effects_by_medication(cls, medication: str) -> Dict:
        """Get side effect profile for specific medication"""
        asm_profiles = ASMDatabase.get_all_ASMS()

        if medication.lower() in asm_profiles:
            asm = asm_profiles[medication.lower()]
            return {
                "common": asm.common_side_effects,
                "serious": asm.serious_side_effects,
                "warnings": asm.black_box_warnings,
                "monitoring": asm.required_monitoring
            }
        else:
            return {}

    @classmethod
    def get_medication_by_side_effect(cls, side_effect: str) -> List[str]:
        """Get medications that commonly cause specific side effect"""
        side_effect = side_effect.lower()
        medications = []

        if any(term in side_effect for term in ["behavior", "irritability", "aggression"]):
            medications.extend(cls.BEHAVIORAL_EFFECTS["medications"])
        elif any(term in side_effect for term in ["cognitive", "memory", "thinking"]):
            medications.extend(cls.COGNITIVE_EFFECTS["medications"])
        elif any(term in side_effect for term in ["rash", "skin"]):
            medications.extend(cls.DERMATOLOGICAL_EFFECTS["medications"])
        elif any(term in side_effect for term in ["cardiac", "ecg", "pr", "qrs"]):
            medications.extend(cls.CARDIAC_EFFECTS["medications"])
        elif any(term in side_effect for term in ["weight", "metabolic"]):
            medications.extend(cls.METABOLIC_EFFECTS["medications"])

        return list(set(medications))


class TreatmentGuidelines:
    """
    Evidence-based treatment guidelines for epilepsy

    ILAE and NICE guideline implementation with
    evidence levels and clinical recommendations.
    """

    # ILAE 2013 guideline evidence ratings
    ILAE_EVIDENCE_LEVELS = {
        "A": "Established efficacy (≥1 Class I RCT)",
        "B": "Likely efficacy (≥1 Class II RCT)",
        "C": "Possible efficacy (≥1 Class III trial)",
        "D": "Potential efficacy (Class IV evidence)"
    }

    @classmethod
    def get_first_line_recommendation(
        cls,
        epilepsy_type: str,
        patient_factors: Optional[Dict] = None
    ) -> Dict[str, List]:
        """
        Get evidence-based first-line treatment recommendations

        Returns:
            Dictionary with 'recommended', 'alternatives', 'avoid' lists
        """
        patient_factors = patient_factors or {}
        recommendations = {
            "recommended": [],
            "alternatives": [],
            "avoid": [],
            "evidence_level": "",
            "considerations": []
        }

        if epilepsy_type == "focal":
            recommendations["recommended"] = ASMDatabase.get_first_line_focal()
            recommendations["alternatives"] = [
                "brivaracetam",
                "perampanel",
                "zonisamide",
                "topiramate"
            ]
            recommendations["avoid"] = []  # No specific contraindications for focal
            recommendations["evidence_level"] = "A"
            recommendations["considerations"] = [
                "Consider comorbidities (depression → avoid levetiracetam if possible)",
                "Consider drug interactions",
                "Consider pregnancy potential",
                "Consider elderly (cognitive effects, drug interactions)"
            ]

        elif epilepsy_type == "generalized":
            recommendations["recommended"] = ASMDatabase.get_first_line_generalized()
            recommendations["alternatives"] = [
                "topiramate",
                "zonisamide",
                "benzodiazepines (adjunctive)"
            ]
            recommendations["avoid"] = [
                "carbamazepine",  # Can worsen generalized seizures
                "phenytoin",     # Can worsen generalized seizures
                "oxcarbazepine", # Can worsen generalized seizures
                "lacosamide"     # Can worsen generalized seizures
            ]
            recommendations["evidence_level"] = "A"
            recommendations["considerations"] = [
                "AVOID sodium channel blockers in generalized epilepsy",
                "Valproate excellent but teratogenic",
                "Lamotrigine excellent for JME and JAE",
                "Levetiracetam good but behavioral side effects"
            ]

        elif epilepsy_type == "absence":
            recommendations["recommended"] = ["ethosuximide", "valproate"]
            recommendations["alternatives"] = ["lamotrigine", "clonazepam"]
            recommendations["avoid"] = [
                "carbamazepine",  # Can worsen absence
                "phenytoin",     # Can worsen absence
                "phenobarbital"  # Can worsen absence
            ]
            recommendations["evidence_level"] = "A"
            recommendations["considerations"] = [
                "Ethosuximide only for absence seizures",
                "Valproate if multiple generalized seizure types",
                "Lamotrigine for absence + GTCS"
            ]

        # Consider pregnancy
        if patient_factors.get("pregnancy"):
            recommendations["considerations"].append(
                "⚠️ AVOID valproate in pregnancy (major teratogen)"
            )
            recommendations["avoid"].append("valproate")

        # Consider elderly
        if patient_factors.get("elderly"):
            recommendations["considerations"].append(
                "Prefer cognitive-friendly ASMs (lamotrigine, levetiracetam)"
            )
            recommendations["considerations"].append(
                "Avoid enzyme inducers if multiple medications"
            )

        return recommendations

    @classmethod
    def get_rescue_medication(cls) -> Dict:
        """Get rescue medication recommendations for seizure clusters"""
        return {
            "recommended": [
                {
                    "medication": "buccal midazolam",
                    "dose": "5-10mg (adults)",
                    "timing": "at seizure onset",
                    "duration": "5-10 minutes action",
                    "considerations": "Can be administered by caregivers"
                },
                {
                    "medication": "rectal diazepam",
                    "dose": "5-20mg (adults)",
                    "timing": "at seizure onset",
                    "duration": "15-30 minutes action",
                    "considerations": "Alternative if buccal not available"
                }
            ],
            "indications": [
                "Seizure clusters (≥2 in 24 hours)",
                "Prolonged seizures (≥5 minutes)",
                "History of status epilepticus",
                "Travel or situations without immediate medical access"
            ],
            "education": [
                "Train caregivers in administration",
                "Have emergency protocol",
                "Call emergency services if seizure continues >5 minutes after rescue",
                "Document use and effectiveness"
            ]
        }


__all__ = [
    'ASMMechanism',
    'ASMCategory',
    'SideEffectSeverity',
    'ASMProfile',
    'ASMDatabase',
    'DrugInteractions',
    'SideEffectProfiles',
    'TreatmentGuidelines'
]