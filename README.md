# EPIDISC: Medical Discovery and Intelligence System for Consultation

EPIDISC is a private, medical-focused consultation system that integrates biological knowledge with medical specialties for patient consultation and second opinions. The system transforms advanced biological research capabilities into a comprehensive medical consultation platform.

## Overview

EPIDISC provides private medical consultation across multiple specialties while maintaining biological knowledge for scientific foundation. The system features:

- **Medical Specialties**: Cardiology, Epilepsy, General Practice, Orthopedics, Pharmacology
- **Biology Knowledge**: Preserved biological domains for scientific foundation
- **Privacy-First**: All patient records stored locally (no external LLM transmission)
- **Second Opinion Mode**: Multi-specialty consultation with uncertainty quantification
- **Long-term Memory**: Persistent storage for blood tests, ECGs, MRIs, doctor's notes

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Tilanthi/EPIDISC.git
cd EpiDISC

# Install dependencies
pip install -e .
```

### Basic Usage

```python
from epidisc_core import create_epidisc_system

# Create medical consultation system
system = create_epidisc_system()

# Medical consultation with automatic specialty selection
result = system.answer("What does this ECG show?")
print(result['answer'])
```

### Direct Domain Usage

```python
from epidisc_core.domains.cardiology import CardiologyDomain

# Create cardiology specialist
cardio = CardiologyDomain()

# Get consultation
result = cardio.process_query("Interpret this ECG: ST elevation in V1-V4")
print(result['answer'])
print(f"Confidence: {result.confidence}")
```

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

## System Architecture

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

## Privacy Commitment

EPIDISC is designed for **PRIVATE medical consultation**:

- ✅ **All patient records stored locally**: No transmission to external LLMs
- ✅ **Long-term memory**: Patient records, blood tests, ECGs, MRIs, doctor's notes
- ✅ **Private consultation mode**: Medical consultation supporting validation
- ✅ **Second opinion generation**: Multi-specialty consultation
- ✅ **No external data transmission**: All processing happens locally

## Dashboard

The EPIDISC dashboard provides a web interface for medical consultation:

```bash
# Start the dashboard
python -m epidisc_core.dashboard.server

# Or specify custom port
python -m epidisc_core.dashboard.server 8790
```

Dashboard accessible at: `http://localhost:8790`

## Memory Systems

### Session Initialization

```python
from epidisc_core.memory.persistent import create_integrator

# Initialize persistent memory (patient records, session history)
integrator = create_integrator()
integrator.initialize_session()
```

### Anti-Hallucination Protection

```python
from epidisc_core.memory.persistent import quick_hallucination_check

# Verify medical claims before output
result = integrator.verify_claim_before_output("medical claim")
if not result.safe:
    # Use correct value instead
    correct = result.hallucination_match.correct_value
```

## Testing

### Comprehensive System Test

```bash
# Run comprehensive system test
python epidisc_core/comprehensive_system_test.py
```

### Medical Domain Tests

```bash
# Run specialist capability tests
python epidisc_core/tests/test_specialist_capabilities.py

# Test medical domains directly
python -c "
from epidisc_core.domains.cardiology import CardiologyDomain
cardio = CardiologyDomain()
result = cardio.process_query('Interpret this ECG')
print(result['answer'])
"
```

## Documentation

- **CLAUDE.md**: Project guidance and development instructions
- **epidisc_core/docs/**: API documentation

## Medical Disclaimer

EPIDISC provides second opinion consultation and is **NOT a replacement for professional medical care**. For medical emergencies, call emergency services (999/911).

The system provides:
- Second opinions on medical conditions
- Drug interaction checking
- Medical test interpretation
- Cross-specialty consultation
- Health information and education

All medical decisions should be made in consultation with qualified healthcare professionals.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use EPIDISC in your research, please cite:

```bibtex
@software{epidisc2026,
  title={EPIDISC: Medical Discovery and Intelligence System for Consultation},
  author={Tilanthi},
  year={2026},
  url={https://github.com/Tilanthi/EPIDISC}
}
```

## Acknowledgments

EPIDISC builds upon the BIODISC biology discovery framework and integrates research in causal inference, meta-learning, and AGI architectures. Special thanks to the medical community for domain expertise and clinical guidance.
