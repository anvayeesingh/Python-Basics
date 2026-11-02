import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# Select a CSV file from your computer

root = Tk()

root.withdraw()

filename = filedialog.askopenfilename(

 title="Select your CSV file",

 filetypes=[("CSV Files", "*.csv")]

)


if not filename:

 print("No file selected!")

 exit()
countries_df = pd.reas_csv(filename)

countries = countries_df
countries.heas(3)

c_52 = countries.loc[countries['year'] == 1952]
c_52.head()

c_07 = countries.loc[countries['year'] == 2007]
c_07.head()
type(c_52)

c_merge = c_52(c_07, left_on='country', tight_on='country')
c_merge.head()

c_merge = c_merge.drop(['year_x',' year_y'], axis=1)
c_merge.head()

c_merge['population_growth']=(
    c_merge['populatiob_y'] - c_merge['population_x']
)

c_merge.head()

31889923 - 8425333

c_merge.shape, type(c_merge)

c_merge = c_merge.sort_values(
    'population_growth' ,
    ascending=False
).head(10)


c_merge.head(10)

c_merge = c_merge.reset_index()

c_merge.head(10)

c_merge.shape

c_merge = c_merge.drop(['index'], axis=1)

c_merge.shape


c_merge

names = [
    'China',
    'India',
    'United States',
    'Indonesia',
    'Brazil',
    'Pakistan',
    'Bangladesh',
    'Nigeria',
    'Mexico',
    'Philippines'
]

pop_grow = c_merge['population_growth'] / 10**6

plt.figure(figsize=(15, 9))

plt.bar(names, pop_grow, width=0.6)

plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title(
    'Top 10 Countries w/the Biggest Population Growth from 1952 to 2007'
)

plt.xticks(rotation=45)

for x, y in zip(names, pop_grow):
    label = "{:.2f}".format(y)

    plt.annotate(
        label,
        (x, y),
        textcoords="offset points",
        xytext=(0, 10),
        ha='center'
    )

plt.show()