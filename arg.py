def shutdown():
    
    user_input = input("Do you want to shut down? (yes/no): ")

    if user_input == "yes":
        print("Shutting down...")
    elif user_input == "no":
        print("Shutdown aborted.")
    else:
        print("Sorry, I didn't understand that.")

shutdown()
