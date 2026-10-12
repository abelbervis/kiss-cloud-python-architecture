import google.generativeai as genai
from utils.security import get_secret

def list_available_models(secret_name: str = "GEMINI_API_KEY"):
    """
    Lists all models available for your API key that support generateContent.
    """
    try:
        api_key = get_secret(secret_name)
        if not api_key:
            print("❌ Could not retrieve API key to list models.")
            return []

        genai.configure(api_key=api_key)
        
        print("\n🔍 Checking available models in your Gemini account...")
        models_list = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"  - {m.name}")
                models_list.append(m.name)
        return models_list
    except Exception as e:
        print(f"❌ Error listing models: {e}")
        return []

def get_gemini_model(secret_name: str = "GEMINI_API_KEY", model_name: str = "gemini-2.5-flash"):
    """
    Retrieves the API key from Secret Manager, configures Gemini, and returns the model.
    """
    api_key = get_secret(secret_name)
    
    if not api_key:
        raise ValueError(f"❌ Could not configure Gemini because API key ('{secret_name}') was not found.")

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def safe_generate_content(model, prompt: str, secret_name: str = "GEMINI_API_KEY"):
    """
    Wraps the generateContent call. If a 404 or not found error occurs,
    it automatically prints the list of available models.
    """
    try:
        return model.generate_content(prompt)
    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg or "not found" in error_msg.lower():
            print(f"\n❌ Model not found error (404): {e}")
            print("💡 Here is the list of models that ARE available in your account:")
            list_available_models(secret_name)
        raise e
