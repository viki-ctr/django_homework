from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def contacts():
    # Читаем содержимое HTML-файла
    with open('contacts.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    # Возвращаем HTML с правильным заголовком
    return html_content, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app.run(debug=True)
