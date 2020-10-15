def handler(context, inputs):
    mqttQueue = inputs["mqttQueue"]
    mqttServer = inputs["mqttServer"]
    queuePayload = {
        "mqttQueue": mqttQueue,
        "mqttServer": mqttServer,
        "mqttStatus": inputs["status"]
    }

    outputs = {}
    outputs['customProperties'] = inputs['customProperties']
    outputs['customProperties']["mqtt"] = queuePayload 

    return outputs
