from m5stack import *
from m5ui import *
from uiflow import *
import urequests as requests
import wifiCfg

setScreenColor(0x111111)

wifiCfg.doConnect('yourSSID', 'yourPassword')
label = M5TextBox(60, 30, "INIT", lcd.FONT_DejaVu56, 0xFFFFFF, rotate=90)

baseUrl = 'yourServerIp/'

res = requests.post(url=baseUrl + 'status')
time.sleep(2)
if res.text == "0":
  m = "OFF"
if res.text == "1":
  m = "ON"
if res.text == "2":
  m = "SOS"
label.setText(str(m))    

while True:
  if btnA.isPressed():
    m = "ON"
    res = requests.post(url=baseUrl + 'arm')
    time.sleep(2)
    label.setText(str(m))
  if btnB.isPressed():
    m = "OFF"
    res = requests.post(url=baseUrl + 'disarm')
    time.sleep(2)
    label.setText(str(m))
  wait_ms(2)
