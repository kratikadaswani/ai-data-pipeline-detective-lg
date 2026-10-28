
import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv

# load_dotenv()

# print("DIAL endpoint:", os.getenv("DIAL_BASE_URL"))
# print("DIAL model configured:", bool(os.getenv("DIAL_MODEL")))
# print("DIAL key configured:", bool(os.getenv("DIAL_API_KEY")))
load_dotenv()

api_key = os.getenv("DIAL_API_KEY")
endpoint = os.getenv("DIAL_BASE_URL")
api_version = os.getenv("DIAL_API_VERSION", "2025-04-01-preview")
model_name = os.getenv("DIAL_MODEL", "gpt-6-luna-2026-09-22")

if not api_key:
    raise RuntimeError("DIAL_API_KEY is missing from .env")

llm = AzureChatOpenAI(
    azure_endpoint=endpoint,
    api_version=api_version,
    api_key=api_key,
    azure_deployment=model_name,
    temperature=0,
)

response = llm.invoke(
    "Explain a Spark pipeline failure in two simple sentences."
)

print(response.content)
