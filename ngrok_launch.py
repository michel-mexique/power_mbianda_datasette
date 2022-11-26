import os
cmd = os.system

print("######   DON'T FORGET TO SET NGROK AUTHTOKEN ENV VARIABLE   ######")
print("######   WITH COMMAND 'export NGROK_AUTHTOKEN=TOKEN'   ######")

# 1) Install pip

cmd('sudo apt-get install python3 python3-pip')

# 2) Install NGrok

cmd('sudo snap install ngrok')
cmd('ngrok config add-authtoken 2FfliNbg5A47ClAEFxGnMDGGUJU_4YhpXh1k2X7chMGgofn3F')

# 4) Web deployment on ngrok

cmd('ngrok http 8001')