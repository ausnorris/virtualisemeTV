def handler(context, inputs):
    mqttQueue = inputs["mqttQueue"]
    mqttServer = inputs["mqttServer"]
    queuePayload = {
        "mqttQueue": mqttQueue,
        "mqttServer": mqttServer,
        "mqttStatus": "ERROR"
    }

    outputs = {}
    outputs['customProperties'] = {}
    outputs['customProperties']["mqtt"] = queuePayload 

    return outputs