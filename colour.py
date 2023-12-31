def autoreset(boolean):
    global autoreset
    if boolean == True:
        autoreset = True
    else:
        autoreset = False

def red(text):
    global autoreset
    if autoreset == True:
        returntext = "\u001b[31m" + text + "\u001b[0m"
    else:
        returntext = "\u001b[31m" + text
    return returntext

def blue(text):
    global autoreset
    if autoreset == True:
        returntext = "\u001b[34m" + text + "\u001b[0m"
    else:
        returntext = "\u001b[34m" + text
    return returntext

def black(text):
    global autoreset
    if autoreset == True:
        returntext = "\u001b[30m" + text + "\u001b[0m"
    else:
        returntext = "\u001b[30m" + text
    return returntext

def green(text):
    global autoreset
    if autoreset == True:
        returntext = "\u001b[32m" + text + "\u001b[0m"
    else:
        returntext = "\u001b[32m" + text
    return returntext
def yellow(text):
    global autoreset
    if autoreset == True:
        returntext = "\u001b[33m" + text + "\u001b[0m"
    else:
        returntext = "\u001b[33m" + text
    return returntext
def magenta(text):
    global autoreset
    if autoreset == True:
        returntext = "\u001b[35m" + text + "\u001b[0m"
    else:
        returntext = "\u001b[35m" + text
    return returntext

def cyan(text):
    global autoreset
    if autoreset == True:
        returntext = "\u001b[36m" + text + "\u001b[0m"
    else:
        returntext = "\u001b[36m" + text
    return returntext

def white(text):
    global autoreset
    if autoreset == True:
        returntext = "\u001b[37m" + text + "\u001b[0m"
    else:
        returntext = "\u001b[37m" + text
    return returntext

def reset(text):
    return "\u001b[0m" + text + "\u001b[0m"