def format_table(name_column, name_line, data):

    NAME = "Benchmark"
    FOUR = 4 # Two spaces and two separators

    # Find some lens
    lines_len = []
    lines_len.append(max(len(max(name_column, key=lambda x: len(x))),
                         len(NAME)) + FOUR)
    for i in range(len(name_line)):
        lines_len.append(max(len(name_line[i]),
                             len(max(data, key=lambda x: len(str(x[i]))))) + FOUR)

    # Printing
    print(f"|{NAME.center(lines_len[0])}|", end="")
    for i in range(len(name_line)):
        print(f"{name_line[i].center(lines_len[i + 1])}|", end="")

    print()
    print("|", end="")
    for i in range(len(lines_len)):
        print("-" * lines_len[i], "|", sep="", end="")
    print()

    for i in range(len(name_column)):
        print(f"|{name_column[i].center(lines_len[0])}|", end="")
        for j in range(len(name_line)):
            print(f"{str(data[i][j]).center(lines_len[j + 1])}|", end="")
        print()


# format_table(["best case", "worst case"],
#              ["quick sort", "merge sort", "bubble sort"],
#              [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
# print()

# format_table(["best case", "worst case"],
#              ["quick sort", "merge sort"],
#              [[1.23, 1.56], [3.3, 2.9]])
# print()

# format_table(["best case", "worst case", "middle case"],
#              ["quick sort", "merge sort", "bubble sort", "new sort"],
#              [[1.23, 1.56, 2.0, 3.0], [3.3, 2.9, 3.9, 6.0],
#               [1.0, 2.0, 3.0, 4.0]])
