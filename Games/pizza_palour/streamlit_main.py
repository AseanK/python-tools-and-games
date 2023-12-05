# Congratulations! you just got a job at python pizza,
# Your first job is to build an automatic pizza orderin system
# Based on user's order, work out the final bill

# Pepperoni for small pizza = $2
# Pepperoni for large and medium pizza = $3
# Extra cheese for any size = $1

# Example input:
# size = L
# add_pepperoni = "Y"
# extra_cheese = "N"
import streamlit as st

st.title("Welcome to Python Pizza! 🍕")
st.subheader("Please follow the instructions to place your order! 😃")
st.markdown("---")
name = st.text_input('What is your name please?')
if name:
    st.write("Greetings " + str(name)+ "😁")
    st.markdown("---")
    bill = 0

    # Small_pizza = 15 #small_pizza
    # Medium_pizza = 20 #medium_pizza
    # Large_pizza = 25 #Large_pizz


    # order = (input("What size of pizza would you like to have?\nWe have the following options:\nS for Small Pizza\nM for Medium-sized Pizza\nand L for Large pizza? "))
    st.write("What size of pizza would you like to have?")
    order = st.radio("We have the following options", ["Small", "Medium", "Large"], captions=["$15", "$20", "$25"], index = None)
    if order == 'Small':
        bill = 15
    if order == 'Medium':
        bill = 20
    if order == 'Large':
        bill = 25
    st.write("Current Bill without any toppings: ", bill)
    st.markdown("---")
    if order:
        wants_pepperoni = st.radio("Do you want Pepperoni in your pizza", ["Yes", "No"], index= None)
        if wants_pepperoni == "Yes":
            size_pepperoni = st.radio("Which size of pepperoni do you want:", ["Small", "Medium", "Large"], captions=["$2", "$3", "$3"], index= None)
            if size_pepperoni == "Small":
                bill+=2
            if size_pepperoni == "Medium":
                bill+=3
            if size_pepperoni == "Large":
                bill+=3
        extra_cheese = st.radio("Do you want Extra Cheese in your pizza", ["Yes", "No"], index= None)
        if extra_cheese == "Yes":
            bill+=1
        st.markdown("---")
    st.write("Your total bill is $", bill)
    st.write("Thank you for your order "+str(name)+" 😁Please pay $"+str(bill)+" to validate your order!")



