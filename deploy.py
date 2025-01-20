import streamlit as st

# Title and description
st.title("Efficient Calculator")
st.subheader("Perform basic arithmetic operations effortlessly!")
st.write("Created by TIPU REHMAN")

# Input fields for numbers
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
with col2:
    num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

# Operation mapping for efficiency
operations = {
    "Addition (+)": lambda x, y: x + y,
    "Subtraction (-)": lambda x, y: x - y,
    "Multiplication (×)": lambda x, y: x * y,
    "Division (÷)": lambda x, y: x / y if y != 0 else "Undefined (division by zero)",
}

# Operation selection
operation = st.selectbox("Choose an operation", list(operations.keys()))

# Calculate and display the result
if st.button("Calculate"):
    result = operations[operation](num1, num2)
    st.write(f"{operation} Result:")
    st.success(result)