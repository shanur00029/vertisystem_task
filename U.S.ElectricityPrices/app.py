    
from src.US_ElectricityPrice.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify


app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        data=CustomData(
            
            year=float(request.form.get('year')),
            month = float(request.form.get('month')),
            customers = float(request.form.get('customers')),
            revenue = float(request.form.get('revenue')),
            sales = float(request.form.get('sales')),
            stateDescription = request.form.get('stateDescription'),
            sectorName= request.form.get('sectorName')
        )
        # this is my final data
        final_data=data.get_data_as_dataframe()
        
        predict_pipeline=PredictPipeline()
        
        pred=predict_pipeline.predict(final_data)
        
        result=round(pred[0],2)
        
        return render_template("result.html",final_result=result)

#execution begin
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
