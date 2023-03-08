#Katherine O'Roark & Saerin Bong
def too_long(name):
    n = len(name)
    if n >= 140:
        print("The message is too long.")
    else:
        print("You can send this as a SMS message!")

too_long('Hello! I hope you are doing well today.')
too_long("Hello! I hope you are doing well today. I've been struggling with my homework lately!!!!!!!!!!!!!!!!! If anyone is in Math 231, please help!!!")
