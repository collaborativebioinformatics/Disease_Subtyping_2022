# Validating Subtype Specific Oncology Drug Predictions

# Authors

Jędrzej Kubica, Emerson Huitt, Yusuke Suita, Amanda S. Khoo, Hyongyoung Shin, David Enoma, Nick Giangreco, Ben Busby

# Abstract

There are an impressive number of data and code reproducibility initiatives, both within Europe and across the world.  To motivate researchers to use this amazing infrastructure, we must show the translational research community that the aforementioned initiatives are able to drive change in translational science.  Here we demonstrate that using public datasets, it is reasonable to build a pipeline for proposal and validation of driver mutation and subtype-specific colorectal cancer medications.  While all three molecular, clinical and chemical name harmonization were necessary, open data and code initiatives -- while varied in their approaches -- made this project possible.  

# Introduction and Methods

Consensus molecular subtypes (CMS) for colorectal cancer were first established by Guinney and collaborators in 2015 [^2].  Since then, many studies have corroborated this work, showing both clinical validity and differential treatment efficacy in the respective subtypes [^5][^7][^8][^9][^10].  We have taken the transcriptional pathways that characterize specific molecular subtypes and crosssed them with the network perturbations cited for approved drugs in the SigCom LINCS [^4] - a project designed to test how particular small molecules (often approved by the FDA) affect transcriptional networks.  Doing this has resulted in a list of normalized associative counts of small molecules that may be specifically effective for particular colorectal cancer subtypes (Table 1).  We have extended this analysis to predict treatment for particular canonical expression changes within  given subtypes.  We have now built a validation engine for these hits, integrating RNA-seq data with clinical outcomes after pharmacological intervention in the disease [^12][^13].  In addition, we are able to further train this validation engine by looking at drugs with which the participants were treated and how effective those drugs were (months total survival).  We are currently extending this validation engine to incorporate recent clinical trial results from Europe and the United States.  Given the molecular scores based on pathway analysis and the theoretic scores from both clinical trials and RWE/EMR analysis (UK Biobank and elsewhere), we intend to build a learning knowledge graph integrating futher molecular and clinical trial information semi-automatically.  Overall, we believe that this is a demonstration that porting federated data from a variety of diverse public sources can have translational applicability, in this case to a number of high-mortality cancers. 

# Results

Work on this project was initially done on the DNAnexus platform, although it should be portable to any command-line based or gui/command-line hybrid bioinformatics ecosystem.  It is available on GitHub at [Disease Subtyping 2022](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022).  


To confirm the assertion made by a number of authors that the efficacy of treatment varies based on subtypes of patients [^17][^18][^19], we have performed survival analysis on the colorectal patients stratified by subtypes and treatment groups.  First, subtyping of colon cancer patient data was performed using the CMScaller algorithm [^13]. This algorithm uses Nearest Template Prediction [^14] to classify colon cancer expression profiles into predefined subtypes.  Subtyped patients were then stratified by CMS and treatment groups for survival analysis. Data preprocessing, algorithm application and survival analysis code can be found on the [Disease Subtyping 2022 GitHub page](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022) in the [cmscaller_pipeline](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/tree/main/cmscaller_pipeline) folder and in the [scripts](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/tree/main/scripts) folder. The survival analysis function allows the user to input subtype and treatment group(s) for comparison, and returns the overall survival of such patient with that specific subtype and treatment. This analysis showed that patients with CMS4 that received bevacizumab, fluorouracil, leucovorin, and irinotecan survied longer than those who received only fluorouracil, leucovorin, and irinotecan. On the other hand, patients with CMS1 who received bevacizumab, fluorouracil, leucovorin, and irinotecan survived shorter than those who received only fluorouracil, leucovorin, and irinotecan. This result provides further support for the previous assertion that subtyping can increase the efficacy of treatment. This survival analysis platform can be used to determine which commonly used treatments are best suited for a particular subtype of colon cancer patients.  

![Figure 1: survival curve of patients who received bevacizumab, fluorouracil, leucovorin, and irinotecan vs fluorouracil, leucovorin, and irinotecan (CMS4)](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/6c4c6cc74e15111db3172218de202ea2ef79dd79/survivalcurve_plots/CMS4.jpeg)
**Figure 1.** Survival analysis curve for patients with CMS4 who received either bevacizumab, fluorouracil, leucovorin, and irinotecan (red line) or fluorouracil, leucovorin, and irinotecan (blue line).


