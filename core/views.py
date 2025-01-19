from django.shortcuts import render
from django.http import JsonResponse
import json
import requests

# Add your function definitions here
BASE_API_URL = ""
LANGFLOW_ID = ""
FLOW_ID = ""

def run_flow(message: str, tweaks: dict = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": f"Bearer {APPLICATION_TOKEN}", "Content-Type": "application/json"}
    if tweaks:
        payload["tweaks"] = tweaks

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def run_flow_view(request):
    if request.method == "POST":
        topic_name = request.POST.get("topic_name")
        if not topic_name:
            return render(request, "index.html", {"error": "Topic name is required."})

        try:
            output = run_flow(topic_name)
            # Extract only the text content
            text_content = output["outputs"][0]["outputs"][0]["results"]["text"]["text"]
            # Add extra line break before each ### heading
            formatted_text = text_content.replace("###", "\n###")
            return render(request, "index.html", {"text_content": formatted_text})
        except Exception as e:
            return render(request, "index.html", {"error": str(e)})

    return render(request, "index.html")

