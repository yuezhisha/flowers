import paho.mqtt.client as mqtt
mqtt_client = mqtt.Client()
mqtt_broker = "mqtt"
mqtt_port = 1883
mqtt_client.connect(mqtt_broker, mqtt_port, 60)