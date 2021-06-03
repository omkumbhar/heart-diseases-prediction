from wtforms import Form, BooleanField, IntegerField,SelectField,SubmitField, StringField ,FloatField

from wtforms.validators import DataRequired,Length

class PredictForm(Form):
    male            = SelectField("What is your gender ", choices=[(1,'Yes'),(2,'No')],validators=[DataRequired()])

    age             = IntegerField('Enter your age :',  validators=[DataRequired(),] )

    education       = SelectField('Enter your completeed education', choices=[(1,"SSC"),(2,"HSC"),(3,"Graduate"),(4,"Post Graduate")] ,validators= [ DataRequired()])

    currentSmoker   = SelectField("Are you current smoker ", choices=[(1,'Yes'),(2,'No')],validators=[DataRequired()  ] )

    cigNumber       =  IntegerField('IF yes enter cigrates per day :', validators=[   ])

    preStrock       = SelectField("Have you experinced prevelent stroke ", choices=[(1,'Yes'),(2,'No')],validators=[DataRequired()])

    prevHype        =  SelectField("Have you experinced prevelent hype ", choices=[(1,'Yes'),(2,'No')],validators=[DataRequired()])

    bloodPressure   = FloatField('Enter your blood pressure :', validators=[ DataRequired() ])

    bmi             = FloatField('Enter your BMI :', validators=[ DataRequired(), ])

    glucose         = FloatField('Enter your Glucose in your blood :', validators=[ DataRequired() ])



    submit          = SubmitField('Predict')

