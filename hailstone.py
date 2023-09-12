
def hailstone(n, total):
    if (n < 0):
        print("Invalid input")
        return
    if (n == 1):
        print(1)
        total = total + n
        return total
    if (n % 2 == 0):
        print(n)
        total = total + n
        return int(hailstone(n/2, total))
    if(n % 2 != 0):
        print(n)
        total = total + n
        return int(hailstone((3*n) + 1, total))


if __name__ == "__main__":
    total = 0
    print("Enter your integer number: ")
    user_input = int(input())
    result = int(hailstone(user_input, total))
    print(f"The sum is: {result}")
