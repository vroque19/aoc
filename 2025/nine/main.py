from icecream import ic

small = "small.txt"
big = "large.txt"
AOC_CONFIG = {"part": 1, "input": big}  # 0, 1,


def read_input(file: str) -> list[str] | None:
    try:
        with open(file, "r") as f:
            # Reads all lines and strips leading/trailing whitespace (including newlines)
            data = [line.strip() for line in f.readlines()]
        return data
    except FileNotFoundError:
        print(f"Error: The file was not found.")
        return None


def get_pairs(data: list[str]):
    pairs: list[tuple[tuple[int, int], tuple[int, int]]] = []  # [((7, 1), 6, 1)]
    for i in range(len(data)):
        nums = data[i].split(",")
        tuple1 = (int(nums[0]), int(nums[1]))
        for j in range(i, len(data)):
            nums2 = data[j].split(",")
            tuple2 = (int(nums2[0]), int(nums2[1]))
            pairs.append((tuple1, tuple2))
    return pairs


def get_area(c1, c2):
    x_delta = abs(c1[0] - c2[0]) + 1
    y_delta = abs(c1[1] - c2[1]) + 1

    return x_delta * y_delta


def part_one(data: list[str]):
    print(data)
    pairs: list[tuple[tuple[int, int], tuple[int, int]]] = get_pairs(data)
    max_area = 0
    best_pair = (0, 0)
    for pair in pairs:
        area = get_area(pair[0], pair[1])
        if area > max_area:
            max_area = area
            best_pair = (pair[0], pair[1])
    print(best_pair, max_area)
    return max_area


def part_two(data: list[str]): ...
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
