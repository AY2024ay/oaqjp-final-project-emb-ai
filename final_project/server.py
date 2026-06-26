from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_api():

    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result is None or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {result.get('anger')}, "
        f"'disgust': {result.get('disgust')}, "
        f"'fear': {result.get('fear')}, "
        f"'joy': {result.get('joy')}, "
        f"'sadness': {result.get('sadness')}. "
        f"The dominant emotion is {result.get('dominant_emotion')}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)    
