from icecream import ic

small = "small.txt"
big = "large.txt"
AOC_CONFIG = {
    "part" : 1, # 0, 1,
    "input": big
}
def read_input(file) -> list[str] | None:
    try:
        with open(file, 'r') as f:
            # Reads all lines and strips leading/trailing whitespace (including newlines)
            data = [line for line in f.readlines()]
        return data
    except FileNotFoundError:
        print(f"Error: The file was not found.")
        return None

def part_one(data: list[str]):
    beams = set()
    cnt = 0
    for line in data:
        ic(line)
        for i in range(len(line)):
            if line[i] == 'S':
                beams.add(i)
            if line[i] == '^':
                if i in beams:
                    cnt += 1
                    beams.add(i-1)
                    beams.add(i+1)
                    beams.remove(i)
    return cnt

def part_two(data: list[str]):
    ...
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



