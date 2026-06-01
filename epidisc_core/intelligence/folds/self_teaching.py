"""
Self-Teaching Intelligence Fold
================================

The self-teaching fold represents intelligence's capacity to:
- Adapt and revise through experience
- Generate new structures of understanding
- Learn from consultation interactions
- Reflect on performance and improve

This is the fold most familiar as "intelligence" in persons - the ability
to teach oneself and adapt based on experience.
"""

from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict
import json


@dataclass
class ConsultationRecord:
    """Record of a medical consultation for learning"""
    query: str
    response: str
    confidence: float
    domain: str
    user_feedback: Optional[str] = None
    outcome: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def was_successful(self) -> bool:
        """Determine if consultation was successful"""
        # High confidence and positive feedback indicates success
        if self.confidence >= 0.8:
            return True
        if self.user_feedback and 'helpful' in self.user_feedback.lower():
            return True
        return False

    def needs_improvement(self) -> bool:
        """Determine if consultation needs improvement"""
        return self.confidence < 0.7 or (
            self.user_feedback and 'unclear' in self.user_feedback.lower()
        )


@dataclass
class LearningPattern:
    """Pattern identified from consultation history"""
    pattern_type: str  # e.g., "high_confidence_success", "domain_weakness"
    description: str
    frequency: int
    confidence_impact: float
    recommendations: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)


class PatternRecognizer:
    """Recognizes patterns in consultation performance"""

    def __init__(self):
        self.pattern_history: List[LearningPattern] = []

    def analyze_consultations(
        self,
        consultations: List[ConsultationRecord]
    ) -> List[LearningPattern]:
        """Analyze consultation history for patterns"""

        patterns = []

        # Pattern 1: High confidence success correlation
        high_conf_success = self._analyze_confidence_success(consultations)
        if high_conf_success:
            patterns.append(high_conf_success)

        # Pattern 2: Domain-specific weaknesses
        domain_weaknesses = self._analyze_domain_weaknesses(consultations)
        patterns.extend(domain_weaknesses)

        # Pattern 3: Query type patterns
        query_patterns = self._analyze_query_patterns(consultations)
        patterns.extend(query_patterns)

        self.pattern_history.extend(patterns)
        return patterns

    def _analyze_confidence_success(
        self,
        consultations: List[ConsultationRecord]
    ) -> Optional[LearningPattern]:
        """Analyze correlation between confidence and success"""

        successful = [c for c in consultations if c.was_successful()]
        if not successful:
            return None

        avg_confidence = sum(c.confidence for c in successful) / len(successful)

        if avg_confidence >= 0.8:
            return LearningPattern(
                pattern_type="confidence_calibration",
                description=f"High confidence ({avg_confidence:.2f}) correlates with success",
                frequency=len(successful),
                confidence_impact=0.1,
                recommendations=["Maintain current confidence calibration"]
            )

        return None

    def _analyze_domain_weaknesses(
        self,
        consultations: List[ConsultationRecord]
    ) -> List[LearningPattern]:
        """Identify domain-specific performance patterns"""

        domain_performance = defaultdict(list)
        for consultation in consultations:
            domain_performance[consultation.domain].append(consultation)

        weaknesses = []
        for domain, domain_consultations in domain_performance.items():
            if len(domain_consultations) < 3:
                continue  # Need sufficient data

            avg_confidence = sum(
                c.confidence for c in domain_consultations
            ) / len(domain_consultations)

            if avg_confidence < 0.7:
                weaknesses.append(LearningPattern(
                    pattern_type="domain_weakness",
                    description=f"Low confidence in {domain} (avg: {avg_confidence:.2f})",
                    frequency=len(domain_consultations),
                    confidence_impact=-0.2,
                    recommendations=[
                        f"Increase {domain} knowledge base",
                        f"Practice {domain} consultations",
                        f"Update {domain} guidelines"
                    ]
                ))

        return weaknesses

    def _analyze_query_patterns(
        self,
        consultations: List[ConsultationRecord]
    ) -> List[LearningPattern]:
        """Analyze patterns in query types and responses"""

        patterns = []

        # Analyze query length vs confidence
        short_queries = [c for c in consultations if len(c.query.split()) < 10]
        long_queries = [c for c in consultations if len(c.query.split()) >= 20]

        if short_queries and long_queries:
            short_avg_conf = sum(c.confidence for c in short_queries) / len(short_queries)
            long_avg_conf = sum(c.confidence for c in long_queries) / len(long_queries)

            if abs(short_avg_conf - long_avg_conf) > 0.2:
                patterns.append(LearningPattern(
                    pattern_type="query_length_impact",
                    description=f"Query length affects confidence (short: {short_avg_conf:.2f}, long: {long_avg_conf:.2f})",
                    frequency=len(short_queries) + len(long_queries),
                    confidence_impact=0.05,
                    recommendations=["Consider query complexity in confidence assessment"]
                ))

        return patterns


