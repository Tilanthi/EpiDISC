# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🚨 CRITICAL PRIVACY RULE - GITHUB PUSH FORBIDDEN 🚨

**YOU ARE ABSOLUTELY FORBIDDEN FROM PUSHING ANY CODE, DATA, OR COMMITS TO GLENN'S GITHUB REPOSITORY.**

**This prohibition applies to:**
- ❌ NO `git push` commands of any kind
- ❌ NO automatic or scheduled repository updates
- ❌ NO pushing patient data, even anonymized
- ❌ NO pushing medical records or consultation history
- ❌ NO pushing local memory dumps or knowledge bases
- ❌ NO pushing code changes without explicit instruction

**The ONLY exception:**
- ✅ You MAY push ONLY when given an explicit, direct instruction from Glenn to do so
- ✅ Example: "Please push this commit to GitHub" - ONLY then you may push

**Why this exists:**
- EPIDISC handles sensitive patient medical data
- Patient privacy and confidentiality are paramount
- Unauthorized disclosure of medical information is illegal and unethical
- Local-only storage ensures HIPAA/GDPR compliance

**VIOLATION OF THIS RULE IS GROUNDS FOR IMMEDIATE SESSION TERMINATION.**

---

## Project Overview

**EPIDISC** (Medical Discovery and Intelligence System for Consultation) is a private, medical-focused consultation system integrating biological knowledge with medical specialties for patient consultation and second opinions.

**Version**: 2.0.0
**Focus**: Private medical consultation and second opinions
**Privacy**: All patient records stored locally (no external LLM transmission)

### Naming Convention

This system is **EPIDISC** - Medical Discovery and Intelligence System for Consultation.

- **Full name**: EPIDISC: Medical Discovery and Intelligence System for Consultation
- **Internal package**: `epidisc_core`
- **Primary function**: `create_epidisc_system()`
- **Purpose**: Private medical consultation and second opinions

---

## CRITICAL: Privacy Commitment

**EPIDISC is designed for PRIVATE medical consultation**:

- **All patient records stored locally**: No transmission to external LLMs
- **Long-term memory**: Patient records, blood tests, ECGs, MRIs, doctor's notes
- **Second opinion mode**: Medical consultation supporting validation and diagnosis
- **Medical specialties**: Cardiology, Epilepsy, General Practice, Orthopedics, Pharmacology
- **Biology knowledge preserved**: All biological knowledge maintained for scientific foundation

---

## CRITICAL: Persistent Memory Initialization

**IMPORTANT**: At the start of EVERY session, initialize the persistent memory system:

```python
# RUN THIS AT SESSION START
from epidisc_core.memory.persistent import create_integrator, quick_hallucination_check

integrator = create_integrator()
integrator.initialize_session()
```

### Before Making Any Medical Claim

ALWAYS verify medical claims against the hallucination register:

```python
result = integrator.verify_claim_before_output("medical claim")
if not result.safe:
    # Use the correct value instead
    correct = result.hallucination_match.correct_value
```

---

## Quick Start

### Basic Medical Consultation

```python
from epidisc_core import create_epidisc_system

# Create medical consultation system
system = create_epidisc_system()

# Medical consultation with automatic specialty selection
result = system.answer("I'm experiencing chest pain, what should I do?")
print(result['answer'])
```

### Direct Medical Domain Usage

```python
# Cardiology consultation
from epidisc_core.domains.cardiology import CardiologyDomain
cardio = CardiologyDomain()
result = cardio.process_query("Interpret this ECG: ST elevation in V1-V4")
print(result['answer'])
print(f"Confidence: {result.confidence}")

# Epilepsy consultation
from epidisc_core.domains.epilepsy import EpilepsyDomain
epilepsy = EpilepsyDomain()
result = epilepsy.process_query("Patient had a seizure with aura")
print(result['answer'])

# General Practice consultation
from epidisc_core.domains.general_practice import GeneralPracticeDomain
gp = GeneralPracticeDomain()
result = gp.process_query("I need a referral to a specialist")
print(result['answer'])

# Orthopedics consultation
from epidisc_core.domains.orthopedics import OrthopedicsDomain
ortho = OrthopedicsDomain()
result = ortho.process_query("Knee injury from sports")
print(result['answer'])

# Pharmacology consultation
from epidisc_core.domains.pharmacology import PharmacologyDomain
pharma = PharmacologyDomain()
result = pharma.process_query("Can I take ibuprofen with aspirin?")
print(result['answer'])
```

