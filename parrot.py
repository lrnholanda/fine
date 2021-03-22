prompt = "\nTell me something, and I wil repeat it back to you"
prompt += "\nEnter 'quit' to end the program."

active = True
message = ""
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)    
