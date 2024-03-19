from sentiment_analysis_spanish.sentiment_analysis import SentimentAnalysisSpanish


sentiment = SentimentAnalysisSpanish()
x = "Esta muy buena esa película"
y = "Que horrible comida!!!"
z = "Tuve una experiencia natural"


def analyze_sentiment(sentiment: SentimentAnalysisSpanish, text):
    try:
        sentiment.sentiment(text)
    except Exception as e:
        print("Error:", e)


analyze_sentiment(sentiment, x)
analyze_sentiment(sentiment, y)
analyze_sentiment(sentiment, z)
