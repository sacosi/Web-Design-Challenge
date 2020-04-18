import pandas as pd

filePath=('Resources/cities.csv')

data_df=pd.read_csv(filePath)

data_html=data_df.to_html(index=False,border=0, justify='left', col_space=100)

text_file = open("data_pandas.html", "w")
text_file.write(data_html)
text_file.close()

