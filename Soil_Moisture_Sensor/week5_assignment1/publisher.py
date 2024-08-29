import paho.mqtt.publish as publish
publish.single("ifn649", "LED_ON", hostname="54.253.242.136")
print("Done")