# Los Angeles crimes data  
  
# Overview and problem description
In this data engineering project, I develop an end-to-end data pipeline for collecting and visualizing data about crimes registered in Los Angeles since the year 2020. The dataset contains various information about the crime (such as crime type and area) and the victim (such as age and gender). I also combine this crimes' data with unemployment rates in Los Angeles, to see if there are any visuals correlations between the crimes' count and the unemployment rate.  
  
The datasets are collected (batch processing) using MAGE pipelines from open data sources belonging to the Los Angeles city and the California state. Then the datasets are processed with MAGE pipelines and put into Google Cloud Storage, and Google BigQuery data warehouse after that. Then the data is transformed with dbt tool, and returned as a new table ready for the dashboard.
  
This final transformed dataset is visualized in Looker Studio. This dasboard gives end-users the opportunity to explore the crimes data in each city' area at different timeframes, assess how safe do they feel being in the city. By looking at the dashboard and filtering the data to their needs, the users are able to see what gender and etnicity groups are most prone to be a victim, which crime type occurs the most, what is the most dangerous hour to be outside, is weapon used under these crimes, what is the overall developemnt of the crime count with time and does it have any correlation with the unemployemnt rate in the city.
  
![image](https://github.com/belaz19/de-project/assets/97640160/408f56eb-3c10-4f20-a512-a16a1dd3aa5b)
  
# Project Architecture  
![DE project flow](https://github.com/belaz19/de-project/assets/97640160/5cc22575-7cb9-4d17-8a60-51684ec8f5b6)
  
# Cloud
The project is developed in the Google Cloud Platform. The follwong resources are used on gcp: Virtual Machine with Linux, Buckets in cloud storage, datasets in BigQuery Studio.  
Terraform (IaC tool) is used to create (and later destroy) buckets and datasets.

# Data ingestion
Batch orchestration is implemented using MAGE running in a docker container. There are three pipelines created, each of them has multiple steps in DAG (data loader, data transformer, data exporter), all steps are orchestrated:
  1. crime_to_gcs. This pipelines loads the Los Angeles crime data (900,000+ records) from open source, define data types for each column, rename headers, and loads everything to the Bucket on Google Cloud Storage in a parquet file.  
  2. crime_to_bq. This pipeline dowloads the data from the data lake, does additional data transformations such as removing uncomplete rows, normalizing some columns' values, selecting the most relevant column, and uploading this data (600,000+ re) to the BigQuery dataset on Google Cloud.  
  3. unemp_to_bq. This pipeline loads data about unemployemnt rates in Los Angeles. Then the relevant rows and columns are selected. This becomes a relatively small dataset containing up to 100 rows, so I upload it directly to the BigQuery studio.

# Transformations
Transformations are defined in dbt cloud. There are two models defined in this dbt project: 1) staging model for staging the two raw input datasets that I have in BigQuery (Crime data and Unemployemnt data), and 2) core model for joining these two datasets together and getting the data ready for a dashboard. There are also some Macros created for changing values in certain column (victim descent and victim sex). After successfull testing a Production environemnt and a Deployment job has been created in dbt cloud to run the worflow whenever needed.

# Data warehouse
BigQuery on Google Cloud Platform is used as data warehouse. As described above the data is loaded to DWH with MAGE orchestrated pipelines, then it is transformed by DBT, and the final dataset is saved as "prod" dataset. The final tables are partitioned on Date and clustered by Area. This partitioning and clustering is implemented via DBT as the last step of data transformation.

# Dashboard