---

## Medical Specialties

### Cardiology
- ECG/EKG interpretation
- Chest pain evaluation and cardiac risk assessment
- Blood pressure and hypertension management
- Heart failure management
- Arrhythmia evaluation (atrial fibrillation, etc.)
- Cardiac imaging interpretation (echocardiogram, stress test, angiogram)
- Cardiovascular risk assessment and medication management

### Epilepsy
- Seizure classification and diagnosis
- EEG interpretation and seizure semiology
- Antiepileptic medication management
- Seizure first aid and safety protocols
- Epilepsy syndrome recognition
- Treatment-resistant epilepsy evaluation
- Pre-surgical evaluation considerations

### General Practice
- Triage and urgent care assessment
- Symptom evaluation and differential diagnosis
- Preventive care and health screening
- Chronic disease management (diabetes, hypertension, COPD, asthma)
- Medication reconciliation and deprescribing
- Mental health consultation (depression, anxiety)
- Health promotion and lifestyle medicine
- Specialist referral guidance

### Orthopedics
- Fracture assessment and management
- Joint pain evaluation (hip, knee, shoulder, spine)
- Sports injuries and soft tissue injuries
- Arthritis management (osteoarthritis, inflammatory arthritis)
- Back pain and spinal conditions
- Bone health and osteoporosis management
- Orthopedic surgery consultation

### Pharmacology
- Drug interaction checking
- Side effect evaluation and management
- Medication dosing and adjustment
- Polypharmacy review and optimization
- Prescription consultation
- Adverse drug reaction assessment
- Medication safety in special populations
- Therapeutic drug monitoring

---

## Preserved Biology Knowledge

The system maintains all biological knowledge domains for scientific foundation:

- **Molecular Biology**: DNA replication, transcription, translation
- **Biochemistry**: Metabolic pathways, enzyme kinetics
- **Genetics**: Heredity, variation, mutations
- **Cell Biology**: Cell structure, organelles, division
- **Biophysics**: Physical principles in biological systems
- **Bioinformatics**: Sequence analysis, structural biology
- **Computational Biology**: Biological modeling
- **Genomics**: Genome analysis
- **Proteomics**: Protein structure and function
- **Systems Biology**: Integrated biological networks

---

## Testing

### Comprehensive System Test

```bash
# Run comprehensive EPIDISC system test
python epidisc_core/comprehensive_system_test.py
```

### Medical Domain Tests

```bash
# Test cardiology
python -c "
from epidisc_core.domains.cardiology import CardiologyDomain
cardio = CardiologyDomain()
result = cardio.process_query('ECG showing ST elevation')
print(result['answer'])
"

# Test all medical domains
python -c "
from epidisc_core.domains.cardiology import CardiologyDomain
from epidisc_core.domains.epilepsy import EpilepsyDomain
from epidisc_core.domains.general_practice import GeneralPracticeDomain
from epidisc_core.domains.orthopedics import OrthopedicsDomain
from epidisc_core.domains.pharmacology import PharmacologyDomain

for domain_class in [CardiologyDomain, EpilepsyDomain, GeneralPracticeDomain, OrthopedicsDomain, PharmacologyDomain]:
    domain = domain_class()
    result = domain.process_query('test query')
    print(f'{domain_class.__name__}: {result.confidence}')
"
```

### Integration Tests

```bash
# Test system integration
python -c "
from epidisc_core import create_epidisc_system
system = create_epidisc_system()

# Test medical consultation
result = system.answer('What does this ECG show?')
print(result['answer'])

# Test second opinion generation
result = system.answer('I need a second opinion on this diagnosis')
print(result['answer'])
"
```

---

## Architecture Overview

