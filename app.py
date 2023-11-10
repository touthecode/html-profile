from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    result = None
    if request.method == 'POST':
        input_integer = request.form.get('inputInteger', '')
        result = 3.14*int(input_integer)**2
    return render_template('areacircle.html', result=result)

@app.route('/areaOftriangle', methods=['GET', 'POST'])
def areaOftriangle():
    result = None
    if request.method == 'POST':
        input_base = request.form.get('inputBase', '')
        input_height = request.form.get('inputHeight', '')
        result = 0.5*int(input_base)*int(input_height)
    return render_template('areatriangle.html', result=result)



@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
