# Image generation demo

Demo of sending a prompt to image generation using Stablity diffusion Model, store the image in S3 bucket.
Then return a presigned url to the image.
This is python code for a lambda function. The function takes a prompt as an input, connects with Bedrock, and returns a pre signed S3 url in the response.

Put the above code in a lambda, create S3 bucket and update the same in the code. Note the model id when connecting to Bedrock can be taken by googling out or the FM documentation page.

Ensure that IAM role for Lambda function has pre-requisite access to Bedrock and S3.

Increase Lambda timeout to 1 min.

Sample input test prompt for lambda:

```
{
  "prompt": "picture of a scottish dog"
}

```

You may also front the lambda by an api gateway, and invoke the api url using postman.

Architecture:
```
postman (prompt) -> api gw -> Lambda -> Bedrock (Stability Diffusion)
                                |
                                |-> S3                                     
```
