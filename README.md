import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Load the mpg dataset
mpg = sns.load_dataset('mpg')

# Display the first few rows of the dataset
print(mpg.head())


# Seaborn Scatter Plot: Horsepower vs. Miles per Gallon
sns.scatterplot(data=mpg, x="horsepower", y="mpg", hue="origin")
plt.title('Horsepower vs. Miles per Gallon - Seaborn')
plt.xlabel('Horsepower')
plt.ylabel('Miles per Gallon')
plt.show()


# Plotly Box Plot: Box plot of mpg across different regions
fig = px.box(mpg, x="origin", y="mpg", title="Box Plot of MPG Across Different Regions - Plotly")
fig.show()

# Plotly Histogram: Distribution of Horsepower
fig = px.histogram(mpg, x="horsepower", title="Distribution of Horsepower - Plotly")
fig.show()
