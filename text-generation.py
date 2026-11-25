from transformers import pipeline

generator = pipeline("text-generation")
generated_text = generator("In this course, we will teach you how to")
print(generated_text)