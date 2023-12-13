import numpy as np
from flask import Flask, jsonify, request, render_template
from Linear_Project.utils import MedicalInsurance

app = Flask(__name__) # creating object of flask

@app.route("/") # home page route
def get_home():
    #return "Hello We are in home Page"
    return render_template("index.html")

@app.route("/predict_charges", methods = ["POST","GET"])
def get_insurance():
    if request.method == "POST":
        data = request.form
        print(">>>>>>",data)
        age = eval(data["age"])
        gender = data["gender"]
        bmi = float(data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]

        med_obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
        charges1 = med_obj.get_predicted_charges()[0]
        return render_template("index.html",charges = np.around(charges1,2))
        # return jsonify({"Result":f"Predicted medical insurance price is {np.around(charges1,2)}"})
        
    else:
        age = eval(request.args.get("age"))
        gender = request.args.get("gender")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")
        
        med_obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
        charges2 = med_obj.get_predicted_charges()[0]
        
        return render_template("index.html",charges = np.around(charges2,2))
    
    
if __name__ == "__main__":
    app.run()