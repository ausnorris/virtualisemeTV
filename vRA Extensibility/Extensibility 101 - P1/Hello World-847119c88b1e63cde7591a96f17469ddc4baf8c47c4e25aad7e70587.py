def handler(context, inputs):
    greeting = "Hello " + inputs["__metadata"]["userName"]
    print(greeting)
    
    outputs = {}
    outputs['customProperties'] = inputs['customProperties']
    outputs['customProperties']['greeting'] = greeting
    
    return outputs


