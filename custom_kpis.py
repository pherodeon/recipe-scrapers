

import pandas as pd


output_base_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/"

# %% Data analysis
print('-' * 60 + '\n' + 'Performing data analysis')
sFileIn = output_base_folder + 'summary.csv'
df = pd.read_csv(sFileIn, sep=';', encoding='windows-1252')  # 'windows-1252')

"""
# Remove rows with sweets and desserts
s_flt = "almíbar|Batido|Brownie|Bizco|Cake|Caramel|Carbón|Chocolate|Coca|Dulce" + \
            "|Flan|Gallet|Gofre|Helado|Magdalena|Mermelada|Natilla|Navidad|Nocilla" + \
            "|Nugget|Palmer|Pan|Plumcake|Strudel|Sorbete|Tarta|Zumo"
# df_flt = df[df['Name'].str.contains(s_flt, case=False)==False]
# df_flt.to_csv(sFilePrefix + sFileIn + '_flt.csv', sep =';', encoding='windows-1252')

# df_flt_neg = df[df['Name'].str.contains(s_flt, case=False)==True]
# df_flt_neg.to_csv(sFilePrefix + sFileIn + '_flt_neg.csv', sep =';', encoding='windows-1252')
"""

fields = ['total_time', 'prep_time', 'cook_time']
for fld in fields:
    # remove outliers
    df = df[df[fld] < df[fld].quantile(.9)]
    # Remove rows with zeros:
    df = df[df[fld] > 0]

df.hist(column=fields, bins=40)

df.hist(column=fields, bins=range(0, 80, 5))

df.hist(column=fields, bins=40)

print('C''est fini!')