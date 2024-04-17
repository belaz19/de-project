# Los Angeles crimes data from 2020 to present  
  
# Overview
In this data engineering project, I develop an end-to-end data pipeline for collecting and visualizing data about crimes registered in Los Angeles since the year 2020. The dataset contains various information about the crime (such as crime type and area) and the victim (such as age and gender). I also combine this crimes' data with unemployment rates in Los Angeles, to see if there are any visuals correlations between the crimes' count and the unemployment rate.  
  
The datasets are collected using MAGE pipelines from open data sources belonging to the Los Angeles city and the California state. Then the datasets are processed with MAGE pipelines and put into Google Cloud Storage, and Google BigQuery data warehouse after that. Then the data is transformed with dbt tool, and returned as a new table ready for the dashboard. All these data pipelines are set to run once a week (batch processing).
  
This final transformed dataset is visualized in Looker Studio. This dasboard gives end-users the opportunity to explore the crimes data in each city' area at different timeframes, assess how safe do they feel being in the city. By looking at the dashboard and filtering the data to their needs, the users are able to see what gender and etnicity groups are most prone to be a victim, which crime type occurs the most, what is the most dangerous hour to be outside, is weapon used under these crimes, what is the overall developemnt of the crime count with time and does it have any correlation with the unemployemnt rate in the city.

This Git repository contains both, codes used by me in different data engineering tools and the instructions how this project can be replicated on your own machine (check "what-to-do" folder for details).
  
# Technologies used
