'''Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"'''


#Remember to go from lowest to highest

def bmi(weight, height):
    bmi_cal = weight / height ** 2 
    if bmi_cal <= 18.25:
        return "Underweight"
    elif bmi_cal <= 25:
        return "Normal"
    elif bmi_cal <= 30:
        return "Overweight"
    elif bmi_cal > 30:
        return "Obese"
    
#Done!!!!
   