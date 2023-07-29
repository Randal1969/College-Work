# converting miles to kilometers.

def main():
  ''' Display the intro screen.'''
  '''Function gets input and tests for exception error.'''
  # Call the intro function.
  intro()
  try:
    # input to get the number of miles
    miles = int(input("Enter the number of miles: "))
    #Convert miles to kilometers
    miles_to_kilometers(miles)
  except:
    print("An exception occurred, Try again by entering only a number")
    print()
    main()
def intro():
  '''The intro function displays an explanation of what program does.'''
  print("This program converts miles to kilometers.")
  print("For your reference the formula is: ")
  print ("1 mile = 1.609344 kilometers.")
def miles_to_kilometers(miles):
  '''The miles_to_kilometers function accepts a number of
  miles and displays the equivalent number of kilometers.'''
  kilometers = miles * 1.609344
  print(f"\n{miles} miles converts to {kilometers} kilometers")
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
               