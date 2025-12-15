
import enum
from turtle import width
from icecream import ic


small = "small.txt"
big = "large.txt"
AOC_CONFIG = {
    "part" : 2, # 0, 1,
    "input": big
}
def read_input(file: str):
    try:
        with open(file, 'r') as f:
            # Reads all lines and strips leading/trailing whitespace (including newlines)
            data = [line for line in f.readlines()]
        return data
    except FileNotFoundError:
        return None

def get_operations(lines: str) -> tuple[list[int], list[str]]:
    widths: list[int] = []
    curr = 0
    ic(lines)
    for  i in range(1, len(lines)):
        fast = i
        if lines[fast] == " ":
            curr += 1
        else:
            widths.append(curr)
            curr = 0
    return widths, lines.split()

def part_one(data: list[str]):
    widths, ops = get_operations(data[len(data)-1].strip())


    data = [line.strip() for line in data]
    expressions: list[str] = ["" for _ in range(len(ops))]
    for i in range(len(data)-1):
        nums = data[i].split()
        for j in range(len(expressions)):
            expressions[j] += nums[j]
            expressions[j] += ops[j] if i < len(data)-2 else ""
    sum = 0
    for e in expressions:
        sum += eval(e)
    print(expressions)
    return sum

def part_two(data: list[str]):
    widths, ops = get_operations(data[len(data)-1].strip())
    ops_len = len(ops) - 1
    ops = ops[:ops_len]
    ic(widths, ops)
    rows = max([len(s) for s in data])
    expressions: list[list[list[str]]] = []
    for i in range(ops_len):
        matrix: list[list[str]] = []
        for _ in range(len(data) - 1):
            row: list[str] = ["-1"] * widths[i]
            matrix.append(row)
        expressions.append(matrix)

    intermediate_list: list[list[str]] = [[] for _ in range(len(data)-1)]
    r = 0
    for line in data[:len(data)-1]:
        if(len(line)) < rows:
            delta = rows - (len(line))
            temp = line.removesuffix("\n")

            temp += " "*delta
            temp += "\n"
            line = temp
        prev = 0
        curr = ""
        w_idx = 0
        for ptr, c in enumerate(line):
            if w_idx >= ops_len:
                break
            if c == " " or c =="\n":
                # if the length of the curr num is length of num
                width = widths[w_idx]
                if (ptr - prev) <= width and ptr > width:
                    continue
                if ptr < width:
                    continue
                ic(width, w_idx)
                w_idx += 1 # found a valid num, get next width
                # print(f"ptr: {ptr}, prev: {prev}, c: {c}")
                num = line[ptr-width:ptr]
                # print(num)
                intermediate_list[r].append(num)
                prev = ptr
                continue
            curr += c
        r += 1

    # add each num from intermediate_list to the 3D matrix row 0 to row
    idx = 0
    r = 0
    ic(len(intermediate_list))
    for nums in intermediate_list:
        m = 0
        for num in nums:
            for idx, c in enumerate(num):
                ic(m, r, c, idx)
                if c != " ":
                    expressions[m][r][idx] = c
            # print(num)
            m += 1
        r += 1
    sum : int = 0
    ic(expressions)
    for i, matrix in enumerate(expressions):
        mat_expression = ""
        for c in range(len(matrix[0])):
            curr = ""
            for r in range(len(matrix)):
                curr += matrix[r][c] if matrix[r][c] != "-1" else ""
            mat_expression += curr
            if c < widths[i] - 1:
                mat_expression += ops[i]

        # print(mat_expression)
        ic(mat_expression)
        sum += eval(mat_expression)
        print(f"sum: {sum}")

    return sum


def main():
    lines = read_input(str(AOC_CONFIG["input"]))
    if lines is None:
        print("error reading file")
        return
    if AOC_CONFIG["part"] == 0 or AOC_CONFIG["part"] == 1:
        ans_one = part_one(lines)
        print(f"Answer 2: {ans_one}")

    if AOC_CONFIG["part"] == 0 or AOC_CONFIG["part"] == 2:
        ans_two = part_two(lines)
        print(f"Answer 2: {ans_two}")


if __name__ == "__main__":
    main()



