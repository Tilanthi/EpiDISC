"""
Comprehensive Test Suite for Paraconsistent Intelligence Architecture
====================================================================

Tests for all 4 phases of the Process-Substrate Intelligence implementation:
- Phase 1: Paraconsistent Reasoning
- Phase 2: Three-Fold Intelligence
- Phase 3: Dynamic Consensus & Wisdom Metrics
- Phase 4: Integration & Testing

Author: EPIDISC Development Team
Version: 1.0.0
Date: June 2026
"""

import sys
import unittest
from datetime import datetime
from typing import Dict, List

# Import all new components
from epidisc_core.paraconsistent import (
    TruthState,
    ParaconsistentClaim,
    classify_medical_claim,
    generate_mystery_response,
    MedicalEvidenceAnalyzer
)

from epidisc_core.intelligence import (
    ProcessSubstrateIntelligence,
    create_process_substrate_system,
    SelfTeachingIntelligence,
    SelfOrganizingIntelligence,
    SelfDistributingIntelligence
)

from epidisc_core.consensus import (
    DynamicNashEquilibrium,
    find_medical_equilibrium,
    MedicalPerspective,
    PerspectiveType
)

from epidisc_core.wisdom import (
    WisdomMetrics,
    calculate_wisdom_score,
    assess_consultation_wisdom
)

from epidisc_core.knowledge import (
    MedicalGRAIL,
    create_grail_system,
    query_medical_evidence
)


class TestParaconsistentReasoning(unittest.TestCase):
    """Test suite for Phase 1: Paraconsistent Reasoning"""

    def test_truth_state_classification(self):
        """Test 0/1/2 truth state classification"""
        # Test State 1 (Validated)
        claim_validated = ParaconsistentClaim(
            claim="Levetiracetam is effective for focal seizures",
            state=TruthState.ONE,
            confidence=0.9,
            evidence_sources=["ILAE guidelines", "Clinical trials"]
        )
        self.assertTrue(claim_validated.is_validated())
        self.assertFalse(claim_validated.requires_clinical_judgment())

        # Test State 0 (Contradictory)
        claim_contradictory = ParaconsistentClaim(
            claim="AED safety in pregnancy",
            state=TruthState.ZERO,
            confidence=0.5,
            evidence_sources=["Study A", "Study B"],
            contradictions=["Study A: Safe vs Study B: Limited data"]
        )
        self.assertTrue(claim_contradictory.requires_clinical_judgment())
        self.assertTrue(claim_contradictory.is_contradictory())

        # Test State 2 (Contextual)
        claim_contextual = ParaconsistentClaim(
            claim="AED selection depends on patient factors",
            state=TruthState.TWO,
            confidence=0.7,
            valid_contexts=["pregnancy", "elderly", "comorbidities"]
        )
        self.assertTrue(claim_contextual.is_perspective_dependent())

    def test_evidence_contradiction_detection(self):
        """Test medical evidence contradiction detection"""
        analyzer = MedicalEvidenceAnalyzer()

        # Test contradictory evidence
        evidence = [
            {
                'source': "Study A",
                'conclusion': "Levetiracetam is safe in pregnancy",
                'quality': 0.7,
                'year': 2024
            },
            {
                'source': "Study B",
                'conclusion': "Levetiracetam has limited pregnancy data",
                'quality': 0.6,
                'year': 2023
            }
        ]

        result = analyzer.analyze_claim_consistency(
            "Levetiracetam safety in pregnancy",
            evidence
        )

        # Should detect contradiction and classify as State ZERO
        self.assertEqual(result.state, TruthState.ZERO)
        self.assertTrue(len(result.contradictions) > 0)

    def test_mystery_state_routing(self):
        """Test routing of undecidable medical claims"""
        from epidisc_core.paraconsistent.mystery_handler import RoutingAction

        # Create contradictory claim
        contradictory_claim = ParaconsistentClaim(
            claim="Optimal AED for treatment-resistant epilepsy",
            state=TruthState.ZERO,
            confidence=0.5,
            contradictions=["Guideline A: Surgical approach vs Guideline B: Medical approach"],
            routing_action="specialist_consultation_required"
        )

        # Generate mystery response
        response = generate_mystery_response(contradictory_claim)

        self.assertIsNotNone(response)
        self.assertIn("specialist", response.lower())

    def test_contextual_validity_classification(self):
        """Test classification of contextually valid claims"""
        evidence = [
            {
                'source': "Pediatric Study",
                'conclusion': "Lamotrigine effective in pediatric population",
                'quality': 0.8
            }
        ]

        result = classify_medical_claim(
            "Lamotrigine efficacy",
            evidence
        )

        # Should be contextual due to population specificity
        self.assertIn(result.claim.state, [TruthState.ONE, TruthState.TWO])


