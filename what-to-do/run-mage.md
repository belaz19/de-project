Already done:
I have cloned this repo to my git: https://github.com/mage-ai/compose-quickstart.git  
These files are needed to run Mage in a docker container  

What you need to do:  
1. in termincal navigate to the mage folder, rename file dev.env into .env  
2. save the previosuly created json-key into the folder mage  
3. run $ sudo docker compose build  
4. run $ sudo docker compose up  
5. pass port 6789 and navigate to http://localhost:6789  
6. open file io_config.yaml and update # GOOGLE inforation there:  
   GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/my-creds.json" # choose the name of your copied .json key  
   GOOGLE_LOCATION: europe-north1 # choose your location  
7. Modify pipeline crime_to_gcs, go to DATA EXPORTER and change
   bucket_name = 'BUCKET_NAME'
   object_key = 'FILE_NAME.parquet'
8. Modify pipeline crime_to_bq, go to DATA LOADER and set the same bucket and object as in the point above, go to DATA EXPORTER and change table_id
   table_id = 'TABLE_ID'
