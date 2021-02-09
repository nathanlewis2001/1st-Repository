import random
#This function should take a message and interleave it with random letters starting at string index start
def obfuscate(message, start=13, interval=4):
#your code goes here
  return coded_message

  
#This function should take the interleaved message, start, and interval, and return the decodded message
def deobfuscate(coded_message, start=13, interval=4):
#your code goes here
  return message

if __name__ == '__main__':
  test_message == ''.join(random.choices(string.ascii_letters, k=20))
  assert deobfuscate(obfuscate(test_message)) == test_message
  assert deobfuscate(obfuscate(test_message,20),20) == test_message
  assert deobfuscate(obfuscate(test_message,20,30),20,30) == test_message


  option = input("(D)ecode or (E)ncode? ")
  if option == 'E' or option == 'D':
    start = random.choices(20)
    message = input("Type your message here: ")
    print(obfuscate(message, start))
    print("The start padding for this message is" + str(start))
  elif option == 'D':
    start = input("What start padding is included with this message?: ")
    coded_message = input("paste your obfuscated message here: ")
    print(deobfuscate(coded_message, start))