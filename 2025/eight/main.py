from collections import defaultdict
import functools
import math

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
            data = [line.strip() for line in f.readlines()]
        return data
    except FileNotFoundError:
        print(f"Error: The file was not found.")
        return None



def part_one(data: list[str]):
    target_pairs = 1000
    coords = [tuple(line.split(',')) for line in data]
    coords = [(int(x), int(y), int(z)) for x, y, z in coords]

    # print(coords)

    dist_list = []
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            p1 = coords[i]
            p2 = coords[j]
            d = (math.dist(p1, p2))
            dist_list.append((d, p1, p2))
    dist_list = sorted(dist_list)[:target_pairs]

    adj_list = defaultdict(list)

    for d, p1, p2 in dist_list:
        adj_list[p1].append(p2)
        adj_list[p2].append(p1)
    print(adj_list)

    visited = set()
    nodes = []

    def dfs(curr_node: tuple[int, int, int]) -> int:
        count = 1
        if curr_node in visited:
            return 0
        visited.add(curr_node)
        for neighbor in adj_list[curr_node]:
            count += dfs(neighbor)

        return count

    counts = []
    for k, v in adj_list.items():
        counts.append(dfs(k))
    c = (sorted(counts, reverse=True)[:3])
    return functools.reduce(lambda x, y: x*y, c)



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



