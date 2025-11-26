from heapq import heappop, heappush, heapify

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
            data = [line for line in f.readlines()]
        return data
    except FileNotFoundError:
        print(f"Error: The file '{f}' was not found.")
        return None

def part_one(data: str):
    max_cals = 0
    curr = 0
    for line in data:
        print(line)
        if line == "\n":
            max_cals = max(max_cals, curr)
            curr = 0
            continue
        curr += int(line)

    return max_cals 

def part_two(data: str):
    max_cals = []
    curr = 0
    for line in data:
        if line == '\n':
            max_cals.append(curr)
            max_cals.sort(reverse=True)
            curr = 0
            continue
        curr += int(line)
    ans = 0
    for i in range(3):
        ans += max_cals[i]
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