![Figure 1: survival curve of patients who received bevacizumab, fluorouracil, leucovorin, and irinotecan vs fluorouracil, leucovorin, and irinotecan ( CMS1)](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/6c4c6cc74e15111db3172218de202ea2ef79dd79/survivalcurve_plots/CMS1.jpeg)
**Figure 2.** Survival analysis curve for patients with CMS1 who received either bevacizumab, fluorouracil, leucovorin, and irinotecan (red line) or  fluorouracil, leucovorin, and irinotecan (blue line).


To further refine this approach to precision medicine, we built a method to perform an RNA-seq or microarray analysis on colon cancer data searching for differentially over- or underexpressed genes that have been demonstrated in the paper by and Buechler collaborators [^1] to be associated with different subtypes of colorectal cancer.  Our method also analyzes 12 different reported driver genes for colorectal cancer [^20], and associates them with various subtypes.  For the purposes of this manuscript, we show the top driver genes (or combination there of) for particular subtypes, outlined in the radar plots shown in Figures 2 a-d.  

![Figure 2a](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/main/radar_plots/cms1_radar_plot.png)
**Figure 2a.** Top driver genes (or their combinations) for CMS1.


![Figure 2b](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/main/radar_plots/cms2_radar_plot.png)
**Figure 2b.** Top driver genes (or their combinations) for CMS2.


![Figure 2c](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/main/radar_plots/cms3_radar_plot.png)
**Figure 2c.** Top driver genes (or their combinations) for CMS3.


![Figure 2d](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/main/radar_plots/cms4_radar_plot.png)
**Figure 2d.** Top driver genes (or their combinations) for CMS4.


The results of the analysis were used to generate drug recommendations based on enzymes involved in those pathways and to find their inhibitors or activators. A quantitative molecular score was then generated for those results (Table 1).  The drug recommendations were then evaluated for clinical tolerance and indications of efficacy, generating a quantitative score from those metrics.  The absolute number of {colorectal cancer OR colon cancer} AND {drug name} mentions (Google Scholar) were first divided by mentions of the drug name with cancer to determine a 'cancer specificity index'.  To be clear, we did not necessarily assume that cancer drugs were the only effective 'off-label' therapeutics for colorectal cancer. A separate frequency index was calculated by dividing the absolute number of mentions by the frequency of searches on the indexable Internet.  Additional categorical factors were assigned: whether the drug appeared in any clinical trial, whether the drug was approved, whether the drug was already in use as an adjuvant or chemotherapeutic, and whether there had been an onoging research on the drug.  These scores were standardized using the scikit.learn package and averaged to create an overall index score.  Those with a calculable score are shown in Table 1. We intend to reverse this process to analyze the potential efficacy of drugs that are 'on-label' and in clinical trials.  Additionally, we intend to improve these scores by including data about adverse events and by collecting enough data to appropriately weight the components of score when they are averaged.       

| Predicted therapy   | CRC specificity score | Evidence score | Approved |
|---------------------|----------------------:|---------------:|---------:|
| Sirolimus           |                 0.523 |          0.855 |      1.0 |
| Birinapant          |                 0.512 |          0.252 |      0.0 |
| Licarbazepine       |                 0.321 |          0.500 |      1.0 |
| Y27632              |                 0.297 |          0.250 |      0.0 |
| Gliquidone          |                 0.294 |          0.500 |      1.0 |
| Bendamustine        |                 0.292 |          0.799 |      1.0 |
| Rituximab           |                 0.286 |          1.000 |      1.0 |
| Clofibrate          |                 0.260 |          0.500 |      1.0 |
| Fenofibrate         |                 0.258 |          0.502 |      1.0 |
| Bezafibrate         |                 0.256 |          0.500 |      1.0 |
| U0126               |                 0.253 |          0.000 |      0.0 |
| SB-590885           |                 0.251 |          0.000 |      0.0 |
| Apafant             |                 0.049 |          0.000 |      0.0 |
| CI-1040 (PD-184352) |                 0.024 |          0.250 |      0.0 |
| BRD-A90543464       |                 0.000 |          0.000 |      0.0 |
| BRD-K12707269       |                 0.000 |          0.000 |      0.0 |

