def lhs(a, b):
    c = (a-b) ** 2
    return c


def rhs(a, b):
    c = (a ** 2) - (2 * a * b) + (b * b)
    return c


num_a = int(input("Enter a number: "))
num_b = int(input("Enter another number"))

ls = lhs(num_a, num_b)
rs = lhs(num_a, num_b)

if ls == rs:
    print("LHS equals RHS proved")
