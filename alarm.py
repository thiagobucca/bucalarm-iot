from m5stack import *
from m5ui import *
from uiflow import *
import urequests as requests
import wifiCfg



def buttonA_wasPressed():
  label.setText("DIS")
  res = requests.post(url=baseUrl + 'disarm')
  time.sleep(2)
  pass
btnA.wasPressed(buttonA_wasPressed)


def buttonB_wasPressed():
  label.setText("ARM")
  res = requests.post(url=baseUrl + 'arm')
  time.sleep(2)
  pass
btnB.wasPressed(buttonB_wasPressed)


def fetch_status():
    res = requests.post(url=baseUrl + 'status')
    time.sleep(2)
    if res.text == "0":
      m = "OFF"
    if res.text == "1":
      m = "ON"
    if res.text == "2":
      m = "SOS"
    return m
    
@timerSch.event('timer1')

def ttimer1():
  label.setText(fetch_status())
  pass

setScreenColor(0x000000)
wifiCfg.doConnect('SSID', 'PASSWORD')
baseUrl = 'YOURAPI'
label = M5TextBox(60, 30, "INIT", lcd.FONT_DejaVu56, 0xFFFFFF, rotate=90)
time.sleep(2)
label.setText(fetch_status())
timerSch.run('timer1', 300000, 0x00)