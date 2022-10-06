# score = int(input("Enter grade"))
# score = int(input("Enter grade"))
def simi():
    counter = 0
    while counter < 5:
        score = int(input("Enter grade"))
        if score < 0 or score > 100:
            print("Enter a valid score")

        elif 90 <= score < 100:
            print("A")
        elif 70 <= score < 89:
            print("B")
        elif 50 <= score < 69:
            print("C")
        elif 40 <= score < 49:
            print("D")
        elif 30 <= score < 39:
            print("E")
        elif 0 < score <= 29:
            print("F :Zero Talent")
        counter += 5


if __name__ == '__main__':
    simi()
    
