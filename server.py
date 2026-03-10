''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
import EmotionDetection as ed

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if len(text_to_analyze) == 0 :
        return "Invalid input! Try again"
    sentiment = ed.emotion_detector(text_to_analyze)
    return " For the given statement, the system response is " \
        + " , ".join([f"'{s}': {sentiment[s]}" \
                for s in sentiment.keys() if 'dominant' not in s]) \
        + f". The dominant emotion is {sentiment['dominant_emotion']}!"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
