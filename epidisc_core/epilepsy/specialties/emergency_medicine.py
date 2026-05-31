"""
EPIDISC Emergency Medicine Module - Status Epilepticus
========================================================

Comprehensive status epilepticus management protocols including
classification, treatment pathways, and emergency interventions.

Based on:
- NICE audit measures for epilepsy (2023)
- European Academy of Neurology (EAN) guidelines (2024)
- American Epilepsy Society (AES) guidelines (2024)
- ILAE status epilepticus task force (2025)

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class SEClassification(Enum):
    """Status epilepticus classification systems"""
    CONVULSIVE_SE = "convulsive_se"           # Tonic-clonic status
    NON_CONVULSIVE_SE = "non_convulsive_se"   # No convulsive movements
    FOCAL_SE = "focal_se"                      # Focal motor status
    REFRACTORY_SE = "refractory_se"            # Failed 2nd-line AED
    SUPER_REFRACTORY_SE = "super_refractory"  # Failed anesthetics, >24h
    MYOCLONIC_SE = "myoclonic_se"             # Myoclonic status


class SETreatmentPhase(Enum):
    """Treatment phases in status epilepticus"""
    PHASE_1_STABILIZATION = "phase_1_stabilization"        # 0-5 min
    PHASE_2_FIRST_LINE = "phase_2_first_line"               # 5-20 min
    PHASE_3_SECOND_LINE = "phase_3_second_line"            # 20-40 min
    PHASE_4_REFRACTORY = "phase_4_refractory"              # 40-60 min
    PHASE_5_SUPER_REFRACTORY = "phase_5_super_refractory"  # >60 min


class EmergencySeverity(Enum):
    """Emergency severity levels for SE"""
    IMMEDIATE_THREAT_TO_LIFE = "immediate_threat"
    HIGH_SEVERITY = "high_severity"
    MODERATE_SEVERITY = "moderate_severity"
    LOW_SEVERITY = "low_severity"


@dataclass
class SEAssessment:
    """
    Complete status epilepticus assessment

    Includes classification, severity, treatment pathway,
    prognostic indicators, and management recommendations.
    """

    se_classification: SEClassification
    severity: EmergencySeverity
    treatment_phase: SETreatmentPhase
    underlying_causes: List[str]
    precipitating_factors: List[str]
    treatment_recommendations: List[str]
    monitoring_requirements: List[str]
    prognostic_indicators: List[str]
    red_flags: List[str]
    confidence: float


class EmergencyMedicineIntegration:
    """
    Comprehensive emergency epilepsy management

    Evidence-based status epilepticus protocols with
    time-critical treatment pathways and prognostication.
    """

    # Status Epilepticus Classification
    SE_DEFINITIONS = {
        SEClassification.CONVULSIVE_SE: {
            "definition": "Continuous or recurrent tonic-clonic seizures lasting >5 minutes",
            "clinical_features": [
                "Bilateral tonic-clonic activity",
                "Loss of consciousness",
                "Autonomic hyperactivity (tachycardia, hypertension)",
                "May have respiratory compromise",
                "Postictal phase absent if continuing"
            ],
            "diagnostic_challenges": [
                "Difficult to assess if ongoing",
                "May mimic nonepileptic status",
                "Need urgent treatment regardless of cause"
            ],
            "mortality_risk": "20-25% if prolonged >60 minutes",
            "treatment_urgency": "IMMEDIATE (within 5 minutes)"
        },
        SEClassification.NON_CONVULSIVE_SE: {
            "definition": "Seizure activity without convulsive movements, altered mental status",
            "clinical_features": [
                "Altered consciousness, confusion",
                "Subtle motor activity (eye movements, facial twitching)",
                "May mimic psychiatric or encephalopathic states",
                "EEG diagnosis required"
            ],
            "diagnostic_challenges": [
                "Often delayed diagnosis",
                "Requires EEG for confirmation",
                "Can be delayed from convulsive SE"
            ],
            "mortality_risk": "Similar to convulsive SE if untreated",
            "treatment_urgency": "HIGH (once diagnosed)"
        },
        SEClassification.FOCAL_SE: {
            "definition": "Continuous focal motor seizure activity",
            "clinical_features": [
                "Repetitive focal motor activity",
                "May be epilepsia partialis continua",
                "Consciousness may be preserved",
                "Often reflects focal lesion"
            ],
            "mortality_risk": "Variable, lower than convulsive",
            "treatment_urgency": "HIGH (prevent secondary generalization)"
        },
        SEClassification.REFRACTORY_SE: {
            "definition": "Failure of second-line AED (usually fosphenytoin/levetiracetam)",
            "clinical_features": [
                "Persistent seizure activity despite first- and second-line",
                "Requires anesthetic agents",
                "ICU admission required",
                "High morbidity and mortality"
            ],
            "treatment_approach": "Anesthetic coma (propofol, midazolam, thiopental)",
            "treatment_urgency": "CRITICAL (ICU-level care)"
        },
        SEClassification.SUPER_REFRACTORY_SE: {
            "definition": "Persistent or recurrent SE >24-48 hours despite anesthetic therapy",
            "clinical_features": [
                "Extremely difficult to control",
                "Multi-organ complications",
                "Very high mortality (>50%)",
                "Consider alternative diagnoses"
            ],
            "treatment_approach": "Combination anesthetics, consider immunotherapy",
            "treatment_urgency": "CRITICAL (consider experimental therapies)"
        }
    }

    # Treatment Pathways by Phase
    TREATMENT_PROTOCOLS = {
        SETreatmentPhase.PHASE_1_STABILIZATION: {
            "time_frame": "0-5 minutes",
            "actions": [
                "**AIRWAY**: Assess airway, give oxygen if hypoxic",
                "**BREATHING**: Monitor respiration, be prepared to assist",
                "**CIRCULATION**: IV access, monitor vital signs",
                "**GLUCOSE**: Check BM, give thiamine + glucose if low",
                "**SAFETY**: Protect from injury, recovery position",
                "**TIME**: Document exact time of seizure onset"
            ],
            "medications": "None yet (stabilization only)",
            "monitoring": [
                "Pulse oximetry",
                "Blood pressure",
                "ECG monitoring if available",
                "Blood glucose"
            ]
        },
        SETreatmentPhase.PHASE_2_FIRST_LINE: {
            "time_frame": "5-20 minutes",
            "actions": [
                "Give first-line benzodiazepine immediately",
                "Document seizure termination time",
                "Prepare second-line treatment",
                "Consider airway intervention if needed"
            ],
            "first_line_options": [
                "**Lorazepam (IV)**: 0.1 mg/kg (max 4 mg) - FIRST LINE",
                "**Buccal midazolam**: 0.5 mg/kg (max 10 mg) - IF IV unavailable",
                "**Rectal diazepam**: 0.5 mg/kg - IF buccal unavailable"
            ],
            "cautions": [
                "Respiratory depression with benzodiazepines",
                "May require airway support",
                "Monitor oxygen saturation closely"
            ],
            "effectiveness": "60-80% terminate with first-line"
        },
        SETreatmentPhase.PHASE_3_SECOND_LINE: {
            "time_frame": "20-40 minutes",
            "actions": [
                "Start second-line AED immediately",
                "Prepare for ICU admission",
                "Consider early intubation if airway compromise",
                "Reassess diagnosis if atypical features"
            ],
            "second_line_options": [
                "**Levetiracetam (IV)**: 60 mg/kg (max 4500 mg) - FIRST CHOICE",
                "**Fosphenytoin (IV)**: 20 mg PE/kg - SECOND CHOICE",
                "**Valproate (IV)**: 40 mg/kg - IF appropriate",
                "**Phenobarbital (IV)**: 15 mg/kg - IF other options unavailable"
            ],
            "cautions": [
                "Levetiracetam: Generally safe, minimal interactions",
                "Fosphenytoin: Cardiac monitoring, hypotension risk",
                "Valproate: Contraindicated in pregnancy, liver disease",
                "Phenobarbital: Respiratory depression, hypotension"
            ],
            "transition_criteria": "Move to refractory protocol if seizures persist"
        },
        SETreatmentPhase.PHASE_4_REFRACTORY: {
            "time_frame": "40-60 minutes",
            "actions": [
                "ICU admission mandatory",
                "Rapid sequence intubation",
                "Anesthetic coma induction",
                "Continuous EEG monitoring",
                "Identify and treat underlying cause"
            ],
            "anesthetic_options": [
                "**Propofol**: 1-3 mg/kg bolus, then infusion",
                "**Midazolam**: 0.2 mg/kg bolus, then infusion",
                "**Thiopental/Pentobarbital**: 3-5 mg/kg bolus, then infusion"
            ],
            "monitoring": [
                "Continuous EEG (burst suppression target)",
                "ICP monitoring if elevated ICP risk",
                "Hemodynamic monitoring",
                "Multimodal monitoring if available"
            ],
            "prognosis": "Mortality increases with each hour of refractory SE"
        },
        SETreatmentPhase.PHASE_5_SUPER_REFRACTORY: {
            "time_frame": ">60 minutes (or >24 hours with anesthetics)",
            "actions": [
                "Re-evaluate diagnosis (could be mimics)",
                "Consider alternative etiologies (autoimmune, infectious)",
                "Trial immunotherapy if autoimmune suspected",
                "Combination anesthetic approaches",
                "Consider experimental therapies"
            ],
            "considerations": [
                "Is this truly epilepsy? (PNES, encephalitis, TTM)",
                "Autoimmune encephalitis? (check anti-NMDA, LGI1, CASPR2)",
                "Infectious encephalitis? (HSV, VZV, etc.)",
                "Metabolic derangement? (electrolytes, organ failure)",
                "Drug toxicity? (all medications reviewed)"
            ],
            "treatment_options": [
                "Combination anesthetics",
                "Immunotherapy (steroids, IVIG, PLEX)",
                "Ketamine infusion (NMDA antagonist)",
                "Therapeutic hypothermia (controversial)",
                "Surgical evaluation if focal"
            ]
        }
    }

    # Common Precipitating Factors
    PRECIPITATING_FACTORS = {
        "medication_factors": [
            "Missed AED doses (most common)",
            "Subtherapeutic AED levels",
            "Recent AED withdrawal",
            "Drug interactions reducing AED levels",
            "Non-adherence to prescribed regimen"
        ],
        "systemic_factors": [
            "Infection (fever, sepsis, meningitis)",
            "Metabolic derangement (electrolyte disturbances)",
            "Hypoglycemia or hyperglycemia",
            "Hepatic or renal failure",
            "Alcohol withdrawal",
            "Sleep deprivation",
            "Stress"
        ],
        "neurological_factors": [
            "Stroke progression",
            "Tumor progression or edema",
            "Head trauma",
            "CNS infection",
            "Progressive underlying epilepsy",
            "Cerebral venous thrombosis"
        ],
        "structural_factors": [
            "New structural lesion",
            "Lesion progression",
            "Post-surgical changes",
            "Cerebral edema"
        ]
    }

    @classmethod
    def assess_status_epilepticus(
        cls,
        clinical_presentation: str,
        duration_minutes: float,
        seizure_history: Dict,
        current_medications: List[str],
        examination_findings: Dict
    ) -> SEAssessment:
        """
        Comprehensive status epilepticus assessment

        Args:
            clinical_presentation: Description of current event
            duration_minutes: Duration of seizure activity
            seizure_history: Known epilepsy diagnosis, previous SE
            current_medications: Current AEDs and other meds
            examination_findings: Physical examination findings

        Returns:
            SEAssessment with complete emergency evaluation
        """
        # Classify SE type
        se_classification = cls._classify_se(clinical_presentation)
        severity = cls._assess_severity(duration_minutes, se_classification)
        treatment_phase = cls._determine_treatment_phase(duration_minutes)

        # Identify precipitating factors
        precipitating_factors = cls._identify_precipitating_factors(
            seizure_history, current_medications, examination_findings
        )

        # Determine underlying causes
        underlying_causes = cls._identify_underlying_causes(
            seizure_history, examination_findings
        )

        # Generate treatment recommendations
        treatment_recommendations = cls._generate_treatment_recommendations(
            se_classification, treatment_phase, duration_minutes
        )

        # Monitoring requirements
        monitoring_requirements = cls._get_monitoring_requirements(
            se_classification, treatment_phase
        )

        # Prognostic indicators
        prognostic_indicators = cls._assess_prognosis(
            duration_minutes, se_classification, underlying_causes
        )

        # Red flags
        red_flags = cls._identify_red_flags(
            clinical_presentation, duration_minutes, examination_findings
        )

        return SEAssessment(
            se_classification=se_classification,
            severity=severity,
            treatment_phase=treatment_phase,
            underlying_causes=underlying_causes,
            precipitating_factors=precipitating_factors,
            treatment_recommendations=treatment_recommendations,
            monitoring_requirements=monitoring_requirements,
            prognostic_indicators=prognostic_indicators,
            red_flags=red_flags,
            confidence=0.90
        )

    @classmethod
    def _classify_se(cls, presentation: str) -> SEClassification:
        """Classify type of status epilepticus"""
        presentation_lower = presentation.lower()

        # Convulsive features
        if any(term in presentation_lower for term in [
            "tonic-clonic", "convulsing", "jerking", "shaking",
            "generalized", "bilateral"
        ]):
            return SEClassification.CONVULSIVE_SE

        # Focal motor features
        elif any(term in presentation_lower for term in [
            "focal motor", "one side", "unilateral", "epilepsia partialis"
        ]):
            return SEClassification.FOCAL_SE

        # Myoclonic features
        elif "myoclonus" in presentation_lower or "myoclonic" in presentation_lower:
            return SEClassification.MYOCLONIC_SE

        # Non-convulsive (altered mental status without convulsions)
        elif any(term in presentation_lower for term in [
            "confused", "disoriented", "altered mental status",
            "stupor", "comatose"
        ]):
            return SEClassification.NON_CONVULSIVE_SE

        # Default
        else:
            return SEClassification.CONVULSIVE_SE  # Most common, safest default

    @classmethod
    def _assess_severity(
        cls,
        duration: float,
        classification: SEClassification
    ) -> EmergencySeverity:
        """Assess emergency severity"""
        # Duration-based severity
        if duration > 60:
            return EmergencySeverity.IMMEDIATE_THREAT_TO_LIFE
        elif duration > 30:
            return EmergencySeverity.HIGH_SEVERITY
        elif duration > 10:
            return EmergencySeverity.MODERATE_SEVERITY
        else:
            return EmergencySeverity.LOW_SEVERITY

    @classmethod
    def _determine_treatment_phase(cls, duration_minutes: float) -> SETreatmentPhase:
        """Determine appropriate treatment phase"""
        if duration_minutes <= 5:
            return SETreatmentPhase.PHASE_1_STABILIZATION
        elif duration_minutes <= 20:
            return SETreatmentPhase.PHASE_2_FIRST_LINE
        elif duration_minutes <= 40:
            return SETreatmentPhase.PHASE_3_SECOND_LINE
        elif duration_minutes <= 60:
            return SETTreatmentPhase.PHASE_4_REFRACTORY
        else:
            return SETreatmentPhase.PHASE_5_SUPER_REFRACTORY

    @classmethod
    def _identify_precipitating_factors(
        cls,
        seizure_history: Dict,
        medications: List[str],
        examination: Dict
    ) -> List[str]:
        """Identify likely precipitating factors"""
        factors = []

        # Medication factors
        if not seizure_history.get("aed_compliance", True):
            factors.append("Missed AED doses")

        if seizure_history.get("recent_aed_change"):
            factors.append("Recent AED change/withdrawal")

        # Systemic factors
        if examination.get("fever"):
            factors.append("Fever (possible infection)")

        if examination.get("hypoglycemia"):
            factors.append("Hypoglycemia")

        # Sleep deprivation
        if seizure_history.get("sleep_deprivation"):
            factors.append("Sleep deprivation")

        # Alcohol
        if seizure_history.get("alcohol_withdrawal"):
            factors.append("Alcohol withdrawal")

        # Stress
        if seizure_history.get("recent_stress"):
            factors.append("Physical/emotional stress")

        return factors if factors else ["Unknown (requires investigation)"]

    @classmethod
    def _identify_underlying_causes(
        cls,
        seizure_history: Dict,
        examination: Dict
    ) -> List[str]:
        """Identify underlying causes"""
        causes = []

        # Known epilepsy
        if seizure_history.get("known_epilepsy"):
            causes.append("Known epilepsy")

            # Additional detail if known etiology
            known_etiology = seizure_history.get("epilepsy_etiology", "")
            if known_etiology:
                causes.append(f"Epilepsy etiology: {known_etiology}")

        else:
            # First presentation SE
            causes.append("First presentation status epilepticus")

            # Consider acute causes
            if examination.get("focal_deficit"):
                causes.append("Possible stroke/structural lesion")

            if examination.get("meningism"):
                causes.append("Possible CNS infection")

            if examination.get("head_trauma"):
                causes.append("Possible traumatic brain injury")

        return causes if causes else ["Under investigation"]

    @classmethod
    def _generate_treatment_recommendations(
        cls,
        classification: SEClassification,
        phase: SETreatmentPhase,
        duration: float
    ) -> List[str]:
        """Generate time-appropriate treatment recommendations"""
        recommendations = []

        # Immediate actions for all
        recommendations.extend([
            "🚨 IMMEDIATE ACTIONS:",
            "- Assess airway, breathing, circulation",
            "- Give oxygen if SpO2 <94%",
            "- IV access (2 large bore if possible)",
            "- Check blood glucose immediately",
            "- Give thiamine + glucose if hypoglycemic",
            "- Protect from injury",
            "- Call for emergency assistance",
            ""
        ])

        # Phase-specific recommendations
        phase_protocols = cls.TREATMENT_PROTOCOLS[phase]

        recommendations.extend([
            f"⏱️ TIME CRITICAL: {phase_protocols['time_frame']} from onset",
            ""
        ])

        # Add treatment actions
        recommendations.extend(phase_protocols['actions'])

        # Add medications if beyond phase 1
        if phase in [SETreatmentPhase.PHASE_2_FIRST_LINE, SETreatmentPhase.PHASE_3_SECOND_LINE]:
            recommendations.append("")
            recommendations.extend(phase_protocols.get('first_line_options' if phase == SETTreatmentPhase.PHASE_2_FIRST_LINE else 'second_line_options', []))

        return recommendations

    @classmethod
    def _get_monitoring_requirements(
        cls,
        classification: SEClassification,
        phase: SETreatmentPhase
    ) -> List[str]:
        """Get monitoring requirements"""
        monitoring = [
            "**Essential Monitoring**:",
            "- Continuous pulse oximetry",
            "- Blood pressure (every 5 min initially)",
            "- Cardiac monitoring (ECG)",
            "- Temperature monitoring",
            "- Blood glucose (hourly initially)",
            ""
        ]

        if phase in [SETreatmentPhase.PHASE_4_REFRACTORY, SETreatmentPhase.PHASE_5_SUPER_REFRACTORY]:
            monitoring.extend([
                "**ICU Monitoring**:",
                "- Continuous EEG monitoring",
                "- Invasive blood pressure monitoring",
                "- Central venous pressure if available",
                "- ICP monitoring if elevated risk",
                "- Arterial blood gases",
                "- Serum AED levels",
                "- Electrolytes (q6-12h)",
                "- Liver and renal function"
            ])

        return monitoring

    @classmethod
    def _assess_prognosis(
        cls,
        duration: float,
        classification: SEClassification,
        underlying_causes: List[str]
    ) -> List[str]:
        """Assess prognostic indicators"""
        indicators = []

        # Duration-based prognosis
        if duration < 30:
            indicators.append("✅ Good prognosis: Early treatment (<30 min)")
        elif duration < 60:
            indicators.append("⚠️ Moderate prognosis: Treatment delay (30-60 min)")
        else:
            indicators.append("🔴 Poor prognosis: Prolonged status (>60 min)")

        # Classification-specific prognosis
        if classification == SEClassification.CONVULSIVE_SE:
            if duration > 60:
                indicators.append("High mortality risk with prolonged convulsive SE")

        elif classification == SEClassification.REFRACTORY_SE:
            indicators.append("Refractory SE: High morbidity and mortality")
            indicators.append("ICU admission required")

        elif classification == SEClassification.SUPER_REFRACTORY_SE:
            indicators.append("Super-refractory: Mortality >50%")
            indicators.append("Consider alternative diagnoses")

        # Underlying cause prognosis
        if "First presentation" in " ".join(underlying_causes):
            indicators.append("First-presentation SE: High mortality if structural cause")

        return indicators if indicators else ["Prognosis dependent on underlying cause"]

    @classmethod
    def _identify_red_flags(
        cls,
        presentation: str,
        duration: float,
        examination: Dict
    ) -> List[str]:
        """Identify red flags requiring urgent attention"""
        red_flags = []

        # Duration red flags
        if duration > 60:
            red_flags.append("🔴 Prolonged SE >60 min: High mortality risk")

        # Examination red flags
        if examination.get("focal_deficit"):
            red_flags.append("🔴 Focal neurological deficit: Possible stroke/structural lesion")

        if examination.get("meningism"):
            red_flags.append("🔴 Meningism: Possible meningitis/encephalitis")

        if examination.get("head_trauma"):
            red_flags.append("🔴 Head trauma: Possible intracranial bleed/injury")

        # Physiological red flags
        if examination.get("hypotension"):
            red_flags.append("🔴 Hypotension: Hemodynamic compromise")

        if examination.get("arrhythmia"):
            red_flags.append("🔴 Arrhythmia: Cardiac monitoring essential")

        return red_flags if red_flags else ["No specific red flags identified"]

    @classmethod
    def get_se_treatment_algorithm(cls) -> List[str]:
        """Get formatted status epilepticus treatment algorithm"""
        return [
            "## STATUS EPILEPTICUS TREATMENT ALGORITHM",
            "",
            "**Definition**:",
            "- Seizure lasting >5 minutes OR",
            "- 3+ seizures without full recovery between",
            "",
            "**⏱️ TIME-CRITICAL PROTOCOL**:",
            "",
            "**0-5 MINUTES (Stabilization)**:",
            "✓ Airway: Assess, give O2 if hypoxic (SpO2 <94%)",
            "✓ Breathing: Monitor, assist if needed",
            "✓ Circulation: IV access, vitals monitoring",
            "✓ Disability: Check BM, give thiamine + glucose if low",
            "✓ Exposure: Remove hazards, protect patient",
            "✓ **Document exact onset time**",
            "",
            "**5-20 MINUTES (First-Line Benzodiazepine)**:",
            "🔵 **Lorazepam (IV)**: 0.1 mg/kg, max 4 mg",
            "🔵 **OR Buccal midazolam**: 0.5 mg/kg, max 10 mg",
            "🔵 **OR Rectal diazepam**: 0.5 mg/kg",
            "",
            "🚨 **Prepare airway equipment**",
            "🚨 **Monitor for respiratory depression**",
            "",
            "**20-40 MINUTES (Second-Line AED)**:",
            "🟢 **Levetiracetam (IV)**: 60 mg/kg, max 4.5 g [FIRST CHOICE]",
            "🟢 **OR Fosphenytoin (IV)**: 20 mg PE/kg",
            "🟢 **OR Valproate (IV)**: 40 mg/kg (if appropriate)",
            "",
            "🚨 **Prepare ICU admission**",
            "🚨 **Consider early intubation**",
            "",
            "**40-60 MINUTES (Refractory SE)**:",
            "🔴 **ICU admission mandatory**",
            "🔴 **Rapid sequence intubation**",
            "🔴 **Anesthetic coma**:",
            "  - Propofol: 1-3 mg/kg, then infusion",
            "  - Midazolam: 0.2 mg/kg, then infusion",
            "  - Thiopental: 3-5 mg/kg, then infusion",
            "",
            "🔴 **Continuous EEG monitoring**",
            "🔴 **Treat underlying cause**",
            "",
            "**>60 MINUTES / >24h ANESTHETICS (Super-Refractory)**:",
            "⚫ **Re-evaluate diagnosis** (mimics, encephalitis)",
            "⚫ **Consider autoimmune encephalitis**",
            "⚫ **Combination anesthetics**",
            "⚫ **Consider immunotherapy**",
            "⚫ **Ketamine, hypothermia (experimental)**",
            "",
            "**⚠️ CRITICAL CONSIDERATIONS**:",
            "",
            "**Medication Factors**:",
            "- Missed AED doses (most common cause)",
            "- Subtherapeutic AED levels",
            "- Recent AED withdrawal/changes",
            "",
            "**Systemic Factors**:",
            "- Infection (fever, sepsis)",
            "- Metabolic derangement",
            "- Alcohol withdrawal",
            "- Sleep deprivation",
            "",
            "**Red Flags**:",
            "- Focal deficit → CT head immediately",
            "- Meningism → Consider LP, antibiotics",
            "- Head trauma → CT head, monitor",
            "",
            "**💊 DRUG DOSING IN EMERGENCY**:",
            "",
            "**Lorazepam**:",
            "- Adults: 0.1 mg/kg IV (max 4 mg)",
            "- Can repeat once in 5-10 min if needed",
            "- CAUTION: Respiratory depression",
            "",
            "**Buccal Midazolam**:",
            "- Adults: 0.5 mg/kg (max 10 mg)",
            "- Use if IV unavailable",
            "- Good for pre-hospital treatment",
            "",
            "**Levetiracetam**:",
            "- Adults: 60 mg/kg IV (max 4.5 g)",
            "- Can be given rapidly",
            "- Generally safe, minimal interactions",
            "",
            "**Fosphenytoin**:",
            "- Adults: 20 mg PE/kg IV",
            "- Cardiac monitoring required",
            "- CAUTION: Hypotension, arrhythmias",
            "",
            "**⚕️ POST-SE MANAGEMENT**:",
            "",
            "- ICU admission for refractory cases",
            "- Identify and treat precipitant",
            "- Review AED regimen",
            "- Consider AED optimization",
            "- Patient education on adherence",
            "- Driving restrictions (variable)",
            "",
            "**Disclaimer**: This is guidance - clinical judgment required."
        ]


__all__ = [
    'SEClassification',
    'SETreatmentPhase',
    'EmergencySeverity',
    'SEAssessment',
    'EmergencyMedicineIntegration'
]
