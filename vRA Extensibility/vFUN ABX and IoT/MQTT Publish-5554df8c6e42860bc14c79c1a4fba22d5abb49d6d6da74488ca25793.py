def handler(context, inputs):
    import paho.mqtt.client as paho
    payload = inputs['customProperties']["mqtt"]
    broker = payload["mqttServer"]
    port=1883
    def on_publish(client,userdata,result):             #create function for callback
        print("data published \n")
        pass
    client1 = paho.Client("ABX")                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)                                 #establish connection
    ret = client1.publish(payload["mqttQueue"], payload["mqttStatus"])                   #publish