**Table 3**: Standardized scores for predicted therapeutic compounds ranked by specificity, evidence support, and approval status.
  
  
While validating the drugs, we found that some putative driver mutations (e.g. MLH1) introduced compounds with a high molecular score to be a 'noise', by the metrics produced above.  We believe this happend because of the collision between the information space of the interactions of the involved pathways (in this case DNA repair) and other drugs targeted at eukaryotic pathogens.  When we build our intended learning system, we will take this kind of information into account in order to calculate molecular scores for colorectal cancer subtypes, as well as for other cancer types.  The clinical learning system will be expanded to incorporate more real world evidence, both from rigorous and updatable searches of clinical trial data, as well as from large scale biobanks (such as the UK Biobank) specifically on the UK Biobank Research Analysis Platform (UKBRAP) in that case.  To that end, we have provided [a notebook](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/blob/emerson-edits/generate_synonyms.ipynb) for generating synonyms for the drug names we find to be relevant in colorectal cancer treatment.  The synonyms include publically available data [^11] and synonyms for combination therapies generated as a part of literature review.  These synonyms were used to normalize patient treatment data used in our analysis.
  
We have made the entire pipeline semi-automatic, such that it may be implemented for other cancer types with definable CMS, such as bladder [^16], small cell lung cancer [^15] or ovarian cancer [^14]. 

The immediate next step for this project is to combine our pipeline with the observational multi-drug pipeline in a subtype dependent way.  We believe this will give the oncology research community the best suggestions for precision delivery of drug combinations.  
  
Overall, the entire workflow creates a link between the colorectal cancer subtype from which a specific patient is suffering, and a drug or a small list of drugs that may be specifically effective in the treatment of individual patients.  
  
# Discussion

We have created a basic validation platform for driver mutation and subtype-specific drug predictions for colorectal cancer.  There are four general directions in which we would like to expand the project.  First, having a more automated data import and metadata harmonization pipeline for transcriptional and clinical data, leveraging modern data sharing and management techniques.  Second, developing a semantic web-based learning system off the back of this analysis, such that scores can be continually refined as more biobanks, clinical trials and RWE comes online. 
Third, developing a proteomic and a DNA-based methods for CMS subtyping that can be leveraged as clinical diagnostics.  Fourth, expanding this analysis to other cancer types that have identified CMS, such as ovarian, bladder and small cell lung cancer.  

# References

