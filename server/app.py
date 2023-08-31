#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# A print_string view should take one parameter, a string. 
# It should print the string in the console and display it in the web browser. 
# Its URL should be of the format /print/parameter.
@app.route("/print/<string:string>")
def print_string(string):
    print(string)
    return f"{string}"


# A count() view should take one parameter, an integer. 
# It should display all numbers in the range of that parameter on separate lines. 
# Its URL should be of the format /count/parameter.
@app.route("/count/<int:number>")
def count(number):
    count = ""
    for num in range(number):
        count = (count + str(num) + "\n")
    
    return count


# A math() view should take three parameters: num1, operation, and num2. 
# It must perform the appropriate operation on the two numbers in the order that they are presented. 
# The included operations should be: +, -, *, div (/ would change the URL path), and %. 
# Its URL should be of the format /math/<num1><operation><num2>.
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return  str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
