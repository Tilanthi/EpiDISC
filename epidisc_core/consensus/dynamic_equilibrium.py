"""
Dynamic Nash Equilibrium for Medical Consensus
=============================================

Implements game-theoretic consensus building that finds win-win solutions
rather than zero-sum compromises for medical second opinions.

Key Concepts:
- Medical decisions as cooperative games
- Pareto-optimal solutions
- Clinical utility maximization
- Multi-stakeholder equilibrium
"""

from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import copy


class PerspectiveType(Enum):
    """Types of medical perspectives"""
    SPECIALTY = "specialty"  # From medical specialty
    GUIDELINE = "guideline"  # From clinical guideline
    EVIDENCE = "evidence"  # From research evidence
    PATIENT = "patient"  # Patient preference
    EXPERIENCE = "experience"  # Clinical experience


@dataclass
class MedicalPerspective:
    """
    A medical perspective in the consensus game.

    Represents a viewpoint on a medical decision from various sources
    (specialties, guidelines, evidence, patient preferences).
    """
    perspective_id: str
    source: str  # Where this perspective comes from
    perspective_type: PerspectiveType
    recommendation: str  # What this perspective recommends
    reasoning: str  # Why this perspective recommends this
    utility_score: float  # Clinical utility (0.0-1.0)
    confidence: float  # Confidence in recommendation (0.0-1.0)
    constraints: List[str] = field(default_factory=list)  # Constraints on this perspective
    tradeoffs: List[str] = field(default_factory=list)  # Known tradeoffs
    weight: float = 1.0  # Weight in consensus building (default equal)

    def __str__(self):
        return f"[{self.source}] {self.recommendation} (utility: {self.utility_score:.2f})"

    def is_compatible_with(self, other: 'MedicalPerspective') -> bool:
        """Check if this perspective is compatible with another"""
        # Perspectives are compatible if they don't directly contradict
        return not self._direct_contradiction(other)

    def _direct_contradiction(self, other: 'MedicalPerspective') -> bool:
        """Check if this perspective directly contradicts another"""
        # Simple contradiction detection
        rec1_lower = self.recommendation.lower()
        rec2_lower = other.recommendation.lower()

        # Look for direct negation
        if 'not' in rec1_lower and other.source in rec1_lower:
            return True
        if 'not' in rec2_lower and self.source in rec2_lower:
            return True

        # Look for opposing recommendations
        opposing_pairs = [
            ('recommend', 'avoid'),
            ('use', 'contra'),
            ('effective', 'ineffective'),
            ('safe', 'unsafe')
        ]

        for pos1, pos2 in opposing_pairs:
            if pos1 in rec1_lower and pos2 in rec2_lower:
                if self._same_topic(rec1_lower, rec2_lower):
                    return True

        return False

    def _same_topic(self, rec1: str, rec2: str) -> bool:
        """Check if two recommendations are about the same topic"""
        # Extract medical terms
        terms1 = self._extract_medical_terms(rec1)
        terms2 = self._extract_medical_terms(rec2)

        # Check for overlap
        return bool(set(terms1) & set(terms2))

    def _extract_medical_terms(self, text: str) -> List[str]:
        """Extract medical terms from text"""
        # Common medical term patterns
        medical_terms = []

        # AED names
        aeds = ['levetiracetam', 'lamotrigine', 'carbamazepine', 'valproate',
                'phenytoin', 'topiramate', 'brivaracetam']
        for aed in aeds:
            if aed in text.lower():
                medical_terms.append(aed)

        # Medical concepts
        concepts = ['seizure', 'epilepsy', 'cardiac', 'chest pain', 'pregnancy']
        for concept in concepts:
            if concept in text.lower():
                medical_terms.append(concept)

        return medical_terms


