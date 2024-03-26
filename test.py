import os
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
    
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("what is the meaning of life?")

for candidate in response.candidates:
    print ([part.text for part in candidate.content.parts])
# print(to_markdown(response.text))