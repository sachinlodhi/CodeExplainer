import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

genai.configure(api_key="AIzaSyCT-vX_Beof6USjD07vScvxk47DM1FaZQw")

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

'''
models/gemini-1.0-pro
models/gemini-1.0-pro-001
models/gemini-1.0-pro-latest
models/gemini-1.0-pro-vision-latest
models/gemini-pro
models/gemini-pro-vision'''

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def explain(query):
    formatted_q = 'I would like you to format this output in pure html assuning it will be pasted into html with linebreaks indicated by <br>: put the comments for the lines in a manner that this \
    code is understandable to all people and then in the end put a docstring to tell what does this code do in its entirety. \
    Also reformat the code to make it prettify.' +  query

    response = chat.send_message(formatted_q)

    script = chat.send_message("Give me overall explanation. Do not use the special character from the code. Make it sound natural. keep it concise.")
    print(response.text)
    print(script.text)
    # calling the text2speech
    # text2speech.generate_speech(script=script.text)



    # print(chat.history)
    return response.text