#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = input("80") 
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = input(tempF - 32) * 5 / 9
  tempC = round(tempC, 1)
  #Output converted temperature.
  print("[tempF] is [tempC]")
 
  tempC = tempF / 3

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
