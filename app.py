import pandas as pd

url = "https://raw.githubusercontent.com/afridalailiyah/davis-course-2024/master/tips.csv"

# reading the database
data = pd.read_csv("url")

# printing the top 10 rows
display(data.head(10))
