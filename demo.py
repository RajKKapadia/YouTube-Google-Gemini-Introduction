import os

import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

# model = genai.GenerativeModel('gemini-pro-vision')

# response = model.generate_content("hi")

# print(response.text)

# print(response.prompt_feedback)

# print(response.candidates)

# response = model.generate_content("What is the meaning of life?", stream=True)

# for chunk in response:
#     print(chunk.text)

# import PIL.Image

# img = PIL.Image.open('licensed-image.jpeg')

# response = model.generate_content(img)

# print(response.text)

# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])

# print(chat)

# response = chat.send_message("Hi")
# print(response.text)

# print(chat.history)

# response = chat.send_message("Can you write a python function to print only prime numbers?")
# print(response.text)

result = genai.embed_content(
    model="models/embedding-001",
    content="What is the meaning of life?",
    task_type="retrieval_document",
    title="Embedding of single string")


print(str(result['embedding'])[:50], '... TRIMMED]')