[^1]: Buechler, S.A., Stephens, M.T., Hummon, A.B. et al. ColoType: a forty gene signature for consensus molecular subtyping of colorectal cancer tumors using whole-genome assay or targeted RNA-sequencing. Sci Rep 10, 12123 (2020). https://doi.org/10.1038/s41598-020-69083-y
[^2]: Guinney, J., Dienstmann, R., Wang, X. et al. The consensus molecular subtypes of colorectal cancer. Nat Med 21, 1350–1356 (2015). https://doi.org/10.1038/nm.3967
[^3]: Eide, P.W., Bruun, J., Lothe, R.A. et al. CMScaller: an R package for consensus molecular subtyping of colorectal cancer pre-clinical models. Sci Rep 7, 16618 (2017). https://doi.org/10.1038/s41598-017-16747-x
[^4]: John Erol Evangelista, Daniel J B Clarke, Zhuorui Xie, Alexander Lachmann, Minji Jeon, Kerwin Chen, Kathleen M Jagodnik, Sherry L Jenkins, Maxim V Kuleshov, Megan L Wojciechowicz, Stephan C Schürer, Mario Medvedovic, Avi Ma’ayan, SigCom LINCS: data and metadata search engine for a million gene expression signatures, Nucleic Acids Research, Volume 50, Issue W1, 5 July 2022, Pages W697–W709, https://doi.org/10.1093/nar/gkac328
[^5]: Sanne ten Hoorn, MD, Tim R de Back, MD, Dirkje W Sommeijer, MD, PhD, Louis Vermeulen, MD, PhD, Clinical Value of Consensus Molecular Subtypes in Colorectal Cancer: A Systematic Review and Meta-Analysis, JNCI: Journal of the National Cancer Institute, Volume 114, Issue 4, April 2022, Pages 503–516, https://doi.org/10.1093/jnci/djab106
[^6]: Hoshida Y (2010) Nearest Template Prediction: A Single-Sample-Based Flexible Class Prediction with Confidence Assessment. PLoS ONE 5(11): e15543. https://doi.org/10.1371/journal.pone.0015543
[^7]: Lenz H-J, Ou F-S, Venook AP, et al.   Impact of consensus molecular subtype on survival in patients with metastatic colorectal cancer: results from CALGB/SWOG 80405 (alliance). J Clin Oncol. 2019;37(22):1876–1885. https://doi.org/10.1002/onco.13521
[^8]: Li Y, Yao Q, Zhang L, et al.   Immunohistochemistry-based consensus molecular subtypes as a prognostic and predictive biomarker for adjuvant chemotherapy in patients with stage II colorectal cancer. Oncologist. 2020;25(12):e1968–e1979. https://doi.org/10.1200/jco.18.02258
[^9]: Mooi JK, Wirapati P, Asher R, et al.   The prognostic impact of consensus molecular subtypes (CMS) and its predictive effects for bevacizumab benefit in metastatic colorectal cancer: molecular analysis of the AGITG MAX clinical trial. Ann Oncol. 2018;29(11):2240–2246. https://doi.org/10.1093/annonc/mdy410
[^10]: Allen WL, Dunne PD, McDade S, et al.   Transcriptional subtyping and CD8 immunohistochemistry identifies poor prognosis stage II/III colorectal cancer patients who benefit from adjuvant chemotherapy. J Clin Oncol Precis Oncol. 2018;(2):1–13 https://ascopubs.org/doi/pdfdirect/10.1200/PO.17.00241
[^11]: A Mohammad. Khaleel, Amer Hayat Khan, S.M. Sheikh Ghadzi, Sami Alshakhshir. Curation of an international drug proprietary names dataset. Data in Brief. Volume 40 2022;1 07701 https://doi.org/10.1016/j.dib.2021.107701.
[^12]: Liu, JianfangCaesar-Johnson, Samantha J. et al. An Integrated TCGA Pan-Cancer Clinical Data Resource to Drive High-Quality Survival Outcome Analytics. Cell, Volume 173, Issue 2, 400 - 416.e11 https://doi.org/10.1016/j.cell.2018.02.052
[^13]: Del Rio M, Mollevi C, Bibeau F, Vie N, Selves J, Emile JF, Roger P, Gongora C, Robert J, Tubiana-Mathieu N, Ychou M, Martineau P. Molecular subtypes of metastatic colorectal cancer are associated with patient response to irinotecan-based therapies. Eur J Cancer. 2017 May;76:68-75. doi: 10.1016/j.ejca.2017.02.003. Epub 2017 Mar 8. PMID: 28284171. https://doi.org/10.1016/j.ejca.2017.02.003
[^14]: Richard W. Tothill, Anna V. Tinker, Joshy George, Robert Brown, Stephen B. Fox, Stephen Lade, Daryl S. Johnson, Melanie K. Trivett, Dariush Etemadmoghadam, Bianca Locandro, Nadia Traficante, Sian Fereday, Jillian A. Hung, Yoke-Eng Chiew, Izhak Haviv, Australian Ovarian Cancer Study Group, Dorota Gertig, Anna deFazio, David D.L. Bowtell; Novel Molecular Subtypes of Serous and Endometrioid Ovarian Cancer Linked to Clinical Outcome. Clin Cancer Res 15 August 2008; 14 (16): 5198–5208. https://doi.org/10.1158/1078-0432.CCR-08-0196
[^15]: Rudin, C.M., Poirier, J.T., Byers, L.A. et al. Molecular subtypes of small cell lung cancer: a synthesis of human and mouse model data. Nat Rev Cancer 19, 289–297 (2019). https://doi.org/10.1038/s41568-019-0133-9
[^16]: McConkey, D.J., Choi, W. Molecular Subtypes of Bladder Cancer. Curr Oncol Rep 20, 77 (2018). https://doi.org/10.1007/s11912-018-0727-5
[^17]: Okita A, Takahashi S, Ouchi K, Inoue M, Watanabe M, Endo M, Honda H, Yamada Y, Ishioka C. Consensus molecular subtypes classification of colorectal cancer as a predictive factor for chemotherapeutic efficacy against metastatic colorectal cancer. Oncotarget. 2018 Apr 10;9(27):18698-18711. doi: 10.18632/oncotarget.24617. PMID: 29721154; PMCID: PMC5922348.
[^18]: S. Stintzing, P. Wirapati, H.-J. Lenz, D. Neureiter, L. Fischer von Weikersthal, T. Decker, A. Kiani, F. Kaiser, S. Al-Batran, T. Heintges, C. Lerchenmüller, C. Kahl, G. Seipelt, F. Kullmann, M. Moehler, W. Scheithauer, S. Held, D.P. Modest, A. Jung, T. Kirchner, D. Aderka, S. Tejpar, V. Heinemann,
Consensus molecular subgroups (CMS) of colorectal cancer (CRC) and first-line efficacy of FOLFIRI plus cetuximab or bevacizumab in the FIRE3 (AIO KRK-0306) trial, Annals of Oncology, Volume 30, Issue 11, 2019, Pages 1796-1803, ISSN 0923-7534, https://doi.org/10.1093/annonc/mdz387.
[^19]: Arndt Stahler, Volker Heinemann, Veronika Schuster, Kathrin Heinrich, Annika Kurreck, Clemens Gießen-Jung, Ludwig Fischer von Weikersthal, Florian Kaiser, Thomas Decker, Swantje Held, Ullrich Graeven, Ingo Schwaner, Claudio Denzlinger, Michael Schenk, Jens Neumann, Thomas Kirchner, Andreas Jung, Jörg Kumbrink, Sebastian Stintzing, Dominik P. Modest,
Consensus molecular subtypes in metastatic colorectal cancer treated with sequential versus combined fluoropyrimidine, bevacizumab and irinotecan (XELAVIRI trial), European Journal of Cancer, Volume 157, 2021, Pages 71-80,ISSN 0959-8049, https://doi.org/10.1016/j.ejca.2021.08.017.
[^20]: Smit, W. L., Spaan, C. N., Johannes de Boer, R., Ramesh, P., Martins Garcia, T., Meijer, B. J., Vermeulen, J. L. M., Lezzerini, M., MacInnes, A. W., Koster, J., Medema, J. P., van den Brink, G. R., Muncan, V., & Heijmans, J. (2020). Driver mutations of the adenoma-carcinoma sequence govern the intestinal epithelial global translational capacity. In Proceedings of the National Academy of Sciences (Vol. 117, Issue 41, pp. 25560–25570). Proceedings of the National Academy of Sciences. https://doi.org/10.1073/pnas.1912772117
         
