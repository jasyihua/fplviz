import streamlit as st

def contact_form():
    st.header("Contact Us")
    st.write("Have a question or feedback? Reach out to us!")

    # Create input fields
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    # Create a submit button
    if st.button("Submit"):
        if name and email and message:
            # Here you would typically handle the form submission
            # For example, sending an email or storing in a database
            # For now, we'll just display a success message
            st.success(f"Thanks for reaching out, {name}! We'll get back to you soon.")
            
            # Optionally, log or display the submitted information
            st.write("Submitted information:")
            st.write(f"Name: {name}")
            st.write(f"Email: {email}")
            st.write(f"Message: {message}")
        else:
            st.error("Please fill out all fields before submitting.")