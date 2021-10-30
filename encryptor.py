def toBinary(message):
    return " ".join("{0:07b}".format(ord(x), "b") for x in message).replace(" ", "")


def toText(message):
    splitted = [message[i : i + 7] for i in range(0, len(message), 7)]

    text = ""

    for binary in splitted:
        integer = int(binary, 2)
        text += chr(integer)

    return text


def decrypt(message, bits):
    m = toBinary(message)

    decryptedMessage = ""

    for i in range(len(m)):
        decryptedMessage += str(int(m[i] != bits[i]))

    return toText(decryptedMessage)


def encrypt(message, bits):
    m = toBinary(message)

    encryptedMessage = ""

    for i in range(len(m)):
        encryptedMessage += str(int(m[i] != bits[i]))

    return toText(encryptedMessage)
