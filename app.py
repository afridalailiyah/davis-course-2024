import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/afridalailiyah/davis-course-2024/master/tips.csv"

# reading the database
data = pd.read_csv(url)

# printing the top 10 rows
st.write(data.head(10))

# Scatter plot with day against tip (plot pertama)
fig1, ax1 = plt.subplots()
ax1.scatter(data['day'], data['tip'])
ax1.set_title("Scatter Plot 1")
ax1.set_xlabel('Day')
ax1.set_ylabel('Tip')
st.pyplot(fig1)

# Scatter plot with day against tip (plot kedua)
fig2, ax2 = plt.subplots()
scatter = ax2.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])
ax2.set_title("Scatter Plot 2")
ax2.set_xlabel('Day')
ax2.set_ylabel('Tip')
plt.colorbar(scatter)
st.pyplot(fig2)

# Scatter plot with tip and size (plot ketiga)
fig3, ax3 = plt.subplots()
ax3.plot(data['tip'], label='Tip')
ax3.plot(data['size'], label='Size')
ax3.set_title("Scatter Plot 3")
ax3.set_xlabel('Day')
ax3.set_ylabel('Tip/Size')
ax3.legend()
st.pyplot(fig3)

# Bar chart with day against tip (plot keempat)
fig4, ax4 = plt.subplots()
ax4.bar(data['day'], data['tip'])
ax4.set_title("Bar Chart")
ax4.set_xlabel('Day')
ax4.set_ylabel('Tip')
st.pyplot(fig4)

# Histogram of total_bills (plot kelima)
fig5, ax5 = plt.subplots()
ax5.hist(data['total_bill'])
ax5.set_title("Histogram")
ax5.set_xlabel('Total Bill')
ax5.set_ylabel('Frequency')
st.pyplot(fig5)

# draw lineplot (plot keenam)
fig6, ax6 = plt.subplots()
sns.lineplot(x="sex", y="total_bill", data=data)
plt.title('Title using Matplotlib Function')
st.pyplot(fig6)

# draw scatterplot (plot ketujuh)
fig7, ax7 = plt.subplots()
sns.scatterplot(x='day', y='tip', data=data)
plt.title('Title using Matplotlib Function')
st.pyplot(fig7)
