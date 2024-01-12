from flask import current_app
from flask_babel import _
from google.cloud import translate_v2 as translate

try:
    translate_client = translate.Client()
except:
    print('Translation disabled: application_default_credentials.json not found')

#From https://cloud.google.com/translate/docs/basic/translating-text
def translate(text, target):
    if isinstance(text, bytes):
        text = text.decode("utf-8")
    #result = translate_client.translate(text, target_language=target)
    try:
        result = translate_client.translate(text, target_language=target)
    except:
        return 'Translation disabled'

    return result["translatedText"]
