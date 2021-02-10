import random
from string import printable
  #This function should take a message and interleave it with random letters starting at string index start
def obfuscate(message, start=13, interval=4):
#your code goes here
  message_array = list(message)

  beginning = ''.join(random.choices([chr(random.randint(33, 126)), chr(random.randint(33, 126)), chr(random.randint(33, 126))], k=interval))

  new_letter = ""
  for letter in message_array:
    new_letter += letter
    x = 0
    while x < interval:
        new_letter += chr(random.choice([random.randint(33, 126)]))
        x += 1
  return beginning + new_letter
#This function should take the interleaved message, start, and interval, and return the decoded message
def deobfuscate(coded_message, start=13, interval=4):

  interval+=1 
  decoded_message = coded_message[start::interval]
  return decoded_message

if __name__ == "__main__":
    option = input("(D)ecode or (E)ncode or (Q)uit?\n").upper()
    while option != 'Q':
      if option == 'E' or option == '':
        start = random.randint(0,20)
        inter = int(input("How far apart would you like your characters in the coded message\n"))
        message = input("Type your message here\n")
        print(f"The start padding for this message is {start} and your interval is {inter}")
        print(obfuscate(message, start))
      elif option == 'D':
        coded_message = input("paste your obfuscated message here\n")
        start = input("What start padding is included with this message?: ")
        inter = int(input("How far apart would you like your characters in the coded message\n"))
        print(f"The start padding for this message is {start} and your interval is {inter}")
        print(deobfuscate(coded_message, start))