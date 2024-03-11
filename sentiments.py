from sentiment_analysis_spanish.sentiment_analysis import SentimentAnalysisSpanish


sentiment = SentimentAnalysisSpanish()


x = "Esta muy buena esa película"
y = "Que horrible comida!!!"
z = "Tuve una experiencia natural"


def new_func(sentiment: SentimentAnalysisSpanish, x):
    try:
        sentiment.sentiment("x: " + x)
    except Exception as e:
        print("Error:", e)


new_func(sentiment, x)


def submit_sentiment(sentiment: SentimentAnalysisSpanish, y):
    try:
        sentiment.sentiment("y: " + y)
    except Exception as e:
        print("Error:", e)


submit_sentiment(sentiment, y)


def analyze_sentiment(sentiment: SentimentAnalysisSpanish, text):
    try:
        sentiment.sentiment(text)
    except Exception as e:
        print("Error:", e)


analyze_sentiment(sentiment, z)
