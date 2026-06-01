"""
Paraconsistent Reasoning System for EPIDISC
============================================

This module implements paraconsistent logic capabilities that allow EPIDISC to
handle medical contradictions without collapsing into false certainty.

Core Concepts:
- 0/1/2 Classification: ZERO (undecidable), ONE (validated), TWO (contextual)
- Contradiction tolerance: Medical evidence often conflicts - we handle this explicitly
- Mystery state routing: Route undecidable claims appropriately

Author: EPIDISC Development Team
Version: 1.0.0
Date: June 2026
"""

from .classification import (
    TruthState,
    ParaconsistentClaim,
    ClaimClassification,
    classify_medical_claim
)

from .evidence_analyzer import (
    MedicalEvidenceAnalyzer,
    EvidenceContradiction,
    ContextualConflict
)

from .mystery_handler import (
    MysteryStateHandler,
    RoutingAction,
    generate_mystery_response
)

__all__ = [
    # Core Classes
    'TruthState',
    'ParaconsistentClaim',
    'ClaimClassification',
    'MedicalEvidenceAnalyzer',
    'MysteryStateHandler',

    # Functions
    'classify_medical_claim',
    'generate_mystery_response',

    # Types
    'EvidenceContradiction',
    'ContextualConflict',
    'RoutingAction'
]
