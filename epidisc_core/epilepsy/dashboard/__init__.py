"""
EPIDISC Epilepsy Dashboard
=========================

Web-based consultation interface for epilepsy care with
patient records, clinical tools, and information resources.

Components:
- Web interface for epilepsy consultation
- Patient record management (local-only storage)
- Clinical consultation tools
- Knowledge base interface
- Literature updates display

Version: 1.0.0
Last Updated: 2026-05-31
"""

from .app import (
    PatientRecord,
    EpilepsyDashboard,
    create_epilepsy_dashboard,
    start_dashboard
)

__all__ = [
    'PatientRecord',
    'EpilepsyDashboard',
    'create_epilepsy_dashboard',
    'start_dashboard'
]
