"""
Questao 1:
    Tecnica estatistica e de aprendizado de maquina utilizada para simplificar conjuntos de dados complexos 
com muitas variáveis, transformando-os em um conjunto menor de novas variáveis, chamadas de componentes 
principais, sem perder a maior parte da informação original

Questao 2:
    O modelo indica fraudes com alta precisão, porém possui o recall eh baixo, ou seja, ele 
deixa passar muitas fraudes reais. Para um sistema de detecção bancária, permitir passar fraudes
pode causar serios problemas

Questao 3:
    Essa causa provavelmnete é um problema de overfitting, pois ele está decorando dados no 
treinamento, o que faz com que a acurácia seja alta, porém no teste real onde há dados diferentes,
ele não possui boa nota de acurácia poiw ele está apenas decorando os dados, não aprendendo a 
lidar com eles realmente. Para correção é possível aplicar técnincas de Redução de 
dimensionalidade com PCA, regularização e mais dados ou validação cruzada.

Questão 4:
    Ambos são recomendados pois oferecem um ótimo desempenho, integração com pipelines de machine
learnig, e código mais confiavel

"""