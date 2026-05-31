"""
EPIDISC Therapeutic Alliance System
Continuous care partnership and patient empowerment
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import json
from collections import defaultdict


class AllianceStatus(Enum):
    """Therapeutic alliance relationship status"""
    ACTIVE = "active"
    ENGAGED = "engaged"
    NEEDS_FOLLOW_UP = "needs_follow_up"
    DISENGAGED = "disengaged"


class CheckInPriority(Enum):
    """Priority levels for check-ins"""
    ROUTINE = "routine"
    MONITORING = "monitoring"
    ATTENTION = "attention"
    URGENT = "urgent"


@dataclass
class CheckInSchedule:
    """Scheduled check-in configuration"""
    frequency_days: int
    priority: CheckInPriority
    topics: List[str]
    assessments: List[str]
    reminder_methods: List[str]


@dataclass
class CheckInSession:
    """A check-in session record"""
    timestamp: datetime
    priority: CheckInPriority
    duration_minutes: int
    topics_discussed: List[str]
    concerns_raised: List[str]
    patient_responses: Dict[str, Any]
    provider_notes: str
    follow_up_needed: bool
    next_check_in: datetime


@dataclass
class EducationModule:
    """Patient education module"""
    module_id: str
    title: str
    content: str
    learning_style: str
    difficulty_level: str
    estimated_time_minutes: int
    prerequisites: List[str]
    assessment_questions: List[Dict]


@dataclass
class SelfManagementSkill:
    """Self-management skill for patient empowerment"""
    skill_name: str
    description: str
    mastery_level: float  # 0.0-1.0
    practice_frequency: str
    barriers: List[str]
    facilitators: List[str]
    goals: List[str]


class ContinuousCheckInSystem:
    """
    Automated check-in system for between-visit monitoring.

    Provides proactive outreach and pattern change detection.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.check_in_schedule = None
        self.check_in_history = []
        self.pending_check_ins = []
        self.alert_thresholds = {}

    def establish_check_in_schedule(self, schedule: CheckInSchedule) -> None:
        """Establish regular check-in schedule"""
        self.check_in_schedule = schedule

    def generate_check_in(self, current_status: Dict) -> Dict[str, Any]:
        """Generate automated check-in based on current patient status"""
        if not self.check_in_schedule:
            return {'status': 'no_schedule'}

        priority = self._determine_check_in_priority(current_status)
        topics = self._select_check_in_topics(priority, current_status)

        check_in = {
            'patient_id': self.patient_id,
            'timestamp': datetime.now().isoformat(),
            'priority': priority.value,
            'estimated_duration': self._estimate_duration(priority),
            'topics': topics,
            'questions': self._generate_check_in_questions(topics, current_status),
            'assessments': self._select_assessments(priority),
            'urgent_alerts': self._check_for_urgent_issues(current_status),
            'follow_up_schedule': self._schedule_follow_up(priority)
        }

        return check_in

    def _determine_check_in_priority(self, current_status: Dict) -> CheckInPriority:
        """Determine priority level for check-in"""
        # Check for urgent indicators
        urgent_indicators = [
            current_status.get('recent_seizures', 0) > 3,
            current_status.get('medication_adherence', 1.0) < 0.5,
            current_status.get('depression_score', 0) > 15,
            current_status.get('suicidal_ideation', False)
        ]

        if any(urgent_indicators):
            return CheckInPriority.URGENT

        # Check for attention indicators
        attention_indicators = [
            current_status.get('recent_seizures', 0) > 0,
            current_status.get('medication_adherence', 1.0) < 0.8,
            current_status.get('stress_level', 5) > 7,
            current_status.get('side_effects', [])
        ]

        if any(attention_indicators):
            return CheckInPriority.ATTENTION

        # Check for monitoring indicators
        monitoring_indicators = [
            current_status.get('seizure_frequency_change', 0) > 0,
            current_status.get('medication_change', False),
            current_status.get('life_event', False)
        ]

        if any(monitoring_indicators):
            return CheckInPriority.MONITORING

        return CheckInPriority.ROUTINE

    def _select_check_in_topics(self, priority: CheckInPriority, status: Dict) -> List[str]:
        """Select topics for check-in based on priority and status"""
        topics = []

        # Core topics for all check-ins
        topics.extend([
            "Seizure activity since last contact",
            "Medication adherence",
            "Overall well-being"
        ])

        # Priority-specific topics
        if priority in [CheckInPriority.ATTENTION, CheckInPriority.URGENT]:
            if status.get('recent_seizures', 0) > 0:
                topics.append("Recent seizure review")
            if status.get('medication_adherence', 1.0) < 0.8:
                topics.append("Medication challenges")
            if status.get('depression_score', 0) > 10:
                topics.append("Mental health support")
            if status.get('stress_level', 5) > 7:
                topics.append("Stress management")

        return topics

    def _generate_check_in_questions(self, topics: List[str], status: Dict) -> List[Dict]:
        """Generate specific questions for check-in topics"""
        questions = []

        for topic in topics:
            if "seizure" in topic.lower():
                questions.append({
                    'topic': topic,
                    'question': "Have you had any seizures since we last spoke?",
                    'type': 'yes_no',
                    'follow_up': "If yes, please describe what happened"
                })
                questions.append({
                    'topic': topic,
                    'question': "Have you noticed any warning signs before seizures?",
                    'type': 'multiple_choice',
                    'options': ['Yes, consistent pattern', 'Yes, sometimes', 'No']
                })

            elif "medication" in topic.lower():
                questions.append({
                    'topic': topic,
                    'question': "How many medication doses have you missed in the past week?",
                    'type': 'number',
                    'range': [0, 7]
                })
                questions.append({
                    'topic': topic,
                    'question': "Have you experienced any side effects?",
                    'type': 'yes_no_detail',
                    'follow_up': "Please describe any side effects"
                })

            elif "well-being" in topic.lower():
                questions.append({
                    'topic': topic,
                    'question': "How would you rate your overall mood today?",
                    'type': 'scale',
                    'range': [1, 10]
                })
                questions.append({
                    'topic': topic,
                    'question': "How has your sleep been lately?",
                    'type': 'multiple_choice',
                    'options': ['Good', 'Fair', 'Poor']
                })

        return questions

    def _select_assessments(self, priority: CheckInPriority) -> List[str]:
        """Select assessments for check-in"""
        assessments = []

        if priority in [CheckInPriority.ATTENTION, CheckInPriority.URGENT]:
            assessments.extend([
                "PHQ-9 depression screening",
                "GAD-7 anxiety screening",
                "Seizure diary review",
                "Medication adherence assessment"
            ])
        else:
            assessments.extend([
                "Brief mood check",
                "Seizure frequency update",
                "Basic medication review"
            ])

        return assessments

    def _check_for_urgent_issues(self, status: Dict) -> List[Dict]:
        """Check for urgent issues requiring immediate attention"""
        urgent_issues = []

        if status.get('recent_seizures', 0) >= 3:
            urgent_issues.append({
                'issue': 'Seizure cluster',
                'severity': 'high',
                'recommendation': 'Contact neurologist today'
            })

        if status.get('suicidal_ideation', False):
            urgent_issues.append({
                'issue': 'Suicidal ideation',
                'severity': 'critical',
                'recommendation': 'Emergency mental health evaluation'
            })

        if status.get('medication_adherence', 1.0) < 0.3:
            urgent_issues.append({
                'issue': 'Severe medication nonadherence',
                'severity': 'high',
                'recommendation': 'Immediate intervention needed'
            })

        return urgent_issues

    def _schedule_follow_up(self, priority: CheckInPriority) -> Dict:
        """Schedule follow-up based on priority"""
        schedules = {
            CheckInPriority.URGENT: "Within 24 hours",
            CheckInPriority.ATTENTION: "Within 3 days",
            CheckInPriority.MONITORING: "Within 1 week",
            CheckInPriority.ROUTINE: "Next scheduled check-in"
        }

        return {
            'follow_up_timeframe': schedules[priority],
            'automatic_reminder': True
        }

    def _estimate_duration(self, priority: CheckInPriority) -> int:
        """Estimate check-in duration in minutes"""
        durations = {
            CheckInPriority.URGENT: 30,
            CheckInPriority.ATTENTION: 20,
            CheckInPriority.MONITORING: 15,
            CheckInPriority.ROUTINE: 10
        }
        return durations[priority]


