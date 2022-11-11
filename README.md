# Validating Subtype Specific Oncology Drug Predictions

# Authors

Jędrzej Kubica, Emerson Huitt, Yusuke S, Amanda Khoo, Nick G, [other previous collaborators], Ben Busby

# Abstract

There are an impressive number of data and code reproducibility initiatives, both within Europe and across the world.  To motivate researchers to use this amazing infrastructure, we must show the translational research community that the aforementioned initiatives are able to drive change in translational science.  Here we demonstrate that using public datasets, it is reasonable to build a pipeline for proposal and validation of driver mutation and subtype specific colorectal cancer medications.  While both molecular, clinical and chemical name harmonization was necessary, open data and code initiatives -- while varied in their approaches -- made this project possible.  

# Introduction and Methods

Consensus molecular subtypes for colorectal cancer were first established by Guinney and collaborators in 2015 [^2].  Since then, many studies have corroborated this work, showing both clinical validity and differential treatment efficacy in the respective subtypes[^5][^7][^8][^9][^10].  We have taken the transcriptional pathways that characterize the specific molecular subtypes and crosssed them with the network perturbations cited for approved drugs in the lincs project [^4], a project designed to test how particular, often FDA approved, small molecules affect transcriptional networks.  Doing this has resulted in a list of normalized associative counts of small molecules that may be specifically effective for particular colorectal cancer subtypes (table 1.)  We have extended this analysis to predict treatment for particular canonical expression changes within a given subtype.  We have now built a validation engine for these hits, integrating RNAseq data with clinical outcomes after pharmacological intervention in disease.  In addition, we are able to further train this validation engine by looking at what drugs tcga participants were treated with and how effective they were (months total survival).  We are currently extending this validation engine to incorporate recent clinical trial results from Europe and the United States.  Given both the molecular scores based on pathway analysis and the information theoretic scores from clinical trial and RWE/EMR analysis (UK Biobank and elsewhere), we intend to build a learning knowledge graph able to integrate futher molecular and clinical trial information semi-automatically.  Overall, we believe that this is a demonstration that porting federated data from a variety of diverse public sources can have translational applicability, in this case to a number of high-mortality cancers. 

# Results

Work on this project was initially done on the DNAnexus platform, although it should be portable to any command line based or gui/command line hybrid bioinformatics ecosystem.  It is available on GitHub at ![repo](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022).  

Our method performs RNA-seq or microarray analysis on colorectal cancer data, in search of differentially (over/under) expressed genes that the Colotype paper [^1] indicates are associated with different subtypes of colorectal cancer.  Our method also analyzes 12 different reported driver genes (ref 8,9,10) for colorectal cancer (table 1), and associates them with various subtypes (Figures 1-4).  For the purposes of this manuscript, we took the top ten driver (or combination there of) subtype combinations. 

![Figure 1a]([https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/radar_plots/cms1_radar_plot.png](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/main/radar_plots/cms1_radar_plot.png))

The analysis result is then used to generate drug recommendations based on enzymes involved in those pathways and finding their inhibitors or activators. A quantitative molecular score is then generated for these results (supplemental table 1).  The drug recommendations are then evaluated for clinical tolerance and indications of efficacy, generating a quantitative score from those metrics.  The absolute number of (colorectal cancer OR colon cancer) AND {drug name} mentions (google scholar) are first divided by mentions of the drug name with cancer to determine a "cancer specificity index".  To be clear, we do not necessarily assume that cancer drugs are the only effective "off-label" therapeutics for colorectal cancer.  A separate frequency index is calculated by dividing the absolute number of mentions by the frequency of searches on the indexable internet. Additional categorical factors were assigned: whether the drug appeared in any trial, whether the drug was approved, whether the drug was already in use as an adjuvant or chemotherapeutic, and whether there was onoging research around the drug. These scores were standardized using the scikit.learn package and averaged to create an overall index score. Those with a calculable score are shown in table 1.  We intend to "reverse" this process to analyze the potential efficacy of drugs that are "on-label" and in clinical trials. Additionally we intend improve these scores by including data about adverse events and by collecting enough data to appropriately weight the components of score when they are averaged.       

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

