"""
Paraconsistent Classification System
===================================

Implements the 0/1/2 paraconsistent truth state classification for medical claims.

Truth States:
- 0 (ZERO): Undecidable/Contradictory - Route to mystery state
- 1 (ONE): Validated/Confirmed - Strong evidence support
- 2 (TWO): Contextually Valid - Perspective-dependent validity
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime


class TruthState(Enum):
    """Paraconsistent truth states for medical claims"""
    ZERO = 0  # Undecidable/Contradictory - Route to mystery state
    ONE = 1   # Validated/Confirmed - Strong evidence support
    TWO = 2   # Contextually Valid - Perspective-dependent validity

    def __str__(self):
        return f"State-{self.value}"

    def is_uncertain(self) -> bool:
        """Check if state represents uncertainty"""
        return self == TruthState.ZERO

    def is_validated(self) -> bool:
        """Check if state is validated"""
        return self == TruthState.ONE

    def is_contextual(self) -> bool:
        """Check if state is contextually valid"""
        return self == TruthState.TWO


@dataclass
class ParaconsistentClaim:
    """
    A medical claim with paraconsistent classification.

    Attributes:
        claim: The medical claim or recommendation
        state: Paraconsistent truth state (0/1/2)
        confidence: Confidence level (0.0-1.0)
        evidence_sources: List of evidence sources supporting classification
        contradictions: List of identified contradictions (for state 0)
        valid_contexts: List of contexts where claim is valid (for state 2)
        synthesis: Synthesis of evidence when contradictions exist
        routing_action: Recommended action for undecidable claims
        timestamp: When classification was made
        metadata: Additional information about the claim
    """
    claim: str
    state: TruthState
    confidence: float
    evidence_sources: List[str] = field(default_factory=list)
    contradictions: List[str] = field(default_factory=list)
    valid_contexts: List[str] = field(default_factory=list)
    synthesis: Optional[str] = None
    routing_action: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def is_contradictory(self) -> bool:
        """Check if claim has identified contradictions"""
        return self.state == TruthState.ZERO and len(self.contradictions) > 0

    def requires_clinical_judgment(self) -> bool:
        """Check if claim requires clinical judgment"""
        return self.state == TruthState.ZERO

    def is_perspective_dependent(self) -> bool:
        """Check if claim validity depends on perspective/context"""
        return self.state == TruthState.TWO

    def get_summary(self) -> str:
        """Get a summary of the paraconsistent claim"""
        summary = f"Claim: {self.claim}\n"
        summary += f"State: {self.state.value} ({self._get_state_description()})\n"
        summary += f"Confidence: {self.confidence:.2f}\n"

        if self.is_contradictory():
            summary += f"\nContradictions Found:\n"
            for contradiction in self.contradictions:
                summary += f"  - {contradiction}\n"
            if self.synthesis:
                summary += f"\nSynthesis: {self.synthesis}\n"
            if self.routing_action:
                summary += f"Routing: {self.routing_action}\n"

        elif self.is_perspective_dependent():
            summary += f"\nValid Contexts:\n"
            for context in self.valid_contexts:
                summary += f"  - {context}\n"

        return summary

    def _get_state_description(self) -> str:
        """Get human-readable state description"""
        descriptions = {
            TruthState.ZERO: "Undecidable - Clinical judgment required",
            TruthState.ONE: "Validated - Strong evidence support",
            TruthState.TWO: "Contextual - Valid in specific contexts"
        }
        return descriptions.get(self.state, "Unknown state")


@dataclass
class ClaimClassification:
    """
    Result of classifying a medical claim with paraconsistent logic.

    Attributes:
        claim: The classified medical claim
        classification_reason: Explanation of why this classification was made
        confidence_breakdown: Detailed breakdown of confidence assessment
        recommendations: Specific recommendations based on classification
        alternative_perspectives: Alternative valid perspectives (for state 2)
    """
    claim: ParaconsistentClaim
    classification_reason: str
    confidence_breakdown: Dict[str, float] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)
    alternative_perspectives: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization"""
        return {
            'claim': self.claim.claim,
            'state': self.claim.state.value,
            'confidence': self.claim.confidence,
            'reason': self.classification_reason,
            'contradictions': self.claim.contradictions,
            'valid_contexts': self.claim.valid_contexts,
            'synthesis': self.claim.synthesis,
            'routing_action': self.claim.routing_action,
            'recommendations': self.recommendations,
            'alternative_perspectives': self.alternative_perspectives
        }


def classify_medical_claim(
    claim: str,
    evidence: List[Dict],
    context: Optional[Dict] = None
) -> ClaimClassification:
    """
    Classify a medical claim using paraconsistent logic.

    Args:
        claim: The medical claim to classify
        evidence: List of evidence dictionaries with 'source', 'conclusion', 'quality'
        context: Optional context information (patient factors, etc.)

    Returns:
        ClaimClassification with paraconsistent analysis
    """
    from .evidence_analyzer import MedicalEvidenceAnalyzer

    analyzer = MedicalEvidenceAnalyzer()
    result = analyzer.analyze_claim_consistency(claim, evidence, context)

    # Generate recommendations based on state
    recommendations = []
    if result.state == TruthState.ZERO:
        recommendations.append("Requires specialist consultation")
        recommendations.append("Present multiple perspectives to patient")
        recommendations.append("Monitor for guideline updates")
    elif result.state == TruthState.TWO:
        recommendations.append("Consider patient-specific factors")
        recommendations.append("Context-dependent recommendation")
        for valid_context in result.valid_contexts:
            recommendations.append(f"Valid for: {valid_context}")
    else:  # TruthState.ONE
        recommendations.append("Strong evidence support")
        recommendations.append("Can be implemented with confidence")

    return ClaimClassification(
        claim=result,
        classification_reason=_generate_classification_reason(result),
        confidence_breakdown=_generate_confidence_breakdown(result, evidence),
        recommendations=recommendations
    )


def _generate_classification_reason(claim: ParaconsistentClaim) -> str:
    """Generate human-readable explanation of classification"""
    if claim.state == TruthState.ZERO:
        if claim.contradictions:
            return f"Contradictory evidence from {len(claim.contradictions)} sources requires clinical judgment"
        return "Insufficient evidence for definitive conclusion"
    elif claim.state == TruthState.TWO:
        return f"Claim valid in {len(claim.valid_contexts)} specific contexts but not universally"
    else:
        return f"Strong evidence support from {len(claim.evidence_sources)} sources"


def _generate_confidence_breakdown(
    claim: ParaconsistentClaim,
    evidence: List[Dict]
) -> Dict[str, float]:
    """Generate detailed confidence assessment"""
    breakdown = {
        'evidence_quality': 0.0,
        'source_count': len(evidence),
        'contradiction_penalty': 0.0,
        'context_adjustment': 0.0
    }

    # Calculate evidence quality score
    if evidence:
        quality_scores = [e.get('quality', 0.5) for e in evidence]
        breakdown['evidence_quality'] = sum(quality_scores) / len(quality_scores)

    # Apply contradiction penalty
    if claim.state == TruthState.ZERO:
        breakdown['contradiction_penalty'] = 0.3 * len(claim.contradictions)

    # Context adjustment for contextual claims
    if claim.state == TruthState.TWO:
        breakdown['context_adjustment'] = 0.1

    return breakdown
