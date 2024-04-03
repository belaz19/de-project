1. on GCP create a service account with the following permissions:
  Viewer, Storage Admin, Storage Object Admin, BigQuery Admin, Compute Admin
2. For this service account do the following: manage keys -> create new key -> JSON
3. Save this key to your VM, I saved it into the folder /home/USER/keys/FILENAME.json
4. Open terraform direcory, update the variables.tf file with your own information like project-id, zone, etc.
5. Open terminal, cd to the terraform directory, then run:  
  $ terraform init  
  $ terraform plan  
  $ terraform apply
