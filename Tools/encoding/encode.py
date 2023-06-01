alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def start():
    eord = input("encode? or decode? \n")
    msg = input("enter your message \n")
    shift = int(input("shifting number \n"))

    if eord == "encode":
        encode(msg, shift)
    elif eord == "decode":
        decode(msg, shift)



def encode(msg, shift):
    encoded = ""
    for i in msg:
        let = alphabet.index(i)
        encoded += alphabet[let + shift]
    print(encoded)

def decode(msg, shift):
    decoded = ""
    for i in msg:
        let = alphabet.index(i)
        decoded += alphabet[let - shift]
    print(decoded)


start()
keep = True
while keep:
    again = input("try again? \n")
    if again == "yes":
        start()
    else:
        break