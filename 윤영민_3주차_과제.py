# 1번
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print(grade(94))
print(grade(64))
print(grade(34))

# 2번
def quadrant(x, y):
    if x > 0 and y > 0:
        return "제 1사분면"
    elif x > 0 and y < 0:
        return "제 4사분면"
    elif x < 0 and y < 0:
        return "제 3사분면"
    elif x < 0 and y > 0:
        return "제 2사분면"
print(quadrant(1,3))
print(quadrant(-1,3))
print(quadrant(-1,-3))
print(quadrant(1,-3))
 
# 3번
def leapYear(year):
    if int(year) % 400 == 0:
        return "윤년입니다."
    elif int(year) % 100 == 0:
        return "윤년이 아닙니다."
    elif int(year) % 4 ==0:
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."
print(leapYear(2024))
print(leapYear(1900))
print(leapYear(2000))
print(leapYear(2023))


# 4번
def dice(a, b, c):
    if a==b==c:
        return 10000 + a*1000
    elif a == b:
        return 1000 + a * 100
    elif b == c:
        return 1000 + b * 100
    elif a == c:
        return 1000 + a*100
    else:
        return max(a,b,c)*100
print(dice(3,3,6))
print(dice(2,2,2))
print(dice(6,2,5))



# 5번
def alarm(time):
    time = str(time)
    a = time[-2:]
    b = time[:-2]
    if not b:
        b = 0
        a = int(a)
        if a < 45:
            return "{0}시 {1}분" .format(23,a+15)
        else:
            return "{0}시 {1}분" .format(b,a-45)
    else:
        b = int(b)
        a = int(a)
        if a < 45:
            return "{0}시 {1}분" .format(b-1,a+15)
        else:
            return "{0}시 {1}분" .format(b,a-45)

print(alarm(900))
print(alarm(30))
print(alarm(2315))
print(alarm(1050))