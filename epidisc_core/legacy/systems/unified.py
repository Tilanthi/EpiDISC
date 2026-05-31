"""
STAN-CORE: Unified AGI System - All Capabilities Integrated (ASTRO ENHANCED)
==============================================================================

This is the new unified STAN system that automatically integrates ALL capabilities
from versions V36-V94 into a single, optimized system that selects the best
approaches for maximum performance without version dependencies.

**ASTRO ENHANCED VERSION**: This specialized version integrates astrophysics domain
knowledge, training data, and specialized reasoning capabilities for astronomy
and physics applications.

Core Integrated Capabilities:
- Symbolic causal reasoning (V36)
- Swarm intelligence & memory (V37)
- Bayesian inference & tools (V38)
- Advanced reasoning capabilities (V39)
- Formal logic & causal models (V40)
- Self-reflection & analogical reasoning (V41)
- GPQA-optimized scientific reasoning (V42-V50)
- Neural-symbolic integration (V80)
- Metacognitive consciousness (V90)
- Embodied social AGI (V91)
- Scientific discovery (V92)
- Self-modifying architecture (V93)
- Embodied learning (V94)

**ASTRO-SPECIFIC ENHANCEMENTS**:
- Gravitational physics and cosmology reasoning
- ISM (Interstellar Medium) physics expertise
- Radiative transfer and spectroscopic analysis
- Interferometry and observational astronomy
- Multi-wavelength data reconciliation
- Astrophysical simulation and modeling

The system automatically selects optimal capabilities based on the task.
"""

__version__ = "3.1.0-ASTRO"

from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum
import numpy as np
import logging

# Import all capabilities from version-specific modules
try:
    # Core reasoning capabilities (from same directory - core_legacy)
    from .v36 import V36CoreSystem
    from .v37 import V37CompleteSystem
    from .v38 import V38CompleteSystem
    from .v39 import V39CompleteSystem
    from .v40 import V40CompleteSystem
    from .v41 import V41CompleteSystem
    from .v42 import V42CompleteSystem
    from .v80 import V80CompleteSystem
    from .v90 import V90CompleteSystem
    from .v91 import V91CompleteSystem
    from .v92 import V92CompleteSystem
    from .v93 import V93CompleteSystem
    from .v94 import V94CompleteSystem
except Exception as e:
    # Log the error but don't fail - legacy modules are optional for V100
    logging.warning(f"Legacy module import failed: {type(e).__name__}: {e}")
    # Set all to None
    V36CoreSystem = None
    V37CompleteSystem = None
    V38CompleteSystem = None
    V39CompleteSystem = None
    V40CompleteSystem = None
    V41CompleteSystem = None
    V42CompleteSystem = None
    V80CompleteSystem = None
    V90CompleteSystem = None
    V91CompleteSystem = None
    V92CompleteSystem = None
    V93CompleteSystem = None
    V94CompleteSystem = None

# Import memory and intelligence systems
from ..memory import MemoryGraph, MORKOntology, ExpandedMORK
from ..intelligence import SwarmOrchestrator, DigitalPheromoneField
from ..capabilities import (
    BayesianInference, CausalDiscovery, AbductiveInference,
    SelfConsistency, ExternalKnowledge, LLMInference,
    MetaLearning, AnalogicalReasoning, ToolIntegration
)

# BIODISC NOTE: Legacy ASTRA astrophysics imports removed
# The following imports were from the ASTRA (astrophysics) system and are not applicable to BIODISC (biology):
# - AstroSwarmSystem, PhysicsEngine
# - GravitationalLensModel, AstrophysicalConstraints
# - StatisticalEquilibriumSolver
# - BayesianSwarmInference
# These modules do not exist in BIODISC and should not be imported.
ASTRO_CAPABILITIES_AVAILABLE = False  # Always False for BIODISC

class TaskType(Enum):
    """Automatically detected task types for optimal capability selection"""
    SCIENTIFIC_REASONING = "scientific"
    MATHEMATICAL = "mathematical"
    CAUSAL_ANALYSIS = "causal"
    PATTERN_RECOGNITION = "pattern"
    SOCIAL_REASONING = "social"
    CREATIVE_PROBLEM_SOLVING = "creative"
    FORMAL_REASONING = "formal"
    METACOGNITIVE = "metacognitive"
    EMBODIED_TASK = "embodied"
    ETHICAL_REASONING = "ethical"
    COMPLEX_SYSTEM = "complex"
    ARBITRARY = "arbitrary"

    # BIODISC-SPECIFIC TASK TYPES
    MOLECULAR_BIOLOGY = "molecular_biology"
    GENETICS = "genetics"
    CELL_BIOLOGY = "cell_biology"
    BIOCHEMISTRY = "biochemistry"
    BIOPHYSICS = "biophysics"
    BIOINFORMATICS = "bioinformatics"
    EVOLUTIONARY_BIOLOGY = "evolutionary_biology"
    SYSTEMS_BIOLOGY = "systems_biology"
    MICROBIOLOGY = "microbiology"

    # BIODISC NOTE: Legacy ASTRA task types removed (ASTROPHYSICS, COSMOLOGY, etc.)

