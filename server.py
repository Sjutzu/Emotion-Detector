"""
Module that hosts the server
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def text_analyzer():
    """ Analyzing text given at the website """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    return (
        f"For the given statement, the system response is 'anger': {result['anger']},\n"
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and\n"
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """ Rendering home page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
