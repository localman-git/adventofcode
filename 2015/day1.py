def main():
    floor = 0
    with open('./inputs/day1.txt', 'r') as f:
        for c in f.read():
            if c == '(':
                floor += 1
            if c == ')':
                floor -= 1
    print(floor)

if __name__ == "__main__":
    main()