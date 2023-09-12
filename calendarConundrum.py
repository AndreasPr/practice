if __name__ == "__main__":
    a, b, c = map(int, input().split())
    formatType = ""

    if a > 31:
        formatType = "Format #3"
    if a in range(12, 32):
        if c > 31:
            formatType = "Format #2"
        if c in range(1, 32):
            formatType = "Ambiguous"
    if a in range(1, 13):
        if b > 12:
            formatType = "Format #1"
        if b in range(1, 13):
            formatType = "Ambiguous"

    print(formatType)