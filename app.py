from flask import Flask, render_template, request, redirect, url_for, flash
import openai

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize OpenAI API key
openai.api_key = 'your_openai_api_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        generated_text = response.choices[0].text.strip()
        return render_template('index.html', prompt=prompt, generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
