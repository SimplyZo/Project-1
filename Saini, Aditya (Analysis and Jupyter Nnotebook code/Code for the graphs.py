# Code for the line graph 

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Ensure that your Jupyter notebook can display graphs
%matplotlib inline

# Example data: Replace this with the actual vote counts
data = {
    'Year': [1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896,
             1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940,
             1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984,
             1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020],
    'Republican': [1.3, 1.9, 2.2, 3.0, 3.6, 4.0, 4.5, 4.8, 5.4, 5.2, 7.1,
                   7.2, 7.6, 7.7, 3.5, 8.5, 16.0, 15.7, 21.4, 15.8, 16.7, 22.3,
                   22.0, 21.9, 34.0, 35.6, 34.1, 27.2, 31.8, 47.0, 39.1, 43.9,
                   54.5, 48.9, 39.1, 39.2, 50.5, 62.0, 59.9, 60.9, 62.9, 74.2],
    'Democrat': [1.8, 1.4, 1.8, 2.7, 2.8, 4.3, 4.4, 4.9, 5.5, 5.6, 6.5,
                 6.4, 5.0, 6.4, 6.3, 9.1, 9.0, 8.4, 15.0, 22.8, 27.7, 27.0,
                 25.6, 24.2, 27.3, 26.0, 34.2, 43.1, 31.3, 29.2, 40.8, 35.5,
                 37.6, 41.8, 44.9, 47.4, 51.0, 59.0, 69.5, 65.9, 65.8, 81.3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Fill missing values with zeros for demonstration purposes
df.fillna(0, inplace=True)

# Plotting
plt.figure(figsize=(14, 7))

# Plot Republican votes
plt.plot(df['Year'], df['Republican'], marker='o', color='r', label='Republican')

# Plot Democratic votes
plt.plot(df['Year'], df['Democrat'], marker='o', color='b', label='Democrat')

# Title and labels
plt.title('Presidential Votes for Republican and Democratic Candidates (1856 - 2020)')
plt.xlabel('Year')
plt.ylabel('Votes (millions)')

# Legend
plt.legend()

# Grid
plt.grid(True)

# Show the plot
plt.show()

# Hypothesis Testing
# Null Hypothesis (H0): There is no significant difference in the mean number of votes
# Alternative Hypothesis (H1): There is a significant difference in the mean number of votes

# Perform two-sample t-test
t_stat, p_value = stats.ttest_ind(df['Republican'], df['Democrat'])

# Output the p-value
print(f'The p-value is: {p_value}')

# Determine if the results are significant
alpha = 0.05  # Commonly used threshold for significance
if p_value < alpha:
    print("We reject the null hypothesis. There is a significant difference in the mean number of votes.")
else:
    print("We fail to reject the null hypothesis. There is no significant difference in the mean number of votes.")











# Code for the bar graph 

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Ensure that your Jupyter notebook can display graphs
%matplotlib inline

# Example data: Replace this with the actual vote counts
data = {
    'Year': [1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896,
             1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940,
             1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984,
             1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020],
    'Republican': [1.3, 1.9, 2.2, 3.0, 3.6, 4.0, 4.5, 4.8, 5.4, 5.2, 7.1,
                   7.2, 7.6, 7.7, 3.5, 8.5, 16.0, 15.7, 21.4, 15.8, 16.7, 22.3,
                   22.0, 21.9, 34.0, 35.6, 34.1, 27.2, 31.8, 47.0, 39.1, 43.9,
                   54.5, 48.9, 39.1, 39.2, 50.5, 62.0, 59.9, 60.9, 62.9, 74.2],
    'Democrat': [1.8, 1.4, 1.8, 2.7, 0, 4.3, 4.4, 4.9, 5.5, 5.6, 6.5,
                 6.4, 5.0, 6.4, 6.3, 9.1, 9.0, 8.4, 15.0, 22.8, 27.7, 27.0,
                 25.6, 24.2, 27.3, 26.0, 34.2, 43.1, 31.3, 29.2, 40.8, 35.5,
                 37.6, 41.8, 44.9, 47.4, 51.0, 59.0, 69.5, 65.9, 65.8, 81.3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(20, 10))

# Setting the positions and width for the bars
pos = list(range(len(df['Year'])))
width = 0.4

# Plotting the bars
plt.bar(pos, df['Republican'], width, alpha=0.5, color='r', label='Republican')

# Create bars with the Democratic data
plt.bar([p + width for p in pos], df['Democrat'], width, alpha=0.5, color='b', label='Democrat')

# Title and labels
plt.title('Presidential Votes for Republican and Democratic Candidates (1856 - 2020)')
plt.xlabel('Year')
plt.ylabel('Votes (millions)')

# X-axis Tick mark labels
plt.xticks([p + 0.5 * width for p in pos], df['Year'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*2)
plt.ylim([0, max(df['Republican'] + df['Democrat'])] )

# Adding the legend and showing the plot
plt.legend(['Republican', 'Democrat'], loc='upper left')
plt.grid()
plt.show()