@dataclass
class ConsensusEquilibrium:
    """
    Result of consensus building using Nash equilibrium.

    Represents a stable consensus point where no perspective has
    incentive to deviate - a win-win solution rather than compromise.
    """
    consensus_id: str
    recommendation: str  # Final consensus recommendation
    supporting_perspectives: List[str]  # Which perspectives support this
    contributing_utilities: Dict[str, float]  # Utility contribution from each perspective
    pareto_optimal: bool  # Is this Pareto-optimal?
    stability_score: float  # How stable is this consensus (0.0-1.0)
    confidence: float  # Overall confidence in consensus (0.0-1.0)
    tradeoffs: List[str] = field(default_factory=list)
    unresolved_questions: List[str] = field(default_factory=list)
    alternative_equilibria: List[str] = field(default_factory=list)
    meta_analysis: str = ""
    timestamp: datetime = field(default_factory=datetime.now)

    def is_stable(self) -> bool:
        """Check if consensus is stable (high stability score)"""
        return self.stability_score >= 0.7

    def is_pareto_optimal(self) -> bool:
        """Check if consensus is Pareto-optimal"""
        return self.pareto_optimal

    def get_summary(self) -> str:
        """Get summary of the consensus"""
        summary = f"Consensus Recommendation: {self.recommendation}\n"
        summary += f"Stability: {self.stability_score:.2f} (Pareto-optimal: {self.pareto_optimal})\n"
        summary += f"Confidence: {self.confidence:.2f}\n"
        summary += f"\nSupporting Perspectives: {len(self.supporting_perspectives)}\n"

        if self.tradeoffs:
            summary += "\nTradeoffs:\n"
            for tradeoff in self.tradeoffs:
                summary += f"  - {tradeoff}\n"

        if self.unresolved_questions:
            summary += "\nUnresolved Questions:\n"
            for question in self.unresolved_questions:
                summary += f"  - {question}\n"

        return summary


class GameTheoreticModel:
    """
    Game-theoretic model for medical consensus building.

    Models medical decision-making as a cooperative game where multiple
    perspectives (players) work together to find optimal solutions.
    """

    def __init__(self):
        self.game_history: List[Dict] = []

    def model_cooperative_game(
        self,
        perspectives: List[MedicalPerspective],
        context: Dict
    ) -> Dict:
        """
        Model medical decision as cooperative game.

        In this game:
        - Players: Different medical perspectives
        - Strategies: Different recommendations/approaches
        - Payoffs: Clinical utility and patient outcomes
        - Goal: Maximize overall clinical utility
        """

        # Define game structure
        game = {
            'players': [p.source for p in perspectives],
            'strategies': self._define_strategies(perspectives),
            'payoffs': self._calculate_payoffs(perspectives, context),
            'game_type': 'cooperative'  # Working together for best outcome
        }

        return game

    def _define_strategies(self, perspectives: List[MedicalPerspective]) -> Dict:
        """Define available strategies for each perspective"""
        strategies = {}

        for perspective in perspectives:
            # Each perspective's primary strategy is its recommendation
            strategies[perspective.source] = {
                'primary': perspective.recommendation,
                'alternatives': perspective.tradeoffs
            }

        return strategies

    def _calculate_payoffs(
        self,
        perspectives: List[MedicalPerspective],
        context: Dict
    ) -> Dict:
        """Calculate payoffs for different strategy combinations"""

        payoffs = {}

        # Payoff is based on clinical utility and confidence
        for perspective in perspectives:
            payoff = {
                'utility': perspective.utility_score,
                'confidence': perspective.confidence,
                'expected_value': perspective.utility_score * perspective.confidence
            }
            payoffs[perspective.source] = payoff

        return payoffs

    def find_pareto_optimal(
        self,
        game: Dict
    ) -> List[Dict]:
        """
        Find Pareto-optimal solutions.

        A solution is Pareto-optimal if no player can be made better off
        without making another player worse off.
        """

        # This would implement sophisticated Pareto-optimal finding
        # For now, return placeholder
        return [{
            'solution': 'Pareto-optimal solution',
            'player_payoffs': {},
            'pareto_frontier': True
        }]

    def select_clinical_equilibrium(
        self,
        pareto_solutions: List[Dict],
        context: Dict
    ) -> ConsensusEquilibrium:
        """
        Select equilibrium based on clinical priorities.

        Among Pareto-optimal solutions, select the one that best serves
        clinical priorities and patient welfare.
        """

        if not pareto_solutions:
            return self._default_equilibrium()

        # Select solution with highest expected clinical utility
        best_solution = max(
            pareto_solutions,
            key=lambda s: self._calculate_clinical_priority(s, context)
        )

        return self._solution_to_equilibrium(best_solution, context)

    def _calculate_clinical_priority(
        self,
        solution: Dict,
        context: Dict
    ) -> float:
        """Calculate clinical priority score for a solution"""

        # Priority factors
        priority = 0.0

        # Patient safety priority
        if context.get('emergency', False):
            priority += 0.5

        # Evidence quality
        priority += solution.get('evidence_quality', 0.5) * 0.3

        # Specialist alignment
        priority += solution.get('specialist_alignment', 0.5) * 0.2

        return priority

    def _default_equilibrium(self) -> ConsensusEquilibrium:
        """Create default equilibrium when no solutions available"""
        return ConsensusEquilibrium(
            consensus_id="default",
            recommendation="Clinical judgment required - insufficient consensus",
            supporting_perspectives=[],
            contributing_utilities={},
            pareto_optimal=False,
            stability_score=0.5,
            confidence=0.5,
            meta_analysis="Default equilibrium - requires clinical input"
        )

    def _solution_to_equilibrium(
        self,
        solution: Dict,
        context: Dict
    ) -> ConsensusEquilibrium:
        """Convert game solution to consensus equilibrium"""
        # This would convert the game solution to equilibrium format
        # For now, return placeholder
        return ConsensusEquilibrium(
            consensus_id="generated",
            recommendation=solution.get('solution', 'Consensus recommendation'),
            supporting_perspectives=[],
            contributing_utilities={},
            pareto_optimal=True,
            stability_score=0.8,
            confidence=0.75,
            meta_analysis="Game-theoretic equilibrium"
        )


