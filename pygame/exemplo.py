# importação de bibliotecas:
import numpy as np
import matplotlib.pyplot as plt
# gerando um banco de dados arbitrário:
np.random.seed(42)
ages = np.random.randint(low=15, high=70, size=40)
# classificando os dados de acordo com a idade:
labels = []
for age in ages:
    if age < 30:
        labels.append(0)
    else:
        labels.append(1)
# "bagunçando" os dados:
for i in range(0, 3):
    r = np.random.randint(0, len(labels) - 1)
    if labels[r] == 0:
        labels[r] = 1
    else:
        labels[r] = 0
# exibindo gráfico dos dados:
#plt.scatter(ages, labels, color="red")
#plt.show()