from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")
generated_text = generator("In this course, we will teach you how to", max_length=30, num_return_sequences=2)
print(generated_text)
# Example output:
# [{'generated_text': 'In this course, we will teach you how to build a successful AI project.'},
#  {'generated_text': 'In this course, we will teach you how to use machine learning in practice.'}]