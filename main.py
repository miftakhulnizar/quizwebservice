from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/api/v1/bmi', methods=['POST'])
def bmi():
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    BMI = weight / (height/100)**2
    msg = "BMI kamu adalah " + str(BMI)
    if BMI <= 18.4:
        keterangan = "kamu Kurus"
    elif BMI <= 25:
        keterangan = "kamu Normal"
    elif BMI <= 40:
        keterangan = "kamu Berlebih"
    else:
        keterangan = "kamu bahaya"
    data = {'result': 'true', 'msg': msg, 'keterangan': keterangan}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=False, port=5000)