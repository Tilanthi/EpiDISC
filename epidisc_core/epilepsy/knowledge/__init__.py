"""
EPIDISC Epilepsy Knowledge Base
================================

Comprehensive epilepsy knowledge system covering all aspects of epileptology
and related neurological specialties for consultant-level clinical reasoning.

Knowledge Domains:
- Core epileptology (ILAE classification, syndromes, treatment)
- Neurophysiology (EEG interpretation, monitoring)
- Neuroradiology (MRI, CT, PET, SPECT interpretation)
- Clinical pharmacology (ASM database, interactions)
- Psychiatry (PNES, comorbidities)
- Sleep medicine (sleep-epilepsy overlap)
- Genetics (channelopathies, testing)
- Internal medicine (systemic seizure etiologies)
- Emergency medicine (status epilepticus)
- Women's health (pregnancy, teratogenicity)
- Geriatric medicine (elderly-specific considerations)
- Neurosurgery (surgical evaluation)
- Social medicine (driving, employment)
- Evidence-based medicine (critical appraisal)
- Continuous learning (literature surveillance)

Version: 1.0.0
Date: 2026-05-31
"""

__version__ = "1.0.0"

# Import main knowledge modules
try:
    from .classification import (
        SeizureClassification,
        EpilepsyClassification,
        ILAEClassification,
        SeizureSemiology,
        ElectroclinicalSyndromes
    )
except ImportError:
    # Will be implemented in Phase 2
    SeizureClassification = None
    EpilepsyClassification = None
    ILAEClassification = None
    SeizureSemiology = None
    ElectroclinicalSyndromes = None

try:
    from .pharmacology import (
        AntiseizureMedications,
        ASMDatabase,
        DrugInteractions,
        SideEffectProfiles,
        TreatmentGuidelines
    )
except ImportError:
    # Will be implemented in Phase 4
    AntiseizureMedications = None
    ASMDatabase = None
    DrugInteractions = None
    SideEffectProfiles = None
    TreatmentGuidelines = None

try:
    from .differential_diagnosis import (
        DifferentialDiagnosisEngine,
        EpilepsyMimics,
        PNESDiagnosis,
        SyncopeDifferentiation,
        MigraineDifferentiation
    )
except ImportError:
    # Will be implemented in Phase 3
    DifferentialDiagnosisEngine = None
    EpilepsyMimics = None
    PNESDiagnosis = None
    SyncopeDifferentiation = None
    MigraineDifferentiation = None

try:
    from .neurophysiology import (
        EEGInterpreter,
        NormalVariants,
        EpileptiformDischarges,
        EEGPatterns
    )
except ImportError:
    # Will be implemented in Phase 3
    EEGInterpreter = None
    NormalVariants = None
    EpileptiformDischarges = None
    EEGPatterns = None

try:
    from .neuroradiology import (
        EpilepsyImagingInterpreter,
        MRIProtocol,
    CommonLesions,
    ImagingFindings
    )
except ImportError:
    # Will be implemented in Phase 3
    EpilepsyImagingInterpreter = None
    MRIProtocol = None
    CommonLesions = None
    ImagingFindings = None

# Knowledge base metadata
EPILEPSY_KNOWLEDGE_VERSION = "1.0.0"
ILAE_CLASSIFICATION_VERSION = "2017"
KNOWLEDGE_LAST_UPDATED = "2026-05-31"

# Core knowledge domains
CORE_DOMAINS = [
    "classification",          # ILAE classification systems
    "syndromes",               # Electroclinical syndromes
    "pharmacology",            # Antiseizure medications
    "differential_diagnosis",  # Epilepsy mimics
    "neurophysiology",         # EEG interpretation
    "neuroradiology",          # Brain imaging
    "genetics",                # Genetic epilepsies
    "psychiatry",              # Psychiatric comorbidities
    "sleep_medicine",          # Sleep-epilepsy overlap
    "emergency",               # Status epilepticus
    "surgery",                 # Surgical evaluation
    "women_health",            # Pregnancy and teratogenicity
    "geriatric",               # Elderly considerations
    "pediatric",               # Childhood epilepsies
    "internal_medicine",       # Systemic etiologies
    "social_medicine"          # Living with epilepsy
]

# Evidence levels for clinical recommendations
EVIDENCE_LEVELS = {
    "A": "Randomized controlled trials or systematic reviews",
    "B": "Cohort studies or case-control studies",
    "C": "Case series or expert consensus",
    "D": "Anecdotal reports or clinical experience"
}

# Guideline sources tracked
GUIDELINE_SOURCES = [
    "ILAE",  # International League Against Epilepsy
    "NICE",  # UK National Institute for Health and Care Excellence
    "AAN",   # American Academy of Neurology
    "AES",   # American Epilepsy Society
    "EAN",   # European Academy of Neurology
    "SIGN"   # Scottish Intercollegiate Guidelines Network
]

# Literature sources for continuous learning
LITERATURE_SOURCES = {
    "primary": [
        "PubMed",
        "PubMed Central (PMC)",
        "Epilepsia",
        "Neurology",
        "Epilepsy & Behavior",
        "Seizure"
    ],
    "preprints": [
        "bioRxiv",
        "medRxiv",
        "arXiv (q-bio)"
    ],
    "guidelines": [
        "ILAE Commission publications",
        "NICE guidelines",
        "AAN practice advisories",
        "AES position statements"
    ]
}

# Core competencies for epilepsy consultation
CONSULTANT_COMPETENCIES = {
    "diagnostic": [
        "Seizure classification",
        "Epilepsy syndrome recognition",
        "EEG interpretation",
        "MRI interpretation",
        "Differential diagnosis",
        "PNES recognition"
    ],
    "therapeutic": [
        "ASM selection",
        "Dose optimization",
        "Polytherapy management",
        "Side effect management",
        "Drug-resistant epilepsy evaluation",
        "Surgical candidacy assessment",
        "Neuromodulation considerations"
    ],
    "comprehensive": [
        "Women's epilepsy care",
        "Psychiatric comorbidity",
        "Genetic counseling",
        "Living with epilepsy guidance",
        "Driving regulations",
        "Quality of life optimization"
    ]
}

__all__ = [
    'EPILEPSY_KNOWLEDGE_VERSION',
    'ILAE_CLASSIFICATION_VERSION',
    'KNOWLEDGE_LAST_UPDATED',
    'CORE_DOMAINS',
    'EVIDENCE_LEVELS',
    'GUIDELINE_SOURCES',
    'LITERATURE_SOURCES',
    'CONSULTANT_COMPETENCIES'
]