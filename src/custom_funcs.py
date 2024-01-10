import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
import math


colors = ['#dfdfde', '#a2798f', '#d7c6cf', '#8caba8', '#ebdada']


def grafico_barras(feature, label):

    plt.figure(figsize=(6,4))

    # Criar um gráfico de contagem (histograma)
    ax = sns.countplot(
        x=feature,
        hue = feature,
        legend=False,
        palette=colors)

    # Adicionar rótulos aos topos das barras
    for patch in ax.patches:
        height = patch.get_height()
        ax.text(patch.get_x() + patch.get_width() / 2, height + 0.1, str(int(height)), ha='center', va='bottom')
        
    # rótulo dos eixos
    plt.xlabel(label, fontsize=8)
    plt.ylabel('qtde', fontsize=8)

    # título do gráfico
    plt.title(f'Distribuição {label}', fontsize=12)

    # removendo as bordas
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # Ajusta layout para evitar sobreposição
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()


def grafico_distribuicao(feature):

    plt.hist(feature, bins=30, density=True, alpha=0.6, color='#d7c6cf')

    mu, sigma = np.mean(feature), np.std(feature)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    curva_normal = stats.norm.pdf(x, mu, sigma)

    plt.plot(x, curva_normal, 'r', color='#8caba8' ,label='Distribuição Normal')
    
    plt.xlabel('Valores')
    plt.ylabel('Densidade de Probabilidade')
    plt.title(f'Gráfico de Distribuição {feature.name} com Curva de Distribuição Normal')
    plt.legend()

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.tight_layout()

    plt.show()


def grafico_bloxpot(lista, data):

    fig, axes = plt.subplots(
        round(len(lista)/2),
        2,
        figsize=(10,8)
    )

    for i, numeric in enumerate(lista):
        if i%2 == 0:
            x = 0
        else:
            x = 1

        if i < 2:
            y = 0
        else:
            y = math.floor(i/2)

        axes[y, x].boxplot(data[numeric], showmeans=True, medianprops=dict(color = '#a2798f'))
        axes[y, x].set_title(f'Boxplot {numeric}')

        axes[y, x].spines['top'].set_visible(False)
        axes[y, x].spines['right'].set_visible(False)

        max_value = np.max(data[numeric])

        axes[y, x].annotate(f'Valor Máximo = {max_value}',
                            xy=(1,max_value),
                            xytext = (1.05, max_value),
                            bbox = dict(facecolor='#d7c6cf', edgecolor='#a2798f'),
                            fontsize = 8
                            )


    if i%2 == 0:
        axes[math.floor(i/2), 1].axis('off')

    plt.tight_layout()

    plt.show()
  


def get_stats(X, y):
    x_new = sm.add_constant(X)
    resultados = sm.GLM(y, x_new, family=sm.families.Poisson()).fit()
    print(resultados.summary())
    return resultados


def forward_regression(X, y):
    initial_list = []
    included = list(initial_list)
    while True:
        changed=False
        excluded = list(set(X.columns)-set(included))
        new_pval = pd.Series(index=excluded)
        for new_column in excluded:
            model = sm.GLM(y, sm.add_constant(pd.DataFrame(X[included+[new_column]])), family=sm.families.Poisson()).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < 0.05:
            best_feature = new_pval.idxmin()
            included.append(best_feature)
            changed=True

        if not changed:
            break

    return included


def feature_importance(model, X_train):

    feature_importances = model.feature_importances_
    feature_names = X_train.columns
    model_name = type(model).__name__

    plt.figure(figsize=(8, 6))
    plt.barh(range(len(feature_importances)), feature_importances, align='center')
    plt.yticks(np.arange(len(feature_names)), feature_names)

    plt.xlabel('Importância das Variáveis')
    plt.title(f'Importância das Variáveis no {model_name}')

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.show()