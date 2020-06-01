import pandas as pd

csv_file = pd.read_csv('zhanhuixinxi.csv', encoding='utf-8')
csv_file.to_excel('MyData.xlsx', sheet_name='data')
print('csv文件转换为xlsx文件')
