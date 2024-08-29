import paho.mqtt.client as mqtt
import serial
def on_connect(client, userdata, flags, rc)
    print(Connected to MQTT)
    print(Connection returned result  + str(rc) )
    client.subscribe(ifn649)
def on_message(client, userdata, msg)
    print(msg.topic+ +str(msg.payload))
    ser = serial.Serial(devrfcomm0, 9600)
    ser.write(msg.payload) # instead of “Startrn”, send the actual message.



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(54.253.242.136, 1883, 60)
client.loop_forever()

