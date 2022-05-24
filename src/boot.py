# This file is executed on every boot (including wake-boot from deepsleep)
from BME280 import BME280
from machine import I2C, Pin
import network
import time
import socket
import gc
import esp
esp.osdebug(None)

gc.collect()


ssid = "greatfamily@unifi"
pwd = "Ehtan@3573"

def setup_connect(ssid, pwd):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.active(True)
        wlan.connect(ssid,pwd)
        while not wlan.isconnected():
            pass
    print("Netork configuration:\n", wlan.ifconfig())

setup_connect(ssid, pwd)

