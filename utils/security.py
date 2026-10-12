from google.cloud import secretmanager
import os

def get_secret(secret_id: str, project_id: str = None) -> str:
    """
    Safely retrieves a secret from Google Cloud Secret Manager.
    Reads the Project ID from environment variables if not passed as an argument.
    """
    project_id = project_id or os.getenv("GCP_PROJECT_ID")
    
    if not project_id:
        print("❌ Error: GCP_PROJECT_ID was not specified in the environment variables.")
        return None

    try:
        client = secretmanager.SecretManagerServiceClient()
        resource_name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
        
        response = client.access_secret_version(request={"name": resource_name})
        payload = response.payload.data.decode("UTF-8")
        
        print(f"✅ SUCCESS: Secret '{secret_id}' retrieved successfully.")
        return payload
        
    except Exception as e:
        print(f"❌ FAILED to retrieve secret '{secret_id}': {e}")
        return None
