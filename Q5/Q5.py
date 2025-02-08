import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('Sales.csv')
except FileNotFoundError:
    # If the file doesn't exist, create a new dataframe
    df = pd.DataFrame({"Months":[],"sales":[]})

Months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
sales = [380,400,660,800,900,1200,1600,2200,1500,1100,600,250] 

plt.bar(Months, sales, color='green', width= 0.5)
plt.title('Bar Chart of Ice-cream Sales')  
plt.xlabel('Month')   
plt.ylabel('Sales(in thousand dollars)')
plt.show()
plt.savefig('Bar chart of Ice-cream Sales')
plt.show()