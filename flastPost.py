from flask import Flask , jsonify, request

app=Flask(__name__)

income=[
    {"description":"Salary","Amount":80000}
]

@app.route("/incomes")
def get_incomes():
    return jsonify(income)

@app.route("/incomes",methods=["POST"])
def add_income():
    income.append(request.get_json())
    return "Created",204

if __name__=='__main__':
    app.run(debug=True, port=5001)