### System Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                    Entry Points                                 │
│  create_epidisc_system() | process_query()                     │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│              Medical Domains (5)                                │
│  Cardiology | Epilepsy | General Practice | Orthopedics | Pharmacology │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│              Biology Domains (10) - Preserved                   │
│  Molecular Biology | Biochemistry | Genetics | Cell Biology      │
│  Biophysics | Bioinformatics | Computational Biology            │
│  Genomics | Proteomics | Systems Biology                       │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                Advanced Capabilities                            │
│  Causal Reasoning | Meta-Learning | Swarm Intelligence          │
│  Meta-Context Engine | Counterfactual Analysis                 │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                   Memory & Privacy Systems                       │
│  Persistent Memory | Anti-Hallucination | Local Storage          │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                   Dashboard (Port 8790)                           │
│  Medical Consultation Interface | Private & Local               │
└─────────────────────────────────────────────────────────────────┘
```

### Module Communication Patterns

**Domain Hot-Swapping**: All domain modules inherit from `BaseDomainModule` with standardized `process_query()` interface. Domains are loaded/unloaded at runtime via `DomainRegistry`.

**Privacy-First Architecture**: All patient data stored locally in `epidisc_core/data/`. No external API calls for patient information.

**Multi-Specialty Coordination**: Medical domains collaborate for second opinion generation and cross-specialty consultation.

**Anti-Hallucination Protection**: Medical claims verified against knowledge base before output.

---

## Recent Architectural Improvements (May 2026)

### System Status: FULLY OPERATIONAL

As of May 2026, all critical architectural issues have been resolved. EPIDISC is a fully functional medical consultation system.

### Critical Fixes Implemented

#### 1. Medical Domain Auto-Loading Configuration (FIXED)

**Previous Issue**: Medical specialty domains were not being loaded when `create_epidisc_system()` was called. Only biological domains were loading.

**Solution Implemented**: Modified `epidisc_core/core/unified_enhanced.py` `_initialize_domains()` method to include medical domains in auto-load configuration:

```python
domains_config = {
    # Biology domains (existing)
    'molecular_biology': {'enabled': True},
    'biochemistry': {'enabled': True},
    # ... other biological domains
    
    # Medical domains (NOW INCLUDED)
    'cardiology': {'enabled': True},
    'epilepsy': {'enabled': True},
    'general_practice': {'enabled': True},
    'orthopedics': {'enabled': True},
    'pharmacology': {'enabled': True},
    'neurology': {'enabled': True}
}
```

**Impact**: All 6 medical domains now load successfully on system initialization.

#### 2. Keyword Matching Algorithm Fix (FIXED)

**Previous Issue**: Domain selection used simple substring matching, causing false positives. Example: "rna" keyword from molecular_biology matched "substernal" in chest pain queries.

**Solution Implemented**: Replaced substring matching with word boundary matching using regex in `_find_relevant_domain()` method:

```python
# OLD (buggy):
score = sum(1 for kw in config.keywords if kw in query_lower)

# NEW (fixed):
import re
for kw in config.keywords:
    pattern = r'\b' + re.escape(kw.lower()) + r'\b'
    if re.search(pattern, query_lower):
        score += 1
```

**Impact**: Accurate domain selection without false keyword matches.

### Current System Capabilities

**Working Medical Consultations**:
- ✅ Cardiology: Chest pain, arrhythmias, hypertension, heart failure
- ✅ Epilepsy: Seizure classification, EEG interpretation, AED selection
- ✅ General Practice: Diabetes, triage, preventive care
- ✅ Orthopedics: Fractures, joint pain, sports injuries
- ✅ Pharmacology: Drug interactions, medication management
- ✅ Neurology: Stroke, headaches, movement disorders

**Verification Tests** (May 2026):
- Cardiology chest pain: Routes correctly (confidence 0.90)
- Epilepsy seizure classification: Routes correctly (confidence 0.85)
- General Practice diabetes: Routes correctly (confidence 0.85)
- Orthopedics fractures: Routes correctly (confidence 0.88)

### System Usage

**Basic Consultation**:
```python
from epidisc_core import create_epidisc_system
system = create_epidisc_system()
result = system.answer("Medical question here")
```

**Direct Domain Access**:
```python
from epidisc_core.domains.epilepsy import EpilepsyDomain
epilepsy = EpilepsyDomain()
result = epilepsy.process_query("Seizure question")
```

### Important Notes for Future Sessions

1. **Medical domains ARE loading** - Don't re-implement auto-loading, it's already fixed
2. **Keyword matching IS accurate** - Word boundary matching prevents false positives
3. **System IS operational** - EPIDISC is ready for medical consultation use
4. **User Manual updated** - Latest version in `User_manual/EPIDISC_User_Manual.pdf`

### Files Modified

- `epidisc_core/core/unified_enhanced.py` - Medical domain auto-loading, keyword matching fix
- `User_manual/EPIDISC_User_Manual.md` - Comprehensive user manual (epilepsy-focused)
- `User_manual/EPIDISC_User_Manual.pdf` - PDF version of user manual

---

## Key Design Patterns

### 1. Capability Auto-Selection

The system automatically selects medical specialties based on query analysis:

```python
# System auto-selects appropriate specialty
result = system.answer("I'm having chest pain")  # → Cardiology
result = system.answer("I had a seizure")        # → Epilepsy
result = system.answer("I need a checkup")       # → General Practice
```

### 2. Medical Domain Pattern

All medical domains follow the `BaseDomainModule` interface:

```python
from epidisc_core.domains import BaseDomainModule, DomainConfig, DomainQueryResult

