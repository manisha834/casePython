# Write a program that asks the user to enter the name of a social media platform
# (Snapchat, Facebook, or Instagram).
# If the platform is Facebook
# oAsk if the user has an account (Yes/No)
# If Yes → display “Login successful”
# Else → display “Please create an account”
# If the platform is Instagram
# oAsk if the user’s account is private or public
# If private → display “Follow request sent”
# Else → display “You can view posts”
# If the platform is Snapchat
# oAsk if the user has added friends
# If Yes → display “You can send snaps”
# Else → display “Add friends to continue”
# Else → display “Invalid platform”

socialMedia=input("Enter the name of social media platform:").lower()
if socialMedia=="facebook":
    result=input("Do you have an account:")
    if result=="yes":
      print("Login Successful")
    else:
     print("Please create an account")  

elif socialMedia=="Instagram":
    result1=input("do you have private account or public:")
    if result1=="private":
      print("Follow request sent")
    else:
     print("You can view posts")  
 
elif socialMedia=="snapchat":
   result2 = input("Do you added friends.")
   if result2=="yes":
    print("you can send snaps")
   else:
    print("Add friends to continue")  
else:
 print("invalid platform")
    