from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classification = classifier("I love using transformers for natural language processing tasks!")
print(classification)