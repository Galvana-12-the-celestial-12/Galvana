#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')

        # Задание №2.Получаем текст
        selected_text1 = request.form.get('textTop')
        selected_text2 = request.form.get('textBottom')
        # Задание №3. Получаем расположение текста
        selected_text_form1 = request.form.get('textTop_y')
        selected_text_form2 = request.form.get("textBottom_y")
        # Задание №3. Получаем цвет текста
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               
                               selected_image=selected_image, 

                               
                               selected_text1=selected_text1,

                                
                               selected_color=selected_color,
                               
                               #Задание №3. Отоброжаем расположение текста
                               selected_text_form1=selected_text_form1,
                               selected_text_form2=selected_text_form2
                               )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
