def stocks():
  '''This is a single function used to work inside the while loop.'''
  # This is the dictionary built to hold stocks and prices.
  stocks = {
    'AAPL': '190.68',
    'MSFT': '337.22',
    'WMT': '153.49',
    'AMZN': '129.78',
    'NFLX': '438.10',
    'META': '290.53',
    'MDT': '85.89',
    'PDCO': '32.02',
    'MMSI': '79.61',
    'MCD': '292.10'
  }
  # input request for stock with upper method to help prevent errors.
  stock = input("Enter you stock ticker symbol. ").upper()
  # The get method passes stock symbol and prints a "symbol not found" message if stock    
  # not found in dictionary.
  price = stocks.get(stock,"\nSorry stock symbol was not found.")
  # print statement will print stock price.
  print(price)
stocks()
while True:
  repeat = input("\nType s for another stock price or type anything else to exit. ")
  if repeat == 's':
    print()
    stocks()
  # anything other than yes will exit the While loop.
  elif repeat != 's':
    break