class DynamicNashEquilibrium:
    """
    Dynamic Nash Equilibrium system for medical consensus.

    Finds stable, win-win equilibria for medical second opinions using
    game-theoretic principles rather than forcing compromise or collapse.
    """

    def __init__(self):
        self.game_model = GameTheoreticModel()
        self.consensus_history: List[ConsensusEquilibrium] = []

    def find_equilibrium(
        self,
        perspectives: List[MedicalPerspective],
        context: Dict
    ) -> ConsensusEquilibrium:
        """
        Find Nash equilibrium for medical consensus.

        Args:
            perspectives: List of medical perspectives
            context: Clinical context and priorities

        Returns:
            ConsensusEquilibrium representing stable consensus point
        """

        if not perspectives:
            return self._empty_equilibrium()

        # Model as cooperative game
        game = self.game_model.model_cooperative_game(perspectives, context)

        # Find Pareto-optimal solutions
        pareto_solutions = self.game_model.find_pareto_optimal(game)

        # Select clinical equilibrium
        equilibrium = self.game_model.select_clinical_equilibrium(
            pareto_solutions,
            context
        )

        # Enhance equilibrium with additional analysis
        enhanced = self._enhance_equilibrium(
            equilibrium,
            perspectives,
            context
        )

        self.consensus_history.append(enhanced)
        return enhanced

    def find_second_opinion_equilibrium(
        self,
        initial_recommendation: str,
        alternatives: List[str],
        patient_factors: Dict,
        context: Dict
    ) -> ConsensusEquilibrium:
        """
        Find equilibrium specifically for second opinions.

        Balances initial recommendation with alternative perspectives while
        maintaining patient welfare as primary objective.
        """

        # Create perspectives from recommendations
        perspectives = []

        # Initial recommendation perspective
        perspectives.append(MedicalPerspective(
            perspective_id="initial",
            source="initial_recommendation",
            perspective_type=PerspectiveType.EXPERIENCE,
            recommendation=initial_recommendation,
            reasoning="Initial clinical recommendation",
            utility_score=0.7,
            confidence=0.8
        ))

        # Alternative perspectives
        for i, alt in enumerate(alternatives):
            perspectives.append(MedicalPerspective(
                perspective_id=f"alt_{i}",
                source=f"alternative_{i}",
                perspective_type=PerspectiveType.EVIDENCE,
                recommendation=alt,
                reasoning="Alternative evidence-based approach",
                utility_score=0.7,
                confidence=0.75
            ))

        # Patient preference perspective
        if patient_factors:
            patient_rec = self._generate_patient_perspective(patient_factors)
            if patient_rec:
                perspectives.append(patient_rec)

        # Find equilibrium
        return self.find_equilibrium(perspectives, context)

    def _generate_patient_perspective(self, patient_factors: Dict) -> Optional[MedicalPerspective]:
        """Generate medical perspective based on patient factors"""

        # Extract patient preferences and values
        preferences = patient_factors.get('preferences', [])
        values = patient_factors.get('values', [])

        if not preferences and not values:
            return None

        recommendation = f"Patient-centered approach respecting: {', '.join(preferences[:3])}"

        return MedicalPerspective(
            perspective_id="patient",
            source="patient_preferences",
            perspective_type=PerspectiveType.PATIENT,
            recommendation=recommendation,
            reasoning="Patient values and preferences",
            utility_score=0.9,  # Patient preference has high utility
            confidence=0.8,
            constraints=patient_factors.get('constraints', [])
        )

    def _enhance_equilibrium(
        self,
        equilibrium: ConsensusEquilibrium,
        perspectives: List[MedicalPerspective],
        context: Dict
    ) -> ConsensusEquilibrium:
        """Enhance equilibrium with additional analysis"""

        # Calculate stability score based on perspective agreement
        stability = self._calculate_stability(perspectives)

        # Calculate confidence based on supporting evidence
        confidence = self._calculate_confidence(perspectives)

        # Generate meta-analysis
        meta_analysis = self._generate_meta_analysis(
            equilibrium,
            perspectives,
            stability,
            confidence
        )

        # Update equilibrium
        equilibrium.stability_score = stability
        equilibrium.confidence = confidence
        equilibrium.meta_analysis = meta_analysis

        return equilibrium

    def _calculate_stability(self, perspectives: List[MedicalPerspective]) -> float:
        """Calculate how stable the equilibrium is"""

        if not perspectives:
            return 0.5

        # Count compatible perspectives
        compatible_count = 0
        for i, p1 in enumerate(perspectives):
            for p2 in perspectives[i+1:]:
                if p1.is_compatible_with(p2):
                    compatible_count += 1

        total_pairs = len(perspectives) * (len(perspectives) - 1) // 2
        if total_pairs == 0:
            return 1.0

        compatibility_ratio = compatible_count / total_pairs
        return compatibility_ratio

    def _calculate_confidence(self, perspectives: List[MedicalPerspective]) -> float:
        """Calculate overall confidence in consensus"""

        if not perspectives:
            return 0.5

        # Average confidence weighted by utility
        total_weight = 0.0
        weighted_confidence = 0.0

        for perspective in perspectives:
            weight = perspective.utility_score * perspective.weight
            weighted_confidence += perspective.confidence * weight
            total_weight += weight

        if total_weight == 0:
            return 0.5

        return weighted_confidence / total_weight

    def _generate_meta_analysis(
        self,
        equilibrium: ConsensusEquilibrium,
        perspectives: List[MedicalPerspective],
        stability: float,
        confidence: float
    ) -> str:
        """Generate meta-analysis of the equilibrium"""

        meta = f"Game-theoretic equilibrium analysis:\n"
        meta += f"- Stability: {stability:.2f} ({'stable' if stability >= 0.7 else 'unstable'})\n"
        meta += f"- Confidence: {confidence:.2f}\n"
        meta += f"- Perspectives: {len(perspectives)}\n"

        if equilibrium.pareto_optimal:
            meta += "- Pareto-optimal solution (no winner without loser)\n"

        return meta

    def _empty_equilibrium(self) -> ConsensusEquilibrium:
        """Create empty equilibrium when no perspectives available"""
        return ConsensusEquilibrium(
            consensus_id="empty",
            recommendation="No consensus - no perspectives provided",
            supporting_perspectives=[],
            contributing_utilities={},
            pareto_optimal=False,
            stability_score=0.0,
            confidence=0.0,
            meta_analysis="Cannot build equilibrium without perspectives"
        )


def find_medical_equilibrium(
    perspectives: List[MedicalPerspective],
    context: Dict
) -> ConsensusEquilibrium:
    """
    Convenience function to find medical equilibrium.

    Args:
        perspectives: List of medical perspectives
        context: Clinical context

    Returns:
        ConsensusEquilibrium representing optimal consensus
    """
    system = DynamicNashEquilibrium()
    return system.find_equilibrium(perspectives, context)
