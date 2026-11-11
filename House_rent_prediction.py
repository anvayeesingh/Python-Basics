import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# Select CSV file from computer

root = Tk()

root.withdraw()

filename = filedialog.askopenfilename(

   title="Select House Dataset",

    filetypes=[("CSV Files", "*.csv")]

)

# Check if file is selected

if not filename:

   print("No file selected!")

   exit()

HouseDF = pd.read_csv(filename)
HouseDF.head()
HouseDF.info()
HouseDF.describe()
HouseDF.columns

sns.pairplot(HouseDF)
numeric_df = HouseDF.select_dtypes(include=[np.number])



plt.figure(figsize=(8,6))

sns.heatmap(
   numeric_df.corr(),
   annot=True,
   cmap='coolwarm',
   linewidth=0.5
)
plt.title("Corretation heatmap")
plt.show()