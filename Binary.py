def decimal_to_binary(decimal_number):
   if decimal_number > 1:
              decimal_to_binary(decimal_number//2)
   print(decimal_number % 2,end = '')
user_input = int(input("Enter an integer: "))
decimal_to_binary(user_input)