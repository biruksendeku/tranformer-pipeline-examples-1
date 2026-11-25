from transformers import pipeline

generator = pipeline("text-generation")
generated_text = generator("In this course, we will teach you how to")
print(generated_text)
# Example output:
# [{'generated_text': 'In this course, we will teach you how to build and train transformer models.'}]