@dataclass
class UnifiedConfig:
    """Configuration for the unified STAN system"""
    # Capability selection
    auto_optimize: bool = True
    use_all_capabilities: bool = True
    prefer_latest_capabilities: bool = True

    # Performance settings
    max_compute_budget: float = 100.0  # Computational units
    timeout_seconds: float = 300.0
    parallel_reasoning: bool = True

    # Specialized modes
    scientific_mode: bool = False
    mathematical_mode: bool = False
    social_mode: bool = False
    ethical_mode: bool = False
    creative_mode: bool = False

    # Advanced capabilities
    enable_metacognition: bool = True
    enable_consciousness: bool = True
    enable_self_modification: bool = True
    enable_embodied_learning: bool = True
    enable_swarm_intelligence: bool = True
    enable_neural_symbolic: bool = True

    # Knowledge integration
    use_external_knowledge: bool = True
    use_bayesian_inference: bool = True
    use_causal_discovery: bool = True
    use_analogical_reasoning: bool = True

    memory_config: Dict[str, Any] = field(default_factory=dict)
    swarm_config: Dict[str, Any] = field(default_factory=dict)

class TaskAnalyzer:
    """Analyzes tasks to determine optimal capability selection"""

    def __init__(self):
        self.task_keywords = {
            TaskType.SCIENTIFIC_REASONING: [
                'experiment', 'hypothesis', 'scientific', 'research', 'analysis',
                'physics', 'chemistry', 'biology', 'gpqa', 'graduate', 'prove'
            ],
            TaskType.MATHEMATICAL: [
                'mathematics', 'calculate', 'derivative', 'integral', 'equation',
                'prove', 'theorem', 'algebra', 'geometry', 'statistics'
            ],
            TaskType.CAUSAL_ANALYSIS: [
                'cause', 'effect', 'because', 'reason', 'causal', 'impact',
                'influence', 'relationship', 'correlation', 'mechanism'
            ],
            TaskType.PATTERN_RECOGNITION: [
                'pattern', 'recognize', 'identify', 'sequence', 'grid',
                'transform', 'analogous', 'similar', 'recurring'
            ],
            TaskType.SOCIAL_REASONING: [
                'social', 'ethical', 'moral', 'people', 'society', 'interaction',
                'cooperation', 'coordination', 'group', 'team', 'culture'
            ],
            TaskType.CREATIVE_PROBLEM_SOLVING: [
                'creative', 'innovate', 'design', 'imagine', 'invent',
                'novel', 'original', 'breakthrough', 'paradigm'
            ],
            TaskType.FORMAL_REASONING: [
                'formal', 'logic', 'theorem', 'prove', 'deduction', 'induction',
                'syllogism', 'premise', 'conclusion', 'valid'
            ],
            TaskType.METACOGNITIVE: [
                'think', 'reflect', 'conscious', 'aware', 'understand',
                'meta', 'self', 'learning', 'improve', 'optimize'
            ],
            # BIODISC-SPECIFIC TASK KEYWORDS
            TaskType.MOLECULAR_BIOLOGY: [
                'dna', 'rna', 'protein', 'gene', 'transcription', 'translation',
                'replication', 'molecule', 'enzyme', 'promoter', 'operon', 'regulation'
            ],
            TaskType.GENETICS: [
                'genetic', 'genome', 'chromosome', 'mutation', 'inheritance',
                'allele', 'genotype', 'phenotype', 'heredity', 'evolution', 'phylogeny'
            ],
            TaskType.CELL_BIOLOGY: [
                'cell', 'cellular', 'membrane', 'organelle', 'nucleus', 'cytoplasm',
                'division', 'cycle', 'mitosis', 'meiosis', 'septum', 'division'
            ],
            TaskType.BIOCHEMISTRY: [
                'biochemical', 'metabolism', 'pathway', 'reaction', 'catalyst',
                'kinetics', 'binding', 'affinity', 'concentration', 'equilibrium', 'atp'
            ],
            TaskType.BIOPHYSICS: [
                'biophysics', 'physical', 'force', 'mechanics', 'diffusion',
                'entropy', 'energy', 'temperature', 'pressure', 'turgor', 'crowding'
            ],
            TaskType.BIOINFORMATICS: [
                'bioinformatics', 'sequence', 'alignment', 'database', 'algorithm',
                'computational', 'analysis', 'data', 'statistics', 'machine learning'
            ],
            TaskType.EVOLUTIONARY_BIOLOGY: [
                'evolution', 'natural selection', 'adaptation', 'speciation', 'phylogeny',
                'ancestor', 'descendant', 'tree', 'homology', 'convergence', 'diversity'
            ],
            TaskType.SYSTEMS_BIOLOGY: [
                'systems biology', 'network', 'interaction', 'integration', 'modeling',
                'simulation', 'emergent', 'complex', 'dynamics', 'regulation'
            ],
            TaskType.MICROBIOLOGY: [
                'bacteria', 'virus', 'microbe', 'microorganism', 'pathogen',
                'infection', 'immune', 'antibiotic', 'resistance', 'strain', 'culture'
            ],
            # BIODISC NOTE: Legacy ASTRA task keywords removed (ASTROPHYSICS, COSMOLOGY, etc.)
                'ionized', 'neutral', 'star formation', 'turbulence', 'magnetic field'
            ],
            TaskType.MULTI_WAVELENGTH: [
                'multi-wavelength', 'x-ray', 'infrared', 'ultraviolet', 'radio',
                'optical', 'gamma ray', 'observation', 'wavelength', 'band',
                'multi-band', 'cross-correlation', 'combined analysis'
            ]
        }

    def analyze_task(self, query: str, context: str = "") -> TaskType:
        """Analyze task to determine the primary type"""
        query_lower = query.lower() + " " + context.lower()

        # Score each task type
        scores = {}
        for task_type, keywords in self.task_keywords.items():
            score = sum(1 for keyword in keywords if keyword in query_lower)
            scores[task_type] = score

        # Return the highest scoring task type
        if max(scores.values()) == 0:
            return TaskType.ARBITRARY

        return max(scores, key=scores.get)

    def get_capability_requirements(self, task_type: TaskType) -> Dict[str, bool]:
        """Get required capabilities for each task type"""
        requirements = {
            TaskType.SCIENTIFIC_REASONING: {
                'bayesian_inference': True,
                'causal_discovery': True,
                'formal_logic': True,
                'external_knowledge': True,
                'mathematical_intuition': True
            },
            TaskType.MATHEMATICAL: {
                'formal_logic': True,
                'theorem_proving': True,
                'symbolic_reasoning': True,
                'neural_symbolic': True
            },
            TaskType.CAUSAL_ANALYSIS: {
                'causal_discovery': True,
                'bayesian_inference': True,
                'swarm_intelligence': True
            },
            TaskType.PATTERN_RECOGNITION: {
                'neural_symbolic': True,
                'analogical_reasoning': True,
                'swarm_intelligence': True
            },
            TaskType.SOCIAL_REASONING: {
                'embodied_cognition': True,
                'theory_of_mind': True,
                'ethical_reasoning': True,
                'metacognition': True
            },
            TaskType.CREATIVE_PROBLEM_SOLVING: {
                'analogical_reasoning': True,
                'insight_generation': True,
                'self_modification': True,
                'metacognition': True
            },
            TaskType.FORMAL_REASONING: {
                'formal_logic': True,
                'theorem_proving': True,
                'symbolic_reasoning': True
            },
            TaskType.METACOGNITIVE: {
                'metacognition': True,
                'consciousness': True,
                'self_reflection': True,
                'self_modification': True
            },
            TaskType.EMBODIED_TASK: {
                'embodied_cognition': True,
                'sensorimotor_integration': True,
                'common_sense': True
            },
            TaskType.ETHICAL_REASONING: {
                'ethical_reasoning': True,
                'value_alignment': True,
                'theory_of_mind': True
            }
        }

        return requirements.get(task_type, {
            'symbolic_reasoning': True,
            'bayesian_inference': True,
            'metacognition': True
        })

class UnifiedEpiDISCSystem:
    """Unified STAN system with all capabilities integrated"""

    def __init__(self, config: Optional[UnifiedConfig] = None):
        self.config = config or UnifiedConfig()
        self.task_analyzer = TaskAnalyzer()

        # Initialize core systems
        self._initialize_core_systems()
        self._initialize_capabilities()
        self._initialize_memory()
        self._initialize_intelligence()

        # Performance tracking
        self.performance_stats = {
            'tasks_processed': 0,
            'capabilities_used': set(),
            'average_confidence': 0.0,
            'success_rate': 0.0
        }
