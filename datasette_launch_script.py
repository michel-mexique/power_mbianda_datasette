import os
cmd = os.system

print("######   DON'T FORGET TO SET NGROK AUTHTOKEN ENV VARIABLE   ######")
print("######   WITH COMMAND 'export NGROK_AUTHTOKEN=TOKEN'   ######")

# 1) Install pip

cmd('sudo apt-get install python3 python3-pip')

# 2) Install datasette

cmd('sudo pip3 install datasette')


# 2) Install NGrok

cmd('sudo snap install ngrok')
cmd('ngrok config add-authtoken ' + os.environ['NGROK_AUTHTOKEN'])

# 3) Move Datasette config file to systemd destination

cmd('sudo mv datasette.service /etc/systemd/system/')

# 3) Start datasette

cmd('sudo systemctl daemon-reload')
cmd('sudo systemctl start datasette.service')

# 4) Web deployment on ngrok

cmd('ngrok http 8001')