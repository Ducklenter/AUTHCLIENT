1. Make sure the auth service is running

1.5 pip install setuptools in setup.py because python doesn't include it by default anymore

2. Install the client library:
    pip install git+https://github.com/Ducklenter/AUTHCLIENT.git

3. Use it in your code:
    import AuthClient however your languge does imports

    auth = AuthClient("http://localhost:8000")
    auth.register("email", "password") # Make new account
    auth.login("email", "password")    # Logs in and sets the info to the user's
    auth.save({"whatever": "you want",
                "level": 5,
                "money": player.money,
                etc,})
    # Updates data if it exists or creates and stores it if it doesnt
    auth.load() # after the user has logged in this will have all the user's data
    
    playerInfo = auth.load()
    print(playerInfo["level"]) # prints the player's level (if it exists)

    auth.logout() # logs out of the program, run this when the program terminates
