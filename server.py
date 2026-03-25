"""
This module uses flask web application for emotion detection.
It uses external API for fetching the emotion score for given text
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def sent_emotion_detector():
    """
    Analyses the text input from the user and returns a emotion score
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )
    return output


@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
