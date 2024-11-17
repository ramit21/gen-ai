# Text summarisation using Cohere

Similar setup as example 1 of image generation.

When calling a model like Cohere, parameters can be taken from AWS documentation:

eg. https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-cohere-command.html

Sample input test prompt for lambda:

```
{
  "prompt": "Summarise this text: A turbine works by converting wind or gas into electricity: \nWind turbines\nThe wind turns the blades of a turbine, which creates kinetic energy. The blades spin the shaft in the nacelle, which connects to a generator in the nacelle. The generator converts the kinetic energy into electricity. \nGas turbines\nAir is drawn in, compressed, and heated. The hot air is then fed into a combustion zone, where fuel is ignited to heat the air even more. The hot gas is then discharged across a turbine, which causes the turbine blades to move. The movement of the blades rotates the central shaft, which is connected to the compressor. "
}

```
