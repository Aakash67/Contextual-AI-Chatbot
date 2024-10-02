from dotenv import load_dotenv
import os
import gradio as gr
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.messages.concrete.SystemMessage import SystemMessage
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment
API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the GroqModel with the API key to access allowed models
llm = GroqModel(api_key="API_KEY")

# Get the available models from the llm instance
allowed_models = llm.allowed_models

# Initialize a MaxSystemContextConversation instance
conversation = MaxSystemContextConversation()

# Define a function to dynamically change the model based on dropdown input
def load_model(selected_model):
    return GroqModel(api_key=API_KEY, name=selected_model)

# Define the function to interact with the agent
def converse(input_text, history, system_context, model_name):
    print(f"System Context: {system_context}")
    print(f"Selected Model: {model_name}")

    # Initialize the model dynamically based on user selection
    llm = load_model(model_name)

    # Initialize the agent with the new model
    agent = SimpleConversationAgent(llm=llm, conversation=conversation)

    # Set the system context
    agent.conversation.system_context = SystemMessage(content=system_context)

    # Ensure input_text is a string
    input_text = str(input_text)

    # Execute the input command with the agent
    result = agent.exec(input_text)

    # Return the result as a string
    return str(result)

# Set up the Gradio ChatInterface with a dropdown for model selection
demo = gr.ChatInterface(
    fn=converse,
    additional_inputs=[
        gr.Textbox(label="System Context"),
        gr.Dropdown(label="Model Name", choices=allowed_models, value=allowed_models[0])  # Dropdown for model selection
    ],
    title="A system context conversation",
    description="Interact with the agent using a selected model and system context."
)

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch(share=True, debug=True)  # Set share=True to enable public sharing