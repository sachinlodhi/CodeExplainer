import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import text2speech

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
    formatted_q = 'Generate commented code with short explanations for each section or line of code based on the provided code snippet. Also reformat the code to make it pretty. The programming language is not specified, and the model should determine it automatically\n Code Snippet:\n' + query



    response = chat.send_message(formatted_q)

    script = chat.send_message("Give me overall explanation. Do not use the special character from the code. Make it sound natural. keep it concise. single paragraph like 5 to 8 lines.")
    print(response.text)
    print(script.text)
    # calling the text2speech
    text2speech.generate_speech(script=script.text)


    clean_resp = response.text.replace("`","")
    # print(chat.history)
    return clean_resp
