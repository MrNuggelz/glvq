"""
========================================
Generalized Learning Vector Quantization
========================================
This example shows how GLVQ classifies.
The plot shows the target class of each data point
(big circle) and which class was predicted (smaller circle). It also
shows the prototypes (black diamond) and their labels (small point inside the diamond).

"""
import numpy as np
import matplotlib.pyplot as plt

from glvq import GlvqModel

print(__doc__)

nb_ppc = 100
print('GLVQ:')
toy_data = np.append(
    np.random.multivariate_normal([0, 0], np.eye(2) / 2, size=nb_ppc),
    np.random.multivariate_normal([5, 0], np.eye(2) / 2, size=nb_ppc), axis=0)
toy_label = np.append(np.zeros(nb_ppc), np.ones(nb_ppc), axis=0)

glvq = GlvqModel()
glvq.fit(toy_data, toy_label)
pred = glvq.predict(toy_data)

plt.scatter(toy_data[:, 0], toy_data[:, 1], c=toy_label)
plt.scatter(toy_data[:, 0], toy_data[:, 1], c=pred, marker='.')
plt.scatter(glvq.w_[:, 0], glvq.w_[:, 1])
plt.axis('equal')

print('classification accuracy:', glvq.score(toy_data, toy_label))
plt.show()
