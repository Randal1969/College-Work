# converting gallons to liters.

def main():
  ''' Display the intro screen.'''
  '''Function gets input and tests for exception error.'''
  # Call the intro function.
  intro()
  try:
    # input to get the number of gallons
    gallons = int(input("Enter the number of gallons: "))
    #Convert gallons to liters
    gallons_to_liters(gallons)
  except:
    print("An exception occurred, Try again by entering only a number")
    print()
    main()
def intro():
  '''The intro function displays an explanation of what program does.'''
  print("This program converts gallons to liters.")
  print("For your reference the formula is: ")
  print ("1 gallon = 3.78541178 liters.")
def gallons_to_liters(gallons):
  '''The gallon_to_liters function accepts a number of
  gallons and displays the equivalent number of liters.'''
  liters = gallons * 3.78541178
  print(f"\n{gallons} gallons converts to {liters} liters")
  # Call the main function.
main()
while True:
  repeat = input("\nType yes to convert again or type anything else to exit. ")
  if repeat == 'yes':
      print()
      main()
  # anything other than yes will exit the While loop.
  else:
      break
               