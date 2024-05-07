import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/afridalailiyah/davis-course-2024/master/tips.csv"

# reading the database
data = pd.read_csv(url)

# printing the top 10 rows
st.write(data.head(10))

# Scatter plot with day against tip
fig1, ax1 = plt.subplots()
ax1.scatter(data['day'], data['tip'])
ax1.set_title("Scatter Plot 1")
ax1.set_xlabel('Day')
ax1.set_ylabel('Tip')
st.pyplot(fig1)

# Scatter plot with day against size
fig2, ax2 = plt.subplots()
ax2.scatter(data['day'], data['size'])
ax2.set_title("Scatter Plot 2")
ax2.set_xlabel('Day')
ax2.set_ylabel('Size')
st.pyplot(fig2)

# Scatter plot with total_bill against tip
fig3, ax3 = plt.subplots()
ax3.scatter(data['total_bill'], data['tip'])
ax3.set_title("Scatter Plot 3")
ax3.set_xlabel('Total Bill')
ax3.set_ylabel('Tip')
st.pyplot(fig3)
