import seaborn as sns
import matplotlib.pyplot as plt

datos = pd.read_csv('datos.csv')        

# Grafico de dispersion
sns.scatterplot(x='edad', y='peso', data=datos)
plt.show()

# Grafico de dispersion con color por genero
sns.scatterplot(x='edad', y='peso', data=datos, hue='genero')
plt.show()

# Grafico de dispersion con color por genero y tamaño por peso
sns.scatterplot(x='edad', y='peso', data=datos, hue='genero', size='peso')
plt.show()

