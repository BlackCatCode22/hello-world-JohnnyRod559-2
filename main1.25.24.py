
UserInput = input("Enter your name: ")
print("Hello", UserInput)

hours_worked = input("Enter Hours: ")
pay_rate = input("Rate: ")
float_hours = float(hours_worked)
float_rate = float(pay_rate)
#print(float_hours, float_rate)
if float_hours > 40:
    #print("Overtime")
    reg = float_rate * float_hours
    otp = (float_hours - 40.0) * (float_rate * 0.5)
    #print(reg,otp)
    total_pay = reg + otp
else:
    #print("Regular")
    total_pay = float(hours_worked) * float(pay_rate)
print("Pay: ", total_pay)
