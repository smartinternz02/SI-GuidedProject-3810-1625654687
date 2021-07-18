import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "00kg5n",
        "typeId": "MYdevice",
        "deviceId":"986788"
    },
    "auth": {
        "token": "789948gfyUUT"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    light_intensity=random.randint(0,500)
    water_level=random.randint(0,100)
    myData={'light_intensity':light_intensity, 'water_level':water_level}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()