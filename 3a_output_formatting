import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    try:
        response = requests.post(URL, json = myobj, headers=header)
        formatted_response = json.loads(response.text)
        V = formatted_response['emotionPredictions'][0]['emotion']
        V['dominant_emotion'] = max(V, key=V.get)
        return V
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)