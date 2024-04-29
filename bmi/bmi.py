def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi = float(weight)/(float(height)*(float(height)))
 print("BMI = " + str(bmi))
 if bmi< 18.5:
  print("Under Weight")
  return -1
 if bmi> 25:
  print("Over Weight")
  return 1
 else :
  print("normal weight")
  return 0
calculate_bmi(weight=57, height=1.73)
