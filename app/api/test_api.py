"""
TEST FASTAPI
"""

from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)

response = client.post(

    "/predict",

    json={

        "text": "Program makan bergizi gratis sangat membantu masyarakat."

    }

)

print("=" * 60)

print("STATUS")

print(response.status_code)

print()

print("JSON")

print(response.json())

print("=" * 60)