# Исследование надежности заемщиков
## Задача
Исследовать влияние различных признаков (семейное положение, количество детей, образование, доход, причина взятия кредита) на факт возврата кредита в срок.
## Проделанная работа
* Удалил дубликаты в исходных данных, заполнил пропуски в доходах клиентов медианным доходом среди клиентов того же типа деятельности и исправил данные в столбцах 'children' и 'education'.
* Распределил клиентов на 4 группы по целям взятия кредита, на 4 группы по количеству детей и на 3 группы по доходу
* Для каждой группы клиентов я посчитал процент должников.
## Выводы
- Бездетные и многодетные редко становятся должниками. Первые потому, что им меньше надо тратить, а вторые потому, что подходят к финансовым вопросам более осознанно. Родители одного или двух детей часто становятся должниками, потому что содержание ребенка требует внушительных средств
- Клиенты, которые были в браке значительно реже становятся должниками, чем те, которые не были. Видимо, жизнь в браке учит рассчитывать свои финансы наперед.
- Богатые берут в кредит более значительные суммы и поэтому тоже часто становятся должниками. Однако все же реже, чем бедняки, благодаря некоторой финансовой подушкой безопасности
- Чаще должниками становятся клиенты цели которых приобретение автомобиля и получение образования. Первые покупают автомобиль, несоразмерный своим доходам, а вторым тяжело совмещать работу и образование.
## Планируемая работа
1. С помощью машинного обучения выделить несколько групп клиентов, и вычислить платежоспособность каждой группы.
2. Построить модель, предсказывающую сможет ли клиент выплатить долг в срок.
## Используемые навыки и инструменты
1. Работа на Python в Jupiter Notebook с библиотекой Pandas.
2. Визуализация данных при помощи библиотек Matplotlib и Seaborn.
3. Обработка данных (работа с пропусками и дубликатами, категоризация, лемматизация).