class TestThreeFoldIntelligence(unittest.TestCase):
    """Test suite for Phase 2: Three-Fold Intelligence Architecture"""

    def test_self_teaching_fold(self):
        """Test self-teaching intelligence fold"""
        teaching_intelligence = SelfTeachingIntelligence()

        # Test query adaptation
        query = "Patient with new-onset seizures"
        adapted = teaching_intelligence.adapt_to_query(query)

        self.assertIn('query_analysis', adapted)
        self.assertIn('adapted_confidence', adapted)

        # Test learning from consultation
        from epidisc_core.intelligence.folds.self_teaching import ConsultationRecord

        record = ConsultationRecord(
            query="Test query",
            response="Test response",
            confidence=0.8,
            domain="epilepsy"
        )

        learning_result = teaching_intelligence.learn_from_consultation(record)

        self.assertIn('patterns_identified', learning_result)

    def test_self_organizing_fold(self):
        """Test self-organizing intelligence fold"""
        organizing_intelligence = SelfOrganizingIntelligence()

        # Test systemic coherence
        coherence_result = organizing_intelligence.maintain_systemic_coherence()

        self.assertIn('coherence_score', coherence_result)
        self.assertIsInstance(coherence_result['coherence_score'], float)

        # Test equilibrium state
        equilibrium = organizing_intelligence.get_equilibrium_state()

        self.assertIsNotNone(equilibrium)
        self.assertIn('coherence_score', equilibrium.equilibrium_factors)

    def test_self_distributing_fold(self):
        """Test self-distributing intelligence fold"""
        distributing_intelligence = SelfDistributingIntelligence()

        # Test consensus coordination
        case_context = {
            'query': "Complex epilepsy case",
            'patient_factors': {'age': 25, 'comorbidities': ['depression']}
        }

        consensus_result = distributing_intelligence.coordinate_consensus(
            {},
            case_context
        )

        self.assertIn('status', consensus_result)

    def test_process_substrate_integration(self):
        """Test integration of all three folds"""
        system = create_process_substrate_system()

        # Test query processing through all three folds
        response = system.process_query(
            "Patient with focal impaired awareness seizures",
            context={'domain': 'epilepsy'}
        )

        self.assertIsNotNone(response)
        self.assertIn('primary_recommendation', response)
        self.assertIn('wisdom_score', response)
        self.assertIn('fold_contributions', response)


