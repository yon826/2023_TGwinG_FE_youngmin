import math

def calcCircleArea(r):
    result = float()
    result = round(math.pi * r * r,2)
    return result


def calcLog(a, b):
    result = float()
    result = round(math.log(b,a),2)
    return result

def calcSin(x):
    result = float()
    result = round(math.sin(x),2)
    return result

def calcFactorial(x):
    result = int()
    result = math.factorial(x)
    return result

def calcCombination(n, r):
    result = int()
    result = math.comb(n,r)
    return result

def calculator(order):
    result = 0
    cmd,var = order.split(':')
    if cmd == "원넓이":
        result = calcCircleArea(float(var))
    elif cmd == "로그":
        x,y = var.split()
        if x == "e":
            x = math.e
        result = calcLog(float(x),float(y))
    elif cmd == "사인":
        result = calcSin(float(var))
    elif cmd == "팩토리얼":
        result = calcFactorial(int(var))
    elif cmd == "조합":
        x,y = var.split()
        result = calcCombination(int(x),int(y))
    return result