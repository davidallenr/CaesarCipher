def encrypt(string, shift):
    result = ""
    # Parse string by lenght
    # add shift to each char
    # store in result
    for index in range(len(string)):
        character = string[index]
        if (character.isupper() and ord(character) != 32):
            result += chr((ord(character) + shift-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif (ord(character) != 32):
            result += chr((ord(character) + shift - 97) % 26 + 97)
        else:
            result += " "
    return result


if __name__ == "__main__":
    print("Hello, Welcome to the Caesar Cypher Demo")
    prompt_string = "Please Input a string to convert:"
    userinput_string = input(prompt_string)
    prompt_shift = "Please input a shift key (Default is 10)"
    userinput_shift = int(input(prompt_shift))
    print("Original String: " + userinput_string)
    print("Your encrpted String: " + encrypt(userinput_string, userinput_shift))

    print("\n\n")
    prompt_name = "Please input your full name: "
    user_name = input(prompt_name)
    print("Caesar Shift of your name: " + encrypt(user_name, 1))
    print("Can you figure out the shift key?")
