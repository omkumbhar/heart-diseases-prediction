from flask import Flask ,flash ,request
from flask import render_template
from form import PredictForm

from classification import Prediction

app = Flask(__name__)

# app.config['SECRETE_KEY'] = '1621a889f3ec902e463eaa697e1f1212'
app.secret_key = '1621a889f3ec902e463eaa697e1f1212'

# @app.route('/')
# def form():
#     return render_template('form.html')

@app.route('/', methods = ['GET','POST'])
def predict():
    form = PredictForm(request.form)

    # print( request.method  )
    # print( f'{form.validate()=}'  )

    if request.method == 'POST' and form.validate(): 
        p = Prediction()
        p.fitModel()

    
        male =   int(form.male.data)
        age  =   int(form.age.data)
        education =   int(form.education.data)
        currentSmoker =   int(form.currentSmoker.data)
        cigNumber =   int(form.cigNumber.data)
        preStrock =   int(form.preStrock.data)
        prevHype =  int( form.prevHype.data)
        bloodPressure =   float(form.bloodPressure.data)
        bmi =    float(form.bmi.data)
        glucose =   float(form.glucose.data)

        pred = p.predict( [male,age,education,currentSmoker,cigNumber,preStrock,prevHype,bloodPressure,bmi,glucose] )


        
        pred = list( pred )

        print(f' {pred =} {male = } {age  = } { education = } {currentSmoker = } {cigNumber =  } {preStrock = } { prevHype = } { bloodPressure =} {bmi =  } {glucose =  }')

        if pred[0] == 0 :
            flash('Congratulations you wont have any heart threat in next 10 years')    
        else: 
            flash('Sorry you may develop coronary heart disease (CHD) in next 10 years')
    else:
        flash('Please fill correct data')   

    return render_template('py_form.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)