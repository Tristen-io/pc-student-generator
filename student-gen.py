import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

pathway= os.getenv('PATHWAY')

df = pd.read_csv(pathway)

pc_names = []

for index, row in df.iterrows():
    first_name, last_name = row['name'].split()

    pc_name = f'pc-{row["pod"]}-{first_name}-{last_name}'

    pc_names.append(pc_name)

pc_df = pd.DataFrame(pc_names, columns=['pc_name'])

pc_df.to_csv('pc-channel-names.csv', index=False)

