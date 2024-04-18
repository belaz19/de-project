1. create a new GCP project. I call it "data-crime-la"  
2. enable "Compute Engine API"  
3. create a new VM. I use the following settings for VM:  
   name: vm-project  
   zone: europe-north1-a  
   machine type: e2-standard-2  
   disk: ubuntu 20.04 LTS, 50 GB  
4. Create an SSH key to be able to connect to VM from your local machine:  
   Create an SSH key by running in terminal: $ ssh-keygen -t rsa -f ~/.ssh/vmp -C belaz -b 2048  
   This creates two files in my .ssh directory. Add the .pub key to the gcp project  
   Open the gcp project, search for ssh keys, and add the ssh key.  
   Test connection to VM by running in terminal (use your username and your VM external IP): $ ssh -i ~/.ssh/vmp belaz@34.88.109.102  
   
5. on you local machine configure access to your vm by running: $ nano .ssh/config  
   And configure ssh accordingly. This is my example:  
   Host vm-project  
    HostName 34.88.109.102  
    User belaz  
    IdentityFile /home/belaz/.ssh/vmp  

6. Install anaconda, docker, docker compose, terraform  
7. Clone this entire Git repository to your VM. Now you are all set to run this data engineering project on your own VM.
