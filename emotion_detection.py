"""
    This is a emotion detection program using IBM watson emotion predition
    algorithm
"""
import json
import requests

def emotion_detector(text_to_analyse):
    """
    This is a emotion detection funtcion using IBM watson emotion predition
    The header and the URL are hard coded but the payload is created on the
    fly using the input text
    """
    url = "https://sn-watson-emotion.labs.skills.network/" + \
            "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    try:
        response = requests.post(url, json = myobj, headers=header,timeout=30)
        formatted_response = json.loads(response.text)
        v = formatted_response['emotionPredictions'][0]['emotion']
        v['dominant_emotion'] = max(v, key=v.get)
        return v
    except requests.exceptions.HTTPError as e:
        if response.status_code == 400:
            print("Caught 400 Bad Request")
        return "Error: " + str(e)
