"""
Mystery State Handler for Undecidable Medical Claims
====================================================

Handles routing and response generation for medical claims that cannot be
definitively resolved (TruthState.ZERO - the mystery state).

Key Capabilities:
- Route undecidable claims to appropriate handlers
- Generate honest uncertainty responses
- Provide structured guidance for clinical judgment
- Maintain patient safety while admitting uncertainty
"""

from typing import Optional, Dict, List
from enum import Enum

from .classification import ParaconsistentClaim, TruthState


class RoutingAction(Enum):
    """Routing actions for undecidable medical claims"""
    SPECIALIST_CONSULTATION = "specialist_consultation_required"
    CLINICAL_JUDGMENT = "clinical_judgment_required"
    EVIDENCE_INSUFFICIENT = "evidence_insufficient"
    SHARED_DECISION = "shared_decision_making"
    MULTI_PERSPECTIVE = "multi_perspective_discussion"
    EMERGENCY_REFERRAL = "emergency_referral_required"


class MysteryStateHandler:
    """
    Handles medical claims that cannot be resolved definitively.

    The mystery state (TruthState.ZERO) represents claims that are:
    - Contradictory between evidence sources
    - Insufficient evidence for definitive conclusion
    - Require clinical judgment or specialist input

    This handler ensures these cases are routed appropriately rather than
    forcing false certainty.
    """

    # Routing action templates
    ROUTING_TEMPLATES = {
        RoutingAction.SPECIALIST_CONSULTATION: """
This medical question involves significant controversy or complexity:

**Claim:** {claim}

**Contradictory Evidence:**
{contradictions}

**Recommendation:** This requires specialist consultation. Refer to appropriate
specialist for definitive management. Do not make definitive recommendations
without expert input.
""",

        RoutingAction.CLINICAL_JUDGMENT: """
This medical question has conflicting evidence:

**Claim:** {claim}

**Conflicting Perspectives:**
{contradictions}

**Recommendation:** Requires individual clinical judgment. Consider:
- Patient-specific factors and preferences
- Risk-benefit analysis for this specific case
- Available local resources and expertise
- Monitor and reassess as evidence evolves
""",

        RoutingAction.EVIDENCE_INSUFFICIENT: """
This medical question has insufficient evidence:

**Claim:** {claim}

**Evidence Gap:** {gap_description}

**Recommendation:** Evidence insufficient for definitive recommendation.
Consider:
- Individualized approach based on patient factors
- Shared decision-making with patient
- Monitor for emerging evidence
- Document uncertainty in decision-making
""",

        RoutingAction.SHARED_DECISION: """
This medical question has multiple valid approaches:

**Claim:** {claim}

**Valid Options:**
{valid_options}

**Recommendation:** Shared decision-making required. Discuss with patient:
- Each option's potential benefits and risks
- Patient's values and preferences
- Available evidence quality and limitations
- Plan for monitoring and follow-up
""",

        RoutingAction.MULTI_PERSPECTIVE: """
This medical question involves multiple valid perspectives:

**Claim:** {claim}

**Different Perspectives:**
{perspectives}

**Recommendation:** Multiple valid approaches exist. Consider:
- All relevant perspectives
- Context-specific factors
- Multi-specialty consultation if available
- Individualized treatment plan
""",

        RoutingAction.EMERGENCY_REFERRAL: """
⚠️ **POTENTIAL EMERGENCY** ⚠️

This medical situation may require emergency evaluation:

**Claim:** {claim}

**Emergency Indicators:**
{emergency_indicators}

**IMMEDIATE ACTION REQUIRED:**
- Assess patient stability urgently
- Consider emergency department evaluation
- Do not delay for specialist appointment if acute concerns
- Emergency services: 911/999 if immediate safety concerns
"""
    }

    def __init__(self):
        # Emergency detection keywords
        self.emergency_keywords = [
            'seizure lasting more than 5 minutes',
            'status epilepticus',
            'sudden loss of consciousness',
            'chest pain',
            'difficulty breathing',
            'severe headache',
            'acute neurological deficit',
            'trauma'
        ]

    def handle_mystery_state(
        self,
        claim: ParaconsistentClaim,
        patient_context: Optional[Dict] = None
    ) -> str:
        """
        Generate appropriate response for undecidable medical claims.

        Args:
            claim: Paraconsistent claim with state ZERO
            patient_context: Optional clinical context for routing

        Returns:
            Formatted response with routing guidance
        """
        if claim.state != TruthState.ZERO:
            return None  # Only handle mystery states

        # Check for emergency indicators
        if self._has_emergency_indicators(claim, patient_context):
            return self._generate_emergency_response(claim)

        # Determine appropriate routing action
        routing_action = self._determine_routing_action(claim, patient_context)

        # Generate response based on routing action
        return self._generate_routing_response(claim, routing_action)

    def _has_emergency_indicators(
        self,
        claim: ParaconsistentClaim,
        patient_context: Optional[Dict]
    ) -> bool:
        """Check if claim indicates potential emergency"""

        # Check claim text
        claim_lower = claim.claim.lower()
        for keyword in self.emergency_keywords:
            if keyword in claim_lower:
                return True

        # Check context if available
        if patient_context:
            context_text = str(patient_context).lower()
            for keyword in self.emergency_keywords:
                if keyword in context_text:
                    return True

        return False

    def _determine_routing_action(
        self,
        claim: ParaconsistentClaim,
        patient_context: Optional[Dict]
    ) -> RoutingAction:
        """Determine appropriate routing action"""

        # Check for existing routing action
        if claim.routing_action:
            try:
                return RoutingAction(claim.routing_action)
            except ValueError:
                pass

        # Determine based on contradiction severity
        if claim.metadata.get('highest_severity', 0) >= 8:
            return RoutingAction.SPECIALIST_CONSULTATION

        # Check contradiction count
        contradiction_count = claim.metadata.get('contradiction_count', 0)
        if contradiction_count > 2:
            return RoutingAction.MULTI_PERSPECTIVE

        # Check evidence quality
        evidence_quality = claim.metadata.get('evidence_quality', 0.5)
        if evidence_quality < 0.3:
            return RoutingAction.EVIDENCE_INSUFFICIENT

        # Default to clinical judgment
        return RoutingAction.CLINICAL_JUDGMENT

    def _generate_emergency_response(self, claim: ParaconsistentClaim) -> str:
        """Generate emergency response"""
        emergency_indicators = self._extract_emergency_indicators(claim)

        return self.ROUTING_TEMPLATES[RoutingAction.EMERGENCY_REFERRAL].format(
            claim=claim.claim,
            emergency_indicators='\n'.join(f'- {ind}' for ind in emergency_indicators)
        )

    def _generate_routing_response(
        self,
        claim: ParaconsistentClaim,
        routing_action: RoutingAction
    ) -> str:
        """Generate routing response based on action"""

        template = self.ROUTING_TEMPLATES[routing_action]

        # Format contradictions
        contradictions_text = '\n'.join(
            f'- {contradiction}' for contradiction in claim.contradictions
        )

        # Generate context-specific content
        if routing_action == RoutingAction.SHARED_DECISION:
            valid_options = self._generate_valid_options(claim)
            return template.format(
                claim=claim.claim,
                valid_options='\n'.join(f'- {opt}' for opt in valid_options)
            )

        elif routing_action == RoutingAction.MULTI_PERSPECTIVE:
            perspectives = self._generate_perspectives(claim)
            return template.format(
                claim=claim.claim,
                perspectives='\n'.join(f'- {persp}' for persp in perspectives)
            )

        elif routing_action == RoutingAction.EVIDENCE_INSUFFICIENT:
            gap_description = claim.synthesis or "Insufficient evidence available"
            return template.format(
                claim=claim.claim,
                gap_description=gap_description
            )

        else:  # SPECIALIST_CONSULTATION or CLINICAL_JUDGMENT
            return template.format(
                claim=claim.claim,
                contradictions=contradictions_text
            )

    def _extract_emergency_indicators(
        self,
        claim: ParaconsistentClaim
    ) -> List[str]:
        """Extract specific emergency indicators from claim"""
        indicators = []

        claim_lower = claim.claim.lower()
        for keyword in self.emergency_keywords:
            if keyword in claim_lower:
                indicators.append(keyword)

        # Also check contradictions for emergency terms
        for contradiction in claim.contradictions:
            contradiction_lower = contradiction.lower()
            for keyword in self.emergency_keywords:
                if keyword in contradiction_lower and keyword not in indicators:
                    indicators.append(f"{keyword} (in contradictory evidence)")

        return indicators if indicators else ["Potential acute neurological condition"]

    def _generate_valid_options(self, claim: ParaconsistentClaim) -> List[str]:
        """Generate valid options for shared decision making"""
        # Extract options from contradictions and synthesis
        options = []

        # Add options from contradictions
        for contradiction in claim.contradictions:
            # Extract the actual recommendations from contradictions
            if 'vs' in contradiction:
                parts = contradiction.split('vs')
                if len(parts) == 2:
                    options.append(parts[0].strip())
                    options.append(parts[1].strip())

        # Add synthesis as option if available
        if claim.synthesis and claim.synthesis not in options:
            options.append(claim.synthesis)

        return options[:5]  # Limit to 5 options

    def _generate_perspectives(self, claim: ParaconsistentClaim) -> List[str]:
        """Generate different perspectives for multi-perspective discussion"""
        perspectives = []

        # Extract perspectives from contradictions
        for contradiction in claim.contradictions:
            if ':' in contradiction:
                source, content = contradiction.split(':', 1)
                perspectives.append(f"{source.strip()}: {content.strip()}")
            else:
                perspectives.append(contradiction)

        return perspectives


def generate_mystery_response(
    claim: ParaconsistentClaim,
    patient_context: Optional[Dict] = None
) -> Optional[str]:
    """
    Convenience function to generate mystery state response.

    Args:
        claim: Paraconsistent claim (should be state ZERO)
        patient_context: Optional clinical context

    Returns:
        Formatted response or None if not a mystery state
    """
    handler = MysteryStateHandler()
    return handler.handle_mystery_state(claim, patient_context)


# Utility functions for routing decisions

def requires_specialist(claim: ParaconsistentClaim) -> bool:
    """Check if claim requires specialist consultation"""
    handler = MysteryStateHandler()
    routing_action = handler._determine_routing_action(claim, None)
    return routing_action == RoutingAction.SPECIALIST_CONSULTATION


def requires_emergency_evaluation(claim: ParaconsistentClaim) -> bool:
    """Check if claim requires emergency evaluation"""
    handler = MysteryStateHandler()
    return handler._has_emergency_indicators(claim, None)


def is_shared_decision_case(claim: ParaconsistentClaim) -> bool:
    """Check if case requires shared decision making"""
    handler = MysteryStateHandler()
    routing_action = handler._determine_routing_action(claim, None)
    return routing_action == RoutingAction.SHARED_DECISION
