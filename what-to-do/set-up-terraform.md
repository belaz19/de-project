# Part 2. Set up terraform
1. on GCP create a service account with the following permissions:  
   Viewer, Storage Admin, Storage Object Admin, BigQuery Admin, Compute Admin  
3. For this service account do the following: manage keys -> create new key -> JSON  
4. Save this key to your VM, I saved it into the folder /home/USER/keys/FILENAME.json
5. cd to the terraform direcory, update the variables.tf file with your own information like project-id, zone, etc.
6. Open terminal, cd to the terraform directory, and then run:  
  $ terraform init  
  $ terraform plan  
  $ terraform apply
  This will create a Storage bucket and a BigQuery dataset in your GCP
