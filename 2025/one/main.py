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

def part_one(data: list[str]):
    val = 50
    MAX = 100
    MIN = 0
    count = 0
    for move in data:
        num = 0
        try:
            num = int(move[1:])
        except ValueError as e:
            print(f"error: {e}")
        num = num % 100
        print(num)
        if move[0] == 'R':
            val += num
        elif move[0] == 'L':
            val -= num
        if val >= MAX:
            val = val - MAX
        elif val < MIN:
            val = MAX + val
        if val == 0:
            print( val)
            count+=1
        
    print("count", count)
    print()
    return count
def part_two(data: list[str]):
    val = 50
    MAX = 100
    MIN = 0
    count = 0
    num = 0
    for move in data:
        try:
            num = int(move[1:])
        except ValueError as e:
            print(f"error: {e}")
        count += (num // 100)
        num = num % 100
        print("val before:", val)
        if move[0] == 'R':
            val += num
        elif move[0] == 'L':
            val -= num
        if val == 0:
            count += 1
            print("is zero")
        if val >= MAX and (val-num != MAX):
            if val - num != MAX:
                count += 1
            val = val - MAX
            print("too big")
        elif val < MIN:
            print("too small")
            if(val + num != 0):
                count += 1
            val = MAX + val
        print( "val after: ", val)
        print("count", count)
        
    print()
    return count

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



