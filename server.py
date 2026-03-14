"""Flask server for Emotion Detection API."""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_endpoint():
    """Process a POST request to analyze emotions in the given text.

    Returns:
        str: Formatted string with emotions and dominant emotion.
        or
        str: Error message for invalid input.
    """

    # Get JSON payload
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text_to_analyze = data["text"]

    # Call the emotion_detector function from the package
    result = emotion_detector(text_to_analyze)

    # Check if dominant emotion is None (invalid input)
    dominant_info = result.get("dominant_emotion")
    if not dominant_info or dominant_info.get("emotion") is None:
        return "Invalid text! Please try again!", 400

    # Extract emotions and dominant emotion
    emotions = result.get("emotions", {})
    dominant = result.get("dominant_emotion", {}).get("emotion", "unknown")

    # Build the formatted response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {emotions.get('anger', 0)}, "
        f"'disgust': {emotions.get('disgust', 0)}, "
        f"'fear': {emotions.get('fear', 0)}, "
        f"'joy': {emotions.get('joy', 0)}, "
        f"'sadness': {emotions.get('sadness', 0)}. "
        f"The dominant emotion is {dominant}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    