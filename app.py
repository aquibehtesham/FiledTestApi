from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.debug = True

swagger = Swagger(app)
from datetime import datetime


@ns.route('/hello_world', methods=['GET','POST'])
def say_hello():
    '''
    this is test route for flask app
    '''
    return "Hello World!"


"""
parser_ProcessPayment = api.parser()

parser_ProcessPayment.add_argument('CreditCardNumber', type=str, required=True, help="Enter valid credit card number.")
parser_ProcessPayment.add_argument('CardHolder', type=str, required=True, help="Enter card holder name.")
parser_ProcessPayment.add_argument('ExpirationDate', type=inputs.datetime_from_iso8601, required=True, help="Enter date of expiry in YYYY-mm-dd format.")
parser_ProcessPayment.add_argument('SecurityCode', type=str, required=False, help="Enter 3 digit security code")
parser_ProcessPayment.add_argument('Amount', type=int, required=True, help="Enter amount to be processed.")

@ns.route("/", methods=["POST", "GET"])
@ns.expect(parser_ProcessPayment, validate=True)
class ProcessPayment(Resource):            
    def post(self):   
        try:
            inp_json = request.args 
            payment_gateway = None               
            if validate_credit_card(inp_json.get("CreditCardNumber")):            
                if validate_expiry_date(inp_json.get("ExpirationDate")):            
                    if float(inp_json.get("Amount")) <= 20:                    
                        payment_gateway = "CheapPaymentGateway"
                    elif 21 <= float(inp_json.get("Amount")) <= 500:                     
                        payment_gateway = "ExpensivePaymentGateway"
                    elif float(inp_json.get("Amount")) > 500:                    
                        payment_gateway = "PremiumPaymentGateway"
                    return  {"status" : payment_gateway, "error_code" : "200", "error_description" : "Payment is processed"}
                else:
                    return {"status" : "error", "error_code" : "400", "error_description" : "The request is invalid"}
            else: return {"status" : "error", "error_code" : "400", "error_description" : "The request is invalid"}
        except:
            return {"status" : "error", "error_code" : "500", "error_description" : "Internal server error"}

    
def validate_expiry_date(exp_date_str):
    exp_date_obj = datetime.fromisoformat(exp_date_str)
    todays_date_obj = datetime.now()
    if exp_date_obj > todays_date_obj:
        return True
    else: return False
    
def validate_credit_card(number_str):   
    """
        "379354508162306" --- valid,  
        "4388576018402626" ---- invalid
    """
    
    valid = False
    def check_number(number) :
        number = list(map(int, number))

        digits = []
        for x in range(len(number) - 2, -1, -2):
            digits.append(number[x] * 2)
        for y in range(len(number) - 1, -1, -2):
            digits.append(number[y])

        digits = list(map(int, ''.join(map(str, digits))))
        return sum(digits) % 10 == 0
    
    if 12 < len(number_str) < 17 :
        first2 = number_str[0:2]
        first4 = number_str[0:4]

        vendor = None
        if number_str[0] == "4" :
            vendor = "Visa"
        if number_str[0] == "5" and "0" < number_str[1] < "6":
            vendor = "MasterCard"
        if first2 in ("36", "38"):
            vendor = "Diners Club"
        if first4 == "6011" or first2 == "65":
            vendor = "Discover"
        if first2 == "35":
            vendor = "JCB"
        if first2 in ("34", "37"):
            vendor = "American Express"

        if vendor is not None:
            if check_number(number_str):
                print('This is a Valid "%s" Credit Card!' % vendor)
                valid = True
            else :
                print('This is not a Valid "%s" Credit Card' % vendor)
        else:
            print('Unknown vendor')
    else:
        print("Sorry, but this is not a Credit Card Number!")
    return valid    
"""    
    
if __name__ == '__main__':
    #app.run(debug=True, use_reloader=True)
    app.debug = True
    app.run(host="0.0.0.0",port=5777)
    

