result = 3
life = 3
print(end="\n")
print(f"Lives: {life}")
num = int(input("Enter any number from 1 to 20 ('0' to exit): "))

while num != result and life != 0:
    if num == 0:
        print("You have exited the game")
        break

    if num < 1 or num > 20:
        print(f"{num} is out of range")
        print(end="\n")
        num = int(input("Enter any number from 1 to 20 ('0' to exit): "))
    else:
        life = life - 1

    if num != result:
        if life == 0:
            print(end="\n")
            print(f"Lives: {life}")
            print("Game Over...You have lost!!!")
        else:
            print("Sorry.Try again")
            print(end="\n")
            print(f"Lives: {life}")
            num = int(input("Enter any number from 1 to 20 ('0' to exit): "))
if num == result and life != 0:
    print("Correct.You have won!")
