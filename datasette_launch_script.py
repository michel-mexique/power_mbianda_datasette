import os
cmd = os.system

print("######   DON'T FORGET TO SET NGROK AUTHTOKEN ENV VARIABLE   ######")
print("######   WITH COMMAND 'export NGROK_AUTHTOKEN=TOKEN'   ######")
# 1) Docker installaton process

cmd('sudo apt-get remove docker docker-engine docker.io containerd runc')
cmd('sudo apt-get update')
cmd("""
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
""")
cmd('sudo mkdir -p /etc/apt/keyrings')
cmd('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg')
cmd("""
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
""")
cmd('sudo apt-get update')
cmd('sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin')
cmd('sudo docker run hello-world')


# 2) NGrok Installation process

cmd('sudo snap install ngrok')
cmd('ngrok config add-authtoken ' + os.environ['NGROK_AUTHTOKEN'])

# 3) Datasette deployement on local domain

cmd("""
docker run -p 8001:8001 -v `pwd`:/mnt \
    datasetteproject/datasette \
    datasette -p 8001 -h 0.0.0.0 mnt/database.db
""")

# 4) Web deployment on ngrok

cmd('ngrok http 8001')