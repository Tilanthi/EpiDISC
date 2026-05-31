"""
EPIDISC Literature Surveillance System
======================================

Continuous medical literature monitoring and knowledge updating
system for epilepsy research, guidelines, and evidence integration.

Based on:
- Current medical literature databases and APIs
- Evidence-based medicine frameworks
- ILAE and professional organization surveillance
- Automated literature processing systems

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta
import json


class LiteratureSource(Enum):
    """Primary literature sources for epilepsy surveillance"""
    PUBMED = "pubmed"
    PMC = "pubmed_central"
    BIORXIV = "biorxiv"
    MEDRXIV = "medrxiv"
    ARXIV_QBIO = "arxiv_q_bio"
    EPILEPSIA = "epilepsia_journal"
    NEUROLOGY = "neurology_journal"
    SEIZURE = "seizure_journal"


class EvidenceLevel(Enum):
    """Evidence quality classification"""
    META_ANALYSIS = "meta_analysis"              # Highest quality
    RANDOMIZED_CONTROLLED_TRIAL = "rct"         # Level I
    COHORT_STUDY = "cohort"                     # Level II
    CASE_CONTROL = "case_control"               # Level III
    CASE_SERIES = "case_series"                 # Level IV
    EXPERT_OPINION = "expert_opinion"          # Level V


class PublicationType(Enum):
    """Types of epilepsy publications"""
    CLINICAL_TRIAL = "clinical_trial"
    OBSERVATIONAL_STUDY = "observational_study"
    GUIDELINE = "guideline"
    REVIEW = "review"
    META_ANALYSIS = "meta_analysis"
    CASE_REPORT = "case_report"
    PREPRINT = "preprint"
    POSITION_STATEMENT = "position_statement"


@dataclass
class LiteratureItem:
    """
    Complete literature item with clinical relevance assessment

    Includes article metadata, relevance scoring, evidence assessment,
    and clinical integration recommendations.
    """

    pmid: str
    title: str
    authors: List[str]
    journal: str
    publication_date: str
    publication_type: PublicationType
    evidence_level: EvidenceLevel
    abstract: str
    keywords: List[str]
    relevance_score: float  # 0-1
    clinical_impact: str  # High, Moderate, Low
    practice_changer: bool
    guideline_relevant: bool
    safety_signal: bool
    novel_treatment: bool
    summary: str
    clinical_takeaways: List[str]
    limitations: List[str]


class LiteratureSurveillance:
    """
    Comprehensive epilepsy literature surveillance system

    Automated monitoring, classification, and clinical integration
    of epilepsy-related medical literature.
    """

    # Epilepsy-specific search terms for literature surveillance
    EPILEPSY_SEARCH_TERMS = {
        "core_terms": [
            "epilepsy", "seizure", "epileptic", "convulsion",
            "antiseizure medication", "ASM", "antiepileptic drug", "AED"
        ],
        "specific_seizure_types": [
            "focal seizure", "generalized seizure", "absence seizure",
            "myoclonic seizure", "tonic-clonic seizure", "status epilepticus"
        ],
        "epilepsy_syndromes": [
            "Dravet syndrome", "Lennox-Gastaut syndrome", "West syndrome",
            "juvenile myoclonic epilepsy", "rolandic epilepsy", "LGS"
        ],
        "treatments": [
            "levetiracetam", "lamotrigine", "valproate", "carbamazepine",
            "brivaracetam", "perampanel", "cenobamate", "lacosamide"
        ],
        "diagnostics": [
            "EEG", "electroencephalogram", "MRI", "neuroimaging",
            "video-EEG", "ambulatory EEG"
        ],
        "special_populations": [
            "pregnancy", "women", "elderly", "pediatric", "neonatal",
            "developmental", "intellectual disability"
        ],
        "complications": [
            "SUDEP", "sudden unexpected death in epilepsy",
            "PNES", "psychogenic nonepileptic seizures",
            "drug-resistant epilepsy", "refractory epilepsy"
        ]
    }

    # Journal-specific priorities
    PRIORITY_JOURNALS = {
        "highest_priority": [
            "Neurology",
            "Epilepsia",
            "Epilepsy & Behavior",
            "Seizure",
            "Lancet Neurology",
            "JAMA Neurology"
        ],
        "moderate_priority": [
            "Annals of Neurology",
            "Brain",
            "Epilepsy Research",
            "Clinical EEG and Neuroscience",
            "Journal of Neurology, Neurosurgery, and Psychiatry"
        ]
    }

    # Guideline sources to monitor
    GUIDELINE_SOURCES = {
        "ILAE": {
            "full_name": "International League Against Epilepsy",
            "update_frequency": "Every 2-3 years",
            "commissions": [
                "Classification Commission",
                "Neuroimaging Commission",
                "Diagnostic Methods Commission",
                "Treatment Guidelines Commission"
            ]
        },
        "NICE": {
            "full_name": "UK National Institute for Health and Care Excellence",
            "update_frequency": "Every 3-5 years",
            "relevant_guidelines": ["CG137", "CG2", "NG217"]
        },
        "AAN": {
            "full_name": "American Academy of Neurology",
            "update_frequency": "Every 3-5 years",
            "guideline_types": ["Practice guidelines", "Position statements"]
        },
        "AES": {
            "full_name": "American Epilepsy Society",
            "update_frequency": "Annual",
            "guideline_types": ["Position statements", "Treatment guidelines"]
        }
    }

    @classmethod
    def get_literature_search_query(cls, timeframe_days: int = 7) -> Dict:
        """
        Get PubMed/literature search query for recent epilepsy literature

        Args:
            timeframe_days: Number of days to search back

        Returns:
            Dictionary with search query and parameters
        """
        # Build comprehensive search query
        core_terms = " OR ".join(cls.EPILEPSY_SEARCH_TERMS["core_terms"])

        # Date range
        today = datetime.now()
        search_date = today - timedelta(days=timeframe_days)

        return {
            "query": core_terms,
            "filters": {
                "publication_date": f"{search_date.strftime('%Y/%m/%d')}:{today.strftime('%Y/%m/%d')}",
                "language": "english",
                "species": "humans"
            },
            "databases": ["pubmed", "PMC"],
            "max_results": 500,
            "sort_by": "relevance"
        }

    @classmethod
    def assess_clinical_relevance(cls, article: Dict) -> Tuple[float, Dict]:
        """
        Assess clinical relevance of epilepsy article

        Args:
            article: Article metadata and content

        Returns:
            (relevance_score, relevance_details)
        """
        relevance_score = 0.0
        relevance_details = {
            "practice_changer": False,
            "safety_signal": False,
            "guideline_relevant": False,
            "novel_treatment": False,
            "reasons": []
        }

        title = article.get("title", "").lower()
        abstract = article.get("abstract", "").lower()
        journal = article.get("journal", "").lower()
        combined_text = f"{title} {abstract}"

        # Check for practice-changing terms
        practice_changers = [
            "first-line", "new recommendation", "guideline update",
            "practice guideline", "standard of care", "should be considered"
        ]
        if any(term in combined_text for term in practice_changers):
            relevance_score += 0.3
            relevance_details["practice_changer"] = True
            relevance_details["reasons"].append("Practice-changing content")

        # Check for safety signals
        safety_terms = [
            "safety", "adverse effect", "warning", "contraindication",
            "side effect", "toxicity", "mortality", "risk"
        ]
        if any(term in combined_text for term in safety_terms):
            relevance_score += 0.25
            relevance_details["safety_signal"] = True
            relevance_details["reasons"].append("Safety signal identified")

        # Check for guideline relevance
        if journal in ["neurology", "epilepsia", "epilepsy & behavior"]:
            relevance_score += 0.15
            relevance_details["guideline_relevant"] = True
            relevance_details["reasons"].append("High-impact journal")

        # Check for novel treatments
        novel_terms = [
            "new treatment", "novel therapy", "investigational",
            "clinical trial", "randomized", "efficacy"
        ]
        if any(term in combined_text for term in novel_terms):
            relevance_score += 0.2
            relevance_details["novel_treatment"] = True
            relevance_details["reasons"].append("Novel treatment data")

        # Check for study type
        if "randomized" in combined_text or "rct" in combined_text:
            relevance_score += 0.2
            relevance_details["reasons"].append("Randomized controlled trial")

        elif "guideline" in combined_text or "recommendation" in combined_text:
            relevance_score += 0.3
            relevance_details["reasons"].append("Guideline or recommendation")

        # Cap score at 1.0
        relevance_score = min(relevance_score, 1.0)

        return relevance_score, relevance_details

    @classmethod
    def classify_evidence(cls, article: Dict) -> EvidenceLevel:
        """Classify evidence level of epilepsy publication"""
        text = f"{article.get('title', '')} {article.get('abstract', '')}".lower()

        if "meta-analysis" in text or "systematic review" in text:
            return EvidenceLevel.META_ANALYSIS
        elif "randomized" in text and ("trial" in text or "rct" in text):
            return EvidenceLevel.RANDOMIZED_CONTROLLED_TRIAL
        elif "cohort" in text or "prospective" in text:
            return EvidenceLevel.COHORT_STUDY
        elif "case control" in text:
            return EvidenceLevel.CASE_CONTROL
        elif "case series" in text or "case report" in text:
            return EvidenceLevel.CASE_SERIES
        else:
            return EvidenceLevel.EXPERT_OPINION

    @classmethod
    def extract_clinical_takeaways(cls, article: Dict) -> List[str]:
        """Extract key clinical takeaways from article"""
        takeaways = []
        abstract = article.get("abstract", "")
        title = article.get("title", "")

        # Look for conclusion statements
        if "conclusion:" in abstract.lower():
            conclusion_start = abstract.lower().find("conclusion:")
            conclusion_text = abstract[conclusion_start+11:conclusion_start+300]  # Next 300 chars
            takeaways.append(f"Conclusion: {conclusion_text.strip()}")

        # Look for key results
        if "results:" in abstract.lower():
            results_start = abstract.lower().find("results:")
            results_text = abstract[results_start+8:results_start+200]
            takeaways.append(f"Key results: {results_text.strip()}")

        # Check for treatment implications
        if "treatment" in title.lower() or "therapy" in title.lower():
            takeaways.append("Treatment implications discussed in article")

        # Check for guideline recommendations
        if "recommend" in abstract.lower() or "guideline" in title.lower():
            takeaways.append("Contains treatment recommendations")

        return takeaways if takeaways else ["Review article for clinical implications"]

    @classmethod
    def format_literature_update(
        cls,
        articles: List[Dict],
        max_articles: int = 10
    ) -> List[str]:
        """Format literature updates for clinical integration"""
        # Sort by relevance score
        scored_articles = []
        for article in articles:
            score, details = cls.assess_clinical_relevance(article)
            if score > 0.3:  # Only include relevant articles
                scored_articles.append((score, article, details))

        # Sort by score (highest first)
        scored_articles.sort(key=lambda x: x[0], reverse=True)

        # Format top articles
        formatted_updates = []
        for i, (score, article, details) in enumerate(scored_articles[:max_articles]):
            update = [
                f"📄 ARTICLE {i+1} (Relevance: {score:.2%})",
                f"Title: {article.get('title', 'Unknown')}",
                f"Journal: {article.get('journal', 'Unknown')} ({article.get('publication_date', 'Unknown')})",
                f"Evidence: {cls.classify_evidence(article).value}",
                f"PMID: {article.get('pmid', 'Unknown')}",
                ""
            ]

            # Add relevance flags
            flags = []
            if details.get("practice_changer"):
                flags.append("🔄 PRACTICE CHANGER")
            if details.get("safety_signal"):
                flags.append("⚠️ SAFETY SIGNAL")
            if details.get("guideline_relevant"):
                flags.append("📋 GUIDELINE RELEVANT")
            if details.get("novel_treatment"):
                flags.append("💊 NOVEL TREATMENT")

            if flags:
                update.append(" | ".join(flags))
                update.append("")

            # Add clinical takeaways
            takeaways = cls.extract_clinical_takeaways(article)
            update.append("Clinical Takeaways:")
            for takeaway in takeaways[:3]:  # Top 3 takeaways
                update.append(f"  • {takeaway}")

            formatted_updates.append("\n".join(update))

        return formatted_updates

    @classmethod
    def get_surveillance_summary(cls, articles: List[Dict]) -> Dict:
        """Get summary statistics of literature surveillance"""
        total_articles = len(articles)

        # Count by evidence level
        evidence_counts = {}
        for article in articles:
            level = cls.classify_evidence(article)
            evidence_counts[level.value] = evidence_counts.get(level.value, 0) + 1

        # Count high-relevance articles
        high_relevance = sum(
            1 for article in articles
            if cls.assess_clinical_relevance(article)[0] > 0.7
        )

        return {
            "total_articles": total_articles,
            "evidence_distribution": evidence_counts,
            "high_relevance_count": high_relevance,
            "surveillance_period": "Weekly",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


class GuidelineSurveillance:
    """
    Clinical guideline surveillance system

    Automated monitoring of epilepsy clinical guidelines
    from major professional organizations.
    """

    @classmethod
    def get_guideline_update_monitoring(cls) -> Dict[str, List[str]]:
        """Get guideline sources and monitoring parameters"""
        monitoring = {}

        for source, details in LiteratureSurveillance.GUIDELINE_SOURCES.items():
            monitoring[source] = [
                f"Source: {details['full_name']}",
                f"Update Frequency: {details['update_frequency']}",
                f"Monitoring: Weekly automated checks",
                f"Alert Level: HIGH for any guideline updates"
            ]

        return monitoring

    @classmethod
    def assess_guideline_relevance(cls, guideline: Dict) -> List[str]:
        """Assess clinical relevance of guideline update"""
        relevance = []

        title = guideline.get("title", "").lower()
        content = guideline.get("content", "").lower()

        # Check for major guideline topics
        major_topics = {
            "new_onset": "new-onset epilepsy",
            "drug_resistant": "drug-resistant epilepsy",
            "women": "women's health/pregnancy",
            "status": "status epilepticus",
            "surgery": "epilepsy surgery",
            "guideline": "treatment guideline"
        }

        for topic, search_term in major_topics.items():
            if search_term in title or search_term in content:
                relevance.append(f"🎯 {topic.replace('_', ' ').title()} - RELEVANT")

        return relevance if relevance else ["General guideline update"]


class KnowledgeIntegration:
    """
    Knowledge base integration system

    Automated integration of new literature findings
    into the EPIDISC knowledge base with quality control.
    """

    @classmethod
    def assess_integration_readiness(cls, article: Dict) -> Tuple[bool, List[str]]:
        """
        Assess if article is ready for knowledge base integration

        Args:
            article: Article with clinical assessment

        Returns:
            (ready_to_integrate, integration_recommendations)
        """
        ready = False
        recommendations = []

        score, details = LiteratureSurveillance.assess_clinical_relevance(article)
        evidence = LiteratureSurveillance.classify_evidence(article)

        # High-quality evidence with clinical relevance
        if score > 0.7 and evidence in [
            EvidenceLevel.RANDOMIZED_CONTROLLED_TRIAL,
            EvidenceLevel.META_ANALYSIS
        ]:
            ready = True
            recommendations.append("✅ High-quality evidence - ready for integration")

        # Guidelines or practice-changing content
        if details.get("practice_changer") or details.get("guideline_relevant"):
            ready = True
            recommendations.append("✅ Practice-changing content - prioritize integration")

        # Safety signals
        if details.get("safety_signal"):
            ready = True
            recommendations.append("⚠️ Safety signal - urgent integration needed")

        # Low-quality evidence
        if evidence in [EvidenceLevel.CASE_REPORT, EvidenceLevel.EXPERT_OPINION]:
            recommendations.append("ℹ️ Lower evidence level - integrate with caution")

        # Preprint
        if article.get("publication_type") == PublicationType.PREPRINT:
            recommendations.append("⏳ Preprint - monitor for peer review before integration")

        return ready, recommendations

    @classmethod
    def generate_integration_summary(cls, articles: List[Dict]) -> List[str]:
        """Generate summary of literature ready for knowledge base integration"""
        summary = [
            "🧠 LITERATURE INTEGRATION SUMMARY",
            "",
            f"Total articles reviewed: {len(articles)}",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            ""
        ]

        ready_for_integration = []
        monitoring_required = []

        for article in articles:
            ready, recommendations = cls.assess_integration_readiness(article)

            if ready:
                ready_for_integration.append({
                    "title": article.get("title", "Unknown"),
                    "pmid": article.get("pmid", "Unknown"),
                    "recommendations": recommendations
                })
            else:
                monitoring_required.append({
                    "title": article.get("title", "Unknown"),
                    "pmid": article.get("pmid", "Unknown"),
                    "recommendations": recommendations
                })

        # Format ready for integration
        if ready_for_integration:
            summary.extend([
                "✅ READY FOR KNOWLEDGE BASE INTEGRATION:",
                ""
            ])
            for i, article in enumerate(ready_for_integration, 1):
                summary.extend([
                    f"{i}. {article['title']}",
                    f"   PMID: {article['pmid']}",
                    f"   Status: {' | '.join(article['recommendations'])}",
                    ""
                ])

        # Format monitoring required
        if monitoring_required:
            summary.extend([
                "⏳ MONITORING REQUIRED:",
                ""
            ])
            for i, article in enumerate(monitoring_required[:5], 1):  # Top 5
                summary.extend([
                    f"{i}. {article['title']}",
                    f"   PMID: {article['pmid']}",
                    f"   Status: {' | '.join(article['recommendations'])}",
                    ""
                ])

        return summary

    @classmethod
    def get_update_protocol(cls) -> List[str]:
        """Get protocol for knowledge base updates"""
        return [
            "🔄 KNOWLEDGE BASE UPDATE PROTOCOL:",
            "",
            "1️⃣ AUTOMATED SURVEILLANCE:",
            "   • Daily literature fetch (PubMed, PMC, preprints)",
            "   • Automated relevance scoring",
            "   • Evidence classification",
            "   • Safety signal prioritization",
            "",
            "2️⃣ QUALITY CONTROL:",
            "   • Peer review status verification",
            "   • Publication source validation",
            "   • Evidence level confirmation",
            "   • Clinical relevance assessment",
            "",
            "3️⃣ INTEGRATION PROCESS:",
            "   • High-priority updates (<24 hours)",
            "   • Safety alerts (<48 hours)",
            "   • Practice changes (<1 week)",
            "   • General updates (<2 weeks)",
            "",
            "4️⃣ VERSION CONTROL:",
            "   • Automatic knowledge base versioning",
            "   • Change tracking and logging",
            "   • Rollback capability",
            "   • Update audit trail",
            "",
            "5️⃣ VALIDATION:",
            "   • Integration testing",
            "   • Clinical reasoning validation",
            "   • Cross-referencing verification",
            "   • Consistency checking"
        ]


__all__ = [
    'LiteratureSource',
    'EvidenceLevel',
    'PublicationType',
    'LiteratureItem',
    'LiteratureSurveillance',
    'GuidelineSurveillance',
    'KnowledgeIntegration'
]