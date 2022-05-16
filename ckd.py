import streamlit as st

import pandas as pd

import plotly.express as px

df = pd.read_csv('israeli_data.csv')

param = df.drop(columns=[
  'shmmitzrach',
  'code', 
  'makor', 
  "ofen_hachana", 
  "ofen_hachanat_makor", 
  "smlmitzrach",
  "kvutza_meyuhedet",
  "shem_mitzrach_mekutzar"])

# for i in df.columns:
#   f'"{i}", '

ops = st.multiselect('פרמטרים נוספים', param.columns.to_list(), default=["food_energy","potassium","phosphorus","sodium"])
num = st.number_input('משקל המוצר בגרמים', 1, 1000, 100)

df_calc = df[ops]

'על ידי לחיצה על הטור למשל אשלגן (באפור ואנגלית) ניתן לעשות סידור של הערכים לפי גדול מ וקטן מ. כדי לראות רשימה של הערכים הגדולים הקטנים'


'אפשר להגדיל את הטבלה על ידי לחיצה על החיצים בצד ימין'

df = pd.concat([df['shmmitzrach'], (df_calc / 100 ) * int(num)], axis=1)

df

# st.plotly_chart(px.bar(df.iloc[:10, ], x='shmmitzrach', y=ops))












