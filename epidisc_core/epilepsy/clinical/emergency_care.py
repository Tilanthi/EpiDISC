"""
EPIDISC Emergency Medicine and Status Epilepticus Protocols
============================================================

Comprehensive acute seizure management and status epilepticus
treatment protocols with emergency care guidance.

Based on:
- ILAE status epilepticus guidelines (2022)
- Neurocritical Care Society recommendations
- NICE clinical guidelines (CG176)
- Current resuscitation protocols

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class StatusType(Enum):
    """Types of status epilepticus"""
    CONVULSIVE_SE = "convulsive_status_epilepticus"          # Convulsive SE
    NON_CONVULSIVE_SE = "non_convulsive_status_epilepticus"  # Non-convulsive SE
    REFRACTORY_SE = "refractory_status_epilepticus"          # Refractory SE
    SUPER_REFRACTORY_SE = "super_refractory_status_epilepticus"  # Super-refractory SE


class EmergencySeverity(Enum):
    """Emergency severity levels"""
    LIFE_THREATENING = "life_threatening"                  # Immediate intervention required
    URGENT = "urgent"                                      # Within minutes
    ACUTE = "acute"                                        # Within hours
    TIME_SENSITIVE = "time_sensitive"                      # Time-critical treatment


@dataclass
class EmergencyProtocol:
    """
    Complete emergency protocol for acute seizure management

    Includes immediate interventions, medication protocols,
    monitoring requirements, and escalation pathways.
    """

    emergency_type: str
    severity: EmergencySeverity
    immediate_actions: List[str]
    first_line_treatment: List[str]
    second_line_treatment: List[str]
    refractory_protocol: List[str]
    monitoring_requirements: List[str]
    escalation_criteria: List[str]
    complications: List[str]
    prognosis: str


class EmergencyEpilepsyCare:
    """
    Comprehensive emergency epilepsy care system

    Evidence-based protocols for acute seizure management,
    status epilepticus treatment, and emergency complications.
    """

    # First seizure management protocol
    FIRST_SEIZURE_PROTOCOL = {
        "immediate_assessment": [
            "ABC (Airway, Breathing, Circulation)",
            "Protect from injury",
            "Position in recovery position",
            "Administer oxygen if hypoxic",
            "Establish intravenous access",
            "Check blood glucose (capillary or venous)"
        ],
        "investigations": [
            "Blood glucose (hypoglycemia exclusion)",
            "Serum electrolytes (Na, K, Ca, Mg)",
            "Toxicology screen if suspected ingestion",
            "ECG if cardiac concern",
            "CT head if postictal deficit or trauma"
        ],
        "disposition": [
            "Admit if: no clear cause, abnormal neuro exam, postictal deficit",
            "Consider discharge if: clear provoking factor, normal workup, reliable observation",
            "Driving restrictions per local regulations",
            "Education on seizure precautions",
            "Arrange specialist follow-up"
        ]
    }

    # Convulsive status epilepticus protocol (ILAE 2022)
    CONVULSIVE_SE_PROTOCOL = {
        "definition": "Seizure lasting >5 minutes OR ≥2 seizures without full recovery",
        "stages": {
            "initial": "0-5 minutes (begin treatment)",
            "early": "5-20 minutes (first-line ASMs)",
            "established": "20-40 minutes (second-line ASMs)",
            "refractory": ">40 minutes (anesthetic agents)"
        },
        "first_line": [
            "⏱️ TREATMENT WITHIN 5 MINUTES",
            "",
            "🚑 Benzodiazepine (choose one):",
            "• Lorazepam 0.1 mg/kg IV (max 4 mg) - FIRST LINE",
            "• Midazolam 10 mg IM/buccal (if IV access unavailable)",
            "• Diazepam 0.15-0.2 mg/kg IV/PR (alternative)",
            "",
            "⚠️ ADJUNCTIVE MEASURES:",
            "• Airway protection",
            "• Oxygen supplementation",
            "• IV access",
            "• Cardiac monitoring",
            "• Blood glucose check"
        ],
        "second_line": [
            "⏱️ IF SEIZURES PERSIST >20 MINUTES",
            "",
            "💊 SECOND-LINE ASM:",
            "• Levetiracetam 60 mg/kg IV (max 4500 mg)",
            "• Valproate 40 mg/kg IV (max 3000 mg)",
            "• Fosphenytoin 20 mg/kg PE IV (max 1500 mg PE)",
            "",
            "💡 CLINICAL DECISION:",
            "• Consider underlying etiology",
            "• Review comorbidities",
            "• Check for drug interactions",
            "• Consider loading dose if patient on existing ASM"
        ],
        "refractory": [
            "⏱️ IF SEIZURES PERSIST >40 MINUTES (REFRACTORY SE)",
            "",
            "🏥 ICU ADMISSION REQUIRED",
            "",
            "💊 ANESTHETIC AGENTS:",
            "• Midazolam infusion (0.05-0.2 mg/kg/hour)",
            "• Propofol infusion (1-3 mg/kg/hour)",
            "• Thiopental/pentobarbital infusion",
            "",
            "⚠️ MONITORING:",
            "• Continuous EEG",
            "• Hemodynamic monitoring",
            "• Respiratory support (often intubated)",
            "• Intracranial pressure monitoring if indicated"
        ],
        "super_refractory": [
            "⏱️ IF SEIZURES PERSIST >24 HOURS (SUPER-REFRACTORY SE)",
            "",
            "🔬 ADDITIONAL CONSIDERATIONS:",
            "• Ketamine infusion",
            "• Inhaled anesthetics (isoflurane, desflurane)",
            "• Pyridoxine (pyridoxine-dependent epilepsy)",
            "• Immunotherapy ( autoimmune encephalitis)",
            "• Ketogenic diet initiation",
            "• Consider neurosurgical consultation"
        ]
    }

    # Non-convulsive status epilepticus protocol
    NON_CONVULSIVE_SE_PROTOCOL = {
        "clinical_features": [
            "Altered mental status",
            "Confusion or disorientation",
            "Behavioral changes",
            "Subtle motor activity (eye deviation, nystagmus)",
            "No obvious convulsions"
        ],
        "diagnosis": [
            "HIGH CLINICAL SUSPICION NEEDED",
            "• Consider in comatose patients",
            "• Post-convulsive SE patients with persistent confusion",
            "• Consider in psychiatric patients with unusual presentations"
        ],
        "diagnostic_tests": [
            "🧪 EEG IS GOLD STANDARD:",
            "• Urgent EEG required",
            "• Continuous EEG monitoring",
            "• Consider continuous EEG in ICU patients",
            "",
            "📋 DIFFERENTIAL DIAGNOSIS:",
            "• Toxic/metabolic encephalopathy",
            "• Postictal state",
            "• Psychiatric disorders",
            "• CNS infection",
            "• Structural brain injury"
        ],
        "treatment": [
            "💊 TREATMENT WHILE AWAITING EEG:",
            "• If NCSE strongly suspected: treat similar to convulsive SE",
            "• Consider benzodiazepine first",
            "• Second-line ASMs if benzodiazepine ineffective",
            "",
            "⚠️ TREATMENT DECISIONS:",
            "• Balance risks of untreated NCSE vs medication side effects",
            "• Individualized treatment approach",
            "• Consider underlying etiology"
        ]
    }

    # Emergency complications
    EMERGENCY_COMPLICATIONS = {
        "aspiration_pneumonia": {
            "risk_factors": ["Seizure during eating", "Loss of airway protection"],
            "prevention": ["NPO during seizures", "Airway protection"],
            "treatment": ["Antibiotics", "Respiratory support", "Chest physiotherapy"]
        },
        "cardiac_arrhythmia": {
            "risk_factors": ["Pre-existing heart disease", "Certain ASMs"],
            "prevention": ["Cardiac monitoring", "ECG"],
            "treatment": ["Cardiology consultation", "ASM adjustment"]
        },
        "trauma": {
            "risk_factors": ["Seizure during activity", "Falls", "No supervision"],
            "prevention": ["Safety precautions", "Supervision"],
            "treatment": ["Trauma assessment", "Appropriate imaging"]
        },
        "sudep": {
            "risk_factors": [
                "Uncontrolled GTCS",
                "Nocturnal seizures",
                "Missed doses of ASMs",
                "Sleeping alone",
                "Male gender"
            ],
            "prevention": [
                "Optimize seizure control",
                "Nocturnal supervision",
                "ASM adherence",
                "Seizure alarms"
            ]
        }
    }

    @classmethod
    def get_emergency_protocol(
        cls,
        emergency_type: str,
        patient_factors: Optional[Dict] = None
    ) -> EmergencyProtocol:
        """
        Get appropriate emergency protocol

        Args:
            emergency_type: Type of emergency (first_seizure, convulsive_se, etc.)
            patient_factors: Patient characteristics for protocol customization

        Returns:
            EmergencyProtocol with complete management plan
        """
        if emergency_type == "first_seizure":
            return EmergencyProtocol(
                emergency_type="First Seizure Management",
                severity=EmergencySeverity.ACUTE,
                immediate_actions=cls.FIRST_SEIZURE_PROTOCOL["immediate_assessment"],
                first_line_treatment=["No immediate treatment required"],
                second_line_treatment=[],
                refractory_protocol=[],
                monitoring_requirements=["Vital signs", "Neurological checks", "Blood glucose"],
                escalation_criteria=["Persistent seizures", "Abnormal imaging", "Neurological deficit"],
                complications=["Consider underlying etiology", "Psychological impact"],
                prognosis="Generally good if provoking factor identified and addressed"
            )

        elif emergency_type == "convulsive_se":
            return EmergencyProtocol(
                emergency_type="Convulsive Status Epilepticus",
                severity=EmergencySeverity.LIFE_THREATENING,
                immediate_actions=[
                    "🚨 IMMEDIATE: PROTECT AIRWAY",
                    "• Position in recovery position",
                    "• Suction if needed",
                    "• Administer oxygen",
                    "• Establish IV access",
                    "• Cardiac monitoring",
                    "• Check blood glucose"
                ],
                first_line_treatment=cls.CONVULSIVE_SE_PROTOCOL["first_line"],
                second_line_treatment=cls.CONVULSIVE_SE_PROTOCOL["second_line"],
                refractory_protocol=cls.CONVULSIVE_SE_PROTOCOL["refractory"],
                monitoring_requirements=[
                    "Continuous cardiac monitoring",
                    "Pulse oximetry",
                    "Blood pressure monitoring",
                    "Temperature monitoring",
                    "Neurological checks every 15 minutes",
                    "Consider continuous EEG"
                ],
                escalation_criteria=[
                    "Seizures persist >20 minutes",
                    "Hemodynamic instability",
                    "Respiratory compromise",
                    "Recurrent seizures"
                ],
                complications=[
                    "Aspiration pneumonia",
                    "Cardiac arrhythmias",
                    "Rhabdomyolysis",
                    "Cerebral edema"
                ],
                prognosis="Variable: 70-80% response to first-line, worse with refractory SE"
            )

        elif emergency_type == "non_convulsive_se":
            return EmergencyProtocol(
                emergency_type="Non-Convulsive Status Epilepticus",
                severity=EmergencySeverity.URGENT,
                immediate_actions=[
                    "🧠 URGENT EEG REQUIRED",
                    "• Assess mental status",
                    "• Protect airway if decreased consciousness",
                    "• Establish IV access",
                    "• Cardiac monitoring"
                ],
                first_line_treatment=cls.NON_CONVULSIVE_SE_PROTOCOL["treatment"],
                second_line_treatment=[],
                refractory_protocol=[],
                monitoring_requirements=[
                    "Continuous EEG",
                    "Neurological assessment",
                    "Vital signs monitoring",
                    "Mental status monitoring"
                ],
                escalation_criteria=[
                    "Worsening mental status",
                    "New epileptiform discharges",
                    "No improvement with treatment"
                ],
                complications=[
                    "Prolonged encephalopathy",
                    "Neuronal injury",
                    "Systemic complications from prolonged decreased consciousness"
                ],
                prognosis="Good with prompt treatment, poor if diagnosis delayed"
            )

        elif emergency_type == "refractory_se":
            return EmergencyProtocol(
                emergency_type="Refractory Status Epilepticus",
                severity=EmergencySeverity.LIFE_THREATENING,
                immediate_actions=[
                    "🏥 IMMEDIATE ICU ADMISSION",
                    "• Airway protection (often intubated)",
                    "• Hemodynamic support",
                    "• Continuous EEG monitoring",
                    "• Involve neurocritical care team"
                ],
                first_line_treatment=[],
                second_line_treatment=[],
                refractory_protocol=cls.CONVULSIVE_SE_PROTOCOL["refractory"],
                monitoring_requirements=[
                    "Continuous EEG",
                    "ICU standard monitoring",
                    "Hemodynamic monitoring",
                    "Intracranial pressure monitoring if indicated",
                    "Laboratory monitoring (drug levels, electrolytes)"
                ],
                escalation_criteria=[
                    "Seizures persist >24 hours (super-refractory)",
                    "Hemodynamic instability",
                    "Raised intracranial pressure",
                    "Multiorgan failure"
                ],
                complications=[
                    "Cerebral edema",
                    "Multiorgan failure",
                    "Permanent neurological injury",
                    "Death (mortality 20-30%)"
                ],
                prognosis="Poor: 20-30% mortality, 40-60% have good outcome with aggressive treatment"
            )

        else:
            # Generic emergency protocol
            return EmergencyProtocol(
                emergency_type="Acute Seizure Management",
                severity=EmergencySeverity.URGENT,
                immediate_actions=["Protect from injury", "ABC assessment", "Establish monitoring"],
                first_line_treatment=["Treat per status epilepticus protocol if seizure >5 minutes"],
                second_line_treatment=[],
                refractory_protocol=[],
                monitoring_requirements=["Continuous observation", "Vital signs"],
                escalation_criteria=["Seizure recurrence", "Respiratory compromise"],
                complications=["Trauma", "Aspiration"],
                prognosis="Variable depending on etiology and response to treatment"
            )

    @classmethod
    def get_rescue_medication_guidance(cls) -> List[str]:
        """Get rescue medication guidance for patients and caregivers"""
        return [
            "💊 RESCUE MEDICATION GUIDANCE:",
            "",
            "🎯 INDICATIONS:",
            "• Seizure clusters (≥2 in 24 hours)",
            "• Prolonged seizure (>5 minutes)",
            "• History of status epilepticus",
            "• Travel/remote areas",
            "",
            "🚑 BUCAL MIDAZOLAM (FIRST LINE):",
            "• Adults: 10 mg buccal",
            "• Children: 0.2-0.3 mg/kg buccal",
            "• Can be administered by caregivers",
            "• Action within 5-10 minutes",
            "",
            "🚑 RECTAL DIAZEPAM (ALTERNATIVE):",
            "• Adults: 10-20 mg rectal",
            "• Children: 0.5 mg/kg rectal",
            "• Alternative if buccal not available",
            "",
            "⚠️ EMERGENCY PROTOCOL:",
            "• Administer rescue medication immediately",
            "• If seizure persists 5 min after rescue: CALL EMERGENCY (999/911)",
            "• Record administration and response",
            "• Seek medical evaluation after rescue",
            "",
            "📋 CAREGIVER EDUCATION:",
            "• Proper administration technique",
            "• Recognition of seizure emergencies",
            "• When to call emergency services",
            "• Documentation of events"
        ]

    @classmethod
    def get_postictal_care_guidance(cls) -> List[str]:
        """Get postictal care recommendations"""
        return [
            "🛏️ POSTICTAL CARE PROTOCOL:",
            "",
            "IMMEDIATE CARE:",
            "• Position in recovery position",
            "• Airway protection",
            "• Oxygen if hypoxic",
            "• Monitor vital signs",
            "• Protect from injury",
            "",
            "OBSERVATION:",
            "• Monitor neurological status",
            "• Check for postictal deficit (Todd's paralysis)",
            "• Assess for trauma",
            "• Monitor for complications",
            "",
            "RECOVERY:",
            "• Allow rest and recovery",
            "• Emotional support",
            "• Document event details",
            "• Consider ASM levels if on therapy",
            "",
            "⚠️ WARNING SIGNS:",
            "• Prolonged confusion (>1 hour)",
            "• Neurological deficit",
            "• Respiratory distress",
            "• Persistent vomiting",
            "• Severe headache",
            "",
            "If any warning signs: SEEK IMMEDIATE MEDICAL ATTENTION"
        ]

    @classmethod
    def get_emergency_preparedness(cls) -> List[str]:
        """Get emergency preparedness recommendations for epilepsy patients"""
        return [
            "🆘 EMERGENCY PREPAREDNESS FOR EPILEPSY PATIENTS:",
            "",
            "👨‍👑 CAREGIVER EDUCATION:",
            "• Seizure first aid training",
            "• Rescue medication administration",
            "• Emergency recognition",
            "• CPR training (if appropriate)",
            "",
            "📋 SEIZURE ACTION PLAN:",
            "• Written emergency protocols",
            "• Rescue medication prescriptions",
            "• Emergency contact numbers",
            "• Hospital preference information",
            "",
            "💊 MEDICATION PREPAREDNESS:",
            "• Rescue medication available",
            "• Check medication expiry dates",
            "• Ensure proper storage",
            "• Backup supply",
            "",
            "🏥 EMERGENCY SERVICES:",
            "• Know local emergency numbers (999/911)",
            "• Have hospital information",
            "• Share seizure diagnosis with emergency services",
            "• Consider medical alert bracelet",
            "",
            "📱 TECHNOLOGY:",
            "• Seizure detection devices (if appropriate)",
            "• GPS tracking for wandering risk",
            "• Emergency communication apps",
            "",
            "💛 QUALITY OF LIFE:",
            "• Balance safety with independence",
            "• Psychological support for patient and family",
            "• Support groups"
        ]


class PostictalCare:
    """
    Postictal care and recovery management

    Evidence-based postictal care protocols and complication
    prevention strategies.
    """

    POSTICTAL_COMPPLICATIONS = {
        "todds_paresis": {
            "description": "Transient postictal weakness",
            "duration": "Minutes to hours (rarely days)",
            "treatment": "Observation, reassurance",
            "prognosis": "Complete recovery expected"
        },
        "postictal_psychosis": {
            "description": "Postictal psychotic symptoms",
            "duration": "Hours to days",
            "treatment": "Low-dose antipsychotics if needed",
            "prognosis": "Self-limiting, recurrent in 25%"
        },
        "postictal_headache": {
            "description": "Migraine-like headache post-seizure",
            "treatment": "Analgesics, rest",
            "prevention": "Optimize seizure control"
        },
        "muscle_pain": {
            "description": "Postictal myalgia from convulsions",
            "treatment": "Analgesics, rest",
            "duration": "Hours to days"
        }
    }

    @classmethod
    def assess_postictal_state(cls, clinical_features: Dict) -> List[str]:
        """Assess postictal complications and provide care guidance"""
        features = clinical_features.get("postictal_features", "").lower()
        assessment = []

        if "weakness" in features or "pare" in features:
            assessment.extend([
                "💪 TODD'S PARALYSIS:",
                "• Transient postictal weakness",
                "• Recovery expected (hours to days)",
                "• Rule out stroke if persistent",
                "• Reassurance and observation"
            ])

        if "confused" in features or "psychosis" in features:
            assessment.extend([
                "🔮 POSTICTAL PSYCHOSIS:",
                "• May last hours to days",
                "• Low-dose antipsychotics if needed",
                "• Protect from harm",
                "• Monitor for resolution"
            ])

        if "headache" in features:
            assessment.extend([
                "🤕 POSTICTAL HEADACHE:",
                "• Migraine-like headache common",
                "• Analgesics as needed",
                "• Rest in quiet environment"
            ])

        return assessment if assessment else ["✓ Normal postictal recovery"]


__all__ = [
    'StatusType',
    'EmergencySeverity',
    'EmergencyProtocol',
    'EmergencyEpilepsyCare',
    'PostictalCare'
]