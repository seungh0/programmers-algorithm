def main():
    row, column = map(int, input().split(" "))
    cards = []
    for i in range(row):
        input_card = list(map(int, input().split(" ")))
        cards.append(min(input_card))

    print(max(cards))


if __name__ == "__main__":
    main()
