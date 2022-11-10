# Abstract

# Introduction 

Consensus molecular subtypes for colorectal cancer were first established by Guinney and collaborators in 2015 (ref 1).  Since then, many studies have corroborated this work, showing both clinical validity and differential treatment efficacy in the respective subtypes (ref 2-5).  We have taken the transcriptional pathways that characterize the specific molecular subtypes and crosssed them with the network perturbations cited for approved drugs in the lincs project (ref 6), a project designed to test how particular, often FDA approved, small molecules affect transcriptional networks.  Doing this has resulted in a list of normalized associative counts of small molecules that may be specifically effective for particular colorectal cancer subtypes (table 1.)  We have extended this analysis to predict treatment for particular canonical expression changes within a given subtype.  We have now built a validation engine for these hits, integrating RNAseq data with clinical outcomes after pharmacological intervention in disease.  In addition, we are able to further train this validation engine by looking at what drugs tcga participants were treated with and how effective they were (months total survival).  We are currently extending this validation engine to incorporate recent clinical trial results from Europe and the United States.  Given both the molecular scores based on pathway analysis and the information theoretic scores from clinical trial and RWE/EMR analysis (UK Biobank and elsewhere), we intend to build a learning knowledge graph able to integrate futher molecular and clinical trial information semi-automatically.  Overall, we believe that this is a demonstration that porting federated data from a variety of diverse public sources can have translational applicability, in this case to a number of high-mortality cancers. 

# Methods

Work on this project was initially done on the DNAnexus platform, although it should be portable to any command line based or gui/command line hybrid bioinformatics ecosystem.  It is available on GitHub at [<url for our repo> ](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022).  

Our method performs RNA-seq or microarray analysis on colorectal cancer data, in search of differentially (over/under) expressed genes that the Colotype paper (ref 7) indicates are associated with different subtypes of colorectal cancer.  Our method also analyzes 12 different reported driver genes (ref 8,9,10) for colorectal cancer (table 2), and associates them with various subtypes (radar plots in figures 1-4).  For the purposes of this manuscript, we took the top ten driver (or combination there of) subtype combinations.   

The analysis result is then used to come up with drug recommendations based on enzymes involved in those pathways and finding their inhibitors or activators. Overall, this entire workflow creates a link between a colorectal cancer subtype that a specific patient is suffering from, the specific and a drug that could be used in treatment of the disease. 

-   KEGG and Drugmonizome API-based applet to fetch all drugs targeting an input gene/pathway in a given disease pathway diagram (e.g. colorectal cancer)
-   Drugs are ranked according to a definition of associative strength (currently associated node count but could be based on another algorithm based on the importance of nodes or representation in literature)
-   Pathway visualization linked with the drug suggestions

## port from disease subtyping githubs


# Results

# Use Cases

# Discussion

# References



