from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Calculator 😄</h2>
    <form action="/calculate" method="get">
        Num1: <input type="number" name="num1" required><br><br>
        Num2: <input type="number" name="num2" required><br><br>
        Operation:
        <select name="operation">
            <option value="add">Add</option>
            <option value="sub">Subtract</option>
            <option value="mul">Multiply</option>
            <option value="div">Divide</option>
        </select><br><br>
        <input type="submit" value="Calculate">
    </form>
    '''

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operation = request.args.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return "Cannot divide by zero ❌"
            result = num1 / num2
        else:
            return "Invalid operation ❌"

        return f"<h3>Result: {result}</h3><br><a href='/'>Go Back</a>"

    except Exception as e:
        return f"Error: {str(e)} ❌"

if __name__ == '__main__':
    # IMPORTANT for Docker
    app.run(host='0.0.0.0', port=5000, debug=True)