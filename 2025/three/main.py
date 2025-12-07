import enum
from heapq import heappop, heappush, heapify

small = "small.txt"
big = "large.txt"
AOC_CONFIG = {
    "part" : 1, # 0, 1,  
    "input": big
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

def get_max_joltage(rating: str) -> int:
    num_list = [int(x) for x in rating]
    nums = list(enumerate(num_list))
    nums = sorted(nums, key=lambda x:x[1], reverse=True)
    print(nums)
    largest = nums[0][0]
    prev_idx = 0
    for i, v in nums:
        if i >= len(nums)-1:
            continue
        largest = v
        prev_idx = i
        break
    for i, v in nums:
        if i > prev_idx:
            return (10*largest)+v
    return 0
def part_one(data: list[str]):
    total_jolt = 0
    for rating in data:
        max_joltage = get_max_joltage((rating.strip()))
        total_jolt += max_joltage
        print(max_joltage)
    return total_jolt


def part_two(data: list[str]):
    ...
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