class TestDynamicConsensus(unittest.TestCase):
    """Test suite for Phase 3: Dynamic Consensus & Wisdom Metrics"""

    def test_nash_equilibrium_finding(self):
        """Test finding Nash equilibrium for medical consensus"""
        equilibrium_system = DynamicNashEquilibrium()

        # Create medical perspectives
        perspectives = [
            MedicalPerspective(
                perspective_id="neurology",
                source="Neurology",
                perspective_type=PerspectiveType.SPECIALTY,
                recommendation="Levetiracetam for focal seizures",
                reasoning="First-line AED with good efficacy",
                utility_score=0.8,
                confidence=0.85
            ),
            MedicalPerspective(
                perspective_id="pharmacology",
                source="Pharmacology",
                perspective_type=PerspectiveType.SPECIALTY,
                recommendation="Consider lamotrigine as alternative",
                reasoning="Different side effect profile",
                utility_score=0.7,
                confidence=0.75
            )
        ]

        equilibrium = equilibrium_system.find_equilibrium(
            perspectives,
            {'priority': 'patient_outcome'}
        )

        self.assertIsNotNone(equilibrium)
        self.assertIn('recommendation', equilibrium)
        self.assertIn('stability_score', equilibrium)

    def test_second_opinion_equilibrium(self):
        """Test equilibrium for second opinions"""
        equilibrium_system = DynamicNashEquilibrium()

        equilibrium = equilibrium_system.find_second_opinion_equilibrium(
            initial_recommendation="Levetiracetam 500mg BID",
            alternatives=["Lamotrigine titration", "Carbamazepine monitoring"],
            patient_factors={'preferences': ['avoid cognitive side effects']},
            context={'case_complexity': 'moderate'}
        )

        self.assertIsNotNone(equilibrium)
        self.assertTrue(equilibrium.is_stable() or equilibrium.has_unresolved_elements())

    def test_wisdom_metrics(self):
        """Test wisdom metrics calculation"""
        metrics = WisdomMetrics()

        # Test wisdom score calculation
        response = {
            'type': 'consultation',
            'has_contradictions': True,
            'perspectives_included': 3,
            'contradiction_handling': 'Clinical judgment required for conflicting guidelines',
            'synthesis_quality': 'high',
            'confidence': 0.75
        }

        wisdom_score = metrics.calculate_wisdom_score(response)

        self.assertIsNotNone(wisdom_score)
        self.assertIn('overall_wisdom', wisdom_score)
        self.assertIn('dimensional_scores', wisdom_score)
        self.assertIsInstance(wisdom_score.overall_wisdom, float)

    def test_contradiction_tolerance_dimension(self):
        """Test contradiction tolerance wisdom dimension"""
        metrics = WisdomMetrics()

        # High contradiction tolerance response
        good_response = {
            'has_contradictions': True,
            'contradiction_handling': 'Multiple perspectives require clinical judgment'
        }

        wisdom_score = metrics.calculate_wisdom_score(good_response)
        tolerance_score = wisdom_score.dimensional_scores.get(
            WisdomDimension.CONTRADICTION_TOLERANCE
        )

        self.assertGreater(tolerance_score, 0.7)  # Should be high

    def test_uncertainty_honesty_dimension(self):
        """Test uncertainty honesty wisdom dimension"""
        metrics = WisdomMetrics()

        # Honest uncertainty response
        honest_response = {
            'confidence': 0.6,
            'uncertainty_indicators': 'Limited evidence, may require specialist input'
        }

        wisdom_score = metrics.calculate_wisdom_score(honest_response)
        honesty_score = wisdom_score.dimensional_scores.get(
            WisdomDimension.UNCERTAINTY_HONESTY
        )

        self.assertGreater(honesty_score, 0.6)  # Should be reasonably high


class TestGRAILKnowledgeGraph(unittest.TestCase):
    """Test suite for GRAIL knowledge graph system"""

    def test_grail_claim_addition(self):
        """Test adding medical claims to GRAIL system"""
        grail = create_grail_system()

        claim = grail.add_medical_claim(
            claim_text="Levetiracetam is first-line for focal seizures",
            domain="epilepsy",
            evidence=[
                {
                    'source': "ILAE Guidelines",
                    'conclusion': "Levetiracetam recommended as first-line",
                    'quality': 0.9
                }
            ]
        )

        self.assertIsNotNone(claim)
        self.assertEqual(claim.domain, "epilepsy")

    def test_grail_contradiction_mapping(self):
        """Test contradiction detection in GRAIL system"""
        grail = create_grail_system()

        # Add claims with contradictions
        claim1 = grail.add_medical_claim(
            "AED is safe in pregnancy",
            "pharmacology",
            [{'source': "Study A", 'conclusion': "Safe in pregnancy", 'quality': 0.7}]
        )

        claim2 = grail.add_medical_claim(
            "AED has limited pregnancy data",
            "pharmacology",
            [{'source': "Study B", 'conclusion': "Limited data", 'quality': 0.6}]
        )

        # Query should identify contradictions
        result = grail.query_with_contradictions("AED safety in pregnancy")

        self.assertGreater(len(result.contradictions), 0)
        self.assertTrue(result.requires_clinical_judgment)

    def test_grail_synthesis_generation(self):
        """Test synthesis generation from contradictory claims"""
        grail = create_grail_system()

        result = grail.query_with_contradictions("Epilepsy surgery decision")

        # Should provide synthesis when contradictions exist
        if result.contradictions:
            self.assertIsNotNone(result.synthesis)


