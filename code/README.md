# SCRIPTS: Spatio-Temporal Flood Event Extraction from News Media to Support Satellite Based Flood Insurance


## Setup
To run any file, please download data in the root folder and rename it as data. Then run `./setup.sh`


## Scripts
### article_scraping
Contains functions to scrape data from different newspapers.
To download data for papers, please visit this link: [Paper Data](http://bit.ly/flood-research-paper-data)
- `serpAPI.py`: Functions to query SERP API
- `all_papers.py`: 
    - Functions to call SERP API, extract data and process it to store it. 
    - Functions for different data distributions
    
### classifier
Contains function to run the classifier, draw time series, and validate data against other data sources
- `BERT_Classifier.ipynb` - Code to run the BERT classifier on data
- `classifier.ipynb` - Code to run rest of Classifiers (Random Forest, Linear SVC, Logistic Regression)
- `dataStats.ipynb` - Statistics about datasets
- `normalization_validation.ipynb` - Code to normalize the data and validate it against other data
- `timeseries.ipynb` - Code to calculate different timeseries (by newspaper, division, district, monthly, daily)
- `functions.py` - Helper file containing functions used in the above files.
- `ccf.py` - Function to calculate the cross-correlation between data

### tagtog
- `ShapeFiles.ipynb` - Code to manipulate shape files with tally of flood articles