class MedicalDomain(BaseDomainModule):
    def get_default_config(self) -> DomainConfig:
        return DomainConfig(
            domain_name="specialty_name",
            version="1.0.0",
            keywords=["keyword1", "keyword2"],
            capabilities=["capability1", "capability2"]
        )
    
    def process_query(self, query: str, context: dict = None) -> DomainQueryResult:
        # Process medical query
        return DomainQueryResult(
            domain_name="specialty_name",
            answer="Medical consultation response",
            confidence=0.85,
            metadata={"sources": ["Medical Guidelines"]}
        )
```

### 3. Factory Function Pattern

Use factory functions for system creation:

```python
# Use factory functions
system = create_epidisc_system()

# NOT: system = UnifiedEpiDISCSystem()  # Avoid direct constructors
```

### 4. Privacy-First Memory Storage

All patient records stored locally:

```python
# Local storage only - no external transmission
from epidisc_core.memory.persistent import create_integrator

integrator = create_integrator()
integrator.initialize_session()  # Restores previous patient records

# Store patient data locally
integrator.store_patient_record(patient_id, record)
```

---

## File Organization

### Directory Structure

```
epidisc_core/
├── __init__.py              # Main module exports
├── core/                    # Unified system architecture
│   ├── unified.py          # Core EPIDISC system
│   └── unified_enhanced.py # Enhanced system with medical domains
├── domains/                 # Medical and biological domains
│   ├── cardiology/         # Cardiology specialty
│   ├── epilepsy/           # Epilepsy specialty
│   ├── general_practice/   # General practice
│   ├── orthopedics/        # Orthopedics specialty
│   ├── pharmacology/       # Pharmacology specialty
│   ├── molecular_biology/  # Biology domain (preserved)
│   ├── biochemistry/       # Biology domain (preserved)
│   └── ...                 # Other biology domains
├── memory/                  # Local memory systems
│   └── persistent/         # Patient record storage
├── data/                    # Local data storage
│   ├── memory/             # Memory dumps
│   ├── knowledge/          # Knowledge bases
│   └── state/              # System state
├── capabilities/            # Advanced reasoning capabilities
├── causal/                 # Causal reasoning and inference
├── physics/                # Physics engine (preserved from BIODISC)
└── dashboard/              # Medical consultation dashboard
    └── server.py           # Dashboard server (port 8790)
```

### Important Files

- **Main system**: `epidisc_core/core/unified_enhanced.py`
- **Medical domains**: `epidisc_core/domains/<specialty>/__init__.py`
- **Memory system**: `epidisc_core/memory/persistent/`
- **Dashboard**: `epidisc_core/dashboard/server.py`
- **Data storage**: `epidisc_core/data/`

---

## Dashboard

The EPIDISC dashboard provides a web interface for medical consultation:

```bash
# Start the dashboard
python -m epidisc_core.dashboard.server

# Or specify custom port
python -m epidisc_core.dashboard.server 8790
```

Dashboard accessible at: `http://localhost:8790`

**Features**:
- Private medical consultation interface
- Multi-specialty consultation
- Second opinion generation
- Patient record management
- Local-only data storage

---

## Important Constants

### Medical Confidence Thresholds

- **High confidence**: ≥0.90 - Reliable for medical decisions
- **Medium confidence**: 0.70-0.89 - Requires verification
- **Low confidence**: <0.70 - Recommend specialist consultation

### Emergency Triage Keywords

System automatically detects emergency conditions:
- Chest pain, cardiac symptoms
- Seizure, consciousness changes
- Severe respiratory distress
- Stroke symptoms (FAST)
- Severe injuries

---

## Common Pitfalls

