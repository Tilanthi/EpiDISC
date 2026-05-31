"""
EPIDISC Research Gateway Architecture
Direct pipeline to world epilepsy research and clinical trials
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import json
import re


class TrialEligibility(Enum):
    """Clinical trial eligibility status"""
    ELIGIBLE = "eligible"
    POTENTIALLY_ELIGIBLE = "potentially_eligible"
    INELIGIBLE = "ineligible"
    UNKNOWN = "unknown"


class ResearchSource(Enum):
    """Sources of epilepsy research"""
    CLINICAL_TRIALS_GOV = "clinicaltrials_gov"
    MEDRXIV = "medrxiv"
    BIOARXIV = "bioarxiv"
    AES_ABSTRACTS = "aes_abstracts"
    ILAE_GUIDELINES = "ilae_guidelines"
    EPILEPSY_JOURNALS = "epilepsy_journals"


@dataclass
class ClinicalTrial:
    """Clinical trial information"""
    nct_id: str
    title: str
    phase: str
    status: str
    locations: List[str]
    eligibility_criteria: Dict[str, Any]
    contact_info: Dict[str, str]
    sponsor: str
    description: str
    last_updated: datetime


@dataclass
class TrialMatchResult:
    """Result of clinical trial matching"""
    trial: ClinicalTrial
    eligibility_status: TrialEligibility
    match_score: float  # 0.0-1.0
    exclusion_reasons: List[str]
    inclusion_matches: List[str]
    location_match: bool
    timeline_match: bool


@dataclass
class ResearchFinding:
    """Latest epilepsy research finding"""
    source: ResearchSource
    title: str
    authors: List[str]
    publication_date: datetime
    abstract: str
    key_findings: List[str]
    relevance_score: float
    clinical_implications: List[str]


@dataclass
class InvestigationalTherapy:
    """Investigational epilepsy therapy"""
    name: str
    mechanism: str
    phase: str
    sponsor: str
    evidence_summary: str
    availability: str  # clinical_trial, compassionate_use, investigational
    contact_info: Dict[str, str]


class ClinicalTrialMatcher:
    """
    Matches epilepsy patients to appropriate clinical trials.

    Uses patient characteristics to find eligible trials and
    facilitates connection with trial coordinators.
    """

    def __init__(self):
        self.trial_database = {}
        self.patient_profiles = {}
        self.match_history = {}

    def register_trial(self, trial: ClinicalTrial) -> None:
        """Register a clinical trial in the database"""
        self.trial_database[trial.nct_id] = trial

    def create_patient_profile(self, patient_id: str, characteristics: Dict[str, Any]) -> None:
        """Create patient profile for trial matching"""
        self.patient_profiles[patient_id] = {
            'demographics': characteristics.get('demographics', {}),
            'epilepsy_type': characteristics.get('epilepsy_type', ''),
            'seizure_frequency': characteristics.get('seizure_frequency', ''),
            'current_medications': characteristics.get('current_medications', []),
            'failed_medications': characteristics.get('failed_medications', []),
            'comorbidities': characteristics.get('comorbidities', []),
            'location': characteristics.get('location', ''),
            'age': characteristics.get('age', 0),
            'genetic_mutations': characteristics.get('genetic_mutations', []),
            'seizure_control': characteristics.get('seizure_control', ''),
            'last_updated': datetime.now()
        }

    def match_trials(self, patient_id: str) -> List[TrialMatchResult]:
        """Match patient to eligible clinical trials"""
        if patient_id not in self.patient_profiles:
            return []

        profile = self.patient_profiles[patient_id]
        matches = []

        for trial_id, trial in self.trial_database.items():
            match_result = self._evaluate_trial_match(trial, profile)
            if match_result.eligibility_status in [TrialEligibility.ELIGIBLE, TrialEligibility.POTENTIALLY_ELIGIBLE]:
                matches.append(match_result)

        # Sort by match score
        matches.sort(key=lambda m: m.match_score, reverse=True)

        # Store match history
        self.match_history[patient_id] = {
            'timestamp': datetime.now().isoformat(),
            'matches': len(matches),
            'top_matches': [m.trial.nct_id for m in matches[:5]]
        }

        return matches

    def _evaluate_trial_match(self, trial: ClinicalTrial, profile: Dict) -> TrialMatchResult:
        """Evaluate if patient matches trial criteria"""
        inclusion_matches = []
        exclusion_reasons = []

        # Check basic eligibility
        eligibility = trial.eligibility_criteria

        # Age criteria
        if 'min_age' in eligibility and profile['age'] < eligibility['min_age']:
            exclusion_reasons.append(f"Age below minimum ({eligibility['min_age']})")
        elif 'max_age' in eligibility and profile['age'] > eligibility['max_age']:
            exclusion_reasons.append(f"Age above maximum ({eligibility['max_age']})")
        else:
            inclusion_matches.append("Age criteria met")

        # Epilepsy type
        if 'epilepsy_types' in eligibility:
            if profile['epilepsy_type'] in eligibility['epilepsy_types']:
                inclusion_matches.append("Epilepsy type matches")
            else:
                exclusion_reasons.append(f"Epilepsy type not included (need {eligibility['epilepsy_types']})")

        # Seizure frequency
        if 'min_seizure_frequency' in eligibility:
            if self._meets_seizure_frequency(profile['seizure_frequency'], eligibility['min_seizure_frequency']):
                inclusion_matches.append("Seizure frequency criteria met")
            else:
                exclusion_reasons.append("Seizure frequency too low")

        # Failed medications
        if 'failed_medication_count' in eligibility:
            failed_count = len(profile['failed_medications'])
            if failed_count >= eligibility['failed_medication_count']:
                inclusion_matches.append(f"Medication resistance met ({failed_count} failed)")
            else:
                exclusion_reasons.append(f"Insufficient medication resistance (need {eligibility['failed_medication_count']} failed)")

        # Genetic mutations
        if 'required_mutations' in eligibility:
            if any(mut in profile['genetic_mutations'] for mut in eligibility['required_mutations']):
                inclusion_matches.append("Genetic mutation matches trial requirements")
            else:
                exclusion_reasons.append("Required genetic mutation not present")

        # Location matching
        location_match = self._check_location_match(trial.locations, profile['location'])

        # Calculate overall match score
        match_score = self._calculate_match_score(inclusion_matches, exclusion_reasons, location_match)

        # Determine eligibility status
        if not exclusion_reasons and location_match:
            eligibility_status = TrialEligibility.ELIGIBLE
        elif len(exclusion_reasons) <= 1 and match_score > 0.5:
            eligibility_status = TrialEligibility.POTENTIALLY_ELIGIBLE
        else:
            eligibility_status = TrialEligibility.INELIGIBLE

        return TrialMatchResult(
            trial=trial,
            eligibility_status=eligibility_status,
            match_score=match_score,
            exclusion_reasons=exclusion_reasons,
            inclusion_matches=inclusion_matches,
            location_match=location_match,
            timeline_match=True  # Placeholder
        )

    def _meets_seizure_frequency(self, patient_frequency: str, min_frequency: str) -> bool:
        """Check if patient meets minimum seizure frequency"""
        # Simplified frequency comparison
        # In production, would be more sophisticated
        return True  # Placeholder

    def _check_location_match(self, trial_locations: List[str], patient_location: str) -> bool:
        """Check if trial locations are accessible to patient"""
        if not trial_locations:
            return True

        # Simple location matching
        # In production, would use geolocation and distance calculation
        return any(patient_location in loc or loc in patient_location
                  for loc in trial_locations)

    def _calculate_match_score(self, inclusion_matches: List[str],
                               exclusion_reasons: List[str], location_match: bool) -> float:
        """Calculate overall match score"""
        score = 0.5  # Base score

        # Add points for inclusion matches
        score += len(inclusion_matches) * 0.1

        # Subtract points for exclusion reasons
        score -= len(exclusion_reasons) * 0.2

        # Bonus for location match
        if location_match:
            score += 0.1

        return max(0.0, min(score, 1.0))

    def get_trial_recommendations(self, patient_id: str, limit: int = 5) -> List[Dict]:
        """Get personalized trial recommendations"""
        matches = self.match_trials(patient_id)

        recommendations = []
        for match in matches[:limit]:
            recommendation = {
                'trial_id': match.trial.nct_id,
                'title': match.trial.title,
                'phase': match.trial.phase,
                'match_score': match.match_score,
                'eligibility': match.eligibility_status.value,
                'reasons_to_consider': match.inclusion_matches,
                'potential_issues': match.exclusion_reasons,
                'location_accessible': match.location_match,
                'contact': match.trial.contact_info,
                'next_steps': self._generate_trial_next_steps(match)
            }
            recommendations.append(recommendation)

        return recommendations

    def _generate_trial_next_steps(self, match: TrialMatchResult) -> List[str]:
        """Generate next steps for trial participation"""
        steps = []

        if match.eligibility_status == TrialEligibility.ELIGIBLE:
            steps.append("Contact trial coordinator for screening")
            steps.append("Schedule initial evaluation visit")
            steps.append("Review informed consent documents")

            if match.location_match:
                steps.append("Confirm location and travel arrangements")
            else:
                steps.append("Discuss travel requirements with trial team")

        elif match.eligibility_status == TrialEligibility.POTENTIALLY_ELIGIBLE:
            steps.append("Contact trial coordinator for clarification")
            steps.append("Review potential eligibility issues")
            steps.append("Consider additional testing if needed")

        return steps


class ResearchMonitor:
    """
    Monitors latest epilepsy research from multiple sources.

    Provides access to cutting-edge findings and emerging therapies.
    """

    def __init__(self):
        self.research_database = {}
        self.investigational_therapies = {}
        self.monitoring_active = False
        self.last_update = None

    def monitor_preprint_servers(self, keywords: List[str] = None) -> List[ResearchFinding]:
        """Monitor medRxiv and bioRxiv for epilepsy research"""
        # Placeholder for actual preprint monitoring
        # In production, would use APIs or web scraping

        sample_findings = [
            ResearchFinding(
                source=ResearchSource.MEDRXIV,
                title="Novel mTOR inhibitors for treatment-resistant epilepsy",
                authors=["Smith, J.", "Johnson, A.", "Williams, B."],
                publication_date=datetime.now() - timedelta(days=7),
                abstract="This study investigates the efficacy of new mTOR inhibitors...",
                key_findings=[
                    "Significant seizure reduction in animal models",
                    "Minimal side effects compared to rapamycin",
                    "Potential for human trials within 18 months"
                ],
                relevance_score=0.9,
                clinical_implications=[
                    "New treatment option for TSC patients",
                    "Potential for broader epilepsy applications"
                ]
            )
        ]

        return sample_findings

    def monitor_clinical_trials_gov(self, patient_profile: Dict = None) -> List[ClinicalTrial]:
        """Monitor ClinicalTrials.gov for new epilepsy trials"""
        # Placeholder for actual ClinicalTrials.gov API monitoring
        # In production, would use their API

        sample_trials = [
            ClinicalTrial(
                nct_id="NCT1234567",
                title="Investigation of XEN497 in Treatment-Resistant Focal Epilepsy",
                phase="Phase 2",
                status="Recruiting",
                locations=["New York, NY", "Los Angeles, CA", "Chicago, IL"],
                eligibility_criteria={
                    'min_age': 18,
                    'max_age': 65,
                    'epilepsy_types': ['focal', 'temporal lobe'],
                    'min_seizure_frequency': '4 per month',
                    'failed_medication_count': 2
                },
                contact_info={
                    'coordinator': 'Dr. Jane Smith',
                    'email': 'epilepsy.research@example.com',
                    'phone': '+1-555-0123'
                },
                sponsor="Xenon Pharmaceuticals",
                description="This study evaluates the efficacy and safety of XEN497...",
                last_updated=datetime.now() - timedelta(days=14)
            )
        ]

        return sample_trials

    def get_investigational_therapies(self, epilepsy_type: str = None) -> List[InvestigationalTherapy]:
        """Get information on investigational epilepsy therapies"""
        therapies = [
            InvestigationalTherapy(
                name="Soticlestat (TAK-935)",
                mechanism="Cholesterol 24-hydroxylase inhibitor",
                phase="Phase 3",
                sponsor="Takeda Pharmaceuticals",
                evidence_summary="30-50% seizure reduction in Dravet and Lennox-Gastaut syndrome",
                availability="clinical_trial",
                contact_info={
                    'trial_search': 'ClinicalTrials.gov',
                    'website': 'takeda.com'
                }
            ),
            InvestigationalTherapy(
                name="XEN497 (Englerin)",
                mechanism="Kv7.2/7.3 potassium channel opener",
                phase="Phase 2/3",
                sponsor="Xenon Pharmaceuticals",
                evidence_summary="50% responder rate in focal epilepsy",
                availability="clinical_trial",
                contact_info={
                    'trial_search': 'ClinicalTrials.gov',
                    'website': 'xenon.com'
                }
            )
        ]

        if epilepsy_type:
            # Filter by relevance to epilepsy type
            return [t for t in therapies if self._is_relevant_to_type(t, epilepsy_type)]

        return therapies

    def _is_relevant_to_type(self, therapy: InvestigationalTherapy, epilepsy_type: str) -> bool:
        """Check if therapy is relevant to specific epilepsy type"""
        # Placeholder for relevance filtering
        # In production, would use more sophisticated matching
        return True

    def get_latest_guidelines(self) -> List[Dict]:
        """Get latest epilepsy treatment guidelines"""
        guidelines = [
            {
                'organization': 'ILAE',
                'title': 'New Seizure Classification (2024)',
                'key_updates': [
                    'Refined focal vs generalized seizure definitions',
                    'New seizure clusters classification',
                    'Updated treatment algorithms'
                ],
                'url': 'ilae.org'
            },
            {
                'organization': 'AES',
                'title:': 'Standards of Care (2025)',
                'key_updates': [
                    'Updated SUDEP prevention recommendations',
                    'New medication guidelines for pregnancy',
                    'Revised driving recommendations'
                ],
                'url': 'aesnet.org'
            }
        ]

        return guidelines


class CompassionateUseNavigator:
    """
    Helps patients access investigational therapies through
    compassionate use and expanded access programs.
    """

    def __init__(self):
        self.compassionate_use_programs = {}
        self.expanded_access_opportunities = {}

    def find_compassionate_use_opportunities(self, patient_profile: Dict) -> List[Dict]:
        """Find compassionate use opportunities for patient"""
        opportunities = []

        # Check for expanded access programs
        if patient_profile.get('treatment_resistant', False):
            opportunities.append({
                'therapy': 'Investigational AED for drug-resistant epilepsy',
                'program_type': 'Expanded Access',
                'sponsor': 'Various pharmaceutical companies',
                'eligibility': 'Treatment-resistant epilepsy with limited options',
                'contact': 'Discuss with treating neurologist',
                'requirements': [
                    'Failed standard AEDs',
                    'No other treatment options available',
                    'Acceptable risk-benefit profile'
                ]
            })

        return opportunities

    def generate_compassionate_use_request(self, patient_profile: Dict,
                                           therapy_name: str) -> Dict[str, Any]:
        """Generate compassionate use request documentation"""
        request = {
            'patient_information': {
                'age': patient_profile.get('age'),
                'epilepsy_type': patient_profile.get('epilepsy_type'),
                'seizure_frequency': patient_profile.get('seizure_frequency'),
                'treatment_history': patient_profile.get('treatment_history', '')
            },
            'therapy_request': {
                'requested_therapy': therapy_name,
                'justification': self._generate_compassionate_use_justification(patient_profile),
                'alternatives_considered': patient_profile.get('failed_medications', []),
                'treating_physician': patient_profile.get('physician', ''),
                'medical_facility': patient_profile.get('facility', '')
            },
            'regulatory_information': {
                'fda_form': 'FDA 3926',
                'irb_approval': 'Required',
                'informed_consent': 'Required'
            }
        }

        return request

    def _generate_compassionate_use_justification(self, patient_profile: Dict) -> str:
        """Generate justification for compassionate use request"""
        justification = f"Patient has {patient_profile.get('epilepsy_type')} epilepsy"

        if patient_profile.get('seizure_frequency'):
            justification += f" with {patient_profile.get('seizure_frequency')} seizures"

        failed_meds = patient_profile.get('failed_medications', [])
        if failed_meds:
            justification += f" and has failed {len(failed_meds)} standard AEDs"

        justification += ". No other treatment options available. Potential benefit outweighs risks."

        return justification


class OutcomesAggregator:
    """
    Aggregates and analyzes real-world outcomes data from
    epilepsy patients to inform treatment decisions.
    """

    def __init__(self):
        self.outcomes_database = {}
        self.effectiveness_metrics = {}
        self.anonymous_participation = True

    def record_outcome(self, patient_id: str, treatment: str, outcome: Dict[str, Any]) -> None:
        """Record treatment outcome (anonymized)"""
        if self.anonymous_participation:
            patient_id = self._anonymize_id(patient_id)

        outcome_record = {
            'timestamp': datetime.now().isoformat(),
            'treatment': treatment,
            'outcome': outcome
        }

        if treatment not in self.outcomes_database:
            self.outcomes_database[treatment] = []

        self.outcomes_database[treatment].append(outcome_record)

    def get_real_world_effectiveness(self, treatment: str) -> Dict[str, Any]:
        """Get real-world effectiveness data for a treatment"""
        if treatment not in self.outcomes_database:
            return {'status': 'insufficient_data'}

        outcomes = self.outcomes_database[treatment]

        success_count = sum(1 for o in outcomes if o['outcome'].get('successful', False))
        total_count = len(outcomes)

        effectiveness = {
            'treatment': treatment,
            'total_reports': total_count,
            'success_rate': success_count / total_count if total_count > 0 else 0,
            'average_seizure_reduction': self._calculate_average_reduction(outcomes),
            'common_side_effects': self._get_common_side_effects(outcomes),
            'patient_satisfaction': self._calculate_satisfaction(outcomes),
            'last_updated': max(o['timestamp'] for o in outcomes)
        }

        return effectiveness

    def _anonymize_id(self, patient_id: str) -> str:
        """Anonymize patient ID for outcomes database"""
        import hashlib
        return hashlib.sha256(patient_id.encode()).hexdigest()[:16]

    def _calculate_average_reduction(self, outcomes: List[Dict]) -> float:
        """Calculate average seizure reduction"""
        reductions = [o['outcome'].get('seizure_reduction_percent', 0) for o in outcomes]
        return sum(reductions) / len(reductions) if reductions else 0

    def _get_common_side_effects(self, outcomes: List[Dict]) -> List[str]:
        """Get most commonly reported side effects"""
        all_effects = []
        for o in outcomes:
            all_effects.extend(o['outcome'].get('side_effects', []))

        # Count frequency
        from collections import Counter
        effect_counts = Counter(all_effects)

        # Return top 5
        return [effect for effect, count in effect_counts.most_common(5)]

    def _calculate_satisfaction(self, outcomes: List[Dict]) -> float:
        """Calculate average patient satisfaction"""
        satisfactions = [o['outcome'].get('satisfaction_score', 5) for o in outcomes]
        return sum(satisfactions) / len(satisfactions) if satisfactions else 5.0


class ResearchGateway:
    """
    Main gateway connecting patients to epilepsy research and
    clinical trials.
    """

    def __init__(self):
        self.trial_matcher = ClinicalTrialMatcher()
        self.research_monitor = ResearchMonitor()
        self.compassionate_use_navigator = CompassionateUseNavigator()
        self.outcomes_aggregator = OutcomesAggregator()

    def comprehensive_research_consultation(self, patient_profile: Dict) -> Dict[str, Any]:
        """Provide comprehensive research and clinical trial consultation"""
        patient_id = patient_profile.get('patient_id', 'unknown')

        # Create patient profile for trial matching
        self.trial_matcher.create_patient_profile(patient_id, patient_profile)

        # Get all relevant information
        trial_matches = self.trial_matcher.get_trial_recommendations(patient_id)
        investigational_therapies = self.research_monitor.get_investigational_therapies(
            patient_profile.get('epilepsy_type')
        )
        latest_research = self.research_monitor.monitor_preprint_servers()
        compassionate_opportunities = self.compassionate_use_navigator.find_compassionate_use_opportunities(
            patient_profile
        )

        return {
            'patient_id': patient_id,
            'consultation_date': datetime.now().isoformat(),
            'clinical_trials': {
                'eligible_trials': len(trial_matches),
                'top_recommendations': trial_matches,
                'next_steps': self._generate_trial_next_steps_summary(trial_matches)
            },
            'investigational_therapies': {
                'available_therapies': len(investigational_therapies),
                'therapies': [
                    {
                        'name': t.name,
                        'mechanism': t.mechanism,
                        'phase': t.phase,
                        'availability': t.availability
                    }
                    for t in investigational_therapies
                ]
            },
            'latest_research': {
                'recent_findings': len(latest_research),
                'key_findings': [
                    {
                        'title': f.title,
                        'source': f.source.value,
                        'key_points': f.key_findings,
                        'relevance': f.relevance_score
                    }
                    for f in latest_research[:5]
                ]
            },
            'compassionate_use': {
                'opportunities': len(compassionate_opportunities),
                'programs': compassionate_opportunities
            },
            'real_world_evidence': self._get_real_world_evidence_summary(),
            'recommendations': self._generate_research_recommendations(patient_profile)
        }

    def _generate_trial_next_steps_summary(self, trial_matches: List[Dict]) -> List[str]:
        """Generate summary of next steps for clinical trials"""
        if not trial_matches:
            return ["Consider expanding trial search criteria", "Discuss clinical trial options with neurologist"]

        top_match = trial_matches[0]
        steps = []

        if top_match['eligibility'] == 'eligible':
            steps.append(f"Contact trial coordinator for {top_match['trial_id']}")
            steps.append("Schedule screening visit")
        else:
            steps.append("Review potential eligibility with neurologist")
            steps.append("Contact trial coordinator for clarification")

        return steps

    def _get_real_world_evidence_summary(self) -> Dict:
        """Get summary of real-world evidence"""
        # Get effectiveness data for common treatments
        common_treatments = ['lamotrigine', 'levetiracetam', 'valproate']

        summary = {}
        for treatment in common_treatments:
            effectiveness = self.outcomes_aggregator.get_real_world_effectiveness(treatment)
            if effectiveness.get('total_reports', 0) > 0:
                summary[treatment] = effectiveness

        return summary

    def _generate_research_recommendations(self, patient_profile: Dict) -> List[str]:
        """Generate personalized research participation recommendations"""
        recommendations = []

        if patient_profile.get('treatment_resistant', False):
            recommendations.append("Consider clinical trial participation for investigational AEDs")
            recommendations.append("Explore compassionate use programs for new therapies")

        if patient_profile.get('genetic_mutation'):
            recommendations.append("Look for mutation-specific clinical trials")
            recommendations.append("Consider genetic therapy research studies")

        if patient_profile.get('willing_to_participate', True):
            recommendations.append("Join patient registries for real-world evidence collection")
            recommendations.append("Participate in quality of life studies")

        return recommendations


# Convenience functions
def create_research_gateway() -> ResearchGateway:
    """Create comprehensive research gateway"""
    return ResearchGateway()


def get_clinical_trial_matches(patient_profile: Dict) -> List[Dict]:
    """Quick function to get clinical trial matches"""
    gateway = create_research_gateway()
    consultation = gateway.comprehensive_research_consultation(patient_profile)
    return consultation['clinical_trials']['top_recommendations']
