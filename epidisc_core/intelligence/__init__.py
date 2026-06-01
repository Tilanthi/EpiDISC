"""
Swarm Intelligence: Swarm Systems for V37 Enhanced System

This package provides:
- Digital Pheromone Dynamics: Stigmergic coordination
- LEAPCore Evolution: Evolutionary meta-theory refinement
- Swarm Orchestrator: Agent coordination
- Three-Fold Intelligence: Process-substrate architecture (NEW)

Version: 38.0 (Enhanced with Process-Substrate Intelligence)
"""

from .pheromone_dynamics import (
    DigitalPheromoneField,
    PheromoneType,
    PheromoneDeposit,
    PheromoneFieldConfig
)

from .leapcore_evolution import (
    LEAPCoreEvolution,
    EvolutionConfig,
    Chromosome,
    Gene,
    GeneType,
    FitnessEvaluator,
    V36FitnessEvaluator
)

from .orchestrator import (
    SwarmOrchestrator,
    SwarmAgent,
    ExplorerAgent,
    FalsifierAgent,
    AnalogistAgent,
    EvolverAgent,
    AgentType,
    AgentState,
    AgentConfig,
    AgentMessage
)

# Three-Fold Process-Substrate Intelligence (NEW)
from .process_substrate import (
    ProcessSubstrateIntelligence,
    ProcessSubstrateResponse,
    create_process_substrate_system
)

from .folds.self_teaching import (
    SelfTeachingIntelligence,
    AdaptiveLearningModule,
    PatternRecognizer
)

from .folds.self_organizing import (
    SelfOrganizingIntelligence,
    SystemicCoherenceModule,
    EquilibriumMaintainer
)

from .folds.self_distributing import (
    SelfDistributingIntelligence,
    SpecialtyCoordinator,
    ConsensusBuilder
)

__version__ = "38.0"

__all__ = [
    # Pheromone Dynamics
    'DigitalPheromoneField',
    'PheromoneType',
    'PheromoneDeposit',
    'PheromoneFieldConfig',

    # LEAPCore Evolution
    'LEAPCoreEvolution',
    'EvolutionConfig',
    'Chromosome',
    'Gene',
    'GeneType',
    'FitnessEvaluator',
    'V36FitnessEvaluator',

    # Orchestrator
    'SwarmOrchestrator',
    'SwarmAgent',
    'ExplorerAgent',
    'FalsifierAgent',
    'AnalogistAgent',
    'EvolverAgent',
    'AgentType',
    'AgentState',
    'AgentConfig',
    'AgentMessage',

    # Process-Substrate Intelligence
    'ProcessSubstrateIntelligence',
    'ProcessSubstrateResponse',
    'create_process_substrate_system',

    # Three Folds
    'SelfTeachingIntelligence',
    'SelfOrganizingIntelligence',
    'SelfDistributingIntelligence',

    # Fold Components
    'AdaptiveLearningModule',
    'PatternRecognizer',
    'SystemicCoherenceModule',
    'EquilibriumMaintainer',
    'SpecialtyCoordinator',
    'ConsensusBuilder'
]
