def remove_left_recursion(productions):
    count = 1
    for prod in productions:
        lhs, rhs = prod.split("->")
        parts = rhs.split("/")
        
        if lhs == parts[0][0]:  # Check for left recursion
            print("Entered production is left recursive")
            alpha, beta = parts[0][1:], parts[1]
            print(f"{lhs}->{beta}{lhs}'")
            print(f"{lhs}'->{alpha}{lhs}'/$")
        else:
            print(f"Entered production {count} is not left recursive")
        count += 1

# Example usage
n = int(input("Enter the number of productions: "))
productions = [input(f"Enter production {i+1}: ") for i in range(n)]
remove_left_recursion(productions)


OUTPUT

Enter the number of productions: 2
Enter production 1: E->E+T/T
Enter production 2: T->T*F/F
Entered production is left recursive
E->TE'
E'->+TE'/$
Entered production is left recursive
T->FT'
T'->*FT'/$
