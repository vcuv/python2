answer = ["red","blue","red","green"]

while True:
    guess = input()
    guess = guess.split()
    output = str()

    for i in range(4):
        if guess[i] == answer[i]:
            output += '1'
        elif guess[i] in answer:
            output += '2'
        else:
            output += '3'

    if output == "1111":
        print("正確答案")
        break
    else:
        print(output)

    break