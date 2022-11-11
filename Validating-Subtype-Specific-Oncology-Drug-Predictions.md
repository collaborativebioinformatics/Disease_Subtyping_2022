# Abstract

There are an impressive number of data and code reproducibility initiatives, both within Europe and across the world.  To motivate researchers to use this amazing infrastructure, we must show the translational research community that the aforementioned initiatives are able to drive change in translational science.  Here we demonstrate that using public datasets, it is reasonable to build a pipeline for proposal and validation of driver mutation and subtype specific colorectal cancer medications.  While both molecular, clinical and chemical name harmonization was necessary, open data and code initiatives -- while varied in their approaches -- made this project possible.  

# Introduction and Methods

Consensus molecular subtypes for colorectal cancer were first established by Guinney and collaborators in 2015 (ref 1).  Since then, many studies have corroborated this work, showing both clinical validity and differential treatment efficacy in the respective subtypes (ref 2-5).  We have taken the transcriptional pathways that characterize the specific molecular subtypes and crosssed them with the network perturbations cited for approved drugs in the lincs project (ref 6), a project designed to test how particular, often FDA approved, small molecules affect transcriptional networks.  Doing this has resulted in a list of normalized associative counts of small molecules that may be specifically effective for particular colorectal cancer subtypes (table 1.)  We have extended this analysis to predict treatment for particular canonical expression changes within a given subtype.  We have now built a validation engine for these hits, integrating RNAseq data with clinical outcomes after pharmacological intervention in disease.  In addition, we are able to further train this validation engine by looking at what drugs tcga participants were treated with and how effective they were (months total survival).  We are currently extending this validation engine to incorporate recent clinical trial results from Europe and the United States.  Given both the molecular scores based on pathway analysis and the information theoretic scores from clinical trial and RWE/EMR analysis (UK Biobank and elsewhere), we intend to build a learning knowledge graph able to integrate futher molecular and clinical trial information semi-automatically.  Overall, we believe that this is a demonstration that porting federated data from a variety of diverse public sources can have translational applicability, in this case to a number of high-mortality cancers. 

# Results

Work on this project was initially done on the DNAnexus platform, although it should be portable to any command line based or gui/command line hybrid bioinformatics ecosystem.  It is available on GitHub at [](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022).  

Our method performs RNA-seq or microarray analysis on colorectal cancer data, in search of differentially (over/under) expressed genes that the Colotype paper (ref 7) indicates are associated with different subtypes of colorectal cancer.  Our method also analyzes 12 different reported driver genes (ref 8,9,10) for colorectal cancer (table 2), and associates them with various subtypes (radar plots in figures 1-4).  For the purposes of this manuscript, we took the top ten driver (or combination there of) subtype combinations.   

The analysis result is then used to generate drug recommendations based on enzymes involved in those pathways and finding their inhibitors or activators. A quantitative molecular score is then generated for these results (supplemental table 1).  The drug recommendations are then evaluated for clinical tolerance and indications of efficacy, generating a quantitative score from those metrics.  The absolute number of (colorectal cancer OR colon cancer) AND {drug name} mentions (google scholar) are first divided by mentions of the drug name with cancer to determine a "cancer specificity index".  To be clear, we do not necessarily assume that cancer drugs are the only effective "off-label" therapeutics for colorectal cancer.  A separate frequency index is calculated by dividing the absolute number of mentions by the frequency of searches on the indexable internet. Additional categorical factors were assigned: whether the drug appeared in any trial, whether the drug was approved, whether the drug was already in use as an adjuvant or chemotherapeutic, and whether there was onoging research around the drug. These scores were standardized using the scikit.learn package and averaged to create an overall index score. Those with a calculable score are shown in table 2.  We intend to "reverse" this process to analyze the potential efficacy of drugs that are "on-label" and in clinical trials. Additionally we intend improve these scores by including data about adverse events and by collecting enough data to appropriately weight the components of score when they are averaged.       

| predicted_therapy   | crc_specificity_score | evidence_score | approved |
|---------------------|----------------------:|---------------:|---------:|
| sirolimus           |                 0.523 |          0.855 |      1.0 |
| birinapant          |                 0.512 |          0.252 |      0.0 |
| Licarbazepine       |                 0.321 |          0.500 |      1.0 |
| Y27632              |                 0.297 |          0.250 |      0.0 |
| gliquidone          |                 0.294 |          0.500 |      1.0 |
| Bendamustine        |                 0.292 |          0.799 |      1.0 |
| rituximab           |                 0.286 |           1.00 |      1.0 |
| Clofibrate          |                 0.260 |          0.500 |      1.0 |
| Fenofibrate         |                 0.258 |          0.502 |      1.0 |
| Bezafibrate         |                 0.256 |          0.500 |      1.0 |
| U0126               |                 0.253 |            0.0 |      0.0 |
| SB-590885           |                 0.251 |            0.0 |      0.0 |
| apafant             |                 0.049 |            0.0 |      0.0 |
| CI-1040 (PD-184352) |                 0.024 |          0.250 |      0.0 |
| BRD-A90543464       |                   0.0 |            0.0 |      0.0 |
| BRD-K12707269       |                   0.0 |            0.0 |      0.0 |

**Table 2**: Standardized scores for predicted therapeutic compounds ranked by colo-rectal
         specificity, evidence support, and then approval status 
  
While validating these drugs, we found that some putative driver mutations (e.g. MLH1) introduced compounds -- with a high molecular score -- we believe to be "noise", by the metrics produced above.  We believe this is because of the collision of the information space of the interactions of the involved pathways -- in this case DNA repair -- with other drugs targeted at eukaryotic pathogens.  When we build our intended learning system, we will take this kind of information into account when calculating molecular scores, for colorectal cancer -- as well as other cancer -- subtypes.  The clinical learning system will be expanded to incorporate more real world evidence, both from rigorous -- and updatable -- searches of clinical trial data, as well as from large scale biobanks, such as the UK Biobank.  To that end, we have provided [a notebook](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/emerson-edits/generate_synonyms.ipynb) for generating synonyms for the drug names we find to be relevant to colo rectal cancer.  These synonyms were used to normalize patient treatment data used in our analysis.
  
We have made the entire pipeline semi-automatic, such that it may be implemented for other cancer types with definable CMS, such as bladder, small cell lung cancer or ovarian cancer (ref 11, 12, 13). In this project, we subtyped publicly available RNA-seq and microarray data using the CMScaller algorithm (<https://rdcu.be/cZqWL>) (Eide, P.W et. al, 2017), which uses Nearest Template Prediction (<https://doi.org/10.1371/journal.pone.0015543>) (Hoshida, Y., 2010) to classify colon cancer expression profiles into predefined subtypes. Our data preprocessing and application of these algorithms can be found on our github page in the cmscaller_pipeline folder. 
  
Overall, this entire workflow creates a link between a colorectal cancer subtype that a specific patient is suffering from, and a drug or small list of drugs that may be specifically effective in the treatment of an individuals' disease.  
  




# Discussion

# References



