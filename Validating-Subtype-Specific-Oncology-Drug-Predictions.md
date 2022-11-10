# Abstract

# Introduction and Methods

Consensus molecular subtypes for colorectal cancer were first established by Guinney and collaborators in 2015 (ref 1).  Since then, many studies have corroborated this work, showing both clinical validity and differential treatment efficacy in the respective subtypes (ref 2-5).  We have taken the transcriptional pathways that characterize the specific molecular subtypes and crosssed them with the network perturbations cited for approved drugs in the lincs project (ref 6), a project designed to test how particular, often FDA approved, small molecules affect transcriptional networks.  Doing this has resulted in a list of normalized associative counts of small molecules that may be specifically effective for particular colorectal cancer subtypes (table 1.)  We have extended this analysis to predict treatment for particular canonical expression changes within a given subtype.  We have now built a validation engine for these hits, integrating RNAseq data with clinical outcomes after pharmacological intervention in disease.  In addition, we are able to further train this validation engine by looking at what drugs tcga participants were treated with and how effective they were (months total survival).  We are currently extending this validation engine to incorporate recent clinical trial results from Europe and the United States.  Given both the molecular scores based on pathway analysis and the information theoretic scores from clinical trial and RWE/EMR analysis (UK Biobank and elsewhere), we intend to build a learning knowledge graph able to integrate futher molecular and clinical trial information semi-automatically.  Overall, we believe that this is a demonstration that porting federated data from a variety of diverse public sources can have translational applicability, in this case to a number of high-mortality cancers. 

# Results

Work on this project was initially done on the DNAnexus platform, although it should be portable to any command line based or gui/command line hybrid bioinformatics ecosystem.  It is available on GitHub at [<url for our repo> ](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022).  

Our method performs RNA-seq or microarray analysis on colorectal cancer data, in search of differentially (over/under) expressed genes that the Colotype paper (ref 7) indicates are associated with different subtypes of colorectal cancer.  Our method also analyzes 12 different reported driver genes (ref 8,9,10) for colorectal cancer (table 2), and associates them with various subtypes (radar plots in figures 1-4).  For the purposes of this manuscript, we took the top ten driver (or combination there of) subtype combinations.   

The analysis result is then used to generate drug recommendations based on enzymes involved in those pathways and finding their inhibitors or activators. A quantitative molecular score is then generated for these results (supplemental table 1).  The drug recommendations are then evaluated for clinical tolerance and indications of efficacy, generating a quantitative score from those metrics.  The absolute number of colorectal cancer AND {drug name} mentions (google scholar) are first divided by mentions with cancer to determine a "cancer specificity index" (expressed as the reciprocal of that number).  To be clear, we do not necessarily assume that cancer drugs are the only effective "off-label" therapeutics for colorectal cancer.  The mentions are then separately divided by all known mentions of the {drug name} on the indexable internet. Those with a calculable score are shown in table 2 given both of the above normalization techniques are shown in table two.  We intend to "reverse" this process to analyze the potential efficacy of drugs that are "on-label" and in clinical trials.       
  
While validating these drugs, we found that some putative driver mutations (e.g. MLH1) introduced compounds -- with a high molecular score -- we believe to be "noise", by the metrics produced above.  We believe this is because of the collision of the information space of the interactions of the involved pathways -- in this case DNA repair -- with other drugs targeted at eukaryotic pathogens.  When we build our intended learning system, we will take this kind of information into account when calculating molecular scores, for colorectal cancer -- as well as other cancer -- subtypes.  The clinical learning system will be expanded to incorporate more real world evidence, both from rigorous -- and updatable -- searches of clinical trial data, as well as from large scale biobanks, such as the UK Biobank.  
  
We have made the entire pipeline semi-automatic, such that it may be implemented for other cancer types with definable CMS, such as bladder, small cell lung cancer or ovarian cancer (ref 11, 12, 13).  
  
Overall, this entire workflow creates a link between a colorectal cancer subtype that a specific patient is suffering from, and a drug or small list of drugs that may be specifically effective in the treatment of an individuals' disease.  
  




# Discussion

# References



