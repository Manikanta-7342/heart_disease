from flask import Flask,request,render_template

from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__) # Entry point to all

app=application

## Route for a home page
@app.route('/') # render to index.html to search in templates folder
def index():
    return render_template('basic_reactive_page.html') # to go to home page

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data=CustomData(
            age=int(request.form.get('age')),
            sex=request.form.get('sex'),
            chest_pain=request.form.get('chest_pain'),
            resting_bp=int(request.form.get('resting_bp')),
            cholesterol=float(request.form.get('cholesterol')),
            fasting_bs=request.form.get('fasting_bs'),
            max_hr=float(request.form.get('max_hr')),
            resting_ecg=request.form.get('resting_ecg'),
            st_slope=request.form.get('st_slope'),
            oldpeak=float(request.form.get('oldpeak')),
            exercise_angina=request.form.get('exercise_angina')
        )
        pred_df=data.get_data_as_data_frame()
        pred_df.to_csv("sample.csv")
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict()
        print("after Prediction")
        st = "Heart-Failure" if results[0]==1 else "No Heart-Disease"
        return render_template('home.html',results=st)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)