class AdaptiveLearningModule:
    """Adaptive learning and memory system"""

    def __init__(self):
        self.learning_history: List[ConsultationRecord] = []
        self.pattern_recognizer = PatternRecognizer()
        self.performance_metrics: Dict[str, float] = {}

    def record_consultation(
        self,
        query: str,
        response: str,
        confidence: float,
        domain: str,
        metadata: Optional[Dict] = None
    ) -> ConsultationRecord:
        """Record a consultation for learning"""

        record = ConsultationRecord(
            query=query,
            response=response,
            confidence=confidence,
            domain=domain,
            metadata=metadata or {}
        )

        self.learning_history.append(record)
        return record

    def add_feedback(self, record: ConsultationRecord, feedback: str):
        """Add user feedback to a consultation record"""
        record.user_feedback = feedback

    def analyze_recent_performance(
        self,
        days: int = 7
    ) -> Dict[str, Any]:
        """Analyze performance over recent period"""

        cutoff_date = datetime.now() - timedelta(days=days)
        recent = [
            c for c in self.learning_history
            if c.timestamp >= cutoff_date
        ]

        if not recent:
            return {"message": "No recent consultations to analyze"}

        return {
            "total_consultations": len(recent),
            "average_confidence": sum(c.confidence for c in recent) / len(recent),
            "success_rate": sum(1 for c in recent if c.was_successful()) / len(recent),
            "domain_breakdown": self._get_domain_breakdown(recent),
            "patterns": self.pattern_recognizer.analyze_consultations(recent)
        }

    def _get_domain_breakdown(
        self,
        consultations: List[ConsultationRecord]
    ) -> Dict[str, Dict]:
        """Get performance breakdown by domain"""

        domain_stats = defaultdict(lambda: {
            'count': 0,
            'avg_confidence': 0.0,
            'success_rate': 0.0
        })

        for consultation in consultations:
            stats = domain_stats[consultation.domain]
            stats['count'] += 1
            stats['avg_confidence'] += consultation.confidence
            if consultation.was_successful():
                stats['success_rate'] += 1

        # Calculate averages
        for domain, stats in domain_stats.items():
            if stats['count'] > 0:
                stats['avg_confidence'] /= stats['count']
                stats['success_rate'] /= stats['count']

        return dict(domain_stats)


