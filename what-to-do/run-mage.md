# Part 3. Run mage
1. Navigate to the mage folder, rename file dev.env into .env  
2. save the previosuly created json-key into that mage folder  
3. Then run `sudo docker compose build` 
4. Then run `sudo docker compose up`  
5. pass port 6789 and navigate to http://localhost:6789  
6. open file io_config.yaml and update # GOOGLE inforation there:  
   `GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/my-creds.json"` choose the name of your copied .json key  
   `GOOGLE_LOCATION: europe-north1` choose your location  
7. Modify pipeline crime_to_gcs, go to DATA EXPORTER and change accroding to your project information
   `bucket_name = 'BUCKET_NAME'`
   `object_key = 'FILE_NAME.parquet'`
8. Modify pipeline crime_to_bq, go to DATA LOADER and set the same bucket and object as in the point above, go to DATA EXPORTER and write the table id
   `table_id = 'TABLE_ID'`
9. Run these 3x pipelines once
