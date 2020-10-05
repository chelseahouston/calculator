# CALCULATING 2 NUMBERS ---
# USER INPUT NUMBERS ---
def calc():
  a = input("Enter a number: ")

  # CONFIRM INTEGER IS INPUT
  try:
    a = int(a)
  except ValueError:
    print("Incorrect value.")
    run()
  b = input("Enter another number: ")
  # CONFIRM INTEGER IS INPUT
  try:
    b = int(b)
  except ValueError:
    print("Incorrect value.")
    run()
  
  # ADDITION A ---
  # SUBTRACTION B ---
  # MULTIPLY C ---
  # DIVIDE D ---
  # POWER OF E ---
  print("To Add these numbers together, type the letter A")
  print("To Subtract your first number from the second, type the letter B")
  print("To Multiply these numbers together, type the letter C")
  print("To Divide the first number by the second, type the letter D")
  print("To times a to the power of b, type the letter E")
  value = input("Type your chosen letter here: ").upper()
  if value == "A":
    print(a + b)
  elif value == "B":
    print(b - a)
  elif value == "C":
    print(a * b)
  elif value == "D":
    print(a/b)
  elif value == "E":
    print(a**b)
  else: 
    print("Error: Incorrect value")
    run()

# RUN AGAIN? ---
def run():
  while True:
    runagain = input("Run again? (Y/N): ").upper()
    if runagain not in ('Y', 'N'):
      print("Invalid Input.")
      run()
      break
    if runagain == 'Y':
      calc()
      run()
      break
    else:
      print("Thank you for using the Calculator. Have a good day.")
      break

# CALL FUNCTIONS ---
calc()
run()
