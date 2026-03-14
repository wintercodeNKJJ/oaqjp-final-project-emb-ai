import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyze text and return emotions with scores and dominant emotion.
    """
        # Handle blank or None input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {"text": text_to_analyze}
    }

    response = requests.post(url, headers=headers, json=payload)

    # Convert response to dictionary
    data = json.loads(response.text)

    try:
        emotion_scores = data["emotionPredictions"][0]["emotion"]
    except (KeyError, IndexError):
        return {"error": "Unable to extract emotions from API response"}

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    dominant_score = emotion_scores[dominant_emotion]

    return {
        "text": text_to_analyze,
        "emotions": emotion_scores,
        "dominant_emotion": {
            "emotion": dominant_emotion,
            "score": dominant_score
        }
    }