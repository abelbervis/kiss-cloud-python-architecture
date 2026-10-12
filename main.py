import os
from dotenv import load_dotenv

# Load environment variables from the .env file at the start
load_dotenv()

from utils.gemini import get_gemini_model, safe_generate_content

def main():
    print("Starting application...")

    try:
        # 1. Get the configured Gemini model
        model = get_gemini_model(model_name="gemini-2.5-flash")

        # 2. Define the prompt
        prompt = "Write a short Python function that says hello. Reply with code only."
        
        print("Consulting Gemini...")
        
        # 3. Generate content safely with automatic fallback diagnostics
        response = safe_generate_content(model, prompt)
        
        print("\n--- CODE RECEIVED FROM GEMINI ---")
        print(response.text.strip())
        print("---------------------------------")

    except Exception as e:
        print(f"\n❌ Execution stopped due to the error above.")

if __name__ == "__main__":
    main()
