# Данная программа создает модель машинного обучения, чтобы использовать информацию об опухолях, для того чтобы предсказать, является ли опухоль доброкачественной или злокачественной
# Здесь я импортирую необходимый датасет
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Здесь я загружаю необходимый набор данных
data = load_breast_cancer()

# Здесь происходит организация данных
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# Здесь я присваиваю отдельным переменным метки классов
print(label_names)
print('Class label = ', labels[0])
print(feature_names)
print(features[0])

# Здесь я организовываю импортированные данные в отдельные наборы для удобства
train, test, train_labels, test_labels = train_test_split(features,
                                                          labels,
                                                          test_size=0.33,
                                                          random_state=42)

# Здесь импортируется классификатор
gnb = GaussianNB()

# Здесь происходит само обучение
model = gnb.fit(train, train_labels)

# Здесь стоится прогноз
preds = gnb.predict(test)
print(preds)

# Здесь программа проверяет точность модели (чем она ближе к 1, тем точнее полученна модель)
print(accuracy_score(test_labels, preds))
