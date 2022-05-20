import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

pd.set_option('display.max_columns', None)  # para que la fila la imprima entera y no con ....
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
np.set_printoptions(suppress=True, linewidth=np.inf) # para que no me ponga exponenciales

# load dataset into Pandas DataFrame
df = pd.read_csv('europe.csv')

features = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
# Separating out the features
x = df.loc[:, features].values
# Separating out the target
y = df.Country.values

# Standardizing the features
x = StandardScaler().fit_transform(x)

pca = PCA()
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents[:, 0], index=y).T

print("Principal Components\n")
print(principalComponents)
print('\n')
print("Principal Components - First Component\n")
print(principalDf)
