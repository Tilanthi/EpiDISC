"""
BIODISC Core Systems (V36-V93)
===============================

Versions:
- V36: Symbolic Causal Reasoning & Meta-Cognitive Scientific Discovery
- V50: Discovery Engine
- V80: Grounded Neural-Symbolic Architecture
- V90-V92: Consciousness, Embodiment, Scientific Discovery
- V93: Recursive Self-Modifying Metacognitive Architecture

Note: V42, V43, V50, V80, V90-V93 modules are optional and may not be available.
"""

import logging

# V50 Discovery Engine (primary system)
try:
    from .v50 import (
        V50DiscoveryEngine,
        V50Config,
        V50Mode,
        V50Result,
        create_v50_standard,
        create_v50_fast,
        create_v50_deep,
        create_v50_discovery,
        create_v50_gpqa
    )
    _V50_AVAILABLE = True
except Exception as e:
    logging.debug(f"V50 import failed (optional): {type(e).__name__}: {e}")
    _V50_AVAILABLE = False

# V80 Grounded Neural-Symbolic Architecture
try:
    from .v80 import (
        V80CompleteSystem, V80Config, V80System,
        create_v80_standard, create_v80_fast, create_v80_deep
    )
    _V80_AVAILABLE = True
except Exception as e:
    logging.debug(f"V80 import failed (optional): {type(e).__name__}: {e}")
    _V80_AVAILABLE = False

# V90 Metacognitive Architecture
try:
    from .v90 import (
        V90CompleteSystem, V90Config, V90MetacognitiveState,
        create_v90_system, create_v90_conscious, create_v90_insightful
    )
    _V90_AVAILABLE = True
except Exception as e:
    logging.debug(f"V90 import failed (optional): {type(e).__name__}: {e}")
    _V90_AVAILABLE = False

# V91 Embodied Social AGI Architecture
try:
    from .v91 import (
        V91CompleteSystem, V91Config, V91MetacognitiveState, AGIReadinessLevel,
        create_v91_system, create_v91_embodied, create_v91_social, create_v91_ethical
    )
    _V91_AVAILABLE = True
except Exception as e:
    logging.debug(f"V91 import failed (optional): {type(e).__name__}: {e}")
    _V91_AVAILABLE = False

# V42 and V43 (optional - may have missing dependencies)
try:
    from .v42 import (
        V42CompleteSystem,
        V42Config,
        V42Mode,
        create_v42_standard,
        create_v42_fast,
        create_v42_deep,
        create_v42_gpqa
    )
    _V42_AVAILABLE = True
except Exception as e:
    logging.debug(f"V42 import failed (optional): {type(e).__name__}: {e}")
    _V42_AVAILABLE = False

try:
    from .v43 import (
        V43CompleteSystem,
        V43Config,
        V43Mode,
        create_v43_standard,
        create_v43_fast,
        create_v43_deep,
        create_v43_gpqa
    )
    _V43_AVAILABLE = True
except Exception as e:
    logging.debug(f"V43 import failed (optional): {type(e).__name__}: {e}")
    _V43_AVAILABLE = False

__all__ = []

# Add V50 exports if available
if _V50_AVAILABLE:
    __all__.extend([
        'V50DiscoveryEngine',
        'V50Config',
        'V50Mode',
        'V50Result',
        'create_v50_standard',
        'create_v50_fast',
        'create_v50_deep',
        'create_v50_discovery',
        'create_v50_gpqa',
    ])

# Add V80 exports if available
if _V80_AVAILABLE:
    __all__.extend([
        'V80CompleteSystem', 'V80Config', 'V80System',
        'create_v80_standard', 'create_v80_fast', 'create_v80_deep'
    ])

# Add V90 exports if available
if _V90_AVAILABLE:
    __all__.extend([
        'V90CompleteSystem', 'V90Config', 'V90MetacognitiveState',
        'create_v90_system', 'create_v90_conscious', 'create_v90_insightful'
    ])

# Add V42 exports if available
if _V42_AVAILABLE:
    __all__.extend([
        'V42CompleteSystem',
        'V42Config',
        'V42Mode',
        'create_v42_standard',
        'create_v42_fast',
        'create_v42_deep',
        'create_v42_gpqa',
    ])

# Add V43 exports if available
if _V43_AVAILABLE:
    __all__.extend([
        'V43CompleteSystem',
        'V43Config',
        'V43Mode',
        'create_v43_standard',
        'create_v43_fast',
        'create_v43_deep',
        'create_v43_gpqa',
    ])

# Add V91 exports if available
if '_V91_AVAILABLE' in globals() and _V91_AVAILABLE:
    __all__.extend([
        'V91CompleteSystem', 'V91Config', 'V91MetacognitiveState', 'AGIReadinessLevel',
        'create_v91_system', 'create_v91_embodied', 'create_v91_social', 'create_v91_ethical'
    ])