class PatientEducationEngine:
    """
    Personalized patient education system.

    Delivers epilepsy education tailored to learning style,
    literacy level, and individual needs.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.learning_profile = {}
        self.education_history = []
        self.available_modules = self._initialize_education_modules()

    def establish_learning_profile(self, profile: Dict) -> None:
        """Establish patient learning profile"""
        self.learning_profile = {
            'learning_style': profile.get('learning_style', 'visual'),  # visual, auditory, kinesthetic
            'literacy_level': profile.get('literacy_level', 'average'),
            'language_preference': profile.get('language', 'english'),
            'attention_span': profile.get('attention_span', 'medium'),
            'interests': profile.get('interests', []),
            'technology_comfort': profile.get('technology_comfort', 'moderate')
        }

    def recommend_education(self, current_needs: Dict) -> List[Dict]:
        """Recommend personalized education modules"""
        recommendations = []

        # Analyze current educational needs
        if current_needs.get('newly_diagnosed', False):
            recommendations.extend(self._get_foundation_modules())

        if current_needs.get('medication_starting', False):
            recommendations.extend(self._get_medication_education(current_needs.get('medication_name')))

        if current_needs.get('seizure_type', '') == 'focal':
            recommendations.extend(self._get_focal_seizure_modules())

        if current_needs.get('treatment_resistant', False):
            recommendations.extend(self._get_advanced_treatment_modules())

        if current_needs.get('pregnancy_planning', False):
            recommendations.extend(self._get_reproductive_health_modules())

        # Personalize based on learning profile
        personalized_recs = []
        for rec in recommendations:
            personalized = self._personalize_for_learning_profile(rec)
            personalized_recs.append(personalized)

        return personalized_recs

    def _get_foundation_modules(self) -> List[Dict]:
        """Get foundational education modules for newly diagnosed"""
        return [
            {
                'module_id': 'epilepsy_basics',
                'title': 'Understanding Epilepsy',
                'description': 'Basic information about epilepsy and seizures',
                'priority': 'high',
                'estimated_time': 20
            },
            {
                'module_id': 'seizure_first_aid',
                'title': 'Seizure First Aid',
                'description': 'What to do when someone has a seizure',
                'priority': 'high',
                'estimated_time': 15
            },
            {
                'module_id': 'medication_basics',
                'title': 'Understanding Your Medication',
                'description': 'Basic information about epilepsy medications',
                'priority': 'high',
                'estimated_time': 25
            }
        ]

    def _get_medication_education(self, medication_name: str = None) -> List[Dict]:
        """Get medication-specific education"""
        medications = {
            'lamotrigine': {
                'module_id': 'lamotrigine_education',
                'title': 'Lamotrigine: What You Need to Know',
                'description': 'Comprehensive guide to lamotrigine use',
                'key_topics': ['Titration schedule', 'Rash prevention', 'Side effects', 'Drug interactions']
            },
            'levetiracetam': {
                'module_id': 'levetiracetam_education',
                'title': 'Levetiracetam: What You Need to Know',
                'description': 'Comprehensive guide to levetiracetam use',
                'key_topics': ['Dosing', 'Behavioral side effects', 'Cognitive effects', 'Stopping safely']
            }
        }

        if medication_name and medication_name.lower() in medications:
            return [medications[medication_name.lower()]]

        return list(medications.values())

    def _get_focal_seizure_modules(self) -> List[Dict]:
        """Get education specific to focal seizures"""
        return [
            {
                'module_id': 'focal_seizures',
                'title': 'Understanding Focal Seizures',
                'description': 'Information about focal seizure types and treatment',
                'estimated_time': 20
            },
            {
                'module_id': 'temporal_lobe_epilepsy',
                'title': 'Temporal Lobe Epilepsy',
                'description': 'Specialized information about TLE',
                'estimated_time': 15
            }
        ]

    def _get_advanced_treatment_modules(self) -> List[Dict]:
        """Get education about advanced treatment options"""
        return [
            {
                'module_id': 'surgery_evaluation',
                'title': 'Epilepsy Surgery Evaluation',
                'description': 'What to expect during surgical evaluation',
                'estimated_time': 30
            },
            {
                'module_id': 'neurostimulation',
                'title': 'Neurostimulation Options',
                'description': 'VNS, DBS, and RNS therapies explained',
                'estimated_time': 25
            },
            {
                'module_id': 'ketogenic_diet',
                'title': 'Dietary Therapies',
                'description': 'Ketogenic diet and other dietary options',
                'estimated_time': 20
            }
        ]

    def _get_reproductive_health_modules(self) -> List[Dict]:
        """Get reproductive health education"""
        return [
            {
                'module_id': 'pregnancy_planning',
                'title': 'Epilepsy and Pregnancy Planning',
                'description': 'Pre-conception counseling and pregnancy management',
                'estimated_time': 30
            },
            {
                'module_id': 'contraception',
                'title': 'Contraception and AED Interactions',
                'description': 'Birth control options with epilepsy medications',
                'estimated_time': 20
            }
        ]

    def _personalize_for_learning_profile(self, module: Dict) -> Dict:
        """Personalize module for patient's learning profile"""
        style = self.learning_profile.get('learning_style', 'visual')

        personalized = module.copy()

        if style == 'visual':
            personalized['delivery_format'] = 'Video with graphics and illustrations'
            personalized['supplementary_materials'] = ['Infographics', 'Diagrams', 'Charts']
        elif style == 'auditory':
            personalized['delivery_format'] = 'Audio with verbal explanations'
            personalized['supplementary_materials'] = ['Podcasts', 'Audio guides', 'Verbal instructions']
        elif style == 'kinesthetic':
            personalized['delivery_format'] = 'Interactive activities and demonstrations'
            personalized['supplementary_materials'] = ['Hands-on practice', 'Interactive exercises', 'Skill building']

        return personalized

    def _initialize_education_modules(self) -> Dict:
        """Initialize available education modules"""
        return {
            'epilepsy_basics': EducationModule(
                module_id='epilepsy_basics',
                title='Understanding Epilepsy',
                content='Comprehensive epilepsy education content...',
                learning_style='universal',
                difficulty_level='beginner',
                estimated_time_minutes=20,
                prerequisites=[],
                assessment_questions=[]
            )
            # Additional modules would be initialized here
        }


