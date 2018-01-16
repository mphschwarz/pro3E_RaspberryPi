#!/binsh

sudo apt install xvfb

sudo wget https://raw.githubusercontent.com/mphschwarz/pro3E_RaspberryPi/master/scripts/offswitch.sh -O /home/pi/offswitch.sh
sudo chmod +x /home/pi/offswitch.sh

sudo wget https://raw.githubusercontent.com/mphschwarz/pro3E_RaspberryPi/master/scripts/startup -O /etc/init.d/startup
sudo chmod +x /etc/init.d/startup
sudo update-rc.d /etc/init.d/startup defaults 100

sudo pip3 install -U https://github.com/mphschwarz/pro3E_RaspberryPi/raw/master/dist/piapp-0.0.0-py2.py3-none-any.whl