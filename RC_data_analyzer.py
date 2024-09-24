import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app setup
st.title("Event Registration and Attendance Analysis")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Load CSV data
    df = pd.read_csv(uploaded_file)
    
    # Combine First Name and Last Name to get Full Name
    df['Full Name'] = df['First Name'] + ' ' + df['Last Name']

    # Separate Attendees (checked in) and Non-attendees (registered but did not check in)
    checked_in = df[df['Attendee Status'] == 'Checked in']  # People who attended
    only_registered = df[df['Attendee Status'] == 'attending']  # People who registered but did not attend
    
    # Display checked-in attendees
    st.subheader("List of Attendees (Checked In)")
    st.write(checked_in[['Full Name', 'Email']])
    
    # Display registered but not attended list
    st.subheader("List of Registered But Did Not Attend")
    st.write(only_registered[['Full Name', 'Email']])
    
    # Plot bar chart showing the difference
    st.subheader("Attendance vs. Registrations")
    
    data = {'Checked In': len(checked_in), 'Only Registered': len(only_registered)}
    labels = list(data.keys())
    values = list(data.values())
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title('Comparison of Attendees vs. Registered Only')
    ax.set_ylabel('Number of People')
    
    st.pyplot(fig)

    # Show summary statistics
    st.write(f"Total Checked In: {len(checked_in)}")
    st.write(f"Total Registered but Did Not Attend: {len(only_registered)}")
