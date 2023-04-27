from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Получаем данные из формы
    amount = request.form['amount']
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    # Формируем URL для запроса курсов валют
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

    # Получаем курсы валют
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]

    # Вычисляем конвертированную сумму
    converted_amount = round(float(amount) * rate, 2)

    # Формируем результат и возвращаем его в шаблон
    result = f'{amount} {from_currency} = {converted_amount} {to_currency}'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

