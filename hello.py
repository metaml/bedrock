using System;
using System.Collections.Generic;
using Amazon;
using Amazon.BedrockRuntime;
using Amazon.BedrockRuntime.Model;

// Create a Bedrock Runtime client in the AWS Region you want to use.
var client = new AmazonBedrockRuntimeClient(RegionEndpoint.USEast1);

// Set the model ID, e.g., Llama 3 8b Instruct.
var modelId = "us.meta.llama3-2-1b-instruct-v1:0";

// Define the user message.
var userMessage = "Describe the purpose of a 'hello world' program in one line.";

// Create a request with the model ID, the user message, and an inference configuration.
var request = new ConverseRequest {
  ModelId = modelId,
  Messages = new List<Message>
  {
    new Message
    {
      Role = ConversationRole.User,
      Content = new List<ContentBlock> { new ContentBlock { Text = userMessage } }
    }
  },
  InferenceConfig = new InferenceConfiguration()
  {
    MaxTokens = 512,
    Temperature = 0.5F,
    TopP = 0.9F
  }
};

try {
  // Send the request to the Bedrock Runtime and wait for the result.
  var response = await client.ConverseAsync(request);

  // Extract and print the response text.
  string responseText = response?.Output?.Message?.Content?[0]?.Text ?? "";
  Console.WriteLine(responseText);
} catch (AmazonBedrockRuntimeException e) {
  Console.WriteLine($"ERROR: Can't invoke '{modelId}'. Reason: {e.Message}");
  throw;
}
