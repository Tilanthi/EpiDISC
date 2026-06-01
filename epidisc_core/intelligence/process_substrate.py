"""
Process-Substrate Intelligence System
=====================================

Unified intelligence system that integrates the three folds:
1. Self-Teaching: Adaptive learning and reflection
2. Self-Organizing: Systemic coherence and equilibrium
3. Self-Distributing: Collective coordination and emergence

This represents intelligence as process-substrate - the fundamental
organizing activity from which mind, consciousness, and matter unfold.

Author: EPIDISC Development Team
Version: 1.0.0
Date: June 2026
"""

from typing import Dict, Optional, Any, List
from dataclasses import dataclass, field
from datetime import datetime

from .folds.self_teaching import SelfTeachingIntelligence
from .folds.self_organizing import SelfOrganizingIntelligence
from .folds.self_distributing import SelfDistributingIntelligence

from ..paraconsistent.classification import ParaconsistentClaim, TruthState
from ..paraconsistent.evidence_analyzer import MedicalEvidenceAnalyzer
from ..paraconsistent.mystery_handler import MysteryStateHandler


@dataclass
class ProcessSubstrateResponse:
    """
    Response from the process-substrate intelligence system.

    Contains not just the answer, but meta-analysis of how the three
    folds contributed to the response.
    """
    primary_recommendation: str
    contributing_folds: Dict[str, Any]  # How each fold contributed
    meta_analysis: str  # Overall meta-analysis
    wisdom_score: float  # 0.0-1.0
    confidence: float  # 0.0-1.0
    paraconsistent_analysis: Optional[ParaconsistentClaim] = None
    fold_contributions: Dict[str, str] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    requires_specialist: bool = False
    requires_clinical_judgment: bool = False

    def get_summary(self) -> str:
        """Get summary of the process-substrate response"""
        summary = f"Recommendation: {self.primary_recommendation}\n"
        summary += f"Confidence: {self.confidence:.2f}\n"
        summary += f"Wisdom Score: {self.wisdom_score:.2f}\n"
        summary += f"\nFold Contributions:\n"
        for fold, contribution in self.fold_contributions.items():
            summary += f"- {fold}: {contribution}\n"

        if self.requires_specialist:
            summary += "\n⚠️ Requires specialist consultation\n"

        if self.requires_clinical_judgment:
            summary += "ℹ️  Requires individual clinical judgment\n"

        return summary


