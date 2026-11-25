from transformers import pipeline

question_answerer = pipeline("question-answering")
result = question_answerer(question='Where do I work?', context='My name is Sylvian and I work at Hugging Face in Brooklyn.')
print(result)
# Example output:
# {'score': 0.99, 'start': 33, 'end': 45, 'answer': 'Hugging Face'}