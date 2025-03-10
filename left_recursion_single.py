def remove_left_recursion(prod):
    lhs, rhs = prod.split("->")
    parts = rhs.split("/")
    
    if lhs == parts[0][0]:  # Check for left recursion
        print("Entered production is left recursive")
        alpha, beta = parts[0][1:], parts[1]
        print(f"{lhs}->{beta}{lhs}'")
        print(f"{lhs}'->{alpha}{lhs}'/$")
    else:
        print("Entered production is not left recursive")

# Example usage
prod = input("Enter the production: ")
remove_left_recursion(prod)
