#!/usr/bin/env bash

#cp -r data/article_scraping/paper_data article_scraping/
cp -r data/classifier/data data/classifier/other_data data/classifier/timeseries_data data/classifier/siteCounts.json classifier/
#cp -r data/tagtog/Shapefiles_Final_30_7_2020.zip tagtog/
ln -s article_scraping/paper_data classifier/paper_data
ln -s article_scraping/all_papers.py classifier/all_papers.py