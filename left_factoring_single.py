def remove_left_factoring(prod):
    lhs, rhs = prod.split("->")
    parts = rhs.split("/")
    i = 0
    while i < len(parts[0]) and i < len(parts[1]) and parts[0][i] == parts[1][i]:
        i += 1
    prefix = parts[0][:i]
    print(f"{lhs}->{prefix}{lhs}'")
    print(f"{lhs}'->{parts[0][i:] or '$'}/{parts[1][i:] or '$'}")

prod = input("Enter production: ")
remove_left_factoring(prod)