class PatientEmpowermentEngine:
    """
    Patient empowerment and self-management skill building.

    Helps patients develop skills for independent epilepsy management.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.skill_assessments = {}
        self.skill_building_plans = {}
        self.empowerment_goals = []

    def assess_self_management_skills(self) -> Dict[str, Any]:
        """Comprehensive assessment of self-management skills"""
        skills = {
            'medication_management': self._assess_medication_management_skill(),
            'seizure_recording': self._assess_seizure_recording_skill(),
            'trigger_identification': self._assess_trigger_identification_skill(),
            'emergency_response': self._assess_emergency_response_skill(),
            'communication_with_providers': self._assess_communication_skill(),
            'lifestyle_management': self._assess_lifestyle_skill(),
            'stress_management': self._assess_stress_management_skill(),
            'sleep_optimization': self._assess_sleep_skill()
        }

        overall_score = sum(s.get('score', 0) for s in skills.values()) / len(skills)

        return {
            'overall_score': overall_score,
            'skill_areas': skills,
            'strengths': [s for s, skill in skills.items() if skill.get('score', 0) >= 0.7],
            'areas_for_improvement': [s for s, skill in skills.items() if skill.get('score', 0) < 0.7],
            'recommended_focus': self._prioritize_skill_development(skills)
        }

    def _assess_medication_management_skill(self) -> Dict:
        """Assess medication management skills"""
        return {
            'score': 0.6,  # Would be calculated from actual assessment
            'components': {
                'adherence': 0.7,
                'timing': 0.6,
                'side_effect_monitoring': 0.5,
                'refill_management': 0.6
            },
            'barriers': ['Forgetfulness', 'Complex schedule'],
            'recommendations': ['Use pill organizer', 'Set phone reminders']
        }

    def _assess_seizure_recording_skill(self) -> Dict:
        """Assess seizure recording skills"""
        return {
            'score': 0.5,
            'components': {
                'timeliness': 0.6,
                'detail': 0.4,
                'consistency': 0.5
            },
            'barriers': ['Forgetfulness', 'Unsure what to record'],
            'recommendations': ['Use seizure diary app', 'Record immediately after events']
        }

    def _assess_trigger_identification_skill(self) -> Dict:
        """Assess trigger identification skills"""
        return {
            'score': 0.4,
            'components': {
                'pattern_recognition': 0.4,
                'environmental_awareness': 0.3,
                'lifestyle_tracking': 0.5
            },
            'barriers': ['Difficulty recognizing patterns'],
            'recommendations': ['Use digital tracking tools', 'Review patterns monthly']
        }

    def _assess_emergency_response_skill(self) -> Dict:
        """Assess emergency response skills"""
        return {
            'score': 0.7,
            'components': {
                'seizure_first_aid': 0.8,
                'rescue_medication_use': 0.7,
                'emergency_contact': 0.6
            },
            'barriers': ['Family unfamiliar with first aid'],
            'recommendations': ['Teach family seizure first aid', 'Keep rescue med accessible']
        }

    def _assess_communication_skill(self) -> Dict:
        """Assess communication with healthcare providers"""
        return {
            'score': 0.6,
            'components': {
                'symptom_reporting': 0.7,
                'question_asking': 0.5,
                'concern_expressing': 0.6
            },
            'barriers': ['Unsure what to ask'],
            'recommendations': ['Prepare questions before appointments', 'Bring seizure diary']
        }

    def _assess_lifestyle_skill(self) -> Dict:
        """Assess lifestyle management skills"""
        return {
            'score': 0.5,
            'components': {
                'sleep_management': 0.5,
                'stress_management': 0.5,
                'alcohol_management': 0.6,
                'activity_regulation': 0.4
            },
            'barriers': ['Difficulty maintaining routines'],
            'recommendations': ['Focus on one lifestyle factor at a time']
        }

    def _assess_stress_management_skill(self) -> Dict:
        """Assess stress management skills"""
        return {
            'score': 0.4,
            'components': {
                'stress_recognition': 0.5,
                'stress_reduction_techniques': 0.3,
                'relaxation_practice': 0.4
            },
            'barriers': ['Limited stress management techniques'],
            'recommendations': ['Learn stress reduction techniques', 'Practice daily']
        }

    def _assess_sleep_skill(self) -> Dict:
        """Assess sleep optimization skills"""
        return {
            'score': 0.5,
            'components': {
                'sleep_schedule': 0.6,
                'sleep_hygiene': 0.4,
                'sleep_quality_monitoring': 0.5
            },
            'barriers': ['Irregular schedule'],
            'recommendations': ['Establish consistent sleep schedule', 'Practice sleep hygiene']
        }

    def _prioritize_skill_development(self, skills: Dict) -> List[str]:
        """Prioritize which skills to develop first"""
        scores = {name: skill.get('score', 0) for name, skill in skills.items()}

        # Sort by score (lowest first)
        prioritized = sorted(scores.items(), key=lambda x: x[1])

        # Return top 3 priority areas
        return [skill[0] for skill in prioritized[:3]]

    def create_skill_building_plan(self, skill_area: str) -> Dict[str, Any]:
        """Create personalized skill building plan"""
        plan = {
            'skill_area': skill_area,
            'current_level': self._get_current_skill_level(skill_area),
            'target_level': 0.8,  # Target proficiency
            'building_steps': self._generate_skill_building_steps(skill_area),
            'timeline_weeks': self._estimate_skill_building_timeline(skill_area),
            'resources': self._identify_skill_building_resources(skill_area),
            'success_metrics': self._define_success_metrics(skill_area),
            'barriers': self._identify_common_barriers(skill_area),
            'support_needed': self._identify_support_needs(skill_area)
        }

        return plan

    def _get_current_skill_level(self, skill_area: str) -> float:
        """Get current skill level for area"""
        assessment = self.assess_self_management_skills()
        return assessment['skill_areas'].get(skill_area, {}).get('score', 0.0)

    def _generate_skill_building_steps(self, skill_area: str) -> List[str]:
        """Generate step-by-step skill building plan"""
        steps = {
            'medication_management': [
                'Week 1: Set up medication reminder system',
                'Week 2: Establish routine medication times',
                'Week 3: Learn to recognize and report side effects',
                'Week 4: Practice medication organization system',
                'Week 5: Develop refill management system'
            ],
            'seizure_recording': [
                'Week 1: Choose seizure diary method',
                'Week 2: Practice recording immediately after events',
                'Week 3: Learn what details to record',
                'Week 4: Establish daily review routine',
                'Week 5: Learn to identify patterns'
            ],
            'trigger_identification': [
                'Week 1: List potential triggers',
                'Week 2: Start trigger tracking',
                'Week 3: Review for trigger patterns',
                'Week 4: Test trigger avoidance strategies',
                'Week 5: Develop personalized trigger management plan'
            ]
        }

        return steps.get(skill_area, ['Skill building steps to be determined'])

    def _estimate_skill_building_timeline(self, skill_area: str) -> int:
        """Estimate weeks needed to build skill"""
        timelines = {
            'medication_management': 6,
            'seizure_recording': 4,
            'trigger_identification': 8,
            'emergency_response': 4,
            'communication_with_providers': 6,
            'lifestyle_management': 12,
            'stress_management': 10,
            'sleep_optimization': 8
        }
        return timelines.get(skill_area, 8)

    def _identify_skill_building_resources(self, skill_area: str) -> List[str]:
        """Identify resources for skill building"""
        resources = {
            'medication_management': ['Pill organizer', 'Phone reminder apps', 'Medication tracking sheets'],
            'seizure_recording': ['Seizure diary app', 'Paper seizure diary', 'Calendar system'],
            'trigger_identification': ['Trigger tracking app', 'Journal', 'Pattern analysis tools']
        }
        return resources.get(skill_area, ['Generic skill building resources'])

    def _define_success_metrics(self, skill_area: str) -> List[str]:
        """Define metrics for skill building success"""
        metrics = {
            'medication_management': [
                '100% medication adherence for 4 weeks',
                'Consistent timing within 1 hour of scheduled time',
                'Proactive side effect reporting'
            ],
            'seizure_recording': [
                'Record all seizures within 24 hours',
                'Include complete details for each event',
                'Consistent recording for 8 weeks'
            ]
        }
        return metrics.get(skill_area, ['Successful skill demonstration'])

    def _identify_common_barriers(self, skill_area: str) -> List[str]:
        """Identify common barriers to skill development"""
        barriers = {
            'medication_management': ['Forgetfulness', 'Complex schedules', 'Side effects'],
            'seizure_recording': ['Forgetfulness', 'Post-seizure confusion', 'Unsure what to record']
        }
        return barriers.get(skill_area, ['Common barriers to be identified'])

    def _identify_support_needs(self, skill_area: str) -> List[str]:
        """Identify support needs for skill development"""
        support = {
            'medication_management': ['Reminder system setup', 'Family support for adherence'],
            'seizure_recording': ['Easy-to-use diary system', 'Family assistance with documentation']
        }
        return support.get(skill_area, ['Support needs to be determined'])


class CommunityConnectionManager:
    """
    Manages connections to epilepsy support communities and peer support.

    Facilitates peer matching and community engagement.
    """

    def __init__(self):
        self.peer_database = {}
        self.support_groups = {}
        self.community_resources = {}

    def find_peer_matches(self, patient_profile: Dict) -> List[Dict]:
        """Find matched peers for support"""
        matches = []

        # Find peers with similar experiences
        for peer_id, peer_profile in self.peer_database.items():
            similarity_score = self._calculate_peer_similarity(patient_profile, peer_profile)

            if similarity_score > 0.6:  # 60% similarity threshold
                matches.append({
                    'peer_id': peer_id,
                    'similarity_score': similarity_score,
                    'shared_experiences': self._identify_shared_experiences(patient_profile, peer_profile),
                    'connection_type': self._determine_connection_type(patient_profile, peer_profile)
                })

        # Sort by similarity score
        matches.sort(key=lambda m: m['similarity_score'], reverse=True)

        return matches[:5]  # Return top 5 matches

    def _calculate_peer_similarity(self, profile1: Dict, profile2: Dict) -> float:
        """Calculate similarity between two patient profiles"""
        similarity = 0.0

        # Epilepsy type match
        if profile1.get('epilepsy_type') == profile2.get('epilepsy_type'):
            similarity += 0.3

        # Age proximity (within 10 years)
        age_diff = abs(profile1.get('age', 0) - profile2.get('age', 0))
        if age_diff <= 10:
            similarity += 0.2

        # Similar treatment experiences
        meds1 = set(profile1.get('current_medications', []))
        meds2 = set(profile2.get('current_medications', []))
        if meds1 & meds2:  # Overlapping medications
            similarity += 0.2

        # Similar life circumstances
        if profile1.get('life_stage') == profile2.get('life_stage'):
            similarity += 0.2

        # Geographic proximity
        if profile1.get('location', '')[:5] == profile2.get('location', '')[:5]:  # Same postal code area
            similarity += 0.1

        return min(similarity, 1.0)

    def _identify_shared_experiences(self, profile1: Dict, profile2: Dict) -> List[str]:
        """Identify shared experiences between peers"""
        shared = []

        if profile1.get('epilepsy_type') == profile2.get('epilepsy_type'):
            shared.append(f"Both have {profile1.get('epilepsy_type')}")

        if profile1.get('treatment_resistant') and profile2.get('treatment_resistant'):
            shared.append("Both treatment-resistant")

        meds1 = set(profile1.get('current_medications', []))
        meds2 = set(profile2.get('current_medications', []))
        shared_meds = meds1 & meds2
        if shared_meds:
            shared.append(f"Both take {', '.join(shared_meds)}")

        return shared

    def _determine_connection_type(self, profile1: Dict, profile2: Dict) -> str:
        """Determine appropriate connection type"""
        if profile1.get('caregiver') and profile2.get('caregiver'):
            return 'caregiver_to_caregiver'
        elif profile1.get('newly_diagnosed') and profile2.get('newly_diagnosed'):
            return 'newly_diagnosed_peer'
        elif profile1.get('treatment_resistant') and profile2.get('treatment_resistant'):
            return 'treatment_resistant_peer'
        else:
            return 'general_epilepsy_peer'

    def find_support_groups(self, patient_location: str, interests: List[str] = None) -> List[Dict]:
        """Find appropriate support groups"""
        groups = []

        # In production, would query actual support group database
        groups.append({
            'name': 'Epilepsy Foundation Support Group',
            'location': patient_location,
            'meeting_type': 'in_person',
            'frequency': 'monthly',
            'contact': 'local@epilepsyfoundation.org'
        })

        groups.append({
            'name': 'Online Epilepsy Community',
            'location': 'Online',
            'meeting_type': 'virtual',
            'frequency': 'weekly',
            'contact': 'community@epilepsy.com'
        })

        return groups


class TherapeuticAllianceBuilder:
    """
    Main builder for comprehensive therapeutic alliance system.

    Integrates check-ins, education, empowerment, and community
    into a continuous care partnership.
    """

    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.check_in_system = ContinuousCheckInSystem(patient_id)
        self.education_engine = PatientEducationEngine(patient_id)
        self.empowerment_engine = PatientEmpowermentEngine(patient_id)
        self.community_manager = CommunityConnectionManager()

    def build_alliance(self, patient_profile: Dict) -> Dict[str, Any]:
        """Build comprehensive therapeutic alliance plan"""
        # Establish learning profile
        self.education_engine.establish_learning_profile(patient_profile)

        # Get comprehensive alliance components
        check_in = self.check_in_system.generate_check_in(patient_profile)
        education = self.education_engine.recommend_education(patient_profile)
        skills = self.empowerment_engine.assess_self_management_skills()
        peers = self.community_manager.find_peer_matches(patient_profile)
        support_groups = self.community_manager.find_support_groups(
            patient_profile.get('location', ''),
            patient_profile.get('interests', [])
        )

        return {
            'patient_id': self.patient_id,
            'alliance_date': datetime.now().isoformat(),
            'check_in_system': {
                'next_check_in': check_in,
                'schedule_recommendations': self._generate_schedule_recommendations(patient_profile)
            },
            'education_plan': {
                'recommended_modules': education,
                'learning_profile': self.education_engine.learning_profile
            },
            'empowerment_plan': {
                'current_skills': skills,
                'priority_areas': skills.get('areas_for_improvement', []),
                'first_focus': skills.get('recommended_focus', [''])[0] if skills.get('recommended_focus') else None
            },
            'peer_support': {
                'peer_matches': peers,
                'support_groups': support_groups
            },
            'next_steps': self._generate_alliance_next_steps(patient_profile, skills)
        }

    def _generate_schedule_recommendations(self, profile: Dict) -> Dict:
        """Generate check-in schedule recommendations"""
        if profile.get('treatment_resistant', False):
            return {
                'frequency': 'weekly',
                'duration': '20 minutes',
                'priority': 'monitoring'
            }
        elif profile.get('medication_change', False):
            return {
                'frequency': 'biweekly',
                'duration': '15 minutes',
                'priority': 'monitoring'
            }
        else:
            return {
                'frequency': 'monthly',
                'duration': '10 minutes',
                'priority': 'routine'
            }

    def _generate_alliance_next_steps(self, profile: Dict, skills: Dict) -> List[str]:
        """Generate next steps for building therapeutic alliance"""
        steps = []

        # Immediate next steps
        steps.append("Complete first check-in to establish baseline")
        steps.append(f"Focus on building skill in {skills.get('recommended_focus', ['medication management'])[0] if skills.get('recommended_focus') else 'medication management'}")

        if profile.get('newly_diagnosed', False):
            steps.append("Start with foundational education modules")
        else:
            steps.append("Review advanced education modules based on current needs")

        # Peer support
        steps.append("Connect with matched peer within 1 week")
        steps.append("Consider joining local support group")

        return steps


# Convenience functions
def create_therapeutic_alliance(patient_id: str) -> TherapeuticAllianceBuilder:
    """Create therapeutic alliance system for patient"""
    return TherapeuticAllianceBuilder(patient_id)
