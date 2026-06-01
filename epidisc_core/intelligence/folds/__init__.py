"""
Three-Fold Intelligence Architecture
=====================================

Process-Substrate Intelligence organized as three folds:
1. Self-Teaching: Adaptive learning and reflection
2. Self-Organizing: Systemic coherence and equilibrium
3. Self-Distributing: Collective coordination and emergence

Author: EPIDISC Development Team
Version: 1.0.0
"""

from .self_teaching import (
    SelfTeachingIntelligence,
    AdaptiveLearningModule,
    PatternRecognizer,
    ConsultationRecord,
    LearningPattern
)

from .self_organizing import (
    SelfOrganizingIntelligence,
    SystemicCoherenceModule,
    EquilibriumMaintainer,
    ConsistencyChecker,
    KnowledgeInconsistency
)

from .self_distributing import (
    SelfDistributingIntelligence,
    SpecialtyCoordinator,
    ConsensusBuilder,
    MedicalPerspective,
    ConsensusEquilibrium
)

__all__ = [
    # Main Intelligence Folds
    'SelfTeachingIntelligence',
    'SelfOrganizingIntelligence',
    'SelfDistributingIntelligence',

    # Self-Teaching Components
    'AdaptiveLearningModule',
    'PatternRecognizer',
    'ConsultationRecord',
    'LearningPattern',

    # Self-Organizing Components
    'SystemicCoherenceModule',
    'EquilibriumMaintainer',
    'ConsistencyChecker',
    'KnowledgeInconsistency',

    # Self-Distributing Components
    'SpecialtyCoordinator',
    'ConsensusBuilder',
    'MedicalPerspective',
    'ConsensusEquilibrium'
]
