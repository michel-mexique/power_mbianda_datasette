import os
cmd = os.system

"""
Docker installaton process
"""

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