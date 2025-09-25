while True:
    user = input("you:")
    if user.lower() in["bye","exit","quit"]:
        print("Bot:good bye!")
        break
    elif user.lower() in ["how are you?"]:
        print("Bot:i am fine")
    elif user.lower() in["whats your name?"]:
        print("Bot:i am bot")
    elif user.lower() in["1"]:
        print("Bot:1")
    else:print("Bot: you said->",user)
     