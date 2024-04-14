import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Загрузим данные
data = pd.read_csv('network_traffic.csv')

# Преобразуем категориальные признаки в числовые с помощью one-hot encoding
data = pd.get_dummies(data, columns=['protocol', 'flags'])

# Отделим целевую переменную от признаков
X = data.drop(['timestamp', 'source_ip', 'destination_ip', 'threat'], axis=1)
y = data['threat']

# Разделим данные на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Инициализируем и обучим модель логистической регрессии
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Сохраняем обученную модель в файл 'model.pkl'
joblib.dump(model, 'model.pkl')

# Предскажем угрозы для тестового набора данных
y_pred = model.predict(X_test)

# Оценим точность модели
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Выведем отчет о классификации
print("Classification Report:")
print(classification_report(y_test, y_pred))