## Supplemental Links (Data and Tools)

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

CPTAC (Clinical Proteomic Tumor Analysis Consortium)
  https://proteomic.datacommons.cancer.gov/pdc/
  
The Human Protein Atlas
  https://www.proteinatlas.org
  
#### Clinical Trials

EU Clinical Trials Registry
  https://www.clinicaltrialsregister.eu
  
US Clinical Trials Registry
  https://clinicaltrials.gov

#### Cancer Datasets

TCGA (The Cancer Genome Atlas)
  https://www.cell.com/cell/fulltext/S0092-8674(18)30229-0
  
UCSC Xena
  http://xena.ucsc.edu

#### SRA dataset list

See files:
  [data/SRR_Acc_List_cms{x}.txt](https://github.com/collaborativebioinformatics/Disease_Subtyping_2022/tree/main/data)

#### Biobanks 

UK Biobank
  https://ukbiobank.dnanexus.com

#### Imaging repositories

TCIA (The Cancer Imaging Archive)
  https://wiki.cancerimagingarchive.net/display/Public/CT+COLONOGRAPHY

## Tools

SUMO (subtyping tool for multi-omic data): https://github.com/ratan-lab/sumo

MultiPLIER (unsupervised transfer learning approach for rare disease transcriptomics): https://github.com/greenelab/multi-plier

Boruta (R package for feature selection): https://www.jstatsoft.org/article/view/v036i11
