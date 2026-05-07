"""
Module for emotion recognition from text
"""
import requests
def emotion_detector(text_to_analyze):
    """ Function to analyze text """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    my_obj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=header, json=my_obj, timeout=30)
    return response.text
    