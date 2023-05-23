from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from flask import Flask, request, jsonify

app = Flask(__name__)

authenticator = IAMAuthenticator('Mz2537RTtqOWaQPTzs5OiRjpaZMdMVtCzOsBFSpluxpP')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c21cfa78-652b-4ed7-b6ff-0b3315ac7310')

@app.route('/translate/english-to-french', methods=['POST'])
def translate_english_to_french():
    text = request.json['text']
    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    translated_text = translation['translations'][0]['translation']
    return jsonify({'translated_text': translated_text})

@app.route('/translate/french-to-english', methods=['POST'])
def translate_french_to_english():
    text = request.json['text']
    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    translated_text = translation['translations'][0]['translation']
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run()
