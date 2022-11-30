import requests
import json
import os


class UserPersonaGenerator:

    def generate_persona(self, name: str, designation: str, comments: str) -> str:
        url = "https://www.everyprompt.com/api/v0/calls/test-107/user-persona-generator-SAgWWs"
        name_and_designation = name + ", " + designation
        print("name_and_designation: " + name_and_designation)
        payload = json.dumps({
            "variables": {
                "name_and_designation": name_and_designation,
                "special_comments": comments
            },
            "user": "YOUR USER ID"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': os.environ.get('BEARER_TOKEN')
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        response_dict = response.json()
        print(response_dict['choices'][0]['text'])
        return response_dict['choices'][0]['text']
