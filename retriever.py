import os
from dotenv import load_dotenv
from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

def query_discovery(question):
    api_key = os.getenv("IBM_API_KEY")
    url = os.getenv("DISCOVERY_URL")
    project_id = os.getenv("DISCOVERY_PROJECT_ID")

    authenticator = IAMAuthenticator(api_key)
    discovery = DiscoveryV2(
        version="2023-11-01",
        authenticator=authenticator
    )
    discovery.set_service_url(url)

    response = discovery.query(
        project_id=project_id,
        natural_language_query=question,
        count=3
    ).get_result()

    # Extract relevant context passages
    context = ""
    for result in response["results"]:
        context += result.get("document_passages", [{}])[0].get("passage_text", "") + "\n"

    return context.strip()
