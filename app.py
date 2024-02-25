from flask import Flask, render_template, request
from openai import OpenAI
import openai

app = Flask(__name__)
lient = OpenAI(api_key="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") # setting locally
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():


    input_text = request.form.get('inputText')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": input_text}
        ]
    )

    # Extracting the generated text from the API response
    generated_text = completion.choices[0].message['content']



    return f'The text you entered is: {input_text}'

if __name__ == '__main__':
    app.run(debug=True)
