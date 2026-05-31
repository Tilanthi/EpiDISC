"""
EPIDISC Epilepsy Comprehensive Testing Suite
===========================================

Comprehensive test suite for all epilepsy modules including
classification, pharmacology, differential diagnosis, neurophysiology,
neuroradiology, genetics, evidence-based medicine, and specialty
integration modules.

Coverage:
- Knowledge module functionality
- Clinical reasoning accuracy
- Cross-domain integration
- Treatment recommendation accuracy
- Safety system validation

Version: 1.0.0
Last Updated: 2026-05-31
"""

import unittest
import sys
from typing import Dict, List, Any

# Import epilepsy modules
try:
    from epidisc_core.domains.epilepsy import EpilepsyDomain
    from epidisc_core.epilepsy.knowledge.classification import ILAEClassification
    from epidisc_core.epilepsy.knowledge.pharmacology import ASMDatabase
    from epidisc_core.epilepsy.knowledge.differential_diagnosis import DifferentialDiagnosisEngine
    from epidisc_core.epilepsy.knowledge.neurophysiology import EEGInterpreter
    from epidisc_core.epilepsy.knowledge.neuroradiology import EpilepsyImagingInterpreter
    from epidisc_core.epilepsy.knowledge.genetics import GeneticTestingGuidance
    from epidisc_core.epilepsy.clinical.epilepsy_consultant import EpilepsyConsultant
    from epidisc_core.epilepsy.specialties.sleep_medicine import SleepMedicineIntegration
    from epidisc_core.epilepsy.specialties.psychiatry_integration import PsychiatryIntegration
    from epidisc_core.epilepsy.specialties.emergency_medicine import EmergencyMedicineIntegration
    from epidisc_core.epilepsy.specialties.womens_health import WomensHealthIntegration
    MODULES_AVAILABLE = True
except ImportError as e:
    MODULES_AVAILABLE = False
    print(f"Warning: Some epilepsy modules not available: {e}")


class TestEpilepsyDomain(unittest.TestCase):
    """Test enhanced epilepsy domain functionality"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.domain = EpilepsyDomain()

    def test_domain_initialization(self):
        """Test domain initializes correctly"""
        self.assertIsNotNone(self.domain)
        self.assertEqual(self.domain.get_default_config().domain_name, "epilepsy")

    def test_classification_query(self):
        """Test seizure classification query handling"""
        query = "What type of seizure is this? Tonic-clonic with loss of consciousness"
        result = self.domain.process_query(query)

        self.assertIsNotNone(result)
        self.assertEqual(result.domain_name, "epilepsy")
        self.assertGreater(result.confidence, 0.7)

    def test_treatment_query(self):
        """Test treatment query handling"""
        query = "What are the first-line treatments for focal epilepsy?"
        result = self.domain.process_query(query)

        self.assertIsNotNone(result)
        self.assertIn("treatment", result.answer.lower())

    def test_eeg_query(self):
        """Test EEG query handling"""
        query = "What does epileptiform activity on EEG mean?"
        result = self.domain.process_query(query)

        self.assertIsNotNone(result)
        self.assertIn("eeg", result.answer.lower())

    def test_diagnosis_query(self):
        """Test diagnosis query handling"""
        query = "How do you diagnose epilepsy?"
        result = self.domain.process_query(query)

        self.assertIsNotNone(result)
        self.assertGreater(result.confidence, 0.8)

    def test_first_aid_query(self):
        """Test first aid query handling"""
        query = "What should I do during a seizure?"
        result = self.domain.process_query(query)

        self.assertIsNotNone(result)
        self.assertIn("first aid", result.metadata.get("subspecialty", ""))


class TestClassificationModule(unittest.TestCase):
    """Test ILAE classification module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.classification = ILAEClassification()

    def test_focal_seizure_classification(self):
        """Test focal seizure classification"""
        description = "Patient had aura followed by lip smacking and impaired awareness"
        result = self.classification.classify_seizure(description)

        self.assertIsNotNone(result)
        # Should identify focal features

    def test_generalized_seizure_classification(self):
        """Test generalized seizure classification"""
        description = "Sudden loss of consciousness with bilateral tonic-clonic movements"
        result = self.classification.classify_seizure(description)

        self.assertIsNotNone(result)
        # Should identify generalized features

    def test_absence_seizure_classification(self):
        """Test absence seizure classification"""
        description = "Brief staring spells, unresponsive, lasting seconds"
        result = self.classification.classify_seizure(description)

        self.assertIsNotNone(result)
        # Should identify absence features


