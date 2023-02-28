import pandas as pd

def transform_data(filename):
   datos = pd.read_csv(f'./static/files/{filename}')
   name = filename.split('.')[0]
   datos.groupby('region').size().to_csv(f'./static/transformed_files/{name}_transformed.csv')