exports.handler = function handler(context, inputs) {

  let outputs = {
    "wavefront": {
            "app": "vra.app." +inputs.customProperties.app,
            "service": "vra.service." + inputs.customProperties.serviceName,
            "deploymentid": "vra.deployment." + inputs.deploymentId
        }
  };

  return outputs;
};