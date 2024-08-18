# Write a program to find out whether a given post is talking about “raju” or not.

about = "raju"
post = input("Enter your post caption: ").lower()

if about in post:
    print(f"This post is about {about}")
else:
    print(f"This post is not about {about}")