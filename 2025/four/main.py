from heapq import heappop, heappush, heapify

small = "small.txt"
big = "large.txt"
AOC_CONFIG = {
    "part" : 2, # 0, 1,  
    "input": small
}
def read_input(file):
    try:
        with open(file, 'r') as f:
            # Reads all lines and strips leading/trailing whitespace (including newlines)
            data = [line for line in f.readlines()]
        return data
    except FileNotFoundError:
        print(f"Error: The file '{f}' was not found.")
        return None

def is_accessible(data: list[str], row, col) -> bool:
    cols = len(data[0])
    rows = len(data)
    roll = '@'
    empty = '.'
    # print(row, col)
    # print("check is accessible")
    if data[row][col] == empty:
        # print("not a roll")
        return False
    rolls = 0
    if row != 0: # can move up
        rolls += data[row-1][col] == roll
        if col < cols - 1: # can move right
            rolls += data[row-1][col+1] == roll
        if col != 0: # can move left
            rolls += data[row-1][col-1] == roll
    if row < rows - 1: # can move down 
        rolls += data[row+1][col] == roll
        if col < cols - 1: # can move right
            rolls += data[row+1][col+1] == roll
        if col != 0: # can move left
            rolls += data[row+1][col-1] == roll

    if col < cols - 1: # can move right
            rolls += data[row][col+1] == roll
    if col != 0: # can move left
            rolls += data[row][col-1] == roll
    # if col != 0: # can move left
    #     rolls += data[row][col-1] == roll
    # if col < cols - 1: # can move right
    #     rolls += data[row][col+1] == roll
    # print(row, col, rolls)
    if rolls < 4:
        return True
    return False

def part_one(data: list[str]):
    ans = 0
    cols = len(data[0]) - 1
    rows = len(data)
    
    for i in range(rows):
        data[i] = data[i].strip()
        # print(len(data[i]))
        for j in range(cols):
            # print(data[i])
            if is_accessible(data, i, j):
                print(i, j)
                ans += 1
    print(data)
    return ans
    

def part_two_helper(data: list[list]):
    data[0][0] = 'M'
    return 1
def part_two(data: list[str]):
    ans = 0
    data_list = [list(line) for line in data]
    part_two_helper(data_list)
    # print(data_list)
    return ans

def main():
    lines = read_input(AOC_CONFIG["input"])
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