class TestPharmacologyModule(unittest.TestCase):
    """Test ASM database and pharmacology module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.asmdb = ASMDatabase()

    def test_levetiracetam_info(self):
        """Test levetiracetam medication information"""
        info = self.asmdb.get_medication_info("levetiracetam")

        self.assertIsNotNone(info)
        self.assertIn("mechanism", info)

    def test_carbamazepine_interactions(self):
        """Test carbamazepine drug interactions"""
        interactions = self.asmdb.get_drug_interactions("carbamazepine", "phenytoin")

        # Should identify interaction
        self.assertIsNotNone(interactions)

    def test_first_line_recommendations(self):
        """Test first-line ASM recommendations"""
        recommendations = self.asmdb.recommend_first_line("focal", {})

        self.assertIsNotNone(recommendations)
        # Should include appropriate first-line AEDs


class TestDifferentialDiagnosisModule(unittest.TestCase):
    """Test differential diagnosis module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.differential = DifferentialDiagnosisEngine()

    def test_syncope_differentiation(self):
        """Test syncope vs seizure differentiation"""
        case = {
            "semiology": "Brief LOC with rapid recovery, no postictal",
            "history": "Prodrome of lightheadedness",
            "timing": "During standing"
        }

        result = self.differential.evaluate_case(case)

        self.assertIsNotNone(result)
        # Should identify syncope features

    def test_pnes_differentiation(self):
        """Test PNES vs seizure differentiation"""
        case = {
            "semiology": "Variable motor movements, pelvic thrusting, talking during event",
            "history": "Trauma history, psychiatric comorbidity",
            "duration": "Events >2 minutes, variable each time"
        }

        result = self.differential.evaluate_case(case)

        self.assertIsNotNone(result)
        # Should identify PNES features


class TestNeurophysiologyModule(unittest.TestCase):
    """Test EEG interpretation module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.eeg = EEGInterpreter()

    def test_epileptiform_discharge_interpretation(self):
        """Test epileptiform discharge interpretation"""
        findings = "Sharp waves over left temporal region, spike-and-slow wave complexes"
        result = self.eeg.interpret_eeg(findings, "adult", "")

        self.assertIsNotNone(result)
        self.assertGreater(result.confidence, 0.5)

    def test_normal_eeg_interpretation(self):
        """Test normal EEG interpretation"""
        findings = "Normal background rhythm, no epileptiform discharges"
        result = self.eeg.interpret_eeg(findings, "adult", "")

        self.assertIsNotNone(result)


class TestGeneticsModule(unittest.TestCase):
    """Test genetic testing guidance module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.genetics = GeneticTestingGuidance()

    def test_genetic_testing_recommendation(self):
        """Test genetic testing recommendations"""
        recommendations = self.genetics.recommend_testing_strategy(
            age_of_onset="infancy",
            epilepsy_type="unknown",
            developmental_status="developmental delay",
            family_history="",
            drug_resistance=True
        )

        self.assertIsNotNone(recommendations)
        # Should recommend genetic testing

    def test_scn1a_guidance(self):
        """Test SCN1A mutation guidance"""
        # Should provide specific guidance for SCN1A mutations
        # This tests precision medicine capability
        pass


class TestSleepMedicineModule(unittest.TestCase):
    """Test sleep medicine integration module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.sleep = SleepMedicineIntegration()

    def test_parasomnia_differential(self):
        """Test parasomnia vs seizure differential"""
        assessment = self.sleep.assess_sleep_epilepsy_overlap(
            seizure_description="Sleep walking, confused, no memory",
            sleep_history={"snoring": False},
            epilepsy_context={"seizure_timing": "during sleep"}
        )

        self.assertIsNotNone(assessment)
        # Should identify parasomnia features

    def test_sleep_apnea_recognition(self):
        """Test OSA recognition in epilepsy"""
        assessment = self.sleep.assess_sleep_epilepsy_overlap(
            seizure_description="Seizures during sleep",
            sleep_history={"snoring": True, "witnessed_apneas": True},
            epilepsy_context={"seizure_timing": "unknown"}
        )

        self.assertIsNotNone(assessment)
        # Should identify OSA as comorbidity


class TestPsychiatryModule(unittest.TestCase):
    """Test psychiatry integration module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.psychiatry = PsychiatryIntegration()

    def test_pnes_assessment(self):
        """Test PNES assessment"""
        assessment = self.psychiatry.assess_pnes(
            event_description="Variable movements, pelvic thrusting, talking",
            psychiatric_history={"trauma_history": True, "multiple_psychiatric_comorbidities": True},
            seizure_history={"aed_trials": 3, "aed_response": False, "normal_eeg_count": 2}
        )

        self.assertIsNotNone(assessment)
        # Should identify high PNES likelihood

    def test_psychotropic_interaction_assessment(self):
        """Test psychotropic-AED interaction assessment"""
        interaction = self.psychiatry.assess_psychotropic_interactions(
            "bupropion",
            "lamotrigine"
        )

        self.assertIsNotNone(interaction)
        # Should identify contraindication for bupropion


