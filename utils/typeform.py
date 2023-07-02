import requests
import json
import pandas as pd
from resources.configs import TYPEFORM_API_KEY

import warnings
warnings.filterwarnings("ignore")

def typeform_responses():

    url = "https://api.typeform.com/forms/DjIIB0vP/responses"

    payload = {}
    headers = {
    'Authorization': f'Bearer {TYPEFORM_API_KEY}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.content)

    answers_data = []
    for item in data['items']:
        answers = item['answers']
        email = item['answers'][0]['text']

        for answer in answers:
            field_id = answer['field']['id']
            field_type = answer['field']['type']
            field_ref = answer['field']['ref']
            field_text = answer['text']
            answers_data.append({
                'email': email,
                'field_id': field_id, 
                'field_type': field_type, 
                'ref': field_ref, 
                'field_text': field_text
            })

    df = pd.DataFrame(answers_data)

    return df

def typeform_fields():

    url = "https://api.typeform.com/forms/DjIIB0vP"

    payload = {}
    headers = {
    'Authorization': f'Bearer {TYPEFORM_API_KEY}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.content)

    fields_list = []
    fields = data['fields']
    for field in fields:
        field_title = field['title']
        field_ref = field['ref']
        field_description = field['properties'].get('description', None)

        field_data = {
            'title': field_title,
            'ref': field_ref,
            'description': field_description
        }
        
        fields_list.append(field_data)

    df = pd.DataFrame(fields_list)

    return df