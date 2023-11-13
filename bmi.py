name= input("Enter your name:")
weight= int(input("Enter your weight in kgs:"))
height= float(input("Enter your height in metres:"))
BMI= weight/height*height
print(BMI)
if BMI>0:
    if BMI<18.5:
      print(name +", you are underweight.")
    elif BMI <= 24.9:
         print(name +", you are normal weight.")
    elif BMI > 25 <= 29.9:
          print(name +", you are overweight.")
    elif BMI>30:
          print(name +", you are obese, please start exercising and maintain a good diet.")
    elif BMI < 39.9:
           print(name +", you are severely obese.")
    else:
           print(name +", you are morbidly obese.")
else:
     print("Please enter valid inputs.")         