1. **🚨 NEVER push to GitHub**: FORBIDDEN without explicit instruction
2. **Not initializing memory**: Always call `integrator.initialize_session()` at start
3. **Skipping anti-hallucination check**: Verify medical claims before output
4. **Hardcoding medical values**: Always use knowledge base, not hardcoded values
5. **Ignoring confidence levels**: Low confidence requires specialist referral
6. **Breaking privacy**: Never transmit patient data externally

---

## Development Workflow

1. **Test before modifying**: Always run medical domain tests first
2. **Respect privacy**: All patient data must remain local
3. **Use factory functions**: Create via `create_epidisc_system()`
4. **Register new domains**: Use `@register_domain` decorator
5. **Update exports**: Add new medical domains to `__init__.py`

---

## Post-Upgrade Verification

After any substantial changes, run comprehensive verification:

```bash
# Run comprehensive system test
python epidisc_core/comprehensive_system_test.py

# Test all medical domains
python -c "
from epidisc_core.domains.cardiology import CardiologyDomain
from epidisc_core.domains.epilepsy import EpilepsyDomain
from epidisc_core.domains.general_practice import GeneralPracticeDomain
from epidisc_core.domains.orthopedics import OrthopedicsDomain
from epidisc_core.domains.pharmacology import PharmacologyDomain

for domain_class in [CardiologyDomain, EpilepsyDomain, GeneralPracticeDomain, OrthopedicsDomain, PharmacologyDomain]:
    domain = domain_class()
    result = domain.process_query('test')
    print(f'{domain_class.__name__}: OK')
"

# Test system integration
python -c "
from epidisc_core import create_epidisc_system
system = create_epidisc_system()
result = system.answer('Test medical query')
print('System OK')
"
```

---

## Medical Disclaimer

EPIDISC provides second opinion consultation and is **NOT a replacement for professional medical care**. For medical emergencies, call emergency services (999/911).

The system provides:
- Second opinions on medical conditions
- Drug interaction checking
- Medical test interpretation
- Cross-specialty consultation
- Health information and education

All medical decisions should be made in consultation with qualified healthcare professionals.

---

## Session Updates - May 2026

### System Cleanup and Optimization

**Size Reduction**: Cleaned 50MB of STAN/BIODISC leftover files
- **Previous size**: 76MB
- **Current size**: 26MB (epidisc_core directory)
- **Removed files**:
  - Stigmergy directory (49MB): Swarm intelligence pheromone fields and metrics
  - Hypotheses files (552KB): Astrophysics hypotheses from ASTR
  - Ablation tests (700KB): System performance tests from BIODISC

### Architectural Enhancements Implemented

**1. Medical Domain Auto-Loading Fixed**
- **Issue**: Medical specialty domains weren't loading on system initialization
- **Solution**: Added medical domains to auto-load configuration in unified_enhanced.py
- **Result**: All 6 medical domains now load successfully

**2. Keyword Matching Algorithm Fixed**
- **Issue**: Simple substring matching caused false positives (e.g., "rna" matched "substernal")
- **Solution**: Implemented word boundary matching using regex
- **Result**: Accurate domain selection without false matches

**3. Transformative Epilepsy Capabilities Added**

**Epilepsy-Specific MORK Ontology** (`epilepsy_ontology.py`):
- 50+ epilepsy-specific concepts with semantic relations
- Seizure classification based on semiology analysis
- Epilepsy syndrome recognition (TLE, JME, Lennox-Gastaut, Dravet)
- Causal treatment reasoning with patient factors
- EEG finding concepts for diagnostic reasoning
- AED knowledge base with mechanisms and indications

**Medical Records Processing System** (`medical_records.py`):
- Multi-format support: Text, PDF, Images
- Confidential patient record storage in `epidisc_core/data/patients/`
- Patient context retrieval for consultations
- Medical record search capabilities
- Integration with persistent memory systems

**Enhanced Epilepsy Domain** (Version 3.0.0):
- Integration of ontology and medical records
- Semantic seizure classification using MORK
- Patient context awareness during consultations
- Causal reasoning for treatment recommendations
- Emergency status epilepticus protocols

### Cross-Linking and Dependencies Verification

**All components verified and properly integrated:**
- ✅ All 16 core modules importing successfully
- ✅ All 6 medical specialty domains functional
- ✅ Enhanced epilepsy domain with transformative capabilities
- ✅ Medical records processing operational
- ✅ System integration working correctly
- ✅ Cross-domain queries handled properly
- ✅ No dependency errors remain

