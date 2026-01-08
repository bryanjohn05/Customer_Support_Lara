from openai import AzureOpenAI
from dotenv import load_dotenv
import os
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


def show_menu():
    print("\n=== Customer Support Response Generator ===")
    for key, value in PROMPTS.items():
        print(f"{key}. {value['name']}")


def get_user_inputs():
    return {
        "company_name": input("Enter company name: "),
        "product_name": input("Enter product/service name: "),
        "issue_type": input("Enter issue type: "),
        "tone": "Formal",
        "max_words": 120,
        "customer_query": input("Enter customer query: ")
    }


def main():
    show_menu()
    choice = input("\nChoose a support type (1/2/3): ")

    if choice not in PROMPTS:
        print("Invalid choice.")
        return

    inputs = get_user_inputs()
    prompt = PROMPTS[choice]["template"].format(**inputs)

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,   # ✅ DEPLOYMENT NAME ONLY
        messages=[
            {"role": "system", "content": "You generate enterprise-safe customer support responses."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    print("\n--- Generated Customer Support Response ---\n")
    text = response.choices[0].message.content

    for sentence in text.split(". "):
        print(sentence.strip())


if __name__ == "__main__":
    main()
