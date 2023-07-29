import json

import requests


#This is my draft. I can't get the try/except block to work just right when testing for connection.

def get_city():
  # This is the information for site and input for city.
  # There is a try except block for testing connection'''
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  appid = "f4185b58e2d038a2eee929c20d336f79"
   
  try:
    r = requests.get(base_url, appid)
    print(f"Connection established. {r.status_code}")
    print()
  except Exception:
    print("Connection failed. {r.status_code}")
   # try except to check input and print an error message.      
  try:  
    city = input("\nEnter the name of the city. ").title()
    url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
    print(url)
    print(f"\n{city}")
    print ()
    get_data(url)
  except Exception:
    print("I could not find that city. Try again by entering a city name.")
    get_city()    
    
def get_zip():
  # This is the information for site and input for Zip Code.
  # There is a try except block for testing connection.
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  appid = "f4185b58e2d038a2eee929c20d336f79"
  try:
    r = requests.get(base_url, appid)
    print(f"Connection established. {r.status_code}")
    print()
  except Exception:
    print("Connection failed. {r.status_code}")
  # try except to check input and print an error message.
  try:
    zip = input("Enter the Zip Code. ").title()
    url = f"{base_url}?q={zip}&units=imperial&APPID={appid}"
    print(url)
    print(f"\n{zip}")
    print ()
    get_data(url)
  except Exception:
    print("I could not find that Zip Code. Try again by entering a Zip Code.")
    print()
    get_zip()    
    
# This fucncion prints out the weather data. 
def get_data(url):
  response = requests.get(url)
  unformated_data = response.json()
  #print(unformated_data)
  temp = unformated_data["main"]["temp"]
  print(f"The current temp is: {temp}")

  temp_max = unformated_data["main"]["temp_max"]
  print(f"The max temp is: {temp_max}")
  print()
# This function is the main option screen.
def main():
  print("Welcome to my program using data from openweathermap.org.")
  while True:
    choice = input("\nType '1' for city, '2' for zip Code, or '3' to quit. ")
    if choice == '1': 
      print()
      get_city()
      
    elif choice == '2':
      print()
      get_zip()
      
    elif choice == '3':
      break
    elif choice != '1' and choice != '2' and choice != '3': 
      print("Invalid data.")
  print("\nThank you for visiting. Goodbye.")
  
main()  