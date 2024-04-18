# Los Angeles crime data  
  
# Overview and problem description
In this data engineering project, I develop an end-to-end data pipeline for collecting and visualizing data about crimes registered in Los Angeles since the year 2020. The dataset contains various information about the crimes (such as crime type and area) and victims (such as age and gender). I also combine this crimes' data with unemployment rates in Los Angeles, to see if there are any visual correlations between the crimes' count and the unemployment rate.  
  
The datasets are collected (batch processing) using MAGE pipelines from open data sources belonging to the Los Angeles city and the California state. Then the datasets are processed by MAGE pipelines and put into Google Cloud Storage, and Google BigQuery data warehouse (after an additional processing). Then the data is transformed with dbt tool for data transformation, and returned as a new table into BigQuery ready for the dashboard.
  
This final transformed dataset is visualized in Looker Studio. This dasboard gives end-users the opportunity to explore the crime data in each city's area at different time intervals, to assess how safe is he city for each people group. By looking at the dashboard and filtering the data to their needs, the users are able to see what gender and etnicity groups have became the victims, which crime types have occured the most and during what time of the day, have weapons been used, how the crime count has changed with time, and does it have any correlation with the unemployemnt rate.
  
![image](https://github.com/belaz19/de-project/assets/97640160/408f56eb-3c10-4f20-a512-a16a1dd3aa5b)
  
# Project Architecture  
![DE project flow](https://github.com/belaz19/de-project/assets/97640160/9ade635b-fc24-4ca8-b24a-f85dbd7442a6)
  
# Cloud
The project is developed in the Google Cloud Platform (GCP). The follwong resources are used on GCP: Virtual Machine (VM) with Linux, Buckets in Cloud Storage, datasets in BigQuery Studio.  
Terraform (IaC tool) is used to create (and later destroy) buckets and datasets.

# Data ingestion
Batch orchestration is implemented using MAGE which I run in a docker container. There are three pipelines created, each of them has multiple steps in DAG (data loader, data transformer, data exporter), all steps are orchestrated. The pipelines:
  1. crime_to_gcs. This pipeline loads the Los Angeles crime data (900,000+ records) from open source, define data types for each column, rename headers, and loads everything to the Bucket on Cloud Storage in a parquet file.  
  2. crime_to_bq. This pipeline loads the data from the data lake, does additional data processing such as removing uncomplete rows, normalizing some columns' values, selecting the most relevant column, and uploading this data (600,000+ records) to the defined BigQuery dataset.  
  3. unemp_to_bq. This pipeline loads data about unemployemnt rates in Los Angeles. Then the relevant rows and columns are selected. This becomes a relatively small dataset (up to 100 rows), so I upload it directly to the BigQuery studio.

# Transformations
Transformations are defined in dbt-cloud. There are two models defined in this dbt project: 1) the staging model for staging the raw input datasets (Crime data and Unemployemnt data from my BigQuery) and 2) the core model for joining these two datasets together and getting the data ready for a dashboard. There are also some Macros created for changing values in two column (victim descent and victim sex). After successfull testing of the models, a Production environemnt and a Deployment job has been created in dbt-cloud to trigger & run this workflow whenever needed.

# Data warehouse
BigQuery on Google Cloud Platform is used as a data warehouse (DWH). As described above, the MAGE orchestrated pipelines loads data into DWH, then it is transformed with dbt-cloud, and returned back to BigQuery as the final "production" dataset and table. This final table is partitioned by Date and clustered by Area. This partitioning and clustering is implemented via dbt-cloud as the last step of data transformation there.

# Dashboard
The dashboard is created in Looker Studio. My "production" table in BigQuery is the data source for this dashboard. The dashboard contains several tiles. Some of the showing distribution of categorigal data such as victims' gender, others showing data across a temporal line such as crime count vs. date.

# Reproducibility
It is possible to reproduce this project with your own machine and cloud. All the steps that has been taken for the development of this project are documented in the "what-to-do" folder. The codes used in different data engineering tools (terraform, mage, dbt) are also stored in this Git repository. You can clone this entire repo and then follow the steps described in the "what-to-do" folder.
