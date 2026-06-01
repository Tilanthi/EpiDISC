"""
GRAIL-Style Medical Knowledge Graph
====================================

Global Resolution, Alignment, and Inquiry Library for Medical Evidence.

Implements contradiction-preserving medical knowledge system that maintains
multiple perspectives rather than collapsing into singular narrative.

Key Concepts:
- Contradiction preservation: Keep conflicting evidence visible
- Contextual validity: Track where evidence is valid
- Synthesis generation: Create balanced summaries
- Evidence evolution: Track how knowledge changes over time
"""

from typing import List, Dict, Optional, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict
import hashlib
import json


@dataclass
class MedicalClaim:
    """A medical claim with evidence and contradictions"""
    claim_id: str
    claim_text: str
    domain: str  # Medical domain (epilepsy, cardiology, etc.)
    evidence: List[Dict]  # Supporting evidence
    contradictions: List[str]  # Contradictory claims
    valid_contexts: List[str]  # Where this claim is valid
    temporal_status: str  # "current", "outdated", "evolving"
    last_updated: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, any] = field(default_factory=dict)

    def add_evidence(self, evidence: Dict):
        """Add supporting evidence to this claim"""
        self.evidence.append(evidence)
        self.last_updated = datetime.now()

    def add_contradiction(self, contradiction: str):
        """Add a contradiction to this claim"""
        self.contradictions.append(contradiction)

    def is_current(self) -> bool:
        """Check if this claim is considered current"""
        if self.temporal_status == "outdated":
            return False
        # Check if recently updated
        return (datetime.now() - self.last_updated).days < 365


@dataclass
class ContradictionNode:
    """A node representing a contradiction between claims"""
    contradiction_id: str
    primary_claim: str
    conflicting_claims: List[str]  # Claim IDs
    resolution_status: str  # "unresolved", "partially_resolved", "resolved"
    resolution_notes: Optional[str] = None
    synthesis: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class GRAILQueryResult:
    """Result of querying the GRAIL system"""
    query: str
    relevant_claims: List[MedicalClaim]
    contradictions: List[ContradictionNode]
    synthesis: Optional[str]
    confidence_level: float
    requires_clinical_judgment: bool
    alternative_perspectives: List[str]
    metadata: Dict[str, any] = field(default_factory=dict)


class EvidenceGraph:
    """Graph structure for medical evidence with contradiction awareness"""

    def __init__(self):
        self.claims: Dict[str, MedicalClaim] = {}
        self.contradictions: List[ContradictionNode] = []
        self.domain_index: Dict[str, Set[str]] = defaultdict(set)  # domain -> claim_ids

    def add_claim(self, claim: MedicalClaim):
        """Add a medical claim to the graph"""
        self.claims[claim.claim_id] = claim
        self.domain_index[claim.domain].add(claim.claim_id)

    def find_claims(self, query: str, domain: Optional[str] = None) -> List[MedicalClaim]:
        """Find claims relevant to a query"""
        relevant = []

        query_lower = query.lower()
        keywords = self._extract_keywords(query)

        for claim_id, claim in self.claims.items():
            # Domain filtering
            if domain and claim.domain != domain:
                continue

            # Keyword matching
            claim_text_lower = claim.claim_text.lower()
            if any(keyword.lower() in claim_text_lower for keyword in keywords):
                relevant.append(claim)

        return relevant

    def _extract_keywords(self, text: str) -> List[str]:
        """Extract relevant keywords from text"""
        # Simple keyword extraction - to be enhanced
        words = text.split()
        # Filter out common words
        stopwords = {'the', 'a', 'an', 'is', 'are', 'what', 'how', 'for'}
        return [w for w in words if w.lower() not in stopwords and len(w) > 3]


