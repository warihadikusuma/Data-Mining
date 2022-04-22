# -*- coding: utf-8 -*-
"""DecisionTree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JeQZ3BKWEsBXU8jP9WL5h2h_6pGsU5OZ
"""

#Import Library Scikit Learn untuk Decision Tree, Dataset & Matplotlit
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
import matplotlib.pyplot as plt

#Load Dataset Iris dari library scikit learn
iris = datasets. load_iris ()
features = iris['data']
target = iris ['target']
print(features)
len(features)

# Membuat Objek Model Decision Tree
decisiontree = DecisionTreeClassifier (random_state=0, max_depth=None,
min_samples_split=2, min_samples_leaf=1,
min_weight_fraction_leaf=0,
max_leaf_nodes=None,
min_impurity_decrease=0)

#Mentraining Model Decision Tree
model = decisiontree. fit (features, target)

#Mengambil sampel observasi dan membuat prediksi
#Sampel berupa data dimensi kelopak
#Fungsi predict () => memeriksa kelas yang dimilikinya
#Fungsi predict_proba() =>memeriksa probabilitas kelas dari prediksi tersebut
observation = [[5, 4, 3, 2]]
model.predict (observation)
model.predict_proba(observation)

#Membuat grafik visualisasi Decision Tree
import pydotplus
from sklearn import tree
dot_data = tree.export_graphviz(decisiontree, out_file=None, 
feature_names=iris['feature_names'], 
class_names=iris['target_names'])
from IPython.display import Image
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
graph.write_png('iris.png')