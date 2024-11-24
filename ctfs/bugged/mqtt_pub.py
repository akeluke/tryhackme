# Python script to attempt to connect to an mqtt service without any username and password, and if connection is succesful , listen on all topics.

import paho.mqtt.client as mqtt
import time
import os

HOST = "10.10.98.11"
PORT = 1883


def on_connect(client, userdata, flags, reason_code):
    client.subscribe('#', qos=1) # prints ALL user defined 'topics' or devices in this case 
    #client.subscribe('$SYS/#') # prints sysetm information such as bytes sent and recieved etc etc

def on_message(client, userdata, message):
    print('Topic: %s | QOS: %s | Message: %s' % (message.topic, message.qos, message.payload))

def on_publish(client, userdata, mid):
    try:
        userdata.remove(mid)
        # why we do this explained here:
        # https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html
    except KeyError:
        print("[!] on_publish error")

def main():

    unacked_publish = set()
    client = mqtt.Client()

    client.on_publish = on_publish

    client.user_data_set(unacked_publish)


    #client.on_connect = on_connect
    #client.on_message = on_message
    
    print("[+] Starting connection\n")

    client.connect(HOST, PORT)
    client.loop_start()

    msg_info = client.publish("TEST", "CMD", qos=1)
    unacked_publish.add(msg_info.mid)

    while len(unacked_publish):
        time.sleep(0.1)

    msg_info.wait_for_publish()

    client.disconnect()
    client.loop_stop()
    
main()
