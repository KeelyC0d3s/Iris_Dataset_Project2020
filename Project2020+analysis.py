#Iris Dataset Project 2020 Programming and Scripting GMIT



#Fisher’s Iris Dataset
#Introduced by British statistician and biologist Ronald Fisher in his 1936 paper entitled “The use of multiple measurements in taxonomic problems”. It is an example of linear discriminate analysis.
#The dataset gives the measurements in centimetres of the sepal length and width and petal length and width of 50 flowers from each species of iris: setosa, versicolor, and virginica.
#The dataset contains a set of 150 records of 5 attributes:
#Sepal length in cm
#Sepal width in cm
#Petal length in cm
#Petal width in cm
#Species of iris: setosa, versicolor, virginica




#Libraries used: pandas, Numpy, seaborn, sys
import pandas as pd
import numpy as np
import seaborn as sns
import sys

#Downloaded iris dataset from https://tinyurl.com/y8fovkyq

sys.stdout = open("variables_summary.txt", "w")

iris_data = pd.read_csv('tableconvert_csv_xin5ac.csv')

iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'variety']

iris_data.head(10)

iris_data.shape
#print(iris_data)

#Get the minimum value of all the columns
print("\nMinimum")
print(iris_data.min())

#Get the maximum value of all the columns
print("\nMaximum")
print(iris_data.max())

#Get the mean value of all the columns
print("\nMean")
print(iris_data.mean())

#Get the median value of all the columns
print("\nMedian")
print(iris_data.median())

#Get the standard deviation of all the columns
print("\nStandard Deviation")
print(iris_data.std())

print(iris_data['variety'].unique())

#Gathered a summary of the data (count, mean, std deviation, minumin, 25%, 50%, 75%, maximum)
#Used call chaining to make code look pretty.

summary = iris_data.describe().transpose().head()
print(summary)

sys.stdout.close()

#Displaying the data using various visualisations to represent all the variables.
#First, box plots.
#Boxplots are useful because they offer a quick and visually pleasing way to compare data.[2][11]
#In this case, I have four separate box plots
#First, comparing sepal length across all three species.

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid", palette="BuGn_r", rc={'figure.figsize':(11.7,8.27)})

title="Compare Distributions of Sepal Length"

sns.boxplot(x="variety", y="sepal_length", data=iris_data)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()
#Then, comparing sepal width across all three species
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid", palette="BuGn_r", rc={'figure.figsize':(11.7,8.27)})

title="Compare Distributions of Sepal Width"

sns.boxplot(x="species", y="sepal_width", data=iris_data)

plt.title(title, fontsize=26)

plt.show()

#Comparing petal length across all three variety
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid", palette="BuGn_r", rc={'figure.figsize':(11.7,8.27)})

title="Compare Distributions of Petal Length"

sns.boxplot(x="variety", y="petal_length", data=iris_data)

plt.title(title, fontsize=26)

plt.show()

#And finally, comparing petal width across all three species
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid", palette="BuGn_r", rc={'figure.figsize':(11.7,8.27)})

title="Compare Distributions of Petal Width"

sns.boxplot(x="variety", y="petal_width", data=iris_data)

plt.title(title, fontsize=26)

plt.show()

#Now, scatterplots!
#Scatterplots didn't work out properly my first go.
#First, again comparing sepal length across all three species
#import seaborn as sns
#import matplotlib.pyplot as plt

#sns.set(style="whitegrid", palette="BuGn_r", rc={'figure.figsize':(11.7,8.27)})

#title="Compare Distributions of Sepal Length Scatterplot"

#sns.scatterplot(x="variety", y="sepal_length", data=iris_data)

#plt.title(title, fontsize=26)

#plt.show()

#Comparing sepal width across all three species
#import seaborn as sns
#import matplotlib.pyplot as plt

#sns.set(style="whitegrid", palette="BuGn_r", rc={'figure.figsize':(11.7,8.27)})

#title="Compare Distributions of Sepal width Scatterplot"

#sns.scatterplot(x="variety", y="sepal_width", data=iris_data)

#plt.title(title, fontsize=26)

#plt.show()

#Comparing petal width across all three species
#import seaborn as sns
#import matplotlib.pyplot as plt

#sns.set(style="whitegrid", palette="BuGn_r", rc={'figure.figsize':(11.7,8.27)})

#title="Compare Distributions of Petal Length Scatterplot"

#sns.scatterplot(x="variety", y="petal_length", data=iris_data)

#plt.title(title, fontsize=26)

#plt.show()

#And finally, comparing petal width across all three species.
#import seaborn as sns
#import matplotlib.pyplot as plt

#sns.set(style="whitegrid", palette="BuGn_r", rc={'figure.figsize':(11.7,8.27)})

#title="Compare Distributions of Petal Width Scatterplot"

#sns.scatterplot(x="variety", y="petal_width", data=iris_data)

#plt.title(title, fontsize=26)

#plt.show()
#Preious scatterplot attempt did not yield the results I was looking for.

#Scatterplots take 2!
 
import seaborn as sns
import matplotlib.pyplot as plt
#Second attempt at scatterplots didn't render the results I wanted either [16].
#plt.figure()
#fig,ax=plt.subplots(1,2,figsize=(17, 9))
#iris_data.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
#iris_data.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
#ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
#ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
#ax[0].legend()
#ax[1].legend()

#plt.show()

#I prefer the code I found at reference [1].
from bokeh.plotting import figure, output_file, show
output_file("test1.html")

color1 = '#FF1493'
color2 = '#9400D3'
color3 = '#008080'
    
#Adding colours
colormap = {'Setosa': color1, 'Versicolor': color2, 'Virginica': color3}
colors = [colormap[x] for x in iris_data['variety']]

#Comparing Petal Width and Petal Length across all three species
p = figure(title = "Petal Width and Petal Length")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'
p.legend.location = "top_left"

p.diamond(iris_data["petal_length"], iris_data["petal_width"],color=colors, fill_alpha=0.2, size=10)

show(p)

#Comparing Sepal Width and Sepal Length across all three species
from bokeh.plotting import figure, output_file, show
output_file("test2.html")

#adding colors
colormap = {'Setosa': color1, 'Versicolor': color2, 'Virginica': color3}
colors = [colormap[x] for x in iris_data['variety']]

#adding labels
p = figure(title = "Sepal Width and Sepal Length")
p.xaxis.axis_label = 'Sepal Length'
p.yaxis.axis_label = 'Sepal Width'


p.circle(iris_data["sepal_length"], iris_data["sepal_width"],
         color=colors, fill_alpha=0.2, size=10)


show(p)





#Histograms
#I decided to use a pairplot here because:
#"This creates a matrix of axes and shows the relationship for each pair of columns in a DataFrame. By default, it also draws the univariate distribution of each variable on the diagonal axes"[12]
#That way, we have all data points available to us in one place to analyse.
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(iris_data, hue="variety", palette="GnBu_d", markers=["o", "s", "D"])

plt.show()


