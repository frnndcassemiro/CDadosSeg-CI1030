from dataf import main
from sklearn import metrics
from sklearn.utils import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import label_binarize
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_score
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import scikitplot as skplt
import numpy as np
import warnings

# gerar  gráfico curvas roc
# def Roc(y_pred, y_test):
# 	skplt.metrics.plot_roc_curve(y_test, y_pred)
# 	plt.show()

def cross_v_train(x,y):
    floor = 0
    size = int(len(x) * 0.2)
    ceil = size
    prec, error, rforest_list = [], [], []
    for i in range(0,5):
        rforest = RandomForestClassifier(n_estimators=100)
        x_test = x[floor:ceil]
        x_train = x[:floor] + x[:ceil]

        y_test = y[floor:ceil]
        y_train = y[:floor] + y[:ceil]

        rforest.fit(x_train,y_train)
        y_pred = rforest.predict(x_train) 

        # Precisão
        p = precision_score(y_train, y_pred, average='micro')
        print("Precisão na pasta ",str(i),":",str(p))

        # Erro
        e = mean_absolute_error(y_train, y_pred)
        print("Erro na pasta ",str(i),":",str(e))

        prec.append(p)
        error.append(e)
        rforest_list.append(rforest)

        # Matriz de confusão
        cm = confusion_matrix(y_train, y_pred, labels = ['0','1','2','3','4','5','6','7','8'])
        print(cm)

        # Curvas ROC
        y_probs = rforest.predict_proba(x_train)
        # Roc(y_probs, y_train)
        skplt.metrics.plot_roc_curve(y_train,y_probs)
        n = "c_roc80_kfold_" + str(i) + ".png"
        plt.savefig(n)

        prec.append(p)

        floor = ceil
        ceil = ceil + size
        print('\n\n')

    max_precision = max(prec)
    index = prec.index(max_precision)
    rforest = rforest_list[index]
    return rforest, np.mean(prec), np.mean(error)

if __name__ == "__main__":
    
    warnings.filterwarnings("ignore")

    x, y = main()

    # Separar seu dataset em 2 porções (80% (train) e 20%(test))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1, stratify=y)

    # Um treinamento deve ser feito com a porção 1 do dataset (80%). Nesta porção, 
    # use divisão 80/20 (percentage split) para treino/teste
    size_train = int(len(x_train) * 0.8)
    # Configuração do algoritimo: n_estimators = 100 (quantidade de árvores de decisão usadas)
    rforest = RandomForestClassifier(n_estimators=100)
    rforest = rforest.fit(x_train[:size_train],y_train[:size_train])

    y_pred = rforest.predict(x_train[size_train:])
    # Precisão
    p = precision_score(y_train[size_train:], y_pred, average='micro')
    print("Precisão:",str(p))

    # Erro
    e = mean_absolute_error(y_train[size_train:], y_pred)
    print("Erro:",str(e))

    # Matriz de confusão
    cm = confusion_matrix(y_train[size_train:], y_pred, labels = ['0','1','2','3','4','5','6','7','8'])
    print(cm)

    # Curvas ROC
    y_probs = rforest.predict_proba(x_train[size_train:])
    # Roc(y_probs, y_train[size_train:])
    skplt.metrics.plot_roc_curve(y_train[size_train:],y_probs)
    plt.savefig("c_roc_modelo1.png")

    # Outro treinamento/teste deve ser feito usando validação cruzada com 5 pastas 
    # (k-fold cross validation com k = 5).
    rforest_cv, score, error = cross_v_train(x_train[:size_train],y_train[:size_train])
    print("Scores Médio teste K-fold: " + str(score), end='\n\n\n')

    # Utilizar a porção 2 do dataset (20%) como “dados de produção não-rotulados”,
    # Utilizar esses 20% para testar o primeiro modelo
    y_pred = rforest.predict(x_test)
    # Precisão
    p = precision_score(y_test, y_pred, average='micro')
    print("Precisão:",str(p))

    # Erro
    e = mean_absolute_error(y_test, y_pred)
    print("Erro:",str(e))

    # Matriz de confusão
    cm = confusion_matrix(y_test, y_pred, labels = ['0','1','2','3','4','5','6','7','8'])
    print(cm)

    # Curvas ROC
    y_probs = rforest.predict_proba(x_test)
    # Roc(y_probs, y_test)
    skplt.metrics.plot_roc_curve(y_test,y_probs)
    plt.savefig("c_roc20_modelo1.png")

    # Utilizar esses 20% para testar o melhor modelo entre os modelos KFold
    y_pred = rforest_cv.predict(x_test)
    # Precisão
    p = precision_score(y_test, y_pred, average='micro')
    print("Precisão:",str(p))

    # Erro
    e = mean_absolute_error(y_test, y_pred)
    print("Erro:",str(e))

    # Matriz de confusão
    cm = confusion_matrix(y_test, y_pred, labels = ['0','1','2','3','4','5','6','7','8'])
    print(cm)

    # Curvas ROC
    y_probs = rforest_cv.predict_proba(x_test)
    # Roc(y_probs, y_test)
    skplt.metrics.plot_roc_curve(y_test,y_probs)
    plt.savefig("c_roc20_kfold.png")

    # size_test = int(len(x_test) * 0.2)
    # floor = 0
    # ceil = size_test

    # for i in range(0, 5):
    #     y_pred = rforest_cv.predict(x_test[floor:ceil])
    #     # Precisão
    #     p = precision_score(y_test[floor:ceil], y_pred, average='micro')
    #     print("Precisão (teste 20%): "+ str(p))

    #     # Erro
    #     e = mean_absolute_error(y_test[floor:ceil], y_pred)
    #     print("Erro (teste 20%): " + str(e))

    #     # Matriz de Confusão
    #     print('Matriz de Confusão K-Fold' + str(i) + ':')
    #     cm = confusion_matrix(y_test[floor:ceil], y_pred, labels = ['0','1','2','3','4','5','6','7','8'])
    #     print(cm)

    #     #Curvas ROC
    #     y_probs = rforest_cv.predict_proba(x_test[floor:ceil])
    #     # Roc(y_probs, y_test[floor:ceil])
    #     skplt.metrics.plot_roc_curve(y_test[floor:ceil],y_probs)
    #     n = "c_roc20" + str(i) + ".png"
    #     plt.savefig(n)

    #     floor = ceil
    #     ceil = ceil + size_test		#do the cross-validation