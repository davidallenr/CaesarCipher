def encrypt(string, shift):
    result = ""
    # Parse string by lenght
    # add shift to each char
    # store in result
    for index in range(len(string)):
        character = string[index]
        if (character.isupper()):
            result += chr((ord(character) + shift-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(character) + shift - 97) % 26 + 97)
    return result


if __name__ == "__main__":
    print(encrypt("David", 3))
