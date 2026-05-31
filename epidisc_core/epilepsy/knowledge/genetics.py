"""
EPIDISC Genetics and Precision Medicine Module
===============================================

Comprehensive genetic epilepsy knowledge system with channelopathies,
variant interpretation, and precision medicine approaches.

Based on:
- Current genetic epilepsy research (2024-2026)
- Channelopathy mechanisms and ASM selection
- ILAE genetic classification recommendations
- Evidence-based precision medicine approaches

Version: 1.0.0
Last Updated: 2026-05-31
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class InheritancePattern(Enum):
    """Inheritance patterns for genetic epilepsies"""
    AUTOSOMAL_DOMINANT = "autosomal_dominant"
    AUTOSOMAL_RECESSIVE = "autosomal_recessive"
    X_LINKED = "x_linked"
    MITOCHONDRIAL = "mitochondrial"
    DE_NOVO = "de_novo"
    OLIGGENIC = "oligogenic"
    POLYGENIC = "polygenic"


class VariantSignificance(Enum):
    """Clinical significance of genetic variants"""
    PATHOGENIC = "pathogenic"
    LIKELY_PATHOGENIC = "likely_pathogenic"
    UNCERTAIN = "uncertain_significance"
    LIKELY_BENIGN = "likely_benign"
    BENIGN = "benign"


@dataclass
class GeneticFinding:
    """
    Complete genetic test interpretation

    Includes variant significance, clinical correlation,
    treatment implications, and genetic counseling considerations.
    """

    gene: str
    variant: str
    significance: VariantSignificance
    inheritance: InheritancePattern
    associated_condition: str
    penetrance: str  # High, moderate, low, variable
    treatment_implications: List[str]
    medication_contraindications: List[str]
    genetic_counseling: List[str]
    family_testing: List[str]
    confidence: float


class GeneticEpilepsies:
    """
    Comprehensive genetic epilepsy knowledge system

    Evidence-based genetic information for epilepsy with
    precision medicine and genetic counseling capabilities.
    """

    # Major epilepsy genes and associated conditions
    EPILEPSY_GENES = {
        "SCN1A": {
            "conditions": ["Dravet syndrome", "Genetic epilepsy with febrile seizures plus", "Focal epilepsy"],
            "inheritance": InheritancePattern.DE_NOVO,
            "penetrance": "High for Dravet syndrome, variable for other conditions",
            "pathophysiology": "Loss-of-function sodium channel mutation",
            "treatment_implications": [
                "⚠️ AVOID sodium channel blockers (carbamazepine, phenytoin, lamotrigine)",
                "Preferred ASMs: Stiripentol, Clobazam, Valproate, Fenfluramine",
                "Consider ketogenic diet",
                "Consider cannabidiol (CBD)"
            ],
            "medication_contraindications": [
                "Carbamazepine (CAN WORSEN SEIZURES)",
                "Phenytoin (CAN WORSEN SEIZURES)",
                "Lamotrigine (CAN WORSEN SEIZURES)",
                "Oxcarbazepine (CAN WORSEN SEIZURES)"
            ],
            "genetic_counseling": [
                "Most cases de novo (90%)",
                "Parental testing recommended (identify parental mosaicism)",
                "Recurrence risk low if both parents negative",
                "Consider prenatal testing for future pregnancies"
            ]
        },
        "SCN2A": {
            "conditions": ["Early infantile epileptic encephalopathy", "Benign familial neonatal-infantile seizures"],
            "inheritance": InheritancePattern.DE_NOVO,
            "penetrance": "High for severe infantile forms",
            "pathophysiology": "Gain-of-function sodium channel mutation",
            "treatment_implications": [
                "✅ Sodium channel blockers often EFFECTIVE (opposite of SCN1A)",
                "Preferred ASMs: Carbamazepine, Phenytoin, Lamotrigine",
                "Consider phenobarbital",
                "Response often good to sodium channel blockers"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "Most cases de novo",
                "Parental testing recommended",
                "Recurrence risk low if both parents negative"
            ]
        },
        "SCN8A": {
            "conditions": ["Early infantile epileptic encephalopathy", "Focal epilepsy"],
            "inheritance": InheritancePattern.DE_NOVO,
            "penetrance": "High for severe forms",
            "pathophysiology": "Gain-of-function sodium channel mutation",
            "treatment_implications": [
                "✅ Sodium channel blockers often effective",
                "Preferred ASMs: Carbamazepine, Phenytoin, Lamotrigine",
                "Consider phenobarbital",
                "High-dose phenytoin reported effective"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "Most cases de novo",
                "Parental testing recommended",
                "Variable expressivity reported"
            ]
        },
        "KCNQ2": {
            "conditions": ["KCNQ2 encephalopathy", "Benign familial neonatal seizures"],
            "inheritance": InheritancePattern.AUTOSOMAL_DOMINANT,
            "penetrance": "High",
            "pathophysiology": "Potassium channel mutation",
            "treatment_implications": [
                "✅ Sodium channel blockers often effective",
                "Preferred ASMs: Carbamazepine, Phenytoin",
                "Consider retigabine (ezogabine) - potassium channel opener",
                "Response often good"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "Autosomal dominant inheritance",
                "50% risk to offspring of affected individual",
                "Variable expressivity"
            ]
        },
        "CDKL5": {
            "conditions": ["CDKL5 deficiency disorder", "Early infantile epileptic encephalopathy"],
            "inheritance": InheritancePattern.X_LINKED,
            "penetrance": "High in affected females",
            "pathophysiology": "CDK-like protein deficiency",
            "treatment_implications": [
                "Generally drug-resistant",
                "Preferred ASMs: Valproate, Clobazam, Vigabatrin",
                "Consider ketogenic diet",
                "Consider cannabidiol (CBD)",
                "Limited response to most ASMs"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "X-linked dominant",
                "Most cases de novo",
                "Parental testing recommended",
                "Prenatal testing available"
            ]
        },
        "STXBP1": {
            "conditions": ["Early infantile epileptic encephalopathy", "Intellectual disability"],
            "inheritance": InheritancePattern.DE_NOVO,
            "penetrance": "High",
            "pathophysiology": "Synaptic protein deficiency",
            "treatment_implications": [
                "Variable response",
                "Consider broad-spectrum ASMs",
                "Levetiracetam sometimes effective",
                "Often drug-resistant"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "Most cases de novo",
                "Parental testing recommended",
                "Recurrence risk low if parents negative"
            ]
        },
        "PCDH19": {
            "conditions": ["PCDH19 clustering epilepsy", "Dravet-like epilepsy"],
            "inheritance": InheritancePattern.X_LINKED,
            "penetrance": "High in females, low in males",
            "pathophysiology": "Protocadherin deficiency",
            "treatment_implications": [
                "Females: Variable response",
                "Males: Often milder",
                "Preferred ASMs: Broad-spectrum agents",
                "Consider ketogenic diet",
                "Consider stiripentol"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "X-linked dominant with cellular interference",
                "Females primarily affected",
                "Asymptomatic carrier males",
                "Prenatal testing available"
            ]
        },
        "DEPDC5": {
            "conditions": ["Focal epilepsy", "Sleep-related hypermotor epilepsy"],
            "inheritance": InheritancePattern.AUTOSOMAL_DOMINANT,
            "penetrance": "Incomplete (variable)",
            "pathophysiology": "mTOR pathway dysregulation",
            "treatment_implications": [
                "Variable response",
                "Often drug-resistant",
                "Consider mTOR inhibitors (everolimus) - emerging",
                "Consider surgical evaluation (often focal)"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "Autosomal dominant with incomplete penetrance",
                "Variable expressivity",
                "Family history often negative (incomplete penetrance)",
                "Consider predictive testing for family members"
            ]
        },
        "GABRA1": {
            "conditions": ["Genetic epilepsy with febrile seizures plus", "Dravet-like syndrome"],
            "inheritance": InheritancePattern.AUTOSOMAL_DOMINANT,
            "penetrance": "Variable",
            "pathophysiology": "GABA-A receptor dysfunction",
            "treatment_implications": [
                "Variable response",
                "Consider GABAergic agents (benzodiazepines, barbiturates)",
                "Often drug-resistant",
                "Consider stiripentol"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "Autosomal dominant",
                "Variable expressivity",
                "Consider family testing"
            ]
        },
        "HCN1": {
            "conditions": ["Early infantile epileptic encephalopathy", "Generalized epilepsy"],
            "inheritance": InheritancePattern.DE_NOVO,
            "penetrance": "High",
            "pathophysiology": "Hyperpolarization-activated cyclic nucleotide channel",
            "treatment_implications": [
                "Consider sodium channel blockers",
                "Consider lamotrigine",
                "Generally drug-resistant"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "Most cases de novo",
                "Parental testing recommended"
            ]
        },
        "GRIN2A": {
            "conditions": ["Epilepsy-aphasia spectrum", "Landau-Kleffner syndrome"],
            "inheritance": InheritancePattern.DE_NOVO,
            "penetrance": "Variable",
            "pathophysiology": "NMDA receptor dysfunction",
            "treatment_implications": [
                "Consider NMDA receptor modulators",
                "Consider dextromethorphan (NMDA antagonist)",
                "Consider memantine",
                "Often drug-resistant"
            ],
            "medication_contraindications": [],
            "genetic_counseling": [
                "Most cases de novo",
                "Associated with neurodevelopmental disorders",
                "Parental testing recommended"
            ]
        }
    }

    # Channelopathy ASM selection guidance
    CHANNELOPATHY_ASM_GUIDANCE = {
        "sodium_channel_gain_of_function": {
            "genes": ["SCN2A", "SCN8A"],
            "effective_ASMS": [
                "Carbamazepine (✅ OFTEN EFFECTIVE)",
                "Phenytoin (✅ OFTEN EFFECTIVE)",
                "Lamotrigine (✅ OFTEN EFFECTIVE)",
                "Oxcarbazepine (✅ OFTEN EFFECTIVE)",
                "Lacosamide (⚠️ MAY BE EFFECTIVE)"
            ],
            "avoid": [],
            "clinical_pearl": "Opposite of SCN1A - sodium channel blockers often help"
        },
        "sodium_channel_loss_of_function": {
            "genes": ["SCN1A"],
            "effective_ASMS": [
                "Stiripentol (✅ EFFECTIVE)",
                "Clobazam (✅ EFFECTIVE)",
                "Valproate (✅ EFFECTIVE)",
                "Fenfluramine (✅ EFFECTIVE)",
                "Cannabidiol (✅ EFFECTIVE)",
                "Ketogenic diet (✅ OFTEN HELPFUL)"
            ],
            "avoid": [
                "⚠️ AVOID: Carbamazepine (CAN WORDEN)",
                "⚠️ AVOID: Phenytoin (CAN WORSEN)",
                "⚠️ AVOID: Lamotrigine (CAN WORSEN)",
                "⚠️ AVOID: Oxcarbazepine (CAN WORSEN)"
            ],
            "clinical_pearl": "Sodium channel blockers can be catastrophic in SCN1A mutations"
        },
        "potassium_channel": {
            "genes": ["KCNQ2", "KCNQ3"],
            "effective_ASMS": [
                "Carbamazepine (✅ OFTEN EFFECTIVE)",
                "Phenytoin (✅ OFTEN EFFECTIVE)",
                "Retigabine/Ezogabine (✅ SPECIFIC FOR POTASSIUM CHANNELS)"
            ],
            "avoid": [],
            "clinical_pearl": "Potassium channel opener retigabine is mechanistically appropriate"
        },
        "gabaergic": {
            "genes": ["GABRA1", "GABRB3", "GABRG2"],
            "effective_ASMS": [
                "Benzodiazepines (✅ MECHANISTICALLY APPROPRIATE)",
                "Phenobarbital (✅ MECHANISTICALLY APPROPRIATE)",
                "Stiripentol (✅ EFFECTIVE)",
                "Valproate (✅ MAY BE HELPFUL)"
            ],
            "avoid": [],
            "clinical_pearl": "GABA-enhancing agents are mechanistically appropriate"
        }
    }

    @classmethod
    def get_genetic_information(cls, gene: str) -> Optional[Dict]:
        """Get comprehensive genetic information for specific gene"""
        return cls.EPILEPSY_GENES.get(gene.upper(), None)

    @classmethod
    def interpret_genetic_finding(
        cls,
        gene: str,
        variant: str,
        significance: str,
        clinical_context: Optional[Dict] = None
    ) -> GeneticFinding:
        """
        Interpret genetic test result with clinical implications

        Args:
            gene: Gene name
            variant: Specific variant
            significance: Clinical significance
            clinical_context: Clinical information for correlation

        Returns:
            GeneticFinding with complete interpretation
        """
        gene_info = cls.get_genetic_information(gene)

        if not gene_info:
            return GeneticFinding(
                gene=gene,
                variant=variant,
                significance=VariantSignificance.UNCERTAIN,
                inheritance=InheritancePattern.DE_NOVO,
                associated_condition="Unknown or not characterized",
                penetrance="Unknown",
                treatment_implications=["Insufficient data for treatment guidance"],
                medication_contraindications=[],
                genetic_counseling=["Consider referral to genetics specialist"],
                family_testing=["Parental testing recommended if de novo suspected"],
                confidence=0.3
            )

        # Map significance string to enum
        significance_map = {
            "pathogenic": VariantSignificance.PATHOGENIC,
            "likely_pathogenic": VariantSignificance.LIKELY_PATHOGENIC,
            "uncertain": VariantSignificance.UNCERTAIN,
            "vus": VariantSignificance.UNCERTAIN,
            "likely_benign": VariantSignificance.LIKELY_BENIGN,
            "benign": VariantSignificance.BENIGN
        }

        variant_significance = significance_map.get(
            significance.lower(),
            VariantSignificance.UNCERTAIN
        )

        return GeneticFinding(
            gene=gene,
            variant=variant,
            significance=variant_significance,
            inheritance=gene_info["inheritance"],
            associated_condition=", ".join(gene_info["conditions"]),
            penetrance=gene_info["penetrance"],
            treatment_implications=gene_info["treatment_implications"],
            medication_contraindications=gene_info["medication_contraindications"],
            genetic_counseling=gene_info["genetic_counseling"],
            family_testing=cls._get_family_testing_recommendations(gene, gene_info),
            confidence=cls._calculate_confidence(variant_significance)
        )

    @classmethod
    def _get_family_testing_recommendations(cls, gene: str, gene_info: Dict) -> List[str]:
        """Get family testing recommendations"""
        recommendations = []

        if gene_info["inheritance"] == InheritancePattern.DE_NOVO:
            recommendations.extend([
                "Parental testing recommended to confirm de novo status",
                "If both parents negative: low recurrence risk",
                "If parental mosaicism identified: recurrence risk increased"
            ])
        elif gene_info["inheritance"] == InheritancePattern.AUTOSOMAL_DOMINANT:
            recommendations.extend([
                "Test both parents",
                "If either parent positive: 50% transmission risk",
                "Consider testing siblings",
                "Prenatal testing available for future pregnancies"
            ])
        elif gene_info["inheritance"] == InheritancePattern.X_LINKED:
            recommendations.extend([
                "Mother testing recommended",
                "Consider family X-linked pattern",
                "Prenatal testing available"
            ])

        return recommendations

    @classmethod
    def _calculate_confidence(cls, significance: VariantSignificance) -> float:
        """Calculate confidence in interpretation"""
        confidence_map = {
            VariantSignificance.PATHOGENIC: 0.95,
            VariantSignificance.LIKELY_PATHOGENIC: 0.85,
            VariantSignificance.UNCERTAIN: 0.5,
            VariantSignificance.LIKELY_BENIGN: 0.85,
            VariantSignificance.BENIGN: 0.95
        }
        return confidence_map.get(significance, 0.5)

    @classmethod
    def get_asm_guidance_by_genetics(cls, gene: str) -> Optional[Dict]:
        """Get ASM selection guidance based on genetic findings"""
        gene_info = cls.get_genetic_information(gene)

        if not gene_info:
            return None

        # Determine channelopathy type
        if gene in ["SCN2A", "SCN8A"]:
            return cls.CHANNELOPATHY_ASM_GUIDANCE["sodium_channel_gain_of_function"]
        elif gene == "SCN1A":
            return cls.CHANNELOPATHY_ASM_GUIDANCE["sodium_channel_loss_of_function"]
        elif gene in ["KCNQ2", "KCNQ3"]:
            return cls.CHANNELOPATHY_ASM_GUIDANCE["potassium_channel"]
        elif gene in ["GABRA1", "GABRB3", "GABRG2"]:
            return cls.CHANNELOPATHY_ASM_GUIDANCE["gabaergic"]
        else:
            return None


class GeneticTestingGuidance:
    """
    Evidence-based genetic testing guidance for epilepsy

    ILAA and clinical practice guideline recommendations
    for appropriate genetic testing in epilepsy evaluation.
    """

    TESTING_INDICATIONS = {
        "high_priority": [
            "Early infantile epileptic encephalopathy (EIEE)",
            "Dravet syndrome (severe myoclonic epilepsy of infancy)",
            "Ohtahara syndrome",
            "Developmental and epileptic encephalopathies (DEEs)",
            "Family history of epilepsy",
            "Consistent family history of seizures",
            "Drug-resistant epilepsy starting <3 years old",
            "Epilepsy with specific syndromic features"
        ],
        "moderate_priority": [
            "Drug-resistant focal epilepsy",
            "Epilepsy with intellectual disability",
            "Epilepsy with autism spectrum features",
            "Epilepsy with dysmorphic features",
            "Epilepsy with movement disorders",
            "Unexplained epilepsy with congenital anomalies"
        ],
        "consider_testing": [
            "Any epilepsy with unexplained etiology",
            "Epilepsy with atypical features",
            "Familial epilepsy patterns",
            "Epilepsy with family planning considerations"
        ]
    }

    TESTING_PANELS = {
        "epilepsy_gene_panel": {
            "genes_tested": "100-300 genes (comprehensive)",
            "indications": "Most epilepsy genetic testing",
            "sensitivity": "30-40% for DEEs, 15-25% for other epilepsies",
            "turnaround": "4-8 weeks",
            "cost": "Variable (often covered for children, adults may have copay)"
        },
        "rapid_genome_sequencing": {
            "genes_tested": "All genes (genome-wide)",
            "indications": "Neonatal/infant critical illness",
            "sensitivity": "Higher than panel testing",
            "turnaround": "1-2 weeks (rapid)",
            "cost": "Higher than panel testing"
        },
        "whole_exome_sequencing": {
            "genes_tested": "All coding genes",
            "indications": "Panel negative, DEE, complex phenotypes",
            "sensitivity": "40-50% for DEEs",
            "turnaround": "8-12 weeks",
            "cost": "Similar to comprehensive panels"
        },
        "targeted_testing": {
            "genes_tested": "Single gene or few genes",
            "indications": "Known familial variant, specific syndrome",
            "sensitivity": "High if correct syndrome",
            "turnaround": "2-4 weeks",
            "cost": "Lowest"
        }
    }

    @classmethod
    def recommend_testing_strategy(
        cls,
        age_of_onset: str,
        epilepsy_type: str,
        developmental_status: str,
        family_history: str,
        drug_resistance: bool
    ) -> List[str]:
        """Recommend appropriate genetic testing strategy"""
        recommendations = []

        # High priority scenarios
        if age_of_onset == "infancy" or age_of_onset == "neonatal":
            recommendations.extend([
                "🧬 HIGH-YIELD GENETIC TESTING RECOMMENDED:",
                "• Comprehensive epilepsy gene panel (first-line)",
                "• Consider rapid genome sequencing if critical illness",
                "• Sensitivity: 30-40% for infantile epilepsies"
            ])

        elif drug_resistance and age_of_onset == "childhood":
            recommendations.extend([
                "🧬 GENETIC TESTING RECOMMENDED:",
                "• Comprehensive epilepsy gene panel",
                "• Consider whole exome sequencing if panel negative",
                "• Sensitivity: 25-35% for drug-resistant childhood epilepsy"
            ])

        elif "intellectual disability" in developmental_status.lower() or "autism" in developmental_status.lower():
            recommendations.extend([
                "🧬 GENETIC TESTING RECOMMENDED:",
                "• Epilepsy gene panel with neurodevelopmental genes",
                "• Consider chromosomal microarray (CMA) simultaneously",
                "• Higher yield with comorbid neurodevelopmental disorders"
            ])

        elif family_history == "positive":
            recommendations.extend([
                "🧬 FAMILY STUDY RECOMMENDED:",
                "• Test affected family member first (most informative)",
                "• If variant identified, targeted testing for relatives",
                "• Genetic counseling recommended for family"
            ])

        # Special considerations
        if drug_resistance:
            recommendations.extend([
                "",
                "💡 DRUG-RESISTANT EPILEPSY:",
                "• Genetic yield higher in drug-resistant cases",
                "• May guide ASM selection (channelopathies)",
                "• May inform prognosis and recurrence risk",
                "• Consider surgical candidacy implications"
            ])

        return recommendations

    @classmethod
    def get_testing_process(cls) -> List[str]:
        """Get genetic testing process and counseling points"""
        return [
            "🧬 GENETIC TESTING PROCESS:",
            "",
            "1️⃣ PRE-TEST COUNSELING:",
            "• Explain purpose and potential outcomes",
            "• Discuss possibility of VUS (variant of uncertain significance)",
            "• Discuss implications for family members",
            "• Discuss insurance coverage and costs",
            "• Obtain informed consent",
            "",
            "2️⃣ TESTING:",
            "• Sample collection (usually blood)",
            "• DNA extraction and analysis",
            "• Variant interpretation and classification",
            "• Quality confirmation",
            "",
            "3️⃣ POST-TEST COUNSELING:",
            "• Explain results and clinical significance",
            "• Discuss treatment implications",
            "• Discuss recurrence risks",
            "• Discuss family testing implications",
            "• Provide psychological support",
            "",
            "📋 INSURANCE CONSIDERATIONS:",
            "• Often covered for children (<18)",
            "• Variable coverage for adults",
            "• Prior authorization may be required",
            "• Financial assistance programs available"
        ]


class PrecisionMedicine:
    """
    Precision medicine approaches in epilepsy

    Evidence-based precision medicine strategies including
    pharmacogenomics, targeted therapies, and personalized treatment.
    """

    PHARMACOGENOMIC_CONSIDERATIONS = {
        "HLA_B_1502": {
            "medication": "Carbamazepine, Oxcarbazepine",
            "population": "Asian ancestry",
            "risk": "Stevens-Johnson syndrome / toxic epidermal necrolysis",
            "recommendation": "Test before starting carbamazepine in Asian populations",
            "alternative": "Use alternative ASMs if positive"
        },
        "CYP2C9": {
            "medication": "Phenytoin",
            "variants": ["*2, *3"],
            "effect": "Reduced metabolism → higher phenytoin levels",
            "recommendation": "Lower starting dose if poor metabolizer",
            "monitoring": "Check phenytoin levels closely"
        },
        "UGT1A4": {
            "medication": "Lamotrigine",
            "effect": "Metabolism variation",
            "recommendation": "Monitor for toxicity in poor metabolizers",
            "clinical_relevance": "Limited evidence currently"
        }
    }

    TARGETED_THERAPIES = {
        "mTOR_inhibitors": {
            "indications": ["DEPDC5 mutations", "TSC1/TSC2 mutations", "mTORopathies"],
            "medications": ["Everolimus", "Sirolimus"],
            "evidence": "Case reports and series, limited RCTs",
            "considerations": "Emerging precision medicine approach"
        },
        "potassium_channel_openers": {
            "indications": ["KCNQ2 mutations", "KCNQ3 mutations"],
            "medications": ["Retigabine/Ezogabine"],
            "evidence": "Mechanistically appropriate, variable clinical response",
            "considerations": "Retigabine availability limited (withdrawn from many markets)"
        },
        "quinine": {
            "indications": ["KCNQ2 gain-of-function"],
            "medications": ["Quinine (off-label)"],
            "evidence": "Limited case reports",
            "considerations": "Experimental approach"
        }
    }

    @classmethod
    def get_precision_medicine_guidance(
        cls,
        genetic_findings: Optional[Dict] = None,
        medication_response: Optional[Dict] = None
    ) -> List[str]:
        """Get precision medicine guidance based on genetics and response"""
        guidance = []

        if genetic_findings:
            gene = genetic_findings.get("gene", "")
            asm_guidance = GeneticEpilepsies.get_asm_guidance_by_genetics(gene)

            if asm_guidance:
                guidance.extend([
                    f"🎯 GENETICS-GUIDED ASM SELECTION ({gene}):",
                    f"Mechanism: {asm_guidance['clinical_pearl']}",
                    "",
                    "✅ EFFECTIVE ASMs:"
                ])
                guidance.extend([f"   • {asm}" for asm in asm_guidance["effective_ASMS"]])

                if asm_guidance["avoid"]:
                    guidance.extend([
                        "",
                        "⚠️ AVOID:"
                    ])
                    guidance.extend([f"   • {asm}" for asm in asm_guidance["avoid"]])

        if medication_response:
            # Pharmacogenomic considerations
            if "carbamazepine" in str(medication_response).lower():
                guidance.extend([
                    "",
                    "💊 PHARMACOGENOMIC CONSIDERATIONS:",
                    "• Consider HLA-B*15:02 testing if Asian ancestry",
                    "• SJS/TEN risk significant in positive carriers"
                ])

        if not guidance:
            guidance.extend([
                "✓ No specific precision medicine recommendations",
                "• Current evidence doesn't support genotype-guided therapy",
                "• Standard ASM selection appropriate",
                "• Consider research trials if appropriate"
            ])

        return guidance

    @classmethod
    def get_emerging_therapies(cls) -> List[str]:
        """Get information on emerging precision therapies"""
        return [
            "🔬 EMERGING PRECISION THERAPIES:",
            "",
            "Gene Therapy:",
            "• Antisense oligonucleotides (ASOs) - in development",
            "• RNA-based therapies - preclinical stage",
            "• Gene editing (CRISPR) - preclinical research",
            "",
            "Targeted Small Molecules:",
            "• mTOR inhibitors (everolimus) - available for TSC",
            "• Potassium channel modulators - in development",
            "• Sodium channel modulators - in development",
            "",
            "Precision Monitoring:",
            "• Pharmacogenomic testing - emerging evidence",
            "• Drug level monitoring - standard of care",
            "• Biomarker development - active research",
            "",
            "💡 CLINICAL TRIALS:",
            "• Consider clinical trial referral for drug-resistant epilepsy",
            "• Precision medicine trials often genotype-specific",
            "• Natural history studies valuable for rare disorders"
        ]


__all__ = [
    'InheritancePattern',
    'VariantSignificance',
    'GeneticFinding',
    'GeneticEpilepsies',
    'GeneticTestingGuidance',
    'PrecisionMedicine'
]