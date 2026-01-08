from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("credit_card_approval_pipeline.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        print("FORM DATA →", request.form)
        df = pd.DataFrame([{
            "AMT_INCOME_TOTAL": float(request.form.get("AMT_INCOME_TOTAL", 0)),
            "CNT_CHILDREN": int(request.form.get("CNT_CHILDREN", 0)),
            "CNT_FAM_MEMBERS": int(request.form.get("CNT_FAM_MEMBERS", 1)),
            "YEARS_EMPLOYED": float(request.form.get("YEARS_EMPLOYED", 0)),
            "AGE_YEARS": float(request.form.get("AGE_YEARS", 30)),
            "CODE_GENDER": request.form.get("CODE_GENDER"),
            "FLAG_OWN_CAR": request.form.get("FLAG_OWN_CAR"),
            "FLAG_OWN_REALTY": request.form.get("FLAG_OWN_REALTY"),
            "NAME_INCOME_TYPE": request.form.get("NAME_INCOME_TYPE"),
            "NAME_EDUCATION_TYPE": request.form.get("NAME_EDUCATION_TYPE"),
            "NAME_FAMILY_STATUS": request.form.get("NAME_FAMILY_STATUS"),
            "NAME_HOUSING_TYPE": request.form.get("NAME_HOUSING_TYPE")
        }])

        prediction = model.predict(df)[0]
        result = "APPROVED ✅" if prediction == 1 else "DECLINED ❌"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        print("ERROR →", e)   # <-- THIS IS CRITICAL
        return render_template("index.html", prediction_text=str(e))


if __name__ == "__main__":
    app.run(debug=True)
