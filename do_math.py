#print("Hello! What is the temperature:")

#temp =  input()
valid = False
while not valid:
    try: 
        temp = int(input ("Enter the temperature : "))
        valid = True
    except ValueError:
        print("That is not a number! Please try again.")
valid = False 
units = {"C": "Celsius", "F": "Farhenheit"}
while not valid :
     
     unit = input (" Enter the unit (C for Celsius and F for Farhenheit): ")
     valid = unit in units 
     
print ("The number you entered was", temp) 
print ("The unit you chose was", units [unit])    

if unit  == "C":
    converted = (temp * 1.8) + 32
    converted_unit = "F"
if unit == "F":
    converted = (temp -32 ) / 1.8
    converted_unit = "C"
    
print (f"The temperature  {temp}{unit} is {round(converted,2)} in {converted_unit}")    