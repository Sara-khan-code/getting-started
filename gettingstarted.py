from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Johny",
        "email": "Johny@example.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200

@app.route("/faiza-issues/<faiza_id>")
def faiza_issues(faiza_id):
    laptop_problems = {
        "faiza_account": "faiza2020@gmail.com",
        "faiza_id": faiza_id,
        "backgroun_issues": "Theme Issues",
        "New_laptop": "cha cha No CHANCE"
    }
    any_solution = request.args.get("any_solution")
    if any_solution:
        laptop_problems['any_solution'] = any_solution
        
        return jsonify(laptop_problems), 200
    
@app.route("/product-info/<get_pinfo>")
def get_product(get_pinfo):
    product_data = {
        "product_name": "Specific product",
        "product_id": get_pinfo,
        "p_type": "Food"
    }
    new_product = request.args.get("new_product")
    if new_product:
        product_data["new_product"] = new_product
        
    return jsonify(product_data), 200


@app.route("/create-user", methods = ["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201
if __name__ == "__main__":
    app.run(debug=True)