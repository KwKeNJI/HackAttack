from aliyunsdkcore.client import AcsClient
from aliyunsdkalimt.request.v20181012 import TranslateGeneralRequest
import json

# Replace with your actual Access Key ID and Access Key Secret
ACCESS_KEY_ID = 'LTAI5tHM6wJs5fnzohrKYfvY'
ACCESS_KEY_SECRET = 'xqAYxPYKWKyrzSAtU63csN2JGNjrHK'
REGION_ID = 'ap-southeast-1'  # Singapore region

# Initialize the client
client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION_ID)

def translate_text(text, target_language):
    # Language detection is not a direct API feature, we assume source is 'auto'
    request = TranslateGeneralRequest.TranslateGeneralRequest()
    request.set_SourceLanguage("auto")  # Use "auto" to automatically detect the language
    request.set_TargetLanguage(target_language)
    request.set_SourceText(text)
    request.set_FormatType("text")  # Add the FormatType parameter
    response = client.do_action_with_exception(request)
    return json.loads(response)

# Example usage
text_to_translate = "abcd" # get from frontend form
target_language = "en"  # English

# Translate the text
translated_text = translate_text(text_to_translate, target_language)

# Print the full response for debugging
print("Full Response:", translated_text)

# Check if 'Data' key exists in the response
if 'Data' in translated_text:
    print("Translated Text:", translated_text['Data']['Translated'])
else:
    print("Error: 'Data' key not found in the response.")
    if 'Message' in translated_text:
        print("Error Message:", translated_text['Message'])
