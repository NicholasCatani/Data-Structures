### Derivative function

from sympy import symbols, diff, simplify

def find_derivative():
    # Get the polynomial expression from the user
    expression_str = input("Enter the polynomial in standard algebraic notation: ")

    # Replace "x" with "*x" for implicit multiplication
    expression_str = expression_str.replace("x", "*x")

    # Define the variable
    x = symbols("x")

    try:
        # Parse the expression and find the derivative
        expression = simplify(expression_str)
        derivative = diff(expression, x)

        # Print the result
        print("Original Polynomial:", expression)
        print("First Derivative:", derivative)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    find_derivative()