from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_page():
    context = {
        'answer': '', 'arg1': '', 'arg2': '', 'op': '',
        'message': 'Hello World!',
    }
    if all([s in request.values for s in ['arg1', 'op', 'arg2']]):
        context['op'] = request.values['op']
        try:
            context['arg1'] = int(request.values['arg1'])
            context['arg2'] = int(request.values['arg2'])
        except ValueError:
            context['answer'] = "Пишите правильно значения!"
            return render_template('index.html', **context)

        try:
            if request.values['op'] == 'plus':
            # try:
                context['answer'] = context['arg1'] + context['arg2']
            if request.values['op'] == 'minus':
                context['answer'] = context['arg1'] - context['arg2']
            if request.values['op'] == 'multiply':
                context['answer'] = context['arg1'] * context['arg2']
            if request.values['op'] == 'divide':
                context['answer'] = context['arg1'] / context['arg2']
        except ZeroDivisionError:
            context['answer'] = 0

    return render_template('index.html', **context)
