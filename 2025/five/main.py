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
            data = [line for line in f.read().splitlines()]
        return data
    except FileNotFoundError:
        print(f"Error: The file '{f}' was not found.")
        return None

def part_one(data: list[str]):
    idx = data.index('')
    ranges = data[:idx]
    ranges = [range(int(r.split('-')[0]), int(r.split('-')[1])+1) for r in ranges]
    # print(ranges)
    print(4 in range(2, 4))
    total_fresh = 0
    ingredients = data[idx+1:]
    for i in ingredients:
        for r in ranges:
            print(i, r)
            if int(i) in r:
                total_fresh += 1
                break
    return total_fresh
    
def part_two(data: list[str]):
    ...
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