**Table 1**: Standardized scores for predicted therapeutic compounds ranked by colo-rectal
         specificity, evidence support, and then approval status 
  
While validating these drugs, we found that some putative driver mutations (e.g. MLH1) introduced compounds -- with a high molecular score -- we believe to be "noise", by the metrics produced above.  We believe this is because of the collision of the information space of the interactions of the involved pathways -- in this case DNA repair -- with other drugs targeted at eukaryotic pathogens.  When we build our intended learning system, we will take this kind of information into account when calculating molecular scores, for colorectal cancer -- as well as other cancer -- subtypes.  The clinical learning system will be expanded to incorporate more real world evidence, both from rigorous -- and updatable -- searches of clinical trial data, as well as from large scale biobanks, such as the UK Biobank.  To that end, we have provided [a notebook](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/emerson-edits/generate_synonyms.ipynb) for generating synonyms for the drug names we find to be relevant to colo rectal cancer.  These synonyms were used to normalize patient treatment data used in our analysis.
  
We have made the entire pipeline semi-automatic, such that it may be implemented for other cancer types with definable CMS, such as bladder, small cell lung cancer or ovarian cancer (ref 11, 12, 13). In this project, we subtyped publicly available RNA-seq and microarray data using the CMScaller algorithm (<https://rdcu.be/cZqWL>) [^3], which uses Nearest Template Prediction (<https://doi.org/10.1371/journal.pone.0015543>) [^6] to classify colon cancer expression profiles into predefined subtypes. Our data preprocessing and application of these algorithms can be found on our github page in the cmscaller_pipeline folder. 
  
Overall, this entire workflow creates a link between a colorectal cancer subtype that a specific patient is suffering from, and a drug or small list of drugs that may be specifically effective in the treatment of an individuals' disease.  
  
# Discussion

# References

[^1]: Buechler SA, Stephens MT, Hummon AB, Ludwig K, Cannon E, Carter TC, Resnick J, Gökmen-Polar Y, Badve SS. ColoType: a forty gene signature for consensus molecular subtyping of colorectal cancer tumors using whole-genome assay or targeted RNA-sequencing. Sci Rep. 2020 Jul 21;10(1):12123. doi: 10.1038/s41598-020-69083-y. PMID: 32694712; PMCID: PMC7374173.
[^2]: Guinney, J., Dienstmann, R., Wang, X. et al. The consensus molecular subtypes of colorectal cancer. Nat Med 21, 1350–1356 (2015). https://doi.org/10.1038/nm.3967
[^3]: Eide, P.W., Bruun, J., Lothe, R.A. et al. CMScaller: an R package for consensus molecular subtyping of colorectal cancer pre-clinical models. Sci Rep 7, 16618 (2017). https://doi.org/10.1038/s41598-017-16747-x
[^4]: John Erol Evangelista, Daniel J B Clarke, Zhuorui Xie, Alexander Lachmann, Minji Jeon, Kerwin Chen, Kathleen M Jagodnik, Sherry L Jenkins, Maxim V Kuleshov, Megan L Wojciechowicz, Stephan C Schürer, Mario Medvedovic, Avi Ma’ayan, SigCom LINCS: data and metadata search engine for a million gene expression signatures, Nucleic Acids Research, Volume 50, Issue W1, 5 July 2022, Pages W697–W709, https://doi.org/10.1093/nar/gkac328
[^5]: Sanne ten Hoorn, MD, Tim R de Back, MD, Dirkje W Sommeijer, MD, PhD, Louis Vermeulen, MD, PhD, Clinical Value of Consensus Molecular Subtypes in Colorectal Cancer: A Systematic Review and Meta-Analysis, JNCI: Journal of the National Cancer Institute, Volume 114, Issue 4, April 2022, Pages 503–516, https://doi.org/10.1093/jnci/djab106
[^6]: Hoshida Y (2010) Nearest Template Prediction: A Single-Sample-Based Flexible Class Prediction with Confidence Assessment. PLoS ONE 5(11): e15543. https://doi.org/10.1371/journal.pone.0015543
[^7]: Lenz H-J, Ou F-S, Venook AP, et al.   Impact of consensus molecular subtype on survival in patients with metastatic colorectal cancer: results from CALGB/SWOG 80405 (alliance). J Clin Oncol. 2019;37(22):1876–1885. https://doi.org/10.1002/onco.13521
[^8]: Li Y, Yao Q, Zhang L, et al.   Immunohistochemistry-based consensus molecular subtypes as a prognostic and predictive biomarker for adjuvant chemotherapy in patients with stage II colorectal cancer. Oncologist. 2020;25(12):e1968–e1979. https://doi.org/10.1200/jco.18.02258
[^9]: Mooi JK, Wirapati P, Asher R, et al.   The prognostic impact of consensus molecular subtypes (CMS) and its predictive effects for bevacizumab benefit in metastatic colorectal cancer: molecular analysis of the AGITG MAX clinical trial. Ann Oncol. 2018;29(11):2240–2246. https://doi.org/10.1093/annonc/mdy410
[^10]: Allen WL, Dunne PD, McDade S, et al.   Transcriptional subtyping and CD8 immunohistochemistry identifies poor prognosis stage II/III colorectal cancer patients who benefit from adjuvant chemotherapy. J Clin Oncol Precis Oncol. 2018;(2):1–13 https://ascopubs.org/doi/pdfdirect/10.1200/PO.17.00241

The results <published or shown> here are in whole or part based upon data generated by the TCGA Research Network: https://www.cancer.gov/tcga

## Relevant Literature

Clinical Outcomes:

https://pubmed.ncbi.nlm.nih.gov/33041226/

Colotype:

https://www.nature.com/articles/s41598-020-69083-y

SV stuff:

https://www.frontiersin.org/articles/10.3389/fcell.2021.758776/full 

https://www.nature.com/articles/s41586-019-1913-9

CRC CMS:

https://www.nature.com/articles/nm.3967#MOESM37

Proteomics:

https://pubmed.ncbi.nlm.nih.gov/31031003/

https://www.nature.com/articles/nature13438

Small Cell Lung Cancer:

https://pubmed.ncbi.nlm.nih.gov/31877723/

Ovarian Cancer:

https://link.springer.com/article/10.1186/s13073-021-00952-5

## Relevant repos

https://github.com/BioITHackathons/Creating-Computable-Knowledge-from-Unstructured-Information (Emerson look at this)

the script with 'drug vs association count' table: https://github.com/collaborativebioinformatics/Disease_subsetting/blob/main/maayan-drug-discovery.ipynb


## Relevant datasets

#### Proteomics

CPTAC
  https://proteomic.datacommons.cancer.gov/pdc/
The Human Protein Atlas
  https://www.proteinatlas.org
  
#### Clinical Trials

EU Clinical Trials Registry
  https://www.clinicaltrialsregister.eu
US Clinical Trials Registry
  clinicaltrials.gov

#### Cancer Datasets

TCGA (SV)

  <Link missing>

<Header missing>

  https://www.cell.com/cell/fulltext/S0092-8674(18)30229-0
  
<Header missing>
  xena.ucsc.edu

#### SRA dataset list

See files
  SRR_Acc_List_cms{x}.txt

#### Biobanks 

UK Biobank
  ukbiobank.dnanexus.com

#### Imaging repositories

TCIA (The Cancer Imaging Archive)
  https://wiki.cancerimagingarchive.net/display/Public/CT+COLONOGRAPHY

## Tools

SUMO: https://github.com/ratan-lab/sumo

MultiPLIER: https://github.com/greenelab/multi-plier

Boruta R package (feature selection): https://www.jstatsoft.org/article/view/v036i11
