# Subscriber
import paho.mqtt.client as mqtt

subscriber = mqtt.Client(client_id="Python_Subscriber", 
                        protocol=mqtt.MQTTv5,
                        callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

@subscriber.connect_callback()
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Berhasil terhubung ke broker MQTT")
        client.subscribe("Tugas AWAN")
    else:
        print(f"Gagal terhubung, reason code: {reason_code}")

@subscriber.message_callback()
def on_message(client, userdata, message):
    print(f"Pesan diterima: {message.topic}")
    print(f"Pesan: {message.payload.decode()}")

broker_address = "broker.hivemq.com"
port = 1883
subscriber.connect(broker_address, port)

# Mulai loop untuk menerima pesan
try:
    subscriber.loop_forever()
except KeyboardInterrupt:
    print("\nMenghentikan subscriber...")
    subscriber.disconnect()