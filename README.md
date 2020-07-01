# cxr-risk
This repository hosts the contributor source files for the cxr-risk model. ModelHub integrates these files into an engine and controlled runtime environment. A unified API allows for out-of-the-box reproducible implementations of published models. For more information, please visit [www.modelhub.ai](http://modelhub.ai/) or contact us [info@modelhub.ai](mailto:info@modelhub.ai).
## meta
| | |
|-|-|
| id | ef562736-2539-43ec-81c0-40e0ff7d1f13 | 
| application_area | Radiology | 
| task | Classification | 
| task_extended | Survival Classification from chest Xray | 
| data_type | X-ray | 
| data_source | https://biometry.nci.nih.gov/cdas/datasets/plco/21/ | 
## publication
| | |
|-|-|
| title | Deep Learning to Assess Long-term Mortality From Chest Radiographs | 
| source | JAMA Network Open | 
| url | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2738349 | 
| year | 2019 | 
| authors |  Michael T. Lu, Alexander Ivanov, Thomas Mayrhofer, Ahmed Hosny, Hugo J.W.L. Aerts, Udo Hoffmann | 
| abstract | Importance:  Chest radiography is the most common diagnostic imaging test in medicine and may also provide information about longevity and prognosis. Objective:  To develop and test a convolutional neural network (CNN) (named CXR-risk) to predict long-term mortality, including noncancer death, from chest radiographs. Design, Setting, and Participants:  In this prognostic study, CXR-risk CNN development (n = 41 856) and testing (n = 10 464) used data from the screening radiography arm of the Prostate, Lung, Colorectal, and Ovarian Cancer Screening Trial (PLCO) (n = 52 320), a community cohort of asymptomatic nonsmokers and smokers (aged 55-74 years) enrolled at 10 US sites from November 8, 1993, through July 2, 2001. External testing used data from the screening radiography arm of the National Lung Screening Trial (NLST) (n = 5493), a community cohort of heavy smokers (aged 55-74 years) enrolled at 21 US sites from August 2002, through April 2004. Data analysis was performed from January 1, 2018, to May 23, 2019. Exposure:  Deep learning CXR-risk score (very low, low, moderate, high, and very high) based on CNN analysis of the enrollment radiograph. Main Outcomes and Measures:  All-cause mortality. Prognostic value was assessed in the context of radiologists diagnostic findings (eg, lung nodule) and standard risk factors (eg, age, sex, and diabetes) and for cause-specific mortality. Results:  Among 10 464 PLCO participants (mean (SD) age, 62.4 (5.4) years - 5405 men (51.6%) - median follow-up, 12.2 years (interquartile range, 10.5-12.9 years)) and 5493 NLST test participants (mean (SD) age, 61.7 (5.0) years - 3037 men (55.3%) - median follow-up, 6.3 years (interquartile range, 6.0-6.7 years)), there was a graded association between CXR-risk score and mortality. The very high-risk group had mortality of 53.0% (PLCO) and 33.9% (NLST), which was higher compared with the very low-risk group (PLCO: unadjusted hazard ratio (HR), 18.3 (95% CI, 14.5-23.2) - NLST: unadjusted HR, 15.2 (95% CI, 9.2-25.3) - both P < .001). This association was robust to adjustment for radiologists findings and risk factors (PLCO: adjusted HR (aHR), 4.8 (95% CI, 3.6-6.4) - NLST: aHR, 7.0 (95% CI, 4.0-12.1) - both P < .001). Comparable results were seen for lung cancer death (PLCO: aHR, 11.1 (95% CI, 4.4-27.8) - NLST: aHR, 8.4 (95% CI, 2.5-28.0) - both P ≤ .001) and for noncancer cardiovascular death (PLCO: aHR, 3.6 (95% CI, 2.1-6.2) - NLST: aHR, 47.8 (95% CI, 6.1-374.9) - both P < .001) and respiratory death (PLCO: aHR, 27.5 (95% CI, 7.7-97.8) - NLST: aHR, 31.9 (95% CI, 3.9-263.5) - both P ≤ .001). | 
| google_scholar | https://scholar.google.com/scholar?oi=bibs&hl=en&cites=16182133894523406915 | 
| bibtex | @article{10.1001/jamanetworkopen.2019.7416, author = {Lu, Michael T. and Ivanov, Alexander and Mayrhofer, Thomas and Hosny, Ahmed and Aerts, Hugo J. W. L. and Hoffmann, Udo}, title = '{Deep Learning to Assess Long-term Mortality From Chest Radiographs}', journal = {JAMA Network Open}, volume = {2}, number = {7}, pages = {e197416-e197416}, year = {2019}, month = {07}, issn = {2574-3805}, doi = {10.1001/jamanetworkopen.2019.7416}, url = {https://doi.org/10.1001/jamanetworkopen.2019.7416},} | 
## model
| | |
|-|-|
| description | CXR pregnosis is a fine tuned residual network based on ResNet-34. It predicts all-cause mortality in chest xrays. | 
| provenance | Conrtibuted by author. | 
| architecture | Convolutional Neural Network (CNN) | 
| learning_type | Supervised learning | 
| format | .pth | 
| I/O | model I/O can be viewed [here](contrib_src/model/config.json) | 
| license | model license can be viewed [here](contrib_src/license/model) | 
## run
To run this model and view others in the collection, view the instructions on [ModelHub](http://app.modelhub.ai/).
## contribute
To contribute models, visit the [ModelHub docs](https://modelhub.readthedocs.io/en/latest/).
