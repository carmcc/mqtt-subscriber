# mqtt-subscriber
Basic implementation of a MQTT client subscriber. 
Recommended use for testing purpose only!
## Usage
- Install [mosquitto](https://mosquitto.org/download/) package.
- Run the broker (the default port is 1883).
  
```
mosquitto
```

- Clone the repository and open it.
```
git clone https://github.com/carmcc/mqtt-subscriber
cd mqtt-subscriber
```
- Install the dependencies.
```
pip install -r requirements.txt
```
- Run the client.
```
python3 subscriber.py
```
- Publish some messages. 
```
mosquitto_pub -d -t 'test/topic' -m 'Message'
``` 
