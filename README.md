# Customer Support Response Generator

A Python-based command-line application that uses **Azure OpenAI** to generate professional, enterprise-safe customer support responses using predefined prompt templates.

## Features

- Interactive CLI menu for selecting support response types  
- Uses Azure OpenAI Chat Completions API  
- Centralized prompt management via `prompts.py`  
- Generates concise, formal customer support replies  

## Requirements

- Python 3.9 or higher  
- An active Azure OpenAI resource with a deployed model  

## Installation

Install the required Python packages:

`pip install openai python-dotenv`

## Project Structure
.
├── main.py
├── prompts.py
├── .env
└── README.md

## Usage

Run the application from the project root:

`python main.py`


## Customizing Prompts

Prompt templates are stored in `prompts.py` inside the PROMPTS dictionary.
You can add, edit, or remove templates to fit different support scenarios.

## Environment Variables

Create a .env file in the project root directory and add the following:

```bash
 AZURE_OPENAI_API_KEY=your_api_key_here
 AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
 AZURE_MODEL=your_deployment_name`