def solve(target, numbers):
    def helper(nums, steps):
        if len(nums) == 1:
            if nums[0] == target:
                return steps
            return None

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                new_nums = [nums[k] for k in range(n) if k not in (i, j)]

                candidates = []
                candidates.append((a + b, "+", a, b))
                candidates.append((a * b, "*", a, b))
                if a >= b:
                    candidates.append((a - b, "-", a, b))
                else:
                    candidates.append((b - a, "-", b, a))
                if b != 0 and a % b == 0:
                    candidates.append((a // b, "/", a, b))
                if a != 0 and b % a == 0:
                    candidates.append((b // a, "/", b, a))

                for val, op, left, right in candidates:
                    result = helper(new_nums + [val], steps + [(left, op, right, val)])
                    if result:
                        return result
        return None

    steps = helper(numbers, [])
    if steps:
        return "\n".join(f"{left} {op} {right} = {result}" for left, op, right, result in steps)
    return None


if __name__ == "__main__":
    target = int(input("Enter target number: "))
    raw = input("Enter base numbers (comma separated): ")
    base = [int(x.strip()) for x in raw.split(",")]
    sol = solve(target, base)
    if sol:
        print(sol)
    else:
        print("No solution found")
