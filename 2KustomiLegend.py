import pandas as pd 
import datetime
import matplotlib.pyplot as plt 

#membaca file data.csv
dataset = pd.read_csv('data.csv')
#Buat kolom baru yg bertipe datetime dalam format '%Y-%m'
dataset['order_month'] = dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
#Buat kolom GMV
dataset['gmv'] = dataset['item_price']*dataset['quantity']

dataset.groupby(['order_month','brand'])['gmv'].sum().unstack().plot()
plt.title('GMV Bulanan Tahun 2019 - Pengelompokan berdasarkan Merek', loc='center',pad=30, fontsize=10, color='blue')
plt.xlabel('Bulan Pemesanan', fontsize=15)
plt.ylabel('Jumlah Total (dalam Miliaran)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.legend(loc='right', bbox_to_anchor=(1.6, 0.5), shadow=True, ncol=2)
plt.gcf().set_size_inches(12, 5)
plt.tight_layout()
plt.savefig('monthly_gmv.png', quality=95)
plt.show()