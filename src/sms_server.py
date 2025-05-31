import requests
import json


API_KEY = "aZHAhXmt8wfo2wx27QH7pvBZfHyryIj3aWig90W1FXqXNTGy"
SMS_API_URL = "https://api.sms.ir/v1/send/bulk"
LINE_NUMBER = "30002108001007"
RECEIVER_NUMBER = ["+989351935907", "+989142438996"]


def send_sms(message):
    """Send sms by sms.ir api"""

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY
    }

    payload = {
        "lineNumber": LINE_NUMBER,
        "messageText": message,
        "mobiles": RECEIVER_NUMBER
    }

    try:
        response = requests.post(SMS_API_URL, json=payload, headers=headers)
        print("Full server response:", response.json())

        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("status") == 1:
                print("SMS sent successfully!")
                print("Message IDs:", response_data.get("data", []))
            else:
                print(f"Error sending SMS: {response_data.get('message')}")

        elif response.status_code == 400:
            print("Logical error in the request (HTTP 400)")
            print("Full server response:", response.text)

        elif response.status_code == 401:
            print("Authentication error (HTTP 401)")

        elif response.status_code == 429:
            print("Too many requests (Rate limited) (HTTP 429)")

        elif response.status_code == 500:
            print("Unexpected server error (HTTP 500)")

        else:
            print(f"Other error: {response.status_code}")

    except Exception as e:
        print(f"General error: {e}")
