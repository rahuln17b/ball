WS = int(input("Enter the number of white balls: "))
OTHER = int(input("Enter the number of other balls: "))


total = WS + OTHER

prob = (WS - 1) / (total - 1)
print("Probability that the second ball is white given the first ball is white:")
print(round(prob, 3))
