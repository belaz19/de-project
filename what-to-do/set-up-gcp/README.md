1. create a new GCP project. I call it "data-crime-la"
2. enable "Compute Engine API"
3. create a VM. I use the following settings:
   name: vm-project
   zone: europe-north1-a
   machine type: e2-standard-2
   disk: ubuntu 20.04 LTS, 50 GB
4. I need to create an SSH key to be able to control my VM on GCP:
   My local machine runs on Ubuntu. I create an SSH key by running in terminal: ssh-keygen -t rsa -f ~/.ssh/vmp -C belaz -b 2048
   This creates two files in my .ssh directory: I need to add the .pub key to my gcp project
   Open the gcp project, search for ssh keys, add ssh key
   test connection to your vm by running in terminal (use your username and your VM external IP): ssh -i ~/.ssh/vmp belaz@34.88.109.102
