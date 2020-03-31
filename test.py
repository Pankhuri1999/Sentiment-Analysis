# For testing the polarity of individual sentences 
from textblob import TextBlob
a = TextBlob(input("Type your statemnt that you want to analyze: "))
print("Polarity: ",a.sentiment.polarity)
print("Subjectivity: ",a.sentiment.subjectivity)
