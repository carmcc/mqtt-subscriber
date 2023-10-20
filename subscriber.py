import paho.mqtt.client as mqtt_client

broker_addr = 'localhost'
port = 1883
topic = input('Enter a topic: ' + '[default] = test/topic')
username = input('Enter a username: ')
password = input('Enter a password: ')


if not topic:
    topic = 'test/topic'
    print('No topic entered, using default topic: test/topic')


def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print('Connected with return code: %s' % return_code)
        client.subscribe(topic)

    else:
        print('Connection failed with return code: %s\nRetrying' % return_code)


def on_message(client, userdata, msg):
    print('Message received on topic: %s' % msg.topic + '\nMessage: %s' % msg.payload.decode())


client = mqtt_client.Client()

if username and password:
    client.username_pw_set(username, password)
else:
    print('No username or password entered, attempting to connect without credentials')

client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_addr, port)
client.loop_forever()
