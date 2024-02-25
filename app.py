from flask import Flask, render_template, request
from openai import OpenAI
import openai

import gemini
import time
import sys

app = Flask(__name__)

def convert(input):
    # Converts unicode to string
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
    
# lient = OpenAI(api_key="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") # setting locally
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loading')
def loading():
    # input_text = request.form.get('inputText')
    # #data = "No data was passed"
    # # urllib2 is used if you have fancy characters in your data like "+"," ", or "="
	# # This is where the loading screen will be.
    # explanation = gemini.explain(input_text)

	# ( You don't have to pass data if you want, but if you do, make sure you have a matching variable in the html i.e {{my_data}} )
    return render_template('loading.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_text = request.form.get('inputText')
    if (input_text != ""):
        explanation = gemini.explain(input_text)
        return f'Explanation: {explanation}'
        #return render_template('success.html', passed_data = explanation)

    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    #         {"role": "user", "content": input_text}
    #     ]
    # )

    # # Extracting the generated text from the API response
    # generated_text = completion.choices[0].message['content']

if __name__ == '__main__':
    app.run(debug=True)