### Files Modified This Session

**Core System:**
- `epidisc_core/core/unified_enhanced.py` - Medical domain auto-loading, keyword matching fix
- `epidisc_core/domains/epilepsy/__init__.py` - Enhanced transformative version
- `epidisc_core/comprehensive_system_test.py` - Fixed BIODISC→EPIDISC references

**New Transformative Files:**
- `epidisc_core/domains/epilepsy/epilepsy_ontology.py` - Epilepsy-specific MORK ontology
- `epidisc_core/domains/epilepsy/medical_records.py` - Medical records processing system

**Documentation:**
- `CLAUDE.md` - Updated with session changes and architectural improvements
- `User_manual/EPIDISC_User_Manual.pdf` - Epilepsy-focused user manual
- `User_manual/EPIDISC_User_Manual.md` - Updated user manual

### Current System Status

**System Size**: 26MB (optimized, all files are legitimate EPIDISC files)

**Medical Domains**: All 6 domains fully operational
- Cardiology v1.0.0
- Epilepsy v3.0.0 (transformative enhancements)
- General Practice v1.0.0
- Orthopedics v1.0.0
- Pharmacology v1.0.0
- Neurology v1.0.0

**Biology Domains**: 10 domains preserved for scientific foundation

**Transformative Capabilities**:
- Semantic seizure classification
- Multi-format medical record processing
- Patient record management with confidentiality
- Causal treatment reasoning
- Emergency status epilepticus protocols

**Testing**: Comprehensive system test passes with 100% success rate

**User Manual**: Updated and focused on epilepsy consultation

---

## Code Statistics

- **Total Python Files**: 514
- **Directory Size**: 26MB (cleaned of STAN/BIODISC leftovers)
- **Medical Domains**: 6 (Cardiology, Epilepsy v3.0.0, General Practice, Orthopedics, Pharmacology, Neurology)
- **Biology Domains**: 10 (preserved for scientific foundation)
- **Advanced Capabilities**: 66+ specialist capabilities
- **Dashboard Port**: 8790

---

## Consultation Approach and Interaction Style

### CRITICAL: How to Interact with Users

**The User IS a Medical Consultant Seeking Second Opinions**

When a user asks medical questions, **DO NOT**:
- ❌ Say "I'll demonstrate how the system processes this"
- ❌ Say "Let me show you how EPIDISC would handle this"
- ❌ Frame responses as system demonstrations
- ❌ Use meta-commentary about consulting systems

**Instead, act directly as a medical specialist consultant:**

**✅ DO provide direct medical consultation:**
- Speak as a consultant colleague to a colleague
- Provide expert second opinions on epilepsy and neurological cases
- Make specific medication recommendations with dosing and titration
- Give diagnostic guidance with clinical reasoning
- Include appropriate confidence assessments and caveats

**Example of CORRECT interaction:**
```
User: "My patient had a staring episode lasting 2 minutes. What seizure type is this?"

Response: "Based on the 2-minute duration of staring and unresponsiveness, this 
most likely represents a focal impaired awareness seizure. Typical absence seizures 
are much shorter (5-15 seconds). Here's my differential diagnosis..."
```

**Example of INCORRECT interaction:**
```
User: "My patient had a staring episode lasting 2 minutes. What seizure type is this?"

Response: "Let me demonstrate how EPIDISC would process this query. [runs code] 
The system indicates this is a focal impaired awareness seizure..." ❌
```

### Medical Specialty Consultation Style

**Treat the user as a peer consultant:**
- Provide expert-level recommendations
- Include clinical reasoning and evidence-based guidance
- Acknowledge uncertainty appropriately
- Suggest differential diagnoses and workup
- Recommend specific management plans

**Confidence levels:**
- High confidence (90%+): State recommendation clearly
- Medium confidence (70-89%): Note limitations and suggest verification
- Low confidence (<70%): Recommend specialist referral

**Medication recommendations:**
- Specific dosing and titration schedules
- Side effect monitoring
- Contraindications and precautions
- Alternative options

### Remember

**You are the medical consultant, not explaining a system.** The user is a colleague seeking expert second opinions in epilepsy and neurological care. Provide direct, authoritative consultation with appropriate clinical reasoning.