class ContradictionMapper:
    """Identifies and maps contradictions in medical evidence"""

    def __init__(self):
        self.contradiction_history: List[ContradictionNode] = []

    def find_contradictions(
        self,
        claim: MedicalClaim,
        existing_claims: List[MedicalClaim]
    ) -> List[ContradictionNode]:
        """Find contradictions between a claim and existing claims"""

        contradictions = []

        for existing_claim in existing_claims:
            if self._claims_contradict(claim, existing_claim):
                contradiction = ContradictionNode(
                    contradiction_id=self._generate_contradiction_id(
                        claim.claim_id,
                        existing_claim.claim_id
                    ),
                    primary_claim=claim.claim_id,
                    conflicting_claims=[existing_claim.claim_id],
                    resolution_status="unresolved"
                )
                contradictions.append(contradiction)

        self.contradiction_history.extend(contradictions)
        return contradictions

    def _claims_contradict(self, claim1: MedicalClaim, claim2: MedicalClaim) -> bool:
        """Check if two claims contradict each other"""

        # Direct text contradiction
        text1_lower = claim1.claim_text.lower()
        text2_lower = claim2.claim_text.lower()

        # Look for explicit contradiction indicators
        if 'vs' in text1_lower or 'versus' in text1_lower:
            # Check if they're about the same topic
            if self._same_topic(claim1, claim2):
                return True

        # Semantic contradiction (safe vs unsafe, etc.)
        if self._semantic_contradiction(text1_lower, text2_lower):
            return True

        return False

    def _same_topic(self, claim1: MedicalClaim, claim2: MedicalClaim) -> bool:
        """Check if claims are about the same medical topic"""
        # Simple check: domain overlap
        return claim1.domain == claim2.domain

    def _semantic_contradiction(self, text1: str, text2: str) -> bool:
        """Check for semantic contradiction"""
        # Safe vs unsafe
        if ('safe' in text1 or 'well tolerated' in text1) and \
           ('unsafe' in text2 or 'contra' in text2 or 'dangerous' in text2):
            return True

        # Effective vs ineffective
        if ('effective' in text1 or 'works' in text1) and \
           ('ineffective' in text2 or 'doesn\'t work' in text2 or 'fails' in text2):
            return True

        # Recommend vs avoid
        if ('recommend' in text1 or 'first-line' in text1) and \
           ('avoid' in text2 or 'contra' in text2 or 'not recommended' in text2):
            return True

        return False

    def _generate_contradiction_id(self, claim_id1: str, claim_id2: str) -> str:
        """Generate unique ID for contradiction"""
        combined = f"{claim_id1}_{claim_id2}"
        hash_input = combined.encode()
        return hashlib.sha256(hash_input).hexdigest()[:16]


class SynthesisGenerator:
    """Generates synthesis from contradictory claims"""

    def generate_synthesis(
        self,
        claims: List[MedicalClaim],
        contradictions: List[ContradictionNode]
    ) -> Optional[str]:
        """Generate synthesis that acknowledges contradictions"""

        if not contradictions:
            return "No significant contradictions identified"

        if len(contradictions) == 1:
            return self._single_contradiction_synthesis(contradictions[0], claims)
        else:
            return self._multiple_contradiction_synthesis(contradictions, claims)

    def _single_contradiction_synthesis(
        self,
        contradiction: ContradictionNode,
        claims: List[MedicalClaim]
    ) -> str:
        """Generate synthesis for single contradiction"""

        primary_claim = next((c for c in claims if c.claim_id == contradiction.primary_claim), None)
        conflicting = [c for c in claims if c.claim_id in contradiction.conflicting_claims]

        if not primary_claim or not conflicting:
            return "Unable to generate synthesis - insufficient information"

        synthesis = f"Conflicting evidence exists:\n"
        synthesis += f"- Perspective A: {primary_claim.claim_text}\n"
        for conf in conflicting:
            synthesis += f"- Perspective B: {conf.claim_text}\n"
        synthesis += "\nClinical judgment required to determine appropriate approach."

        return synthesis

    def _multiple_contradiction_synthesis(
        self,
        contradictions: List[ContradictionNode],
        claims: List[MedicalClaim]
    ) -> str:
        """Generate synthesis for multiple contradictions"""

        synthesis = f"Multiple evidence conflicts exist ({len(contradictions)}):\n"

        for i, contradiction in enumerate(contradictions[:3], 1):  # Limit to 3
            synthesis += f"{i}. {contradiction.primary_claim} vs {', '.join(contradiction.conflicting_claims)}\n"

        synthesis += "\nRequires careful clinical consideration and possibly specialist consultation."

        return synthesis


