from heapq import heappop, heappush, heapify
from os import sep
small = "small.txt"
big = "large.txt"
AOC_CONFIG = {
    "part" : 2, # 0, 1,  
    "input": small
}
def read_input(file):
    try:
        with open(file, 'r') as f:
            # reads all lines and strips leading/trailing whitespace (including newlines)
            data = f.read().split(',')
        return data
    except FileNotFoundError:
        print(f"error: the file '{f}' was not found.")
        return None

def is_valid(code: str) -> bool:
    return not code[:len(code)//2] == code[len(code)//2:]

def part_one(data: list[str]):
    ans = 0
    count = 0
    for code in data:
        sep_idx = code.find('-')
        first = code[:sep_idx]
        last = code[sep_idx+1:]
        for i in range(int(first), int(last)+1):
            if not is_valid(str(i)):
                curr_sum = int(i)
                count += 1
            else: curr_sum = 0
            ans += curr_sum
    return ans

def sequence_repeated_at_least_twice(code: str) -> bool:
    first_rep_idx = 0
    slow, fast = 0, 1
    for i in range(1, len(code)):
        fast = i
        if code[slow] == code[fast]:
            if first_rep_idx == 0:
                first_rep_idx = i
            slow += 1
            print(slow, fast, len(code) - 1, fast == (len(code) - 1))
    if fast == (len(code) - 1) and fast - first_rep_idx == (slow + 1):
        return True
    return False


def part_two(data: list[str]):
    ans = 0
    count = 0
    for code in data:
        sep_idx = code.find('-')
        first = code[:sep_idx]
        last = code[sep_idx+1:]
        for i in range(int(first), int(last)+1):
            if sequence_repeated_at_least_twice(str(i)):
                print(count)
                print(i)
                curr_sum = int(i)
                count += 1
            else: curr_sum = 0
            ans += curr_sum
    return ans

def main():
    lines = read_input(AOC_CONFIG["input"])
    if lines is None:
        print("error reading file")
        return
    if AOC_CONFIG["part"] == 0 or AOC_CONFIG["part"] == 1:
        ans_one = part_one(lines)
        print(f"Answer 1: {ans_one}")

    if AOC_CONFIG["part"] == 0 or AOC_CONFIG["part"] == 2:
        ans_two = part_two(lines)
        print(f"Answer 2: {ans_two}")


if __name__ == "__main__":
    main()



