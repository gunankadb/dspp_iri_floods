# DATA: Spatio-Temporal Flood Event Extraction from News Media to Support Satellite Based Flood Insurance 


## DATA
### article_scraping
Contains data about the articles, from different newspapers
- paper_data/all_paper_data - newspaper flood article data
    - <newspaper-name>.json contains scraped articles from that newspaper.
    - Each article contains metadata(article link, query keyword, date published), article text and a unique id
To download data for papers (the above data folder), please visit this link: [Paper Data](http://bit.ly/flood-research-paper-data)

### classifier
Contains data used for classification and validation
- data - data.json contains the data to train the classifier. This is labelled data, labelled using tagtog.net
- other_data - validation data (other datasets)
    - Sentinel1_ts - Sentinel 1 timeseries from 2017 - 2019 for all divisions and bangladesh
    - Damage data_Hassan.csv - Red Cross damage data for Bangladesh floods 
    - emdat_flood.csv - EMDAT damage data for Bangladesh floods 
    - Flood_Affected_Area_Barchart.csv - Government Flood area affected data for Bangladesh floods
    - tweets.json - Flood tweets data from Twitter from 2015 - 2020 <br/>
    To download tweets data, please visit this link: [Tweets Data](http://bit.ly/flood-research-tweets)
- timeseries_data - flood article data
    - all_data/all_isFlood.json - Contains all classified flood articles
    - logistics:
        - GeoIDMap.json - Geomap ids of districts and divisions in bangladesh
        - under_district.json - Upazilla under districts
        - under_division.json - Districts under divisions
    - twitter: Twitter Data
        - Twitter<division_name>.json - Twitter data for bangladesh 'all' and for each division
    - yearPublished_day: Daily flood article distribution data
        - yearPublished_<division_name>.json - Flood Articles for bangladesh 'all' and for each division, on a daily basis
    - yearPublished_day_newspaper - Daily flood article distribution data for each newspaper
        - <newspaper-name>.json - Flood article distribution for that newspaper
    - yearPublished_year_month - Monthly and yearly flood article distribution 
        - <division_name>.json - Monthly and yearly Flood articles distribution for bangladesh 'all' and for each division
- siteCounts.json - total number of articles published per newspaper from 2015 to 2020

### tagtog
- `Shapefiles_Final_30_7_2020.zip` - Shape file for Bangladesh <br/>
To download this shape file, please visit this link: [Bangladesh Shape File](http://bit.ly/flood-research-bangladesh-shapefile)