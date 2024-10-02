# Contextual AI Chatbot

This repository contains the code for a contextual AI chatbot deployed on Hugging Face Spaces using Gradio. The chatbot is designed to engage in dynamic conversations and understand context for more intelligent and adaptive responses. You can try out the live demo [here](https://huggingface.co/spaces/Aakash67/demo_space).

## Features
- Powered by an AI language model.
- Built using **Gradio** to create an intuitive web interface.
- Deployed on **Hugging Face Spaces** for easy access and sharing.

## Deployment Link
Check out the deployed chatbot: [Hugging Face Spaces Demo](https://huggingface.co/spaces/Aakash67/demo_space).

## How to Set Up Locally

If you'd like to clone this repository and run the project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Contextual-AI-Chatbot.git
cd Contextual-AI-Chatbot
```

### 2. Set Up a Virtual Environment (myvenv)

It's a good practice to use a virtual environment to manage dependencies and avoid conflicts. Here's how you can set up a virtual environment called `myvenv`:

#### On Windows:
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

### 3. Install the dependencies

After activating the virtual environment, install the dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Setting Up API Keys

This chatbot uses an external API to provide responses (if needed). To securely store API keys, we use a `.env` file. You will need to create a `.env` file in the root of your project directory and add the required keys.

#### Example `.env` file:
```bash
API_KEY=your-api-key-here
```

Make sure to replace `your-api-key-here` with your actual API key.

### 5. Running the App Locally

After setting up the environment and installing the dependencies, you can run the app locally using the following command:

```bash
python file.py
```

This will start a Gradio interface that you can access in your browser to interact with the chatbot.

## Deployment on Hugging Face Spaces

To deploy this chatbot on Hugging Face Spaces:
1. Install the required libraries using the `requirements.txt` file.
2. Use the following command to deploy the space:

```bash
gradio deploy
```

This command will guide you through the deployment process, and your app will be available on Hugging Face Spaces.
