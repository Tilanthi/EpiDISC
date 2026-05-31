"""
EPIDISC Epilepsy Specialties Integration
========================================

Cross-specialty integration modules for comprehensive epilepsy care
including sleep medicine, psychiatry, emergency medicine, and women's health.

Specialties:
- Sleep Medicine: Parasomnia differential, sleep-epilepsy overlap
- Psychiatry: PNES diagnosis, psychiatric comorbidities
- Emergency Medicine: Status epilepticus protocols
- Women's Health: Pregnancy, teratogenicity, hormonal influences
- Internal Medicine: Systemic seizure etiologies
- Geriatric Medicine: Elderly-specific considerations
- Pediatrics: Childhood epilepsy considerations

Version: 1.0.0
Last Updated: 2026-05-31
"""

# Import specialty modules
try:
    from .sleep_medicine import (
        SleepDisorderType,
        ParasomniaType,
        SleepRelatedEpilepsy,
        SleepEpilepsyAssessment,
        SleepMedicineIntegration
    )
except ImportError:
    SleepDisorderType = None
    ParasomniaType = None
    SleepRelatedEpilepsy = None
    SleepEpilepsyAssessment = None
    SleepMedicineIntegration = None

try:
    from .psychiatry_integration import (
        PsychiatricComorbidity,
        PNESType,
        PsychiatricMedicationInteraction,
        PNESAssessment,
        PsychotropicInteractionAssessment,
        PsychiatryIntegration
    )
except ImportError:
    PsychiatricComorbidity = None
    PNESType = None
    PsychiatricMedicationInteraction = None
    PNESAssessment = None
    PsychotropicInteractionAssessment = None
    PsychiatryIntegration = None

try:
    from .emergency_medicine import (
        SEClassification,
        SETreatmentPhase,
        EmergencySeverity,
        SEAssessment,
        EmergencyMedicineIntegration
    )
except ImportError:
    SEClassification = None
    SETreatmentPhase = None
    EmergencySeverity = None
    SEAssessment = None
    EmergencyMedicineIntegration = None

try:
    from .womens_health import (
        PregnancyStage,
        TeratogenicityRisk,
        HormonalInfluence,
        PregnancyRiskAssessment,
        PreConceptionConsultation,
        WomensHealthIntegration
    )
except ImportError:
    PregnancyStage = None
    TeratogenicityRisk = None
    HormonalInfluence = None
    PregnancyRiskAssessment = None
    PreConceptionConsultation = None
    WomensHealthIntegration = None

__all__ = [
    # Sleep medicine
    'SleepDisorderType',
    'ParasomniaType',
    'SleepRelatedEpilepsy',
    'SleepEpilepsyAssessment',
    'SleepMedicineIntegration',
    # Psychiatry
    'PsychiatricComorbidity',
    'PNESType',
    'PsychiatricMedicationInteraction',
    'PNESAssessment',
    'PsychotropicInteractionAssessment',
    'PsychiatryIntegration',
    # Emergency medicine
    'SEClassification',
    'SETreatmentPhase',
    'EmergencySeverity',
    'SEAssessment',
    'EmergencyMedicineIntegration',
    # Women's health
    'PregnancyStage',
    'TeratogenicityRisk',
    'HormonalInfluence',
    'PregnancyRiskAssessment',
    'PreConceptionConsultation',
    'WomensHealthIntegration'
]
