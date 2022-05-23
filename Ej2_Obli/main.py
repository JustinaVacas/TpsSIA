import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import plotly.express as px

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
principalComponents = pca.fit_transform(x)                              # tira los componentes principales
principalDf = pd.DataFrame(data=principalComponents[:, 0], index=y).T   # tira el primero de los componentes principales

print("Principal Components\n")
print(principalComponents)
print('\n')
print("Principal Components - First Component\n")
print(principalDf)
print('\n')
print("Varianza acumulada\n")
print(pca.explained_variance_ratio_.cumsum())

loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

fig = px.scatter(principalComponents, x=0, y=1, color=df['Country'])

for i, feature in enumerate(features):
    fig.add_shape(
        type='line',
        x0=0, y0=0,
        x1=loadings[i, 0],
        y1=loadings[i, 1]
    )
    fig.add_annotation(
        x=loadings[i, 0],
        y=loadings[i, 1],
        ax=0, ay=0,
        xanchor="center",
        yanchor="bottom",
        text=feature,
    )

    fig.update_xaxes(dict(
        title=f'PCA 1 - variance {pca.explained_variance_ratio_[0] * 100:.2f}%',
    ))

    fig.update_yaxes(dict(
        title=f'PCA 2 - variance {pca.explained_variance_ratio_[1] * 100:.2f}%'
    ))

fig.show()