import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

#It looks like you've created a Pandas DataFrame named df with 200 rows and 3 columns ('a', 'b', 'c'), filled with random values from a standard normal distribution (using np.random.randn). This is a common way to create a DataFrame for testing or demonstration purposes in data analysis with Python and Pandas.

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

#It appears that you're using the Altair library to create a scatter plot (mark_circle()) based on the data in your Pandas DataFrame df. The x-axis is represented by the 'a' column, the y-axis by the 'b' column, and the size and color of the circles are determined by the 'c' column. Additionally, you've specified a tooltip to display information about the 'a', 'b', and 'c' values when hovering over data points.

#Here's a breakdown of the Altair chart code:

#alt.Chart(df) : Specifies the DataFrame (df) as the data source for the chart.
#.mark_circle(): Specifies that you want to create a scatter plot with circles.
#.encode(...) : Defines how the columns in the DataFrame should be mapped to visual properties of the chart. In this case:
#x='a': Maps the 'a' column to the x-axis.
#y='b': Maps the 'b' column to the y-axis.
#size='c': Maps the 'c' column to the size of the circles.
#color='c': Maps the 'c' column to the color of the circles.
#tooltip=['a', 'b', 'c']: Specifies that when you hover over a data point, it should display the values of 'a', 'b', and 'c


st.write(df)

st.write(c)