class TestIntegration(unittest.TestCase):
    """Test suite for Phase 4: Integration & System Performance"""

    def test_full_system_integration(self):
        """Test complete integration of all phases"""
        # Create process substrate system
        system = create_process_substrate_system()

        # Process complex medical query
        response = system.process_query(
            "25-year-old woman with focal seizures planning pregnancy",
            context={
                'domain': 'epilepsy',
                'patient_factors': {
                    'age': 25,
                    'gender': 'female',
                    'plans_pregnancy': True
                }
            }
        )

        # Verify all three folds contributed
        self.assertIn('self_teaching', response.fold_contributions)
        self.assertIn('self_organizing', response.fold_contributions)
        self.assertIn('self_distributing', response.fold_contributions)

        # Verify wisdom metrics are calculated
        self.assertGreater(response.wisdom_score, 0.0)
        self.assertLessEqual(response.wisdom_score, 1.0)

    def test_system_performance_validation(self):
        """Test system performance against validation scenarios"""

        # Scenario 1: Known medical controversy
        system = create_process_substrate_system()

        controversy_response = system.process_query(
            "AED selection in pregnancy - levetiracetam vs lamotrigine",
            evidence=[
                {'source': "Study A", 'conclusion': "Levetiracetam appears safe", 'quality': 0.6},
                {'source': "Study B", 'conclusion': "Lamotrigine has more data", 'quality': 0.8}
            ]
        )

        # System should handle controversy appropriately
        self.assertTrue(
            controversy_response.requires_clinical_judgment or
            controversy_response.requires_specialist
        )

        # Scenario 2: Emergency case
        emergency_response = system.process_query(
            "Patient seizing for 10 minutes",
            context={'emergency': True}
        )

        # Should handle emergency appropriately
        self.assertIn('emergency', emergency_response.primary_recommendation.lower())

    def test_wisdom_benchmark_comparison(self):
        """Test wisdom score comparison to expert benchmarks"""
        metrics = WisdomMetrics()

        # Create expert-level response
        expert_response = {
            'has_contradictions': True,
            'contradiction_handling': 'Multiple perspectives considered, recommend specialist input',
            'perspectives_included': 4,
            'synthesis_quality': 'high',
            'confidence': 0.7  # Appropriate uncertainty
        }

        wisdom_score = metrics.calculate_wisdom_score(expert_response)
        benchmark_comparison = metrics._compare_to_benchmarks(wisdom_score)

        # Expert-level response should compare favorably
        self.assertEqual(benchmark_comparison['expert_minimum'], "above")

    def test_system_maintenance(self):
        """Test periodic system maintenance"""
        system = create_process_substrate_system()

        # Perform system maintenance
        maintenance_log = system.perform_system_maintenance()

        self.assertIn('timestamp', maintenance_log)
        self.assertIn('operations', maintenance_log)
        self.assertEqual(len(maintenance_log['operations']), 3)  # All three folds


def run_comprehensive_tests():
    """Run all test suites and generate report"""

    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestParaconsistentReasoning))
    suite.addTests(loader.loadTestsFromTestCase(TestThreeFoldIntelligence))
    suite.addTests(loader.loadTestsFromTestCase(TestDynamicConsensus))
    suite.addTests(loader.loadTestsFromTestCase(TestGRAILKnowledgeGraph))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Generate report
    print("\n" + "="*70)
    print("COMPREHENSIVE TEST REPORT")
    print("="*70)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")

    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED - System ready for deployment")
    else:
        print("\n❌ SOME TESTS FAILED - Review failures above")

    print("="*70)

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)
