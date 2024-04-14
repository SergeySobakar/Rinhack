import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Загрузим обученную модель из файла
model = joblib.load('model.pkl')

# Загрузим данные
new_data = pd.read_csv('learn_traffic.csv')

# Преобразуем категориальные признаки в числовые с помощью one-hot encoding
new_data = pd.get_dummies(new_data, columns=['protocol', 'flags'])

# Отделим целевую переменную от признаков
X_new = new_data.drop(
    ['timestamp', 'source_ip', 'destination_ip', 'threat'], axis=1)
y_new = new_data['threat']

# Предскажем угрозы для новых данных
y_pred_new = model.predict(X_new)

data = pd.read_csv("learn_traffic.csv")
data["is_danger"] = False
data["is_danger"][data["threat"] != "Normal"] = True
# Оценим точность модели на новых данных
accuracy_new = accuracy_score(y_new, y_pred_new)
print("Accuracy on new data:", accuracy_new)

# Выведем отчет о классификации на новых данных
print("Classification Report on new data:")
print(classification_report(y_new, y_pred_new))

# Сохраним данные в новый файл CSV с дополнительным столбцом is_danger
new_data.to_csv('learn_traffic_with_is_danger.csv', index=False)
data.to_csv("learn_traffic_update.csv")
