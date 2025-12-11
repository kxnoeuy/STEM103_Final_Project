import random # Imports the random library that will be used to randomly select a response

# create a list of magic eight ball responses
response = ["Yes, definitely!", 
            "Ask again later", 
            "That will be a no", 
            "Signs point to yes", 
            "It looks hazy, try later", 
            "Naaaah", 
            "Thnking... yeah I guess so",
            "Survey says: Maybe!"]

def random_response(): # function that will return a random response
    return random.choice(response)

print("Welcome to the Magic Eight Ball")

# main loop to prompt the user to ask a question- "Ask the Magic Eight Ball a Question: "
while True: 
    question = input("Ask the Magic Eight Ball a yes/no question: ")

    print("Thinking...")
    answer = random_response()
    print("Magic 8 Ball says:", answer)

    # Ask if user wants to continue
    continue_playing = input("Do you want to ask another question? (yes/no): ")

    if continue_playing == "yes":
        continue
    elif continue_playing == "no":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Ending program.")
        break