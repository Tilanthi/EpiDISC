"""
Dynamic Consensus Building System
==================================

Implements game-theoretic consensus building for medical second opinions
using Nash equilibrium principles to find win-win solutions rather than
zero-sum compromises.

Author: EPIDISC Development Team
Version: 1.0.0
"""

from .dynamic_equilibrium import (
    DynamicNashEquilibrium,
    GameTheoreticModel,
    MedicalPerspective,
    PerspectiveType,
    ConsensusEquilibrium,
    find_medical_equilibrium
)

__all__ = [
    'DynamicNashEquilibrium',
    'GameTheoreticModel',
    'MedicalPerspective',
    'PerspectiveType',
    'ConsensusEquilibrium',
    'find_medical_equilibrium'
]