class MedicalGRAIL:
    """
    Global Resolution, Alignment, and Inquiry Library for Medical Evidence.

    Maintains medical knowledge with explicit contradiction preservation.
    Unlike traditional knowledge bases that collapse contradictions, GRAIL
    maintains conflicting perspectives as computable structures.
    """

    def __init__(self):
        self.evidence_graph = EvidenceGraph()
        self.contradiction_mapper = ContradictionMapper()
        self.synthesis_generator = SynthesisGenerator()
        self.query_history: List[GRAILQueryResult] = []

    def add_medical_claim(
        self,
        claim_text: str,
        domain: str,
        evidence: List[Dict],
        metadata: Optional[Dict] = None
    ) -> MedicalClaim:
        """Add a medical claim with evidence to GRAIL system"""

        # Generate unique ID
        claim_id = self._generate_claim_id(claim_text, domain)

        # Check for existing contradictions
        existing_claims = self.evidence_graph.find_claims(claim_text, domain)
        contradictions = self.contradiction_mapper.find_contradictions(
            None,  # Will be created below
            existing_claims
        )

        # Create claim
        claim = MedicalClaim(
            claim_id=claim_id,
            claim_text=claim_text,
            domain=domain,
            evidence=evidence,
            contradictions=[c.contradiction_id for c in contradictions],
            valid_contexts=self._extract_valid_contexts(evidence),
            temporal_status="current",
            metadata=metadata or {}
        )

        # Add to graph
        self.evidence_graph.add_claim(claim)

        # Add contradictions to graph
        for contradiction in contradictions:
            self.evidence_graph.contradictions.append(contradiction)

        return claim

    def query_with_contradictions(
        self,
        query: str,
        domain: Optional[str] = None
    ) -> GRAILQueryResult:
        """Query GRAIL system with contradiction awareness"""

        # Find relevant claims
        relevant_claims = self.evidence_graph.find_claims(query, domain)

        # Identify contradictions among claims
        contradictions = []
        for claim in relevant_claims:
            claim_contradictions = [
                c for c in self.evidence_graph.contradictions
                if c.primary_claim == claim.claim_id or
                claim.claim_id in c.conflicting_claims
            ]
            contradictions.extend(claim_contradictions)

        # Generate synthesis
        synthesis = self.synthesis_generator.generate_synthesis(
            relevant_claims,
            contradictions
        )

        # Calculate confidence
        confidence = self._calculate_confidence(relevant_claims, contradictions)

        return GRAILQueryResult(
            query=query,
            relevant_claims=relevant_claims,
            contradictions=contradictions,
            synthesis=synthesis,
            confidence_level=confidence,
            requires_clinical_judgment=len(contradictions) > 0,
            alternative_perspectives=self._extract_alternative_perspectives(
                relevant_claims,
                contradictions
            ),
            metadata={
                'domain': domain,
                'claims_found': len(relevant_claims),
                'contradictions_found': len(contradictions)
            }
        )

    def _generate_claim_id(self, claim_text: str, domain: str) -> str:
        """Generate unique ID for medical claim"""
        combined = f"{domain}_{claim_text[:50]}"
        hash_input = combined.encode()
        return hashlib.sha256(hash_input).hexdigest()[:16]

    def _extract_valid_contexts(self, evidence: List[Dict]) -> List[str]:
        """Extract contexts where evidence is valid"""
        contexts = set()

        for ev in evidence:
            # Check for population indicators
            ev_text = str(ev).lower()
            if 'pediatric' in ev_text:
                contexts.add('pediatric_population')
            if 'adult' in ev_text:
                contexts.add('adult_population')
            if 'pregnant' in ev_text or 'pregnancy' in ev_text:
                contexts.add('pregnancy')

        return list(contexts)

    def _calculate_confidence(
        self,
        claims: List[MedicalClaim],
        contradictions: List[ContradictionNode]
    ) -> float:
        """Calculate confidence level for query results"""

        if not claims:
            return 0.0

        # Base confidence from claim quality
        base_confidence = 0.8

        # Penalty for contradictions
        contradiction_penalty = len(contradictions) * 0.1

        # Boost for multiple consistent claims
        consistency_boost = min(len(claims) * 0.05, 0.2)

        confidence = base_confidence - contradiction_penalty + consistency_boost
        return max(0.0, min(1.0, confidence))

    def _extract_alternative_perspectives(
        self,
        claims: List[MedicalClaim],
        contradictions: List[ContradictionNode]
    ) -> List[str]:
        """Extract alternative perspectives from claims and contradictions"""

        alternatives = []

        # Add claim texts as alternatives
        for claim in claims:
            alternatives.append(claim.claim_text)

        # Add perspectives from contradictions
        for contradiction in contradictions:
            for claim_id in contradiction.conflicting_claims:
                claim = self.evidence_graph.claims.get(claim_id)
                if claim:
                    alternatives.append(claim.claim_text)

        return alternatives[:5]  # Limit to 5 alternatives

    def get_knowledge_graph_stats(self) -> Dict[str, Any]:
        """Get statistics about the knowledge graph"""
        return {
            'total_claims': len(self.evidence_graph.claims),
            'total_contradictions': len(self.evidence_graph.contradictions),
            'domains_represented': list(self.evidence_graph.domain_index.keys()),
            'queries_processed': len(self.query_history),
            'average_confidence': (
                sum(q.confidence_level for q in self.query_history) / len(self.query_history)
                if self.query_history else 0.0
            )
        }

    def update_temporal_status(self):
        """Update temporal status of claims based on age and evidence"""
        cutoff_date = datetime.now() - timedelta(days=365*2)  # 2 years

        for claim in self.evidence_graph.claims.values():
            if claim.last_updated < cutoff_date:
                claim.temporal_status = "outdated"
            elif claim.last_updated < datetime.now() - timedelta(days=365):
                claim.temporal_status = "evolving"


# Convenience functions

def create_grail_system() -> MedicalGRAIL:
    """Create a new GRAIL system instance"""
    return MedicalGRAIL()


def query_medical_evidence(
    query: str,
    domain: Optional[str] = None
) -> GRAILQueryResult:
    """
    Convenience function to query medical evidence with contradiction awareness.

    Args:
        query: Medical question or topic
        domain: Optional medical domain to filter by

    Returns:
        GRAILQueryResult with contradiction-aware analysis
    """
    grail = create_grail_system()
    return grail.query_with_contradictions(query, domain)