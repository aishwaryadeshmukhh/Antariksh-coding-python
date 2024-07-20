import matplotlib.pyplot as plt
import pandas as pd

#csv file attachment
data = pd.read_csv('social_media_sales_data.csv')

months = data['Month']
impressions = data['Social_Media_Impressions']
sales = data['Sales']

#plotting
plt.figure(figsize=(10, 4))

#plot impressions
plt.plot(months, impressions, marker='o', linestyle='-', color='g', label='Social Media Impressions')

#plot sales
plt.plot(months, sales, marker='s', linestyle='--', color='r', label='Sales')

plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Influence of Social Media on Sales')

#plt.grid(True)

plt.legend()        #legend of chart

plt.tight_layout()
plt.show()