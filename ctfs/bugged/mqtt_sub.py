# Python script to attempt to connect to an mqtt service without any username and password, and if connection is succesful , listen on all topics.

import paho.mqtt.client as mqtt
import time
import os

HOST = "10.10.98.11"
PORT = 1883

topic_to_subscribe = input("Please enter topic to subscribe to: ")


def on_connect(client, userdata, flags, reason_code):
    client.subscribe(topic_to_subscribe) # prints ALL user defined 'topics' or devices in this case 
    #client.subscribe('$SYS/#') # prints sysetm information such as bytes sent and recieved etc etc

def on_message(client, userdata, message):
    print('Topic: %s | QOS: %s | Message: %s' % (message.topic, message.qos, message.payload))

def main():


    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message
    
    print("[+] Starting connection\n")

    client.connect(HOST, PORT)
    client.loop_forever()

  
    
main()
