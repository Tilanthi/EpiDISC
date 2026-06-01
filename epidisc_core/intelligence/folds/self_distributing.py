"""
Self-Distributing Intelligence Fold
====================================

The self-distributing fold represents intelligence's capacity to:
- Coordinate across multiple medical specialties
- Build consensus without collapsing contradictions
- Enable collective intelligence through distributed networks
- Transcend local perspectives into shared understanding

This fold handles the relational aspect of intelligence - how intelligence
emerges through interaction, coordination, and distributed consensus.
"""

from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json
import hashlib


class Specialty(Enum):
    """Medical specialties that can contribute perspectives"""
    CARDIOLOGY = "cardiology"
    EPILEPSY = "epilepsy"
    NEUROLOGY = "neurology"
    GENERAL_PRACTICE = "general_practice"
    ORTHOPEDICS = "orthopedics"
    PHARMACOLOGY = "pharmacology"
    PSYCHIATRY = "psychiatry"
    INTERNAL_MEDICINE = "internal_medicine"


@dataclass
class MedicalPerspective:
    """A medical perspective from a specialty or approach"""
    perspective_id: str
    source: str  # Specialty or source type
    recommendation: str
    reasoning: str
    evidence_quality: float  # 0.0-1.0
    confidence: float  # 0.0-1.0
    constraints: List[str] = field(default_factory=list)
    alternatives_considered: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return f"[{self.source}] {self.recommendation} (confidence: {self.confidence:.2f})"


@dataclass
class ConsensusEquilibrium:
    """Result of consensus building between perspectives"""
    consensus_id: str
    primary_recommendation: str
    contributing_perspectives: List[str]
    tradeoffs: List[str]
    unresolved_questions: List[str]
    stability_score: float  # 0.0-1.0
    confidence_level: float  # 0.0-1.0
    alternative_options: List[str] = field(default_factory=list)
    meta_analysis: str = ""
    timestamp: datetime = field(default_factory=datetime.now)

    def is_stable(self) -> bool:
        """Check if consensus is stable (high stability score)"""
        return self.stability_score >= 0.7

    def has_unresolved_elements(self) -> bool:
        """Check if consensus has unresolved questions"""
        return len(self.unresolved_questions) > 0


class SpecialtyCoordinator:
    """Coordinates across medical specialties for complex cases"""

    def __init__(self):
        self.available_specialties = list(Specialty)
        self.coordination_history: List[Dict] = []

    def gather_perspectives(
        self,
        case_context: Dict
    ) -> List[MedicalPerspective]:
        """Gather perspectives from relevant medical specialties"""

        # Determine which specialties are relevant
        relevant_specialties = self._identify_relevant_specialties(case_context)

        # Gather perspective from each specialty
        perspectives = []
        for specialty in relevant_specialties:
            perspective = self._get_specialty_perspective(specialty, case_context)
            if perspective:
                perspectives.append(perspective)

        return perspectives

    def _identify_relevant_specialties(
        self,
        case_context: Dict
    ) -> List[Specialty]:
        """Identify which medical specialties are relevant to this case"""

        relevant = []

        # Check for seizure/epilepsy indicators
        query_lower = case_context.get('query', '').lower()
        if any(kw in query_lower for kw in ['seizure', 'epilepsy', 'convulsion', 'eeg']):
            relevant.append(Specialty.EPILEPSY)
            relevant.append(Specialty.NEUROLOGY)

        # Check for cardiac indicators
        if any(kw in query_lower for kw in ['heart', 'chest pain', 'cardiac', 'ecg']):
            relevant.append(Specialty.CARDIOLOGY)

        # Check for medication-related queries
        if any(kw in query_lower for kw in ['medication', 'drug', 'interaction', 'side effect']):
            relevant.append(Specialty.PHARMACOLOGY)

        # Always include general practice for comprehensive view
        if Specialty.GENERAL_PRACTICE not in relevant:
            relevant.append(Specialty.GENERAL_PRACTICE)

        return list(set(relevant))  # Remove duplicates

    def _get_specialty_perspective(
        self,
        specialty: Specialty,
        case_context: Dict
    ) -> Optional[MedicalPerspective]:
        """Get perspective from a specific specialty"""
        # This would query the actual specialty domain
        # For now, return placeholder perspective
        return MedicalPerspective(
            perspective_id=f"{specialty.value}_{datetime.now().timestamp()}",
            source=specialty.value,
            recommendation=f"Recommendation from {specialty.value}",
            reasoning=f"Reasoning based on {specialty.value} principles",
            evidence_quality=0.7,
            confidence=0.75
        )


