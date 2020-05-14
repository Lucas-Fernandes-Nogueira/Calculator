def insistForValidInput(request, alert, validation):
    while True:
        try:
            userInput = validation(input(request))
            break
        except:
            print(alert)
    return userInput


def operatorValidation(operator):
    operators = ["x", "+", "-", "/", "%"]
    if operator not in operators:
        raise Exception
    else:
        return operator


def operate(operator, leftOperand, rightOperand):
    if operator == "x":
        result = leftOperand * rightOperand
    elif operator == "+":
        result = leftOperand + rightOperand
    elif operator == "-":
        result = leftOperand - rightOperand
    elif operator == "/":
        if(rightOperand == 0):
            print("Well done, you've reached a singularity!")
        else:
            result = leftOperand / rightOperand
    elif operator == "%":
        return leftOperand % rightOperand
    else:
        print("How did you even get here?")
    print(result)
    return result

def userInputCalculator():
    print("I am a calculator:")
    operator = insistForValidInput(
        "Operator:", "Give one of the following: x, +, -, /", operatorValidation)
    leftOperand = insistForValidInput(
        "Left Operand (integer):", "Only integers allowed", int)
    rightOperand = insistForValidInput(
        "Right Operand (integer):", "Only integers allowed", int)

    operate(operator, leftOperand, rightOperand)

def fileInputCalculator():
    with open("step_2.txt", "r") as file:
        lines = file.read().splitlines()
        total = 0
        for line in lines:
            parameters = line.split()
            total += operate(parameters[1], int(parameters[2]),  int(parameters[3]) )
        print("Total: " + str(total))

def interpreter(line, lineNumber, lines):
    parameters =  line.split()
    if parameters[0] == "goto":
        return executeGoTo(parameters), lines
        
    elif parameters[0] == "replace":
        return lineNumber + 1, executeReplace(parameters, lines)
    else:
        lines, lineNumber = executeRemove(parameters, lines, lineNumber)
        return lineNumber + 1, lines

def executeGoTo(parameters):
    if len(parameters) == 2:
        return int(parameters[1])
    else:
        return int(operate(parameters[2], int(parameters[3]), int(parameters[4])))

def executeReplace(parameters, lines):
    pasteTo = int(parameters[1])
    copyFrom = int(parameters[2])
    if pasteTo <= len(lines) and copyFrom <= len(lines):
        lines[pasteTo - 1] = lines[copyFrom - 1]
    return lines

def executeRemove(parameters, lines, lineNumber):
    removeLine = int(parameters[1])
    if removeLine <= len(lines):
        del lines[removeLine - 1]
    if removeLine <= lineNumber:
        return lines, lineNumber - 1
    else:
        return lines, lineNumber

def goToLine(lineNumber, lines):
    return lines[lineNumber - 1]

def fileNavigator():
    with open("step_4.txt", "r") as file:
        lines = file.read().splitlines()
        history = []
        currentLine = lines[0]
        lineNumber = 1

        while currentLine not in history:
            history.append(currentLine)
            lineNumber, lines = interpreter(currentLine, lineNumber, lines)
            currentLine = goToLine(lineNumber, lines)
        
        print("Statement: " + currentLine)
        print("Line number: " + str(lineNumber))

fileNavigator()