class SelfTeachingIntelligence:
    """
    Self-teaching fold of intelligence.

    Represents intelligence's capacity to:
    - Adapt and revise through experience
    - Generate new structures of understanding
    - Reflect on performance and improve

    This fold is the adaptive, learning aspect of intelligence that allows
    EPIDISC to improve through consultation experience.
    """

    def __init__(self):
        self.learning_module = AdaptiveLearningModule()
        self.pattern_recognizer = PatternRecognizer()
        self.reflection_history: List[Dict] = []

    def adapt_to_query(
        self,
        query: str,
        context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Adapt response strategy based on query and learning history"""

        # Analyze query characteristics
        query_analysis = self._analyze_query(query)

        # Check for relevant patterns
        relevant_patterns = self._find_relevant_patterns(query_analysis)

        # Adapt confidence based on learning
        adapted_confidence = self._adapt_confidence(query_analysis, relevant_patterns)

        return {
            'query_analysis': query_analysis,
            'relevant_patterns': relevant_patterns,
            'adapted_confidence': adapted_confidence,
            'learning_recommendations': self._generate_learning_recommendations(relevant_patterns)
        }

    def learn_from_consultation(
        self,
        record: ConsultationRecord
    ) -> Dict[str, Any]:
        """Extract learning from a consultation"""

        # Record in learning module
        self.learning_module.record_consultation(
            record.query,
            record.response,
            record.confidence,
            record.domain,
            record.metadata
        )

        # Analyze for patterns
        patterns = self.pattern_recognizer.analyze_consultations(
            self.learning_module.learning_history
        )

        return {
            'patterns_identified': len(patterns),
            'patterns': patterns,
            'performance_impact': self._assess_performance_impact(patterns)
        }

    def reflect_on_performance(self) -> Dict[str, Any]:
        """Periodic reflection to improve performance"""

        # Analyze recent performance
        recent_performance = self.learning_module.analyze_recent_performance(days=7)

        # Generate improvement recommendations
        recommendations = self._generate_improvement_recommendations(recent_performance)

        reflection = {
            'timestamp': datetime.now(),
            'performance_analysis': recent_performance,
            'recommendations': recommendations,
            'calibration_score': self._calculate_calibration_score(),
            'knowledge_gaps': self._identify_knowledge_gaps()
        }

        self.reflection_history.append(reflection)
        return reflection

    def _analyze_query(self, query: str) -> Dict[str, Any]:
        """Analyze query characteristics"""

        words = query.split()
        return {
            'length': len(words),
            'complexity': self._assess_complexity(query),
            'domain_indicators': self._identify_domain_indicators(query),
            'certainty_level': self._assess_certainty_level(query)
        }

    def _assess_complexity(self, query: str) -> str:
        """Assess query complexity"""
        words = query.split()

        if len(words) < 10:
            return "simple"
        elif len(words) < 20:
            return "moderate"
        else:
            return "complex"

    def _identify_domain_indicators(self, query: str) -> List[str]:
        """Identify medical domain indicators in query"""
        domain_keywords = {
            'cardiology': ['heart', 'chest pain', 'ecg', 'cardiac', 'hypertension'],
            'epilepsy': ['seizure', 'epilepsy', 'convulsion', 'eeg', 'aed'],
            'neurology': ['stroke', 'headache', 'movement disorder', 'tremor'],
            'orthopedics': ['fracture', 'joint', 'bone', 'sports injury'],
            'pharmacology': ['drug', 'medication', 'interaction', 'side effect']
        }

        indicators = []
        query_lower = query.lower()

        for domain, keywords in domain_keywords.items():
            if any(keyword in query_lower for keyword in keywords):
                indicators.append(domain)

        return indicators

    def _assess_certainty_level(self, query: str) -> str:
        """Assess how certain the query is"""
        uncertainty_indicators = ['maybe', 'possibly', 'might', 'could', 'uncertain']
        certainty_indicators = ['definitely', 'certainly', 'is', 'are']

        query_lower = query.lower()

        if any(indicator in query_lower for indicator in certainty_indicators):
            return "certain"
        elif any(indicator in query_lower for indicator in uncertainty_indicators):
            return "uncertain"
        else:
            return "neutral"

    def _find_relevant_patterns(
        self,
        query_analysis: Dict[str, Any]
    ) -> List[LearningPattern]:
        """Find patterns relevant to current query"""
        # This would check the pattern history for relevant patterns
        # For now, return empty list - to be implemented
        return []

    def _adapt_confidence(
        self,
        query_analysis: Dict[str, Any],
        patterns: List[LearningPattern]
    ) -> float:
        """Adapt confidence based on learning"""
        base_confidence = 0.8

        # Adjust for query complexity
        if query_analysis['complexity'] == 'complex':
            base_confidence -= 0.1

        # Adjust for relevant patterns
        for pattern in patterns:
            base_confidence += pattern.confidence_impact

        return max(0.0, min(1.0, base_confidence))

    def _generate_learning_recommendations(
        self,
        patterns: List[LearningPattern]
    ) -> List[str]:
        """Generate recommendations based on learning patterns"""
        recommendations = []
        for pattern in patterns:
            recommendations.extend(pattern.recommendations)
        return recommendations

    def _generate_improvement_recommendations(
        self,
        performance: Dict[str, Any]
    ) -> List[str]:
        """Generate improvement recommendations"""
        recommendations = []

        if isinstance(performance, dict) and 'average_confidence' in performance:
            if performance['average_confidence'] < 0.7:
                recommendations.append("Focus on improving knowledge base in weak domains")

            if performance.get('success_rate', 0) < 0.8:
                recommendations.append("Review consultation strategies for common failure patterns")

        return recommendations

    def _calculate_calibration_score(self) -> float:
        """Calculate how well-calibrated confidence estimates are"""
        # This would compare predicted confidence with actual success rates
        # For now, return default value
        return 0.75

    def _identify_knowledge_gaps(self) -> List[str]:
        """Identify areas where knowledge is insufficient"""
        # Analyze recent low-confidence consultations to identify gaps
        recent_consultations = self.learning_module.learning_history[-50:]

        low_confidence_domains = defaultdict(int)
        for consultation in recent_consultations:
            if consultation.confidence < 0.7:
                low_confidence_domains[consultation.domain] += 1

        gaps = [
            f"{domain} ({count} low-confidence consultations)"
            for domain, count in low_confidence_domains.items()
            if count >= 3
        ]

        return gaps

    def _assess_performance_impact(
        self,
        patterns: List[LearningPattern]
    ) -> str:
        """Assess the impact of identified patterns"""
        if not patterns:
            return "No significant patterns identified"

        positive_impact = sum(
            1 for p in patterns if p.confidence_impact > 0
        )
        negative_impact = len(patterns) - positive_impact

        if positive_impact > negative_impact:
            return f"Positive impact: {positive_impact} beneficial patterns"
        elif negative_impact > positive_impact:
            return f"Negative impact: {negative_impact} concerning patterns"
        else:
            return "Mixed impact: both positive and negative patterns present"
