def invite_to_event(username):
    invitation = f"Dear {username}, we have the honour to invite you to our event"
    return invitation



username = input("Enter your name: ")
print(invite_to_event(username))

