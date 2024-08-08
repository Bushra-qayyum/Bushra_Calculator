import streamlit as st
import add
import subtract
import multiply
import divide


def main():
    st.title('Bushra Calculator')

    # User inputs
    num1 = st.number_input("Enter the first number:", format="%.2f")
    num2 = st.number_input("Enter the second number:", format="%.2f")

    operator = st.selectbox("Select an operator:", ['+', '-', '*', '/'])

    # Perform the calculation based on the operator
    if st.button("Calculate"):
        if operator == '+':
            result = add.add(num1, num2)
        elif operator == '-':
            result = subtract.subtract(num1, num2)
        elif operator == '*':
            result = multiply.multiply(num1, num2)
        elif operator == '/':
            if num2 != 0:
                result = divide.divide(num1, num2)
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operator"

        # Display the result
        st.write(f"The result is: {result}")


if __name__ == "__main__":
    main()