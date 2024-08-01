from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def home():
    """Show form to input words for Madlibs story."""
    return render_template('form.html', prompts=story.prompts)

@app.route('/story')
def show_story():
    """Show resulting story from the filled form."""
    answers = request.args
    generated_story = story.generate(answers)
    return render_template('story.html', story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)
