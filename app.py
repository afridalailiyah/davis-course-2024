import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Menambahkan judul dengan st.title()
st.title("💻 Menyajikan data tips.csv pada platform Streamlit!")

url = "https://raw.githubusercontent.com/afridalailiyah/davis-course-2024/master/tips.csv"

# reading the database
data = pd.read_csv(url)

# printing the top 10 rows
st.write(data.head(10))

# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# Scatter plot with day against tip
fig, ax = plt.subplots()
scatter = ax.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar(scatter)

# Bar chart with day against tip
plt.bar(data['day'], data['tip'])

plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# histogram of total_bills
plt.hist(data['total_bill'])

plt.title("Histogram")

# draw lineplot
sns.lineplot(x="sex", y="total_bill", data=data)

# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')

sns.scatterplot(x='day', y='tip', data=data,)

# plotting the scatter chart
fig = px.scatter(data, x="day", y="tip", color='sex')

# plotting the scatter chart
fig = px.line(data, y='tip', color='sex')

plot = px.Figure(data=[px.Scatter(
	y=data['tip'],
	mode='lines',)
])

plot.update_layout(
	xaxis=dict(
		rangeselector=dict(
			buttons=list([
				dict(count=1,
					step="day",
					stepmode="backward"),
			])
		),
		rangeslider=dict(
			visible=True
		),
	)
)

st.pyplot(fig)
