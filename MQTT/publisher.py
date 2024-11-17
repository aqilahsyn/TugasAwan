# Publisher
import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Berhasil terhubung ke broker MQTT")
    else:
        print(f"Gagal terhubung, return code: {rc}")


def on_publish(client, userdata, mid, properties=None):
    print(f"Pesan berhasil dipublish")


publisher = mqtt.Client(client_id="Python_Publisher", protocol=mqtt.MQTTv5)
publisher.on_connect = on_connect
publisher.on_publish = on_publish

# Broker punya public
broker_address = "broker.hivemq.com" 
port = 1883
publisher.connect(broker_address, port)

publisher.loop_start()

topic = "Tugas AWAN"
message = "Tugasnya Alma dan Hasya"

try:
    while True:
        publisher.publish(topic, message)
        time.sleep(5)  #5 biar ngga lama dan ngga cepet
except KeyboardInterrupt:
    print("\nMenghentikan publisher...")
    publisher.loop_stop()
    publisher.disconnect()