from transformers import pipeline

unmasker = pipeline('fill-mask', top_k=2)
result = unmasker("This course will teach you all about <mask> models.")
print(result)