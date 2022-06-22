from flask import Flask,request,render_template,jsonify
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
  logging.info('Calling index')
  return render_template('index.html')

@app.route('/process',methods= ['POST'])
def process():
  logging.info('Processing...')
  weight_in_kg  = float(request.form['weight_in_kg'])
  height_in_foot_and_inches = float(request.form['height_in_foot_and_inches'])
  height_in_meters=0.304* float(height_in_foot_and_inches)
  output = str(weight_in_kg / (height_in_meters*height_in_meters))
  bmi =float(output)
  if bmi <=18.5:
    logging.info('thin')
    return jsonify({'output':'You are Under weight as your bmi is: ' + output})
  elif (bmi >=18.5) and (bmi <=24.9):
    logging.info('OK')
    return jsonify({'output':'Perfect!You have normal weight and your bmi is : '+ output})
  elif bmi >=25 and bmi <=29.9:
   logging.warning('thick')
   return jsonify({'output':'You are Overweight as your bmi is: ' + output})
  elif bmi>=30:
   logging.critical('really thick')
   return jsonify({'output':'You are highly obese as your bmi is: ' + output})
  else :
   logging.warning('only calculated')
   return jsonify({'output':'and your bmi is : '+ output})
  logging.error('Uncalculatable')
  return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)