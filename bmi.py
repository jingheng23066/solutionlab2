def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("BMI = " +str(bmi))

    if(bmi < 18.5):
        print("Under weight")
    elif(bmi >18.5 and bmi <= 25.0):
        print("Normal Weight")
    elif(bmi > 25.0):
        print("Overweight")



calculate_bmi(weight=50, height=1.73)


