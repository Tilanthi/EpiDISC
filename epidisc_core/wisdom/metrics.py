"""
Wisdom Metrics Implementation
============================

Quantifiable wisdom assessment for medical intelligence systems.

Wisdom is operationalized as measurable properties:
- Contradiction tolerance: How well does system handle medical contradictions?
- Perspective integration: Can it synthesize multiple viewpoints?
- Revision resilience: How does it handle new contradictory evidence?
- Contextual sensitivity: Does it adapt to patient-specific factors?
- Uncertainty honesty: Does it admit uncertainty appropriately?
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class WisdomDimension(Enum):
    """Different dimensions of wisdom"""
    CONTRADICTION_TOLERANCE = "contradiction_tolerance"
    PERSPECTIVE_INTEGRATION = "perspective_integration"
    REVISION_RESILIENCE = "revision_resilience"
    CONTEXTUAL_SENSITIVITY = "contextual_sensitivity"
    UNCERTAINTY_HONESTY = "uncertainty_honesty"


@dataclass
class WisdomScore:
    """
    Overall wisdom score with dimensional breakdowns.

    Represents wisdom as a measurable property rather than abstract concept.
    """
    overall_wisdom: float  # 0.0-1.0
    dimensional_scores: Dict[ WisdomDimension, float]  # Score per dimension
    confidence_in_score: float  # How confident are we in this score?
    assessment_timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def get_summary(self) -> str:
        """Get summary of wisdom score"""
        summary = f"Overall Wisdom: {self.overall_wisdom:.2f}\n"
        summary += f"Confidence: {self.confidence_in_score:.2f}\n"
        summary += "\nDimensional Scores:\n"

        for dimension, score in self.dimensional_scores.items():
            dimension_name = dimension.value.replace('_', ' ').title()
            summary += f"- {dimension_name}: {score:.2f}\n"

        return summary

    def is_high_wisdom(self) -> bool:
        """Check if this represents high wisdom"""
        return self.overall_wisdom >= 0.8

    def needs_improvement(self) -> bool:
        """Check if wisdom needs improvement"""
        return self.overall_wisdom < 0.6

    def get_weakest_dimension(self) -> Optional[ WisdomDimension]:
        """Get the dimension with lowest score"""
        if not self.dimensional_scores:
            return None

        return min(self.dimensional_scores.items(), key=lambda x: x[1])[0]

    def get_strongest_dimension(self) -> Optional[ WisdomDimension]:
        """Get the dimension with highest score"""
        if not self.dimensional_scores:
            return None

        return max(self.dimensional_scores.items(), key=lambda x: x[1])[0]


class WisdomMetrics:
    """
    Quantifiable wisdom assessment for medical intelligence.

    Wisdom is operationalized as measurable properties that can be tracked,
    improved, and benchmarked.
    """

    def __init__(self):
        self.assessment_history: List[WisdomScore] = []
        self.benchmark_scores: Dict[ str, float] = {
            'expert_minimum': 0.7,
            'expert_average': 0.8,
            'expert_maximum': 0.9
        }

    def calculate_wisdom_score(
        self,
        response: Dict[str, Any],
        context: Optional[Dict] = None
    ) -> WisdomScore:
        """
        Calculate wisdom score for a consultation response.

        Args:
            response: Consultation response to assess
            context: Optional clinical context

        Returns:
            WisdomScore with dimensional analysis
        """

        # Assess each wisdom dimension
        dimensional_scores = {
            WisdomDimension.CONTRADICTION_TOLERANCE: self._assess_contradiction_tolerance(response),
            WisdomDimension.PERSPECTIVE_INTEGRATION: self._assess_perspective_integration(response),
            WisdomDimension.REVISION_RESILIENCE: self._assess_revision_resilience(response, context),
            WisdomDimension.CONTEXTUAL_SENSITIVITY: self._assess_contextual_sensitivity(response, context),
            WisdomDimension.UNCERTAINTY_HONESTY: self._assess_uncertainty_honesty(response)
        }

        # Calculate overall wisdom
        overall = sum(dimensional_scores.values()) / len(dimensional_scores)

        # Calculate confidence in score
        confidence = self._calculate_score_confidence(response, dimensional_scores)

        wisdom_score = WisdomScore(
            overall_wisdom=overall,
            dimensional_scores=dimensional_scores,
            confidence_in_score=confidence,
            metadata={
                'response_type': response.get('type', 'unknown'),
                'has_contradictions': response.get('has_contradictions', False),
                'perspectives_included': response.get('perspectives_included', 1)
            }
        )

        self.assessment_history.append(wisdom_score)
        return wisdom_score

    def _assess_contradiction_tolerance(self, response: Dict) -> float:
        """
        Assess how well system handles medical contradictions.

        High score: Contradictions are explicitly surfaced and handled appropriately
        Low score: Contradictions cause collapse or are ignored
        """

        # Check if response handles contradictions well
        if response.get('has_contradictions', False):
            handling = response.get('contradiction_handling', '')

            # Good: Explicitly acknowledges and routes contradictions
            if any(kw in handling.lower() for kw in ['clinical judgment', 'specialist', 'multiple perspectives', 'context']):
                return 0.9

            # Medium: Acknowledges but doesn't route well
            elif any(kw in handling.lower() for kw in ['conflicting', 'uncertain', 'however']):
                return 0.6

            # Poor: Ignores or forces resolution
            else:
                return 0.3
        else:
            # No contradictions to handle - neutral score
            return 0.7

    def _assess_perspective_integration(self, response: Dict) -> float:
        """
        Assess how well system integrates multiple perspectives.

        High score: Synthesizes multiple viewpoints into coherent response
        Low score: Single perspective or forced consensus
        """

        perspectives_count = response.get('perspectives_included', 1)

        if perspectives_count >= 3:
            # Multiple perspectives integrated
            synthesis_quality = response.get('synthesis_quality', 'medium')
            if synthesis_quality == 'high':
                return 0.9
            elif synthesis_quality == 'medium':
                return 0.7
            else:
                return 0.5
        elif perspectives_count == 2:
            # Two perspectives - moderate integration
            return 0.6
        else:
            # Single perspective - low integration
            return 0.4

    def _assess_revision_resilience(self, response: Dict, context: Optional[Dict]) -> float:
        """
        Assess how system handles revision when new evidence emerges.

        High score: Responds adaptively to new evidence
        Low score: Rigid, unwilling to revise
        """

        # Check if response indicates openness to revision
        revision_indicators = [
            'monitor', 'reassess', 'follow-up', 'may change',
            'evidence evolves', 'new guidelines'
        ]

        response_text = str(response).lower()

        revision_friendly = sum(
            1 for indicator in revision_indicators
            if indicator in response_text
        )

        if revision_friendly >= 2:
            return 0.9
        elif revision_friendly == 1:
            return 0.7
        else:
            return 0.5

    def _assess_contextual_sensitivity(self, response: Dict, context: Optional[Dict]) -> float:
        """
        Assess how well system adapts to patient-specific context.

        High score: Explicitly considers patient factors and individualization
        Low score: One-size-fits-all approach
        """

        if not context:
            return 0.5  # Neutral if no context provided

        # Check if response considers patient factors
        context_keywords = [
            'patient', 'individual', 'specific', 'factors',
            'preferences', 'values', 'comorbidities'
        ]

        response_text = str(response).lower()

        context_sensitive = sum(
            1 for keyword in context_keywords
            if keyword in response_text
        )

        if context_sensitive >= 3:
            return 0.9
        elif context_sensitive >= 2:
            return 0.7
        elif context_sensitive == 1:
            return 0.6
        else:
            return 0.4

    def _assess_uncertainty_honesty(self, response: Dict) -> float:
        """
        Assess how honestly system admits uncertainty.

        High score: Explicitly admits uncertainty when appropriate
        Low score: False certainty or overconfidence
        """

        # Check for uncertainty indicators
        uncertainty_indicators = [
            'uncertain', 'limited evidence', 'may', 'might',
            'consider', 'clinical judgment', 'specialist',
            'insufficient data', 'requires evaluation'
        ]

        response_text = str(response).lower()

        uncertainty_honest = sum(
            1 for indicator in uncertainty_indicators
            if indicator in response_text
        )

        confidence = response.get('confidence', 0.8)

        # High confidence but explicit uncertainty admission = good
        if confidence >= 0.7 and uncertainty_honest >= 1:
            return 0.9
        # Moderate confidence with uncertainty = good
        elif confidence >= 0.5 and uncertainty_honest >= 1:
            return 0.8
        # Low confidence without uncertainty admission = bad
        elif confidence < 0.5 and uncertainty_honest == 0:
            return 0.3
        # High confidence without uncertainty = potentially overconfident
        elif confidence >= 0.9 and uncertainty_honest == 0:
            return 0.5
        else:
            return 0.6

    def _calculate_score_confidence(
        self,
        response: Dict,
        dimensional_scores: Dict[ WisdomDimension, float]
    ) -> float:
        """Calculate how confident we are in this wisdom score"""

        # Confidence based on consistency of dimensional scores
        scores = list(dimensional_scores.values())

        if not scores:
            return 0.5

        # Calculate variance (lower variance = higher confidence)
        avg_score = sum(scores) / len(scores)
        variance = sum((s - avg_score) ** 2 for s in scores) / len(scores)

        # Lower variance = higher confidence
        confidence = 1.0 - min(variance, 1.0)

        return confidence

    def assess_consultation_wisdom(
        self,
        consultation_record: Dict,
        expected_outcome: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Comprehensive wisdom assessment of a consultation.

        Args:
            consultation_record: Complete consultation record
            expected_outcome: Optional expected outcome for comparison

        Returns:
            Comprehensive wisdom assessment
        """

        # Calculate wisdom score
        wisdom_score = self.calculate_wisdom_score(consultation_record)

        # Compare to benchmarks
        benchmark_comparison = self._compare_to_benchmarks(wisdom_score)

        # Generate improvement recommendations
        recommendations = self._generate_wisdom_recommendations(wisdom_score)

        # Assess outcome alignment if expected outcome provided
        outcome_alignment = None
        if expected_outcome:
            outcome_alignment = self._assess_outcome_alignment(
                consultation_record,
                expected_outcome
            )

        return {
            'wisdom_score': wisdom_score,
            'benchmark_comparison': benchmark_comparison,
            'recommendations': recommendations,
            'outcome_alignment': outcome_alignment,
            'overall_assessment': self._generate_overall_assessment(wisdom_score)
        }

    def _compare_to_benchmarks(self, wisdom_score: WisdomScore) -> Dict[str, str]:
        """Compare wisdom score to expert benchmarks"""

        comparison = {}

        for benchmark_name, benchmark_value in self.benchmark_scores.items():
            if wisdom_score.overall_wisdom >= benchmark_value:
                comparison[benchmark_name] = "above"
            else:
                comparison[benchmark_name] = "below"

        return comparison

    def _generate_wisdom_recommendations(self, wisdom_score: WisdomScore) -> List[str]:
        """Generate recommendations to improve wisdom"""

        recommendations = []

        # Check each dimension
        for dimension, score in wisdom_score.dimensional_scores.items():
            if score < 0.6:
                dimension_name = dimension.value.replace('_', ' ').title()
                recommendations.append(
                    f"Improve {dimension_name} (current: {score:.2f})"
                )

        # Check overall wisdom
        if wisdom_score.overall_wisdom < 0.7:
            recommendations.append("Focus on overall wisdom enhancement")

        # Add specific recommendations based on weakest dimension
        weakest = wisdom_score.get_weakest_dimension()
        if weakest:
            if weakest == WisdomDimension.CONTRADICTION_TOLERANCE:
                recommendations.append("Practice explicit contradiction handling")
            elif weakest == WisdomDimension.PERSPECTIVE_INTEGRATION:
                recommendations.append("Increase multi-specialty consultation")
            elif weakest == WisdomDimension.REVISION_RESILIENCE:
                recommendations.append("Embrace adaptive learning approaches")
            elif weakest == WisdomDimension.CONTEXTUAL_SENSITIVITY:
                recommendations.append("Enhance patient-specific individualization")
            elif weakest == WisdomDimension.UNCERTAINTY_HONESTY:
                recommendations.append("Practice admitting uncertainty appropriately")

        return recommendations

    def _assess_outcome_alignment(
        self,
        consultation_record: Dict,
        expected_outcome: str
    ) -> Dict[str, Any]:
        """Assess if consultation aligned with expected outcome"""

        # This would compare actual outcome with expected
        # For now, return placeholder
        return {
            'aligned': True,
            'alignment_score': 0.8,
            'notes': 'Outcome assessment to be implemented'
        }

    def _generate_overall_assessment(self, wisdom_score: WisdomScore) -> str:
        """Generate overall assessment text"""

        if wisdom_score.is_high_wisdom():
            return "High wisdom consultation - demonstrates excellent clinical judgment"
        elif wisdom_score.needs_improvement():
            return "Wisdom needs improvement - review recommendations"
        else:
            return "Adequate wisdom - room for enhancement in specific dimensions"

    def get_wisdom_trends(self, days: int = 30) -> Dict[str, Any]:
        """Analyze wisdom trends over time"""

        cutoff_date = datetime.now() - timedelta(days=days)
        recent_assessments = [
            score for score in self.assessment_history
            if score.assessment_timestamp >= cutoff_date
        ]

        if not recent_assessments:
            return {
                'message': 'No recent wisdom assessments available',
                'trend': 'insufficient_data'
            }

        # Calculate trends
        overall_scores = [score.overall_wisdom for score in recent_assessments]
        avg_wisdom = sum(overall_scores) / len(overall_scores)

        # Check for improvement
        if len(overall_scores) >= 2:
            first_half = overall_scores[:len(overall_scores)//2]
            second_half = overall_scores[len(overall_scores)//2:]

            if first_half and second_half:
                first_avg = sum(first_half) / len(first_half)
                second_avg = sum(second_half) / len(second_half)

                if second_avg > first_avg + 0.05:
                    trend = "improving"
                elif second_avg < first_avg - 0.05:
                    trend = "declining"
                else:
                    trend = "stable"
            else:
                trend = "insufficient_data"
        else:
            trend = "insufficient_data"

        return {
            'assessments_count': len(recent_assessments),
            'average_wisdom': avg_wisdom,
            'trend': trend,
            'dimensional_trends': self._calculate_dimensional_trends(recent_assessments)
        }

    def _calculate_dimensional_trends(
        self,
        assessments: List[WisdomScore]
    ) -> Dict[str, str]:
        """Calculate trends for each wisdom dimension"""

        dimensional_trends = {}

        for dimension in WisdomDimension:
            scores = [
                score.dimensional_scores.get(dimension, 0.5)
                for score in assessments
            ]

            if not scores:
                dimensional_trends[dimension.value] = "insufficient_data"
                continue

            # Simple trend calculation
            if len(scores) >= 2:
                first_avg = scores[0]
                last_avg = scores[-1]

                if last_avg > first_avg + 0.05:
                    dimensional_trends[dimension.value] = "improving"
                elif last_avg < first_avg - 0.05:
                    dimensional_trends[dimension.value] = "declining"
                else:
                    dimensional_trends[dimension.value] = "stable"
            else:
                dimensional_trends[dimension.value] = "insufficient_data"

        return dimensional_trends


def calculate_wisdom_score(
    response: Dict[str, Any],
    context: Optional[Dict] = None
) -> WisdomScore:
    """
    Convenience function to calculate wisdom score.

    Args:
        response: Consultation response to assess
        context: Optional clinical context

    Returns:
        WisdomScore with dimensional analysis
    """
    metrics = WisdomMetrics()
    return metrics.calculate_wisdom_score(response, context)


def assess_consultation_wisdom(
    consultation_record: Dict,
    expected_outcome: Optional[str] = None
) -> Dict[str, Any]:
    """
    Convenience function for comprehensive wisdom assessment.

    Args:
        consultation_record: Complete consultation record
        expected_outcome: Optional expected outcome

    Returns:
        Comprehensive wisdom assessment
    """
    metrics = WisdomMetrics()
    return metrics.assess_consultation_wisdom(consultation_record, expected_outcome)
