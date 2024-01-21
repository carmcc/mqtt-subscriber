import paho.mqtt.client as mqtt_client

DEFAULT_PORT = 1883
DEFAULT_BROKER_ADDR = 'localhost'
DEFAULT_TOPIC = 'test/topic'


def get_valid_port():
    while True:
        port = input(f'Enter a port: [default = {DEFAULT_PORT}]: ')
        if not port:
            return DEFAULT_PORT
        elif port.isdigit() and 0 <= int(port) <= 65535:
            return int(port)
        else:
            print('Invalid port entered, please try again')


def get_valid_topic():
    while True:
        topic = input(f'Enter a topic: [default = {DEFAULT_TOPIC}]: ')
        if not topic:
            return DEFAULT_TOPIC
        elif '#' in topic or '+' in topic:
            print('Invalid topic entered. Topics should not contain wildcards like # or +')
        else:
            return topic


port = get_valid_port()
topic = get_valid_topic()
broker_addr = input(f'Enter a broker address: [default = {DEFAULT_BROKER_ADDR}]: ')
username = input('Enter a username: ')
password = input('Enter a password: ')

if not broker_addr:
    broker_addr = 'localhost'
    print('No broker address entered, using default address: %s' % broker_addr)


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
