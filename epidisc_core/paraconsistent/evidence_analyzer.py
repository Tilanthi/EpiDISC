"""
Medical Evidence Analyzer for Contradiction Detection
====================================================

Analyzes medical evidence for contradictions and contextual conflicts.
Implements paraconsistent logic to handle conflicting medical information.

Key Capabilities:
- Direct contradiction detection between evidence sources
- Contextual conflict identification (population differences, etc.)
- Evidence quality assessment
- Synthesis generation for contradictory evidence
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from itertools import combinations
import re

from .classification import (
    ParaconsistentClaim,
    TruthState
)


@dataclass
class EvidenceContradiction:
    """
    Represents a direct contradiction between two evidence sources.

    Attributes:
        source_a: First evidence source
        source_b: Second evidence source
        claim_a: Claim/conclusion from source A
        claim_b: Claim/conclusion from source B
        contradiction_type: Type of contradiction (direct, partial, etc.)
        severity: How severe the contradiction is (1-10)
    """
    source_a: str
    source_b: str
    claim_a: str
    claim_b: str
    contradiction_type: str
    severity: int

    def __str__(self):
        return f"{self.source_a} ({self.claim_a}) vs {self.source_b} ({self.claim_b})"


@dataclass
class ContextualConflict:
    """
    Represents a contextual conflict where evidence differs by context.

    Examples:
    - Pediatric vs adult populations
    - Different disease severities
    - Different time periods (guideline evolution)
    - Geographic/ethnic differences
    """
    source: str
    claim: str
    context_differences: List[str]
    still_valid_in_contexts: List[str]

    def __str__(self):
        return f"{self.source}: Valid in {', '.join(self.still_valid_in_contexts)}"


class MedicalEvidenceAnalyzer:
    """
    Analyzes medical evidence for contradictions and contextual conflicts.

    Uses paraconsistent logic to identify when evidence conflicts without
    forcing premature resolution.
    """

    def __init__(self):
        # Medical contradiction patterns
        self.contradiction_patterns = {
            'safety': [
                r'(safe|well.tolerated)',
                r'(unsafe|contraindicated|dangerous|harmful)'
            ],
            'efficacy': [
                r'(effective|works|improves)',
                r'(ineffective|does not work|fails|worsens)'
            ],
            'recommendation': [
                r'(recommended|first.line|preferred)',
                r'(not recommended|avoid|contra.indicated)'
            ]
        }

    def analyze_claim_consistency(
        self,
        claim: str,
        evidence: List[Dict],
        context: Optional[Dict] = None
    ) -> ParaconsistentClaim:
        """
        Analyze claim consistency across multiple evidence sources.

        Args:
            claim: The medical claim to analyze
            evidence: List of evidence dicts with 'source', 'conclusion', 'quality', 'year'
            context: Optional clinical context (patient factors, etc.)

        Returns:
            ParaconsistentClaim with classification and contradictions
        """
        if not evidence:
            return ParaconsistentClaim(
                claim=claim,
                state=TruthState.ZERO,
                confidence=0.0,
                evidence_sources=[],
                synthesis="No evidence available - clinical judgment required",
                routing_action="evidence_insufficient"
            )

        # Check for direct contradictions
        contradictions = self._find_contradictions(claim, evidence)

        # Check for contextual conflicts
        contextual_conflicts = self._identify_contextual_conflicts(evidence, context)

        # Assess overall evidence quality
        evidence_quality = self._assess_evidence_quality(evidence)

        # Determine paraconsistent state
        if contradictions:
            return self._create_contradictory_claim(
                claim, evidence, contradictions, evidence_quality
            )
        elif contextual_conflicts:
            return self._create_contextual_claim(
                claim, evidence, contextual_conflicts, evidence_quality
            )
        else:
            return self._create_validated_claim(
                claim, evidence, evidence_quality
            )

    def _find_contradictions(
        self,
        claim: str,
        evidence: List[Dict]
    ) -> List[EvidenceContradiction]:
        """Identify direct contradictions between evidence sources"""

        contradictions = []

        for e1, e2 in combinations(evidence, 2):
            if self._claims_contradict(e1.get('conclusion', ''), e2.get('conclusion', '')):
                contradiction = EvidenceContradiction(
                    source_a=e1.get('source', 'Unknown'),
                    source_b=e2.get('source', 'Unknown'),
                    claim_a=e1.get('conclusion', ''),
                    claim_b=e2.get('conclusion', ''),
                    contradiction_type=self._classify_contradiction_type(e1, e2),
                    severity=self._assess_contradiction_severity(e1, e2)
                )
                contradictions.append(contradiction)

        return contradictions

    def _claims_contradict(self, claim_a: str, claim_b: str) -> bool:
        """Check if two claims directly contradict each other"""

        # Normalize claims for comparison
        claim_a_lower = claim_a.lower()
        claim_b_lower = claim_b.lower()

        # Check for explicit contradiction words
        contradiction_indicators = [
            ('however', 'although', 'conversely', 'in contrast'),
            ('not', 'no', 'neither', 'never'),
            ('fails to', 'does not', 'unable to')
        ]

        # Direct negation detection
        for indicator_tuple in contradiction_indicators:
            for indicator in indicator_tuple:  # Iterate through tuple elements
                if indicator in claim_a_lower and indicator not in claim_b_lower:
                    # Check if they're talking about the same thing
                    if self._same_topic(claim_a, claim_b):
                        return True

        # Safety contradictions
        if any(word in claim_a_lower for word in ['safe', 'well tolerated']):
            if any(word in claim_b_lower for word in ['unsafe', 'harmful', 'dangerous']):
                return True

        # Efficacy contradictions
        if any(word in claim_a_lower for word in ['effective', 'improves']):
            if any(word in claim_b_lower for word in ['ineffective', 'worsens', 'fails']):
                return True

        # Data limitation contradictions (definitive vs limited data)
        definitive_indicators = ['safe', 'proven', 'effective', 'recommended', 'first-line']
        limitation_indicators = ['limited', 'insufficient', 'uncertain', 'unknown', 'lacking', 'inadequate', 'insufficient data']

        if any(word in claim_a_lower for word in definitive_indicators):
            # Check if claim B has limitation indicators
            for limitation in limitation_indicators:
                if limitation in claim_b_lower:
                    # Check if they're about the same topic
                    if self._same_topic(claim_a, claim_b):
                        return True

        return False

    def _same_topic(self, claim_a: str, claim_b: str) -> bool:
        """Check if two claims are about the same topic"""
        # Extract key medical terms from both claims
        terms_a = self._extract_medical_terms(claim_a)
        terms_b = self._extract_medical_terms(claim_b)

        # Check for overlap in medical terms
        overlap = set(terms_a) & set(terms_b)
        return len(overlap) > 0

    def _extract_medical_terms(self, claim: str) -> List[str]:
        """Extract key medical terms from a claim"""
        # Common medical term patterns
        medical_patterns = [
            r'\b[Aa]ED(?:s)?\b',  # Antiepileptic drugs
            r'\b[A-Z][a-z]+(?:azole|etine|amine|parin|mab)\b',  # Drug names
            r'\bseizure(?:s)?\b',
            r'\bepileps(?:y|ic)\b',
            r'\bpregnanc(?:y|ies)\b',
            r'\bpedia(?:tric|trics)\b',
            r'\badult(?:s)?\b'
        ]

        terms = []
        for pattern in medical_patterns:
            matches = re.findall(pattern, claim, re.IGNORECASE)
            terms.extend(matches)

        return terms

    def _classify_contradiction_type(self, e1: Dict, e2: Dict) -> str:
        """Classify the type of contradiction"""
        quality_diff = abs(e1.get('quality', 0.5) - e2.get('quality', 0.5))

        if quality_diff > 0.3:
            return "quality_mismatch"
        elif self._different_populations(e1, e2):
            return "population_difference"
        else:
            return "direct_contradiction"

    def _different_populations(self, e1: Dict, e2: Dict) -> bool:
        """Check if evidence refers to different populations"""
        pop_keywords = ['pediatric', 'adult', 'elderly', 'pregnant', 'neonatal']

        e1_pops = [kw for kw in pop_keywords if kw in e1.get('conclusion', '').lower()]
        e2_pops = [kw for kw in pop_keywords if kw in e2.get('conclusion', '').lower()]

        return bool(set(e1_pops) ^ set(e2_pops))  # Different populations

    def _assess_contradiction_severity(self, e1: Dict, e2: Dict) -> int:
        """Assess how severe a contradiction is (1-10)"""
        # Factors that increase severity
        severity = 5  # Base severity

        # High-quality evidence increases severity
        avg_quality = (e1.get('quality', 0.5) + e2.get('quality', 0.5)) / 2
        severity += int(avg_quality * 3)

        # Recent evidence increases severity
        if e1.get('year', 2000) > 2020 and e2.get('year', 2000) > 2020:
            severity += 2

        # Clinical recommendations increase severity
        if any(word in e1.get('conclusion', '').lower() for word in ['recommend', 'should']):
            severity += 1

        return min(severity, 10)  # Cap at 10

    def _identify_contextual_conflicts(
        self,
        evidence: List[Dict],
        context: Optional[Dict]
    ) -> List[ContextualConflict]:
        """Identify contextual conflicts in evidence"""

        conflicts = []

        # Check for population-based contextual differences
        populations = self._identify_populations(evidence)
        if len(populations) > 1:
            # Create contextual conflicts for population differences
            for pop in populations:
                relevant_evidence = [
                    e for e in evidence
                    if pop in e.get('conclusion', '').lower()
                ]
                if relevant_evidence:
                    conflict = ContextualConflict(
                        source="Population-based evidence",
                        claim=f"Evidence specific to {pop} population",
                        context_differences=list(populations),
                        still_valid_in_contexts=[pop]
                    )
                    conflicts.append(conflict)

        return conflicts

    def _identify_populations(self, evidence: List[Dict]) -> set:
        """Identify different populations mentioned in evidence"""
        population_keywords = {
            'pediatric', 'adult', 'elderly', 'pregnant',
            'neonatal', 'adolescent', 'geriatric'
        }

        populations_found = set()
        for e in evidence:
            conclusion_lower = e.get('conclusion', '').lower()
            for pop in population_keywords:
                if pop in conclusion_lower:
                    populations_found.add(pop)

        return populations_found

    def _assess_evidence_quality(self, evidence: List[Dict]) -> float:
        """Assess overall quality of evidence (0.0-1.0)"""
        if not evidence:
            return 0.0

        quality_scores = [e.get('quality', 0.5) for e in evidence]
        return sum(quality_scores) / len(quality_scores)

    def _create_contradictory_claim(
        self,
        claim: str,
        evidence: List[Dict],
        contradictions: List[EvidenceContradiction],
        evidence_quality: float
    ) -> ParaconsistentClaim:
        """Create a contradictory claim (State 0)"""

        contradiction_descriptions = [
            f"{c.source_a}: {c.claim_a} vs {c.source_b}: {c.claim_b}"
            for c in contradictions
        ]

        # Generate synthesis
        synthesis = self._generate_contradiction_synthesis(
            claim, contradictions, evidence_quality
        )

        # Determine routing action
        routing_action = self._determine_routing_action(contradictions)

        return ParaconsistentClaim(
            claim=claim,
            state=TruthState.ZERO,
            confidence=0.5,  # Low confidence due to contradiction
            evidence_sources=[e.get('source', 'Unknown') for e in evidence],
            contradictions=contradiction_descriptions,
            synthesis=synthesis,
            routing_action=routing_action,
            metadata={
                'contradiction_count': len(contradictions),
                'evidence_quality': evidence_quality,
                'highest_severity': max(c.severity for c in contradictions)
            }
        )

    def _create_contextual_claim(
        self,
        claim: str,
        evidence: List[Dict],
        contextual_conflicts: List[ContextualConflict],
        evidence_quality: float
    ) -> ParaconsistentClaim:
        """Create a contextually valid claim (State 2)"""

        # Extract valid contexts
        valid_contexts = []
        for conflict in contextual_conflicts:
            valid_contexts.extend(conflict.still_valid_in_contexts)

        synthesis = f"Valid in specific contexts: {', '.join(set(valid_contexts))}"

        return ParaconsistentClaim(
            claim=claim,
            state=TruthState.TWO,
            confidence=0.7,
            evidence_sources=[e.get('source', 'Unknown') for e in evidence],
            valid_contexts=list(set(valid_contexts)),
            synthesis=synthesis,
            routing_action="context_dependent",
            metadata={
                'context_count': len(valid_contexts),
                'evidence_quality': evidence_quality
            }
        )

    def _create_validated_claim(
        self,
        claim: str,
        evidence: List[Dict],
        evidence_quality: float
    ) -> ParaconsistentClaim:
        """Create a validated claim (State 1)"""

        synthesis = f"Strong evidence support from {len(evidence)} sources"

        return ParaconsistentClaim(
            claim=claim,
            state=TruthState.ONE,
            confidence=min(evidence_quality + 0.1, 0.95),
            evidence_sources=[e.get('source', 'Unknown') for e in evidence],
            synthesis=synthesis,
            routing_action="implement_with_confidence",
            metadata={
                'evidence_count': len(evidence),
                'evidence_quality': evidence_quality
            }
        )

    def _generate_contradiction_synthesis(
        self,
        claim: str,
        contradictions: List[EvidenceContradiction],
        evidence_quality: float
    ) -> str:
        """Generate synthesis when contradictions exist"""

        if len(contradictions) == 1:
            return f"Single contradiction identified - clinical judgment required"

        high_severity = [c for c in contradictions if c.severity >= 7]
        if high_severity:
            return f"High-severity contradictions ({len(high_severity)}) require specialist consultation"

        return f"Multiple contradictions ({len(contradictions)}) - weigh evidence quality and context"

    def _determine_routing_action(
        self,
        contradictions: List[EvidenceContradiction]
    ) -> str:
        """Determine appropriate routing for contradictory claims"""

        if any(c.severity >= 8 for c in contradictions):
            return "specialist_consultation_required"
        elif len(contradictions) > 2:
            return "multi_perspective_discussion"
        else:
            return "clinical_judgment_required"
