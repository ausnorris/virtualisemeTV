def handler(context, inputs):
    platform = inputs["tags"]["platform"]
    mqttQueue = inputs["mqttQueue"]
    mqttServer = inputs["mqttServer"]
    print(platform + " " + mqttServer + " " + mqttQueue)
    queuePayload = {
        "mqttQueue": mqttQueue,
        "mqttServer": mqttServer,
        "mqttStatus": platform.upper()
    }

    outputs = {}
    outputs['customProperties'] = inputs['customProperties']
    outputs['customProperties']["mqtt"] = queuePayload 

    return outputs
