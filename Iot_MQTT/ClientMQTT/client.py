import paho.mqtt.client as mqtt

# Callback when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("Amjaad/#")

# Callback for when a message is received from the server.
def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt-dashboard.com", 1883, 60)
client.loop_forever()
