def parenthesis(n):
    def generate(current, open_count, close_count):
        if len(current) == 2 * n:
            pattern.append(current)
            return
        if open_count < n:
            generate(current + '{', open_count + 1, close_count)
        if close_count < open_count:
            generate(current + '}', open_count, close_count + 1)

    pattern = []
    generate('', 0, 0)
    return pattern

print(parenthesis(3))