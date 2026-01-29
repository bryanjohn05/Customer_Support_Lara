"""
Customer Support Response Generator.

This script collects user input and generates enterprise-safe
customer support responses using Azure OpenAI.
"""
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from prompts import PROMPTS

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

DEPLOYMENT_NAME = os.getenv("AZURE_MODEL")
# print("Endpoint:", os.getenv("AZURE_OPENAI_ENDPOINT"))
# print("Deployment:", DEPLOYMENT_NAME)
# print("Key Loaded:", bool(os.getenv("AZURE_OPENAI_API_KEY")))



def get_user_inputs():
    """
       Collects required user inputs for the selected prompt template.

       Returns:
           dict: User-provided values mapped to template variables.
       """
    return {
        "company_name": input("Enter company name: "),
        "product_name": input("Enter product/service name: "),
        "issue_type": input("Enter issue type: "),
        "tone": "Formal",
        "max_words": 120,
        "customer_query": input("Enter customer query: ")
    }


def main():
    """
       Main application entry point.

       Prompts the user for a template choice, gathers inputs,
       sends the request to Azure OpenAI, and prints the response.
       """
    print("\n=== Customer Support Response Generator ===")
    print("1. General Customer Support ")
    print("2. Billing Support")
    print("3. Technical Support")

    choice = input("\nChoose a support type (1/2/3): ")

    if choice not in PROMPTS:
        print("Invalid choice.")
        return

    inputs = get_user_inputs()
    prompt = PROMPTS[choice]["template"].format(**inputs)

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "Generate enterprise-safe customer-support-responses"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    print("\n--- Generated Customer Support Response ---\n")
    text = response.choices[0].message.content

    for sentence in text.split(". "):
        print(sentence.strip())


if __name__ == "__main__":
    main()
