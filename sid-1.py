val = ""
while (True):
    entertext = input("Say Something: ")
    if entertext != '/end':
        val = val + entertext.capitalize() +". "
    else:
        break
print(val)