class ProcessSubstrateIntelligence:
    """
    Three-fold intelligence as unified process-substrate.

    This system represents intelligence as the organizing activity that is
    simultaneously self-teaching, self-organizing, and self-distributing.

    All three folds contribute to every response, creating a more complete
    and wise medical intelligence than any single fold could provide.
    """

    def __init__(self):
        # Initialize the three folds
        self.self_teaching = SelfTeachingIntelligence()
        self.self_organizing = SelfOrganizingIntelligence()
        self.self_distributing = SelfDistributingIntelligence()

        # Initialize paraconsistent components
        self.evidence_analyzer = MedicalEvidenceAnalyzer()
        self.mystery_handler = MysteryStateHandler()

        # System metadata
        self.consultation_count = 0
        self.last_system_check: Optional[datetime] = None

    def process_query(
        self,
        query: str,
        context: Optional[Dict] = None,
        evidence: Optional[List[Dict]] = None
    ) -> ProcessSubstrateResponse:
        """
        Process query through all three folds.

        This is the main entry point for the process-substrate intelligence
        system. All queries flow through all three folds:
        1. Self-teaching: Initial understanding and learning
        2. Self-organizing: Coherence and equilibrium
        3. Self-distributing: Consensus and coordination
        """

        # Increment consultation counter
        self.consultation_count += 1

        # Build context from query and provided context
        full_context = self._build_context(query, context)

        # Fold 1: Self-teaching - Initial understanding and learning
        teaching_response = self.self_teaching.adapt_to_query(query, full_context)

        # Analyze evidence if provided
        paraconsistent_claim = None
        if evidence:
            paraconsistent_claim = self.evidence_analyzer.analyze_claim_consistency(
                query, evidence, full_context
            )

        # Fold 2: Self-organizing - Ensure systemic coherence
        organized_response = self.self_organizing.assure_coherence(
            teaching_response,
            full_context
        )

        # Fold 3: Self-distributing - Coordinate across perspectives
        distributed_response = self.self_distributing.coordinate_consensus(
            organized_response,
            full_context
        )

        # Generate final response
        response = self._generate_response(
            query,
            teaching_response,
            organized_response,
            distributed_response,
            paraconsistent_claim
        )

        # Learn from this consultation
        self._learn_from_consultation(query, response, full_context)

        return response

    def _build_context(self, query: str, provided_context: Optional[Dict]) -> Dict:
        """Build complete context from query and provided context"""
        context = provided_context.copy() if provided_context else {}
        context['query'] = query
        context['timestamp'] = datetime.now()
        context['consultation_number'] = self.consultation_count
        return context

    def _generate_response(
        self,
        query: str,
        teaching_response: Dict,
        organized_response: Dict,
        distributed_response: Dict,
        paraconsistent_claim: Optional[ParaconsistentClaim]
    ) -> ProcessSubstrateResponse:
        """Generate final response from all three folds"""

        # Extract primary recommendation
        primary = self._extract_primary_recommendation(distributed_response)

        # Calculate wisdom score
        wisdom_score = self._calculate_wisdom_score(
            teaching_response,
            organized_response,
            distributed_response
        )

        # Determine confidence
        confidence = self._calculate_overall_confidence(
            teaching_response,
            organized_response,
            distributed_response,
            paraconsistent_claim
        )

        # Build fold contributions
        fold_contributions = {
            'self_teaching': self._summarize_teaching_contribution(teaching_response),
            'self_organizing': self._summarize_organizing_contribution(organized_response),
            'self_distributing': self._summarize_distributing_contribution(distributed_response)
        }

        # Generate meta-analysis
        meta_analysis = self._generate_meta_analysis(
            teaching_response,
            organized_response,
            distributed_response,
            wisdom_score
        )

        # Check if specialist or clinical judgment required
        requires_specialist = False
        requires_clinical_judgment = False

        if paraconsistent_claim:
            requires_specialist = paraconsistent_claim.routing_action == "specialist_consultation_required"
            requires_clinical_judgment = paraconsistent_claim.routing_action == "clinical_judgment_required"

        return ProcessSubstrateResponse(
            primary_recommendation=primary,
            contributing_folds={
                'teaching': teaching_response,
                'organizing': organized_response,
                'distributing': distributed_response
            },
            meta_analysis=meta_analysis,
            wisdom_score=wisdom_score,
            confidence=confidence,
            paraconsistent_analysis=paraconsistent_claim,
            fold_contributions=fold_contributions,
            requires_specialist=requires_specialist,
            requires_clinical_judgment=requires_clinical_judgment
        )

    def _extract_primary_recommendation(self, distributed_response: Dict) -> str:
        """Extract primary recommendation from distributed response"""
        if distributed_response.get('status') == 'consensus_built':
            consensus = distributed_response.get('consensus')
            if consensus:
                return consensus.primary_recommendation

        return distributed_response.get('recommendation', 'Consultation processed')

    def _calculate_wisdom_score(
        self,
        teaching_response: Dict,
        organized_response: Dict,
        distributed_response: Dict
    ) -> float:
        """Calculate overall wisdom score from three folds"""

        # Wisdom components from each fold
        teaching_wisdom = self._assess_teaching_wisdom(teaching_response)
        organizing_wisdom = self._assess_organizing_wisdom(organized_response)
        distributing_wisdom = self._assess_distributing_wisdom(distributed_response)

        # Weighted average (self-organizing most important for wisdom)
        wisdom_score = (
            teaching_wisdom * 0.25 +
            organizing_wisdom * 0.40 +
            distributing_wisdom * 0.35
        )

        return min(1.0, max(0.0, wisdom_score))

    def _assess_teaching_wisdom(self, teaching_response: Dict) -> float:
        """Assess wisdom contribution from self-teaching fold"""
        # Based on confidence calibration and learning
        adapted_confidence = teaching_response.get('adapted_confidence', 0.7)
        return adapted_confidence * 0.9  # Slight discount for uncertainty

    def _assess_organizing_wisdom(self, organized_response: Dict) -> float:
        """Assess wisdom contribution from self-organizing fold"""
        # Based on systemic coherence and equilibrium
        if 'coherence_score' in organized_response:
            return organized_response['coherence_score']
        return 0.8  # Default if no coherence score available

    def _assess_distributing_wisdom(self, distributed_response: Dict) -> float:
        """Assess wisdom contribution from self-distributing fold"""
        # Based on consensus stability
        if distributed_response.get('status') == 'consensus_built':
            return distributed_response.get('stability', 0.7)
        return 0.7  # Default for individual intelligence

    def _calculate_overall_confidence(
        self,
        teaching_response: Dict,
        organized_response: Dict,
        distributed_response: Dict,
        paraconsistent_claim: Optional[ParaconsistentClaim]
    ) -> float:
        """Calculate overall confidence from all components"""

        # Base confidence from teaching
        base_confidence = teaching_response.get('adapted_confidence', 0.7)

        # Adjust for paraconsistent analysis
        if paraconsistent_claim:
            if paraconsistent_claim.state == TruthState.ZERO:
                base_confidence *= 0.5  # Significant reduction for contradictions
            elif paraconsistent_claim.state == TruthState.TWO:
                base_confidence *= 0.8  # Moderate reduction for contextual claims

        # Adjust for consensus stability
        if distributed_response.get('status') == 'consensus_built':
            stability = distributed_response.get('stability', 0.7)
            base_confidence = (base_confidence + stability) / 2

        return min(1.0, max(0.0, base_confidence))

    def _summarize_teaching_contribution(self, teaching_response: Dict) -> str:
        """Summarize self-teaching fold contribution"""
        patterns = teaching_response.get('relevant_patterns', [])
        if patterns:
            return f"Identified {len(patterns)} relevant learning patterns"
        return "Adaptive learning applied"

    def _summarize_organizing_contribution(self, organized_response: Dict) -> str:
        """Summarize self-organizing fold contribution"""
        if 'coherence_score' in organized_response:
            coherence = organized_response['coherence_score']
            return f"Systemic coherence maintained (score: {coherence:.2f})"
        return "Systemic coherence assured"

    def _summarize_distributing_contribution(self, distributed_response: Dict) -> str:
        """Summarize self-distributing fold contribution"""
        status = distributed_response.get('status', 'unknown')
        if status == 'consensus_built':
            perspectives = distributed_response.get('perspectives_count', 0)
            return f"Multi-specialty consensus from {perspectives} perspectives"
        elif status == 'no_perspectives':
            return "Individual intelligence (no perspectives available)"
        else:
            return "Perspective coordination applied"

    def _generate_meta_analysis(
        self,
        teaching_response: Dict,
        organized_response: Dict,
        distributed_response: Dict,
        wisdom_score: float
    ) -> str:
        """Generate meta-analysis of the response"""

        meta = f"Process-substrate analysis with wisdom score {wisdom_score:.2f}. "

        if wisdom_score >= 0.8:
            meta += "High wisdom: Multiple folds confirm recommendation. "
        elif wisdom_score >= 0.6:
            meta += "Moderate wisdom: Folds show general agreement. "
        else:
            meta += "Lower wisdom: Folds show significant disagreement. "

        # Add fold-specific insights
        if distributed_response.get('status') == 'consensus_built':
            meta += "Multi-specialty consensus provides robust foundation. "
        else:
            meta += "Individual assessment - consider specialist input for confirmation. "

        return meta

    def _learn_from_consultation(
        self,
        query: str,
        response: ProcessSubstrateResponse,
        context: Dict
    ):
        """Learn from consultation to improve future performance"""

        # Record consultation in self-teaching fold
        from .folds.self_teaching import ConsultationRecord

        record = ConsultationRecord(
            query=query,
            response=response.primary_recommendation,
            confidence=response.confidence,
            domain=context.get('domain', 'general'),
            metadata={
                'wisdom_score': response.wisdom_score,
                'fold_contributions': response.fold_contributions
            }
        )

        # Extract learning from consultation
        learning_result = self.self_teaching.learn_from_consultation(record)

        # Periodic reflection every 100 consultations
        if self.consultation_count % 100 == 0:
            reflection = self.self_teaching.reflect_on_performance()
            # Store reflection for analysis

    def get_system_status(self) -> Dict[str, Any]:
        """Get current system status across all three folds"""
        return {
            'consultation_count': self.consultation_count,
            'last_system_check': self.last_system_check,
            'self_teaching': {
                'learning_history_size': len(self.self_teaching.learning_module.learning_history),
                'pattern_count': len(self.self_teaching.pattern_recognizer.pattern_history)
            },
            'self_organizing': {
                'coherence_score': self.self_organizing.get_equilibrium_state().coherence_score,
                'stability_index': self.self_organizing.get_equilibrium_state().stability_index
            },
            'self_distributing': {
                'collective_memory_size': len(self.self_distributing.collective_memory),
                'consensus_count': len(self.self_distributing.consensus_builder.consensus_history)
            }
        }

    def perform_system_maintenance(self) -> Dict[str, Any]:
        """Perform periodic system maintenance across all folds"""
        maintenance_log = {
            'timestamp': datetime.now(),
            'operations': []
        }

        # Self-organizing: Check systemic coherence
        coherence_result = self.self_teaching.reflect_on_performance()
        maintenance_log['operations'].append({
            'fold': 'self_teaching',
            'operation': 'performance_reflection',
            'result': 'completed'
        })

        # Self-organizing: Check systemic coherence
        coherence_check = self.self_organizing.maintain_systemic_coherence()
        maintenance_log['operations'].append({
            'fold': 'self_organizing',
            'operation': 'coherence_check',
            'result': f"coherence_score: {coherence_check.get('coherence_score', 0.0):.2f}"
        })

        # Self-distributing: Analyze collective memory
        collective_stats = self.self_distributing.get_collective_memory_stats()
        maintenance_log['operations'].append({
            'fold': 'self_distributing',
            'operation': 'collective_memory_analysis',
            'result': f"resolutions: {collective_stats['total_resolutions']}"
        })

        self.last_system_check = datetime.now()
        return maintenance_log


def create_process_substrate_system() -> ProcessSubstrateIntelligence:
    """
    Factory function to create process-substrate intelligence system.

    This is the recommended way to create the enhanced EPIDISC system
    with three-fold intelligence architecture.
    """
    return ProcessSubstrateIntelligence()