class ConsensusBuilder:
    """Builds consensus between multiple medical perspectives"""

    def __init__(self):
        self.consensus_history: List[ConsensusEquilibrium] = []

    def build_consensus(
        self,
        perspectives: List[MedicalPerspective],
        case_context: Optional[Dict] = None
    ) -> ConsensusEquilibrium:
        """Build consensus from multiple perspectives"""

        if not perspectives:
            return self._empty_consensus()

        # Analyze perspectives for common ground and conflicts
        analysis = self._analyze_perspectives(perspectives)

        # Find equilibrium point
        equilibrium = self._find_equilibrium(perspectives, analysis)

        # Generate consensus
        consensus = ConsensusEquilibrium(
            consensus_id=self._generate_consensus_id(),
            primary_recommendation=equilibrium['recommendation'],
            contributing_perspectives=[p.source for p in perspectives],
            tradeoffs=equilibrium['tradeoffs'],
            unresolved_questions=equilibrium['unresolved'],
            stability_score=equilibrium['stability'],
            confidence_level=equilibrium['confidence'],
            alternative_options=equilibrium['alternatives'],
            meta_analysis=equilibrium['meta_analysis']
        )

        self.consensus_history.append(consensus)
        return consensus

    def find_equilibrium(
        self,
        initial_recommendation: str,
        alternatives: List[str],
        case_context: Dict
    ) -> ConsensusEquilibrium:
        """Find equilibrium (win-win) not zero-sum compromise"""

        # Create perspectives from recommendations
        perspectives = [
            MedicalPerspective(
                perspective_id="initial",
                source="initial_recommendation",
                recommendation=initial_recommendation,
                reasoning="Initial recommendation",
                evidence_quality=0.8,
                confidence=0.7
            )
        ]

        for alt in alternatives:
            perspectives.append(
                MedicalPerspective(
                    perspective_id=f"alt_{len(perspectives)}",
                    source="alternative",
                    recommendation=alt,
                    reasoning="Alternative perspective",
                    evidence_quality=0.7,
                    confidence=0.65
                )
            )

        return self.build_consensus(perspectives, case_context)

    def _analyze_perspectives(
        self,
        perspectives: List[MedicalPerspective]
    ) -> Dict:
        """Analyze perspectives for common ground and conflicts"""

        analysis = {
            'common_elements': [],
            'conflicts': [],
            'confidence_range': [0.0, 1.0],
            'evidence_quality_range': [0.0, 1.0]
        }

        if not perspectives:
            return analysis

        # Calculate ranges
        confidences = [p.confidence for p in perspectives]
        qualities = [p.evidence_quality for p in perspectives]

        analysis['confidence_range'] = [min(confidences), max(confidences)]
        analysis['evidence_quality_range'] = [min(qualities), max(qualities)]

        # Identify conflicts (very different recommendations)
        if len(perspectives) >= 2:
            for p1, p2 in zip(perspectives[:-1], perspectives[1:]):
                if self._recommendations_conflict(p1.recommendation, p2.recommendation):
                    analysis['conflicts'].append({
                        'source_1': p1.source,
                        'source_2': p2.source,
                        'conflict': f"{p1.recommendation} vs {p2.recommendation}"
                    })

        return analysis

    def _recommendations_conflict(self, rec1: str, rec2: str) -> bool:
        """Check if two recommendations conflict"""
        # Simple conflict detection - to be enhanced
        conflict_indicators = ['vs', 'instead of', 'rather than', 'however']

        rec1_lower = rec1.lower()
        rec2_lower = rec2.lower()

        for indicator in conflict_indicators:
            if indicator in rec1_lower or indicator in rec2_lower:
                return True

        return False

    def _find_equilibrium(
        self,
        perspectives: List[MedicalPerspective],
        analysis: Dict
    ) -> Dict:
        """Find equilibrium point between perspectives"""

        # Weight perspectives by evidence quality and confidence
        weighted_recommendations = []
        for perspective in perspectives:
            weight = (perspective.evidence_quality + perspective.confidence) / 2
            weighted_recommendations.append((perspective.recommendation, weight))

        # Sort by weight
        weighted_recommendations.sort(key=lambda x: x[1], reverse=True)

        # Primary recommendation is highest weighted
        primary = weighted_recommendations[0][0]

        # Generate tradeoffs and alternatives
        tradeoffs = []
        alternatives = []

        if analysis['conflicts']:
            tradeoffs.extend([
                f"Conflict between: {conflict['conflict']}"
                for conflict in analysis['conflicts']
            ])

        # Add lower-weighted recommendations as alternatives
        for rec, weight in weighted_recommendations[1:]:
            if weight > 0.5:  # Only include reasonable alternatives
                alternatives.append(rec)

        # Calculate stability
        conflicts_count = len(analysis['conflicts'])
        stability = 1.0 - (conflicts_count * 0.1)

        # Calculate confidence
        avg_confidence = sum(p.confidence for p in perspectives) / len(perspectives)

        return {
            'recommendation': primary,
            'tradeoffs': tradeoffs,
            'unresolved': [f"Conflict: {c['conflict']}" for c in analysis['conflicts']],
            'stability': max(0.0, stability),
            'confidence': avg_confidence,
            'alternatives': alternatives,
            'meta_analysis': f"Consensus built from {len(perspectives)} perspectives"
        }

    def _empty_consensus(self) -> ConsensusEquilibrium:
        """Create empty consensus when no perspectives available"""
        return ConsensusEquilibrium(
            consensus_id="empty",
            primary_recommendation="No consensus - insufficient perspectives",
            contributing_perspectives=[],
            tradeoffs=[],
            unresolved_questions=["No perspectives provided"],
            stability_score=0.0,
            confidence_level=0.0,
            meta_analysis="Cannot build consensus without perspectives"
        )

    def _generate_consensus_id(self) -> str:
        """Generate unique ID for consensus"""
        timestamp = datetime.now().timestamp()
        hash_input = str(timestamp).encode()
        return hashlib.sha256(hash_input).hexdigest()[:16]


