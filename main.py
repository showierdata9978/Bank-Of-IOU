if __name__ == '__main__':
    #function
    import time 
    from functions.mainfunc import main_func
    time.sleep(.1)
    print("Loading")
    time.sleep(1)
    print("done")
    SignedIn = False
    main_func(SignedIn)
    while SignedIn:
      main_func(SignedIn)
    