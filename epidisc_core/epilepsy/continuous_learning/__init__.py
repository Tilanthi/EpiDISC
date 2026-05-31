"""
EPIDISC Continuous Learning System
===================================

Automated literature surveillance, knowledge extraction, and
knowledge base updating for continuous learning and maintenance
of clinical knowledge currency.

Components:
- Automation system for literature surveillance
- Knowledge extraction and validation
- Quality control and integration
- Version control and rollback
- Guideline monitoring

Version: 1.0.0
Last Updated: 2026-05-31
"""

from .automation import (
    UpdateFrequency,
    UpdatePriority,
    UpdateStatus,
    KnowledgeUpdate,
    SurveillanceResult,
    ContinuousLearningSystem,
    create_continuous_learning_system
)

__all__ = [
    'UpdateFrequency',
    'UpdatePriority',
    'UpdateStatus',
    'KnowledgeUpdate',
    'SurveillanceResult',
    'ContinuousLearningSystem',
    'create_continuous_learning_system'
]
