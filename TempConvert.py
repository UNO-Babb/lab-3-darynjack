#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = input("What is the temperature in Fahrenheit?") 
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempF = int(tempF)
  
  tempC = (tempF -32)/(9/5)

  tempC = round(tempC, 1)
  #Output converted temperature.
  print(tempF, "is", tempC, "degrees celcius.")
if __name__ == '__main__':
  main()