class SelfDistributingIntelligence:
    """
    Self-distributing fold of intelligence.

    Represents intelligence's capacity to:
    - Coordinate across multiple medical specialties
    - Build consensus without collapsing contradictions
    - Enable collective intelligence through distributed networks
    - Transcend local perspectives into shared understanding

    This fold handles the relational, emergent aspect of intelligence that
    arises through interaction and coordination.
    """

    def __init__(self):
        self.specialty_coordinator = SpecialtyCoordinator()
        self.consensus_builder = ConsensusBuilder()
        self.collective_memory: List[Dict] = []

    def coordinate_consensus(
        self,
        organized_response: Dict,
        context: Optional[Dict] = None
    ) -> Dict:
        """Coordinate consensus across medical perspectives"""

        # Gather perspectives from relevant specialties
        perspectives = self.specialty_coordinator.gather_perspectives(context or {})

        if not perspectives:
            return {
                'status': 'no_perspectives',
                'message': 'Could not gather relevant perspectives',
                'recommendation': organized_response
            }

        # Build consensus
        consensus = self.consensus_builder.build_consensus(perspectives, context)

        # Store in collective memory
        self._store_case_resolution(context or {}, consensus)

        return {
            'status': 'consensus_built',
            'consensus': consensus,
            'perspectives_count': len(perspectives),
            'stability': consensus.stability_score,
            'recommendation': consensus.primary_recommendation
        }

    def synthesize_second_opinion(
        self,
        initial_recommendation: str,
        case_context: Dict
    ) -> ConsensusEquilibrium:
        """Generate second opinion that synthesizes multiple perspectives"""

        # Identify potential contradictions in initial recommendation
        contradictions = self._identify_contradictions(initial_recommendation)

        # Gather alternative perspectives
        alternatives = self._gather_alternative_perspectives(case_context)

        # Find equilibrium (not just alternative recommendation)
        equilibrium = self.consensus_builder.find_equilibrium(
            initial_recommendation,
            alternatives,
            case_context
        )

        return equilibrium

    def _identify_contradictions(self, recommendation: str) -> List[str]:
        """Identify potential contradictions in recommendation"""
        # This would check recommendation against knowledge base
        # For now, return empty
        return []

    def _gather_alternative_perspectives(self, context: Dict) -> List[str]:
        """Gather alternative medical perspectives"""
        # This would gather actual alternative recommendations
        # For now, return placeholder alternatives
        return [
            "Consider alternative medication",
            "Specialist consultation recommended",
            "Individualized approach based on patient factors"
        ]

    def _store_case_resolution(
        self,
        case_context: Dict,
        consensus: ConsensusEquilibrium
    ):
        """Store case resolution in collective memory"""
        resolution = {
            'timestamp': datetime.now(),
            'case_context': case_context,
            'consensus_id': consensus.consensus_id,
            'stability_score': consensus.stability_score,
            'contributing_perspectives': consensus.contributing_perspectives
        }
        self.collective_memory.append(resolution)

    def get_collective_memory_stats(self) -> Dict:
        """Get statistics about collective memory"""
        if not self.collective_memory:
            return {
                'total_resolutions': 0,
                'average_stability': 0.0,
                'most_common_perspectives': []
            }

        total = len(self.collective_memory)
        avg_stability = sum(
            r['stability_score'] for r in self.collective_memory
        ) / total

        # Count perspective frequencies
        perspective_counts = defaultdict(int)
        for resolution in self.collective_memory:
            for perspective in resolution['contributing_perspectives']:
                perspective_counts[perspective] += 1

        most_common = sorted(
            perspective_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]

        return {
            'total_resolutions': total,
            'average_stability': avg_stability,
            'most_common_perspectives': [
                {'perspective': p, 'count': c} for p, c in most_common
            ]
        }

    def enable_collective_intelligence(
        self,
        query: str,
        context: Dict
    ) -> Dict:
        """Enable collective intelligence for complex queries"""

        # Check if this query would benefit from collective intelligence
        if self._requires_collective_intelligence(query, context):
            return self.coordinate_consensus({}, context)
        else:
            return {
                'status': 'individual_intelligence',
                'message': 'Query handled by individual intelligence'
            }

    def _requires_collective_intelligence(self, query: str, context: Dict) -> bool:
        """Determine if query requires collective intelligence"""
        # Collective intelligence for:
        # - Multi-specialty cases
        # - Contradictory evidence
        # - Complex medical decisions

        query_lower = query.lower()

        # Multi-specialty indicators
        specialty_count = sum([
            1 for specialty in [
                'cardiac', 'seizure', 'medication', 'fracture'
            ]
            if specialty in query_lower
        ])

        # Complexity indicators
        complex_indicators = [
            'multiple', 'combined', 'comorbid', 'polypharmacy',
            'contradiction', 'conflicting', 'versus'
        ]

        complexity_score = sum([
            1 for indicator in complex_indicators
            if indicator in query_lower
        ])

        return specialty_count >= 2 or complexity_score >= 2
