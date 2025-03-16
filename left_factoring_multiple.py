def remove_left_factoring(productions):
    for prod in productions:
        lhs, rhs = prod.split("->")
        parts = rhs.split("/")
        
        i = 0
        while i < len(parts[0]) and i < len(parts[1]) and parts[0][i] == parts[1][i]:
            i += 1
        
        prefix = parts[0][:i]
        
        if prefix:
            beta1 = parts[0][i:] or "$"
            beta2 = parts[1][i:] or "$"
            print(f"{lhs}->{prefix}{lhs}'")
            print(f"{lhs}'->{beta1}/{beta2}")
        else:
            print(f"No left factoring needed for '{prod}'")

# Example usage
n = int(input("Enter the number of productions: "))
productions = [input(f"Enter production {i+1}: ") for i in range(n)]
remove_left_factoring(productions)
