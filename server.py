from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector app")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Extract emotions and dominant emotion
    anger = response.get("anger", 0)
    disgust = response.get("disgust", 0)
    fear = response.get("fear", 0)
    joy = response.get("joy", 0)
    sadness = response.get("sadness", 0)
    dominant_emotion = response.get("dominant_emotion", "unknown")

    # Format the response string
    result_message = (f"For the given statement, the system response is "
                          f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
                          f"'joy': {joy} and 'sadness': {sadness}. "
                          f"The dominant emotion is {dominant_emotion}.")
    return result_message
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)