from heapq import heappop, heappush, heapify
from os import sep
small = "small.txt"
big = "large.txt"
AOC_CONFIG = {
    "part" : 2, # 0, 1,  
    "input": big
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

def helper_two(code: str) -> bool:
    # 14151415
    sublength = len(code)

    while sublength != 1:
        # print(code)
        if len(code) % sublength == 0:
            # sublength = 4
            nums = set()
            for i in range(sublength):
                # print("sublength: ", i)
                # if code[i*sublength:(i+1)*sublength]
                nums.add(code[i*(len(code)//sublength):(i+1)*(len(code)//sublength)])
                # print("nums: ", nums, "i:", i, "sublength", sublength, i*(len(code)//sublength), (i+1)*(len(code)//sublength))
            if len(nums) == 1:
                # got a sequence repeat at least once
                print("invalid", code, nums, len(nums))
                return True
        sublength -= 1
    return False

def part_two(data: list[str]):
    ans = 0
    count = 0
    for code in data:
        sep_idx = code.find('-')
        first = code[:sep_idx]
        last = code[sep_idx+1:]
        for i in range(int(first), int(last)+1):
            invalid = helper_two(str(i))
            if invalid:
                count += 1
                ans += i
    print(f"count: {count}")
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