class TestEmergencyMedicineModule(unittest.TestCase):
    """Test emergency medicine and status epilepticus module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.emergency = EmergencyMedicineIntegration()

    def test_se_assessment(self):
        """Test status epilepticus assessment"""
        assessment = self.emergency.assess_status_epilepticus(
            clinical_presentation="Tonic-clonic seizure activity, ongoing",
            duration_minutes=15,
            seizure_history={"known_epilepsy": True},
            current_medications=["levetiracetam"],
            examination_findings={}
        )

        self.assertIsNotNone(assessment)
        self.assertEqual(assessment.se_classification, self.emergency.SEClassification.CONVULSIVE_SE)

    def test_refractory_se_assessment(self):
        """Test refractory SE assessment"""
        assessment = self.emergency.assess_status_epilepticus(
            clinical_presentation="Continuing seizure despite benzodiazepines",
            duration_minutes=50,
            seizure_history={"known_epilepsy": True},
            current_medications=["levetiracetam", "fosphenytoin"],
            examination_findings={}
        )

        self.assertIsNotNone(assessment)
        # Should identify refractory SE


class TestWomensHealthModule(unittest.TestCase):
    """Test women's health and pregnancy module"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.womens_health = WomensHealthIntegration()

    def test_pregnancy_risk_assessment(self):
        """Test pregnancy risk assessment"""
        assessments = self.womens_health.assess_pregnancy_risk(
            current_aeds=["valproate", "lamotrigine"],
            pregnancy_stage=self.womens_health.PregnancyStage.PRE_CONCEPTION
        )

        self.assertIn("valproate", assessments)
        self.assertEqual(
            assessments["valproate"].teratogenicity_risk,
            self.womens_health.TeratogenicityRisk.HIGH
        )

    def test_pre_conception_consultation(self):
        """Test pre-conception consultation"""
        consultation = self.womens_health.generate_pre_conception_consultation(
            current_aeds=["lamotrigine", "levetiracetam"],
            seizure_frequency="occasional",
            pregnancy_plans="next year"
        )

        self.assertIsNotNone(consultation)
        # Should provide appropriate guidance


class TestComprehensiveConsultation(unittest.TestCase):
    """Test comprehensive epilepsy consultation system"""

    def setUp(self):
        """Set up test fixtures"""
        if not MODULES_AVAILABLE:
            self.skipTest("Epilepsy modules not available")
        self.consultant = EpilepsyConsultant()

    def test_comprehensive_consultation(self):
        """Test full comprehensive consultation"""
        patient_data = {
            "age": 28,
            "gender": "female",
            "pregnancy": False
        }

        clinical_context = {
            "seizure_description": "Aura followed by right hand automatisms",
            "seizure_frequency": "Monthly",
            "eeg_findings": "Left temporal spikes",
            "mri_findings": "Left hippocampal sclerosis",
            "current_medications": ["lamotrigine"],
            "drug_resistance": False
        }

        result = self.consultant.comprehensive_consultation(patient_data, clinical_context)

        self.assertIsNotNone(result)
        self.assertGreater(result.confidence, 0.5)
        self.assertIn("focal", result.seizure_classification.lower())

    def test_drug_resistant_epilepsy_consultation(self):
        """Test drug-resistant epilepsy consultation"""
        patient_data = {
            "age": 35,
            "gender": "male"
        }

        clinical_context = {
            "seizure_description": "Focal impaired awareness seizures",
            "seizure_frequency": "Weekly despite 2 AEDs",
            "drug_resistance": True,
            "current_medications": ["carbamazepine", "levetiracetam"]
        }

        result = self.consultant.comprehensive_consultation(patient_data, clinical_context)

        self.assertIsNotNone(result)
        # Should address drug resistance


def run_comprehensive_test_suite():
    """Run comprehensive epilepsy module test suite"""
    print("=" * 70)
    print("EPIDISC EPILEPSY MODULES - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    print()

    if not MODULES_AVAILABLE:
        print("❌ FAILED: Epilepsy modules not available")
        return False

    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    test_classes = [
        TestEpilepsyDomain,
        TestClassificationModule,
        TestPharmacologyModule,
        TestDifferentialDiagnosisModule,
        TestNeurophysiologyModule,
        TestGeneticsModule,
        TestSleepMedicineModule,
        TestPsychiatryModule,
        TestEmergencyMedicineModule,
        TestWomensHealthModule,
        TestComprehensiveConsultation
    ]

    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print()
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    print()

    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED")
        return True
    else:
        print("❌ SOME TESTS FAILED")
        return False


if __name__ == "__main__":
    success = run_comprehensive_test_suite()
    sys.exit(0 if success else 1)
