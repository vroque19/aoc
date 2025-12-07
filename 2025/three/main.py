import enum
from heapq import heappop, heappush, heapify
from typing import final

small = "small.txt"
big = "large.txt"
AOC_CONFIG = {
    "part" : 2, # 0, 1,  
    "input": big
}
def read_input(file):
    try:
        with open(file, 'r') as f:
            # Reads all lines and strips leading/trailing whitespace (including newlines)
            data = [line for line in f.read().splitlines()]
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

def get_first_idx(rating: str) -> int:
    num_list = [int(x) for x in rating]
    nums = list(enumerate(num_list))
    nums = sorted(nums, key=lambda x:x[1], reverse=True)
    largest = nums[0][0]
    idx = 0
    for i, v in nums:
        if i > len(nums)-12:
            continue
        largest = v
        idx = i
        return idx
    return idx


def get_best_joltage(joltage: str) -> int:
    largest_joltage = joltage[0]
    curr_idx = 1
    max_len = 12
    digits = len(largest_joltage)
    while digits < max_len:
        curr_rem = joltage[curr_idx:]
        next_poss = curr_rem[:len(curr_rem)-(max_len - digits)+1]
        best = max(list(next_poss))
        largest_joltage += best
        curr_idx= curr_idx + curr_rem.index(best) +1
        digits += 1

         
    return int(largest_joltage)

def part_two(data: list[str]):
    total_jolt = 0
    for rating in data:
        largest_idx = get_first_idx(rating)
        print(largest_idx)
        total_jolt += get_best_joltage(rating[largest_idx:])
    return total_jolt
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



