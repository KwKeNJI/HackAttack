# Cultural Immersion Personalised Tourism Algorithm

import os
import pandas as pd
import dashscope
from dashscope import Generation
from http import HTTPStatus

# Get API
dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'
dashscope.api_key = os.getenv('CIPTA_API_KEY')

# Implement database here
file_path = 'events.csv'
events_df = pd.read_csv(file_path)
events_str = events_df.to_csv(index=False)

# Model to call Qwen
def call_qwen(model, messages):
    response = Generation.call(
        model=model,
        messages=messages
    )
    # print("Raw Response from Qwen API:", response)  # Debug purpose
    if 'output' in response and 'text' in response['output']:
        return response['output']['text']
    else:
        return "An error occurred while retrieving events. Please try again."

def get_qwen_response(preferences):
    # Create a message for Qwen to read the CSV and provide suitable events
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': f'Here is a list of events:\n{events_str}\nUser preferences are: {preferences}. Based on these preferences, which events are most suitable? If no exact match is found, provide the closest match.'}
    ]
    return call_qwen('qwen-turbo', messages)

def main():
    # Ask the user for their preferences three times
    preferences = []
    for i in range(3):
        preference = input(f"Preference {i+1:}: ")
        preferences.append(preference)

    # Get the response from Qwen
    qwen_response = get_qwen_response(preferences)
    print("\n\nSuitable events based on your preferences:")
    print(qwen_response)

if __name__ == '__main__':
    main()
