# -*- coding: utf-8 -*-
"""Лабораторная работа NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cOg4AAtx12lYNiwuH6ZjHoY-fJHZBzRy

#Рассчитайте метрики TF-IDF для любых 10 песен на одном языке,которые вы сами выберите.Не забудьте,что нужно привести слова к начальной форме, убрать стоп-слова
"""

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# Загрузим список стоп-слов
nltk.download('stopwords')
from nltk.corpus import stopwords

# Замените text1 на вашу строковую переменную
texts = [
    "Белый снег, серый лед На растрескавшейся земле Одеялом лоскутным на ней Город в дорожной петле А над городом плывут облака Закрывая небесный свет А над городом желтый дым Городу две тысячи лет Прожитых под светом Звезды по имени Солнце И две тысячи лет война Война без особых причин Война дело молодых Лекарство против морщин Красная, красная кровь Через час уже просто земля Через два на ней цветы и трава Через три она снова жива И согрета лучами звезды По имени Солнце И мы знаем, что так было всегда Что судьбою больше любим Кто живет по законам другим И кому умирать молодым Он не помнит слово «Да» и слово «Нет» Он не помнит ни чинов, ни имен И способен дотянуться до звезд Не считая, что это сон И упасть, опаленным звездой По имени Солнце",
    "В наших глазах  Постой, не уходи! Мы ждали лета — пришла зима. Мы заходили в дома, Но в домах шел снег. Мы ждали завтрашний день, Каждый день ждали завтрашний день. Мы прячем глаза за шторами век.  В наших глазах крики «Вперед!» В наших глазах окрики «Стой!» В наших глазах рождение дн И смерть огня. В наших глазах звездная ночь, В наших глазах потерянный рай, В наших глазах закрытая дверь. Что тебе нужно? Выбирай!  Мы хотели пить, не было воды. Мы хотели света, не было звезды. Мы выходили под дождь И пили воду из луж. Мы хотели песен, не было слов. Мы хотели спать, не было снов. Мы носили траур, оркестр играл туш…  В наших глазах крики «Вперед!» В наших глазах окрики «Стой!» В наших глазах рождение дн И смерть огня. В наших глазах звездная ночь, В наших глазах потерянный рай, В наших глазах закрытая дверь. Что тебе нужно? Выбирай!",

  "Пустынной улицей вдвоем с тобой куда-то мы идем А я курю а ты конфетки ешь И светят фонари давно ты говоришь пойдешь в кино А я тебя зову м в кабак конечно припев: М-м-м-м-м восьмиклассница м-м-м-м-м  Ты говоришь что у тебя по географии трояк А мне на это просто наплевать Ты говоришь из-за тебя там кто-то получил синяк Многозначительно молчу и дальше мы идем гулять припев: М-м-м-м-м восьмиклассница м-м-м-м-м М-м-м-м-м восьмиклассница м-м-м-м-м  Мамина помада сапоги старшей сестры Нелегко с тобой, а ты гордишься мной Ты любишь своих кукол и воздушные шары Но в десять ровно мама ждет тебя домой. припев: М-м-м-м-м восьмиклассница М-м-м-м-м восьмиклассница М-м-м-м-м восьмиклассница М-м-м-м-м восьмиклассница  ",

   "Мне бы в небо  Руки,ноги,дэнс,голова бум бум бам Мои мозги похожи на кусок бабл гам, Можно жить так,но лучше ускориться, Я лично бухаю,а кто то колится.   Припев. Мне бы в небо,мне бы в небо. Здесь я был,а там я не был. Мне бы в небо,мне бы в небо. Здесь я был а там я не был.   Новые районы,дома как корабли. Хочешь жить,набивай кулаки. Кто то жрет таблетки,а кто то колется. Я лично бухаю,но могу ускориться.   Припев. Мне бы в небо,мне бы в небо. Здесь я был,а там я не был. Мне бы в небо,мне бы в небо. Здесь я был а там я не был.   Все это похоже на какую то разводку. Наркотики нельзя,но можно водку. Газеты и журналы печатают муру. Дельфин будет жить,а я умру.   Припев. Мне бы в небо,мне бы в небо. Здесь я был,а там я не был. Мне бы в небо,мне бы в небо. Здесь я был а там я не был.   Путевка в небо достается очень быстро. Вышел на улицу,случайный выстрел. Можно ждать его,но лучше ускорится. Я лично бухаю,а кто то колется.   Припев. Мне бы в небо,мне бы в небо. Здесь я был,а там я не был. Мне бы в небо,мне бы в небо. Здесь я был а там я не был.  Мне бы в небо,мне бы в небо. Здесь я был,а там я не был. Мне бы в небо,мне бы в небо. Здесь я был а там я не был.  ",

   "Ни кого не жалко  Все Мы геpои фильмов пpо войнy Или пpо пеpвый полёт на лyнy Или пpо жизнь одиноких сеpдец У каждого фильма свой конец   Hикого не жалко никого Hи тебя ни меня ни его Hикого не жалко никого Hи тебя ни меня ни его   Hет дpyзей и нет пpиятелей Hет вpагов и нет пpедателей Многим из нас yже жить не хочется Все мы дpочим или дpочимся  Hикого не жалко никого Hи тебя ни меня ни его Hикого не жалко никого Hи тебя ни меня ни его ",

   " Пожалуйста не умирай, или мне придется тоже... Ты конечно сразу в рай, а я не думаю, что тоже... Ты конечно сразу в рай, А я не думаю, что тоже...  Хочешь сладких апельсинов, Хочешь вслух рассказов длинных, Хочешь, я взорву все звезды, что мешают спать... Пожалуйста, только живи, Ты же видишь, я живу тобой.... Моей огромной любви хватит нам двоим с головою...  Хочешь - в море с парусами, Хочешь - музык новых самых, Хочешь, я убью соседей, что мешают спать...  Хочешь - солнце вместо лампы, Хочешь за окошком Альпы, Хочешь я отдам все песни, Про тебя отдам все песни...  ",

"Мы разбиваемся  Мы разбегаемся по делам Земля разбивается пополам Сотри меня, смотри в меня Останься Прости меня за слабость И за то, что я так странно и отчаянно люблю  Вздох сожаления на губах Зависли в неправильных городах Звонки телефонные под луной Границы условные Я с тобой Сотри, смотри в меня Останься Прости меня за слабость И за то, что я так странно и отчаянно люблю  Мы разбегаемся по делам Земля разбивается пополам Вздох сожаления на губах Зависли в неправильных городах Звонки телефонные под луной Границы условные Я с тобой Мы разбегаемся по делам Земля разбивается пополам Мы разбегаемся Земля разбивается Мы разбиваемся  ",

  "Австралия  Расскажи мне про Австралию, Мне безумно интересно! Может, в этом самом месте, Я решусь и брошу якорь. И в беседах с океаном, Под дождем или под планом Мне откроются секреты, Я пойму и стану легче. И прозрачными руками Подниму себя за плечи. Расскажи мне про Австралию.  Поболтаем об иронии, Мне безумно интересно! Это глупо или честно? Я рискну и встану ближе.. Твои запахи смущают, Их названий я не знаю.. Я вобще тебя не знаю.. Ты меня впервые видишь, Я заранее прощаю, Ты напротив - ненавидишь. Поболтаем об иронии.  Расскажи мне про Австралию- Мне безумно интересно...интересно..  ",

 "Кукла Колдуна  Тёмный, мрачный коридор, Я на цыпочках, как вор, Пробираюсь, чуть дыша, Чтобы не спугнуть Тех, кто спит уже давно, Тех, кому не всё равно, В чью я комнату тайком Желаю заглянуть, Чтобы увидеть...Как бессонница в час ночной Меняет, нелюдимая, облик твой, Чьих невольница ты идей? Зачем тебе охотиться на людей? Крестик на моей груди, На него ты погляди, Что в тебе способен он Резко изменить? Много книжек я читал, Много фокусов видал, Свою тайну от меня Не пытайся скрыть! Я это видел! Как бессонница в час ночной Меняет, нелюдимая, облик твой, Чьих невольница ты идей? Зачем тебе охотиться на людей? Очень жаль, что ты тогда Мне поверить не смогла, В то, что новый твой приятель Не такой, как все! Ты осталась с ним вдвоём, Не зная ничего о нём. Что для всех опасен он, Наплевать тебе! И ты попала! К настоящему колдуну, Он загубил таких, как ты, не одну! Словно куклой и в час ночной Теперь он может управлять тобой! Всё происходит, будто в страшном сне. И находиться здесь опасно мне!  ",

   "Проклятый старый дом  1.В заросшем парке Стоит старинный дом - Забиты окна, И мрак царит извечно в нем.   Сказать я пытался: Чудовищ нет на земле. Hо тут же раздался Ужасный голос во мгле. Голос во мгле...   Припев: Мне больно видеть белый свет, Мне лучше в полной темноте. Я очень много-много лет Мечтаю только о еде.   Мне слишком тесно взаперти, И я мечтаю об одном: Скорей свободу обрести, Прогрызть свой ветхий старый дом. Проклятый старый дом!..    2.Был дед, да помер Слепой и жутко злой, Никто не вспомнил О нем с зимы холодной той. Соседи не стали Его тогда хоронить. Лишь доски достали, Решили заколотить Двери и окна...   Припев   И это место стороной Обходит сельский люд. И суеверные твердят: Там призраки живут."
]

text1 = texts[1]
print(len(texts))


nltk.download('punkt')

for x in texts:
      text1 = x
      # Разбейте текст на слова (токены) и удалите стоп-слова
      nltk_tokens = nltk.word_tokenize(text1)
      nltk_tokens = [word.lower() for word in nltk_tokens if word.isalnum()]
      filtered_tokens = [word for word in nltk_tokens if word not in stopwords.words('russian')]

      # Преобразуйте список слов обратно в строку
      filtered_text = ' '.join(filtered_tokens)

      # Создайте матрицу TF-IDF
      tfidf_vectorizer = TfidfVectorizer()
      tfidf_matrix = tfidf_vectorizer.fit_transform([filtered_text])

      # Преобразуйте матрицу TF-IDF в массив
      tfidf_array = tfidf_matrix.toarray()

      # Выведите результаты
      print(tfidf_array)

"""#"""



"""# Цель этого задания - использовать предварительно

обученную модель BERT для классификации тональности отзывов на фильмы.
- Скачайте датасет отзывов на фильмы. Датасет содержит
текст отзыва и бинарную метку тональности (положительный/отрицательный).
- Используйте библиотеку Hugging Face для загрузки предварительно обученной
модели BERT и токенизатора.
- Подготовьте данные: используйте токенизатор BERT для преобразования
текстовых данных в формат, который можно подать на вход модели BERT.
- Создайте классификатор на основе BERT: это может быть модель BERT с одним линейным слоем для классификации на вершине.
- Обучите классификатор на данных обучения и оцените его
производительность на данных для тестирования.
"""

from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/My Drive/content/Copy of IMDB Dataset.csv'
import pandas as pd


# Чтение CSV файла с использованием pandas
df = pd.read_csv(file_path)

df

import torch
!pip install transformers
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, Dataset, RandomSampler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

# Разделите данные на обучающий и тестовый наборы
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Загрузка предварительно обученного токенизатора и модели BERT
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
model.classifier = torch.nn.Linear(in_features=model.config.hidden_size, out_features=2)

# Оптимизатор и функция потерь
optimizer = AdamW(model.parameters(), lr=1e-5)
loss_fn = torch.nn.CrossEntropyLoss()

# Класс Dataset для загрузки данных
class IMDbDataset(Dataset):
    def __init__(self, text, labels, tokenizer, max_length):
        self.text = text
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.text)

    def __getitem__(self, idx):
        text = str(self.text.iloc[idx])
        label = int(self.labels.iloc[idx])
        encoding = self.tokenizer(
            text,
            add_special_tokens=True,
            truncation=True,
            max_length=self.max_length,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt'
        )
        return {
            'text': text,
            'labels': label,
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten()
        }

# Создание DataLoader для обучающего и тестового наборов
train_dataset = IMDbDataset(train_df['review'], train_df['sentiment'], tokenizer, max_length=128)
test_dataset = IMDbDataset(test_df['review'], test_df['sentiment'], tokenizer, max_length=128)

train_data_loader = DataLoader(train_dataset, batch_size=32, sampler=RandomSampler(train_dataset))
test_data_loader = DataLoader(test_dataset, batch_size=32)

# Обучение модели
model.train()

num_epochs = 3  # Выберите желаемое количество эпох

for epoch in range(num_epochs):
    for batch in train_data_loader:
        inputs = tokenizer(batch['text'], return_tensors='pt', padding=True, truncation=True)
        labels = batch['labels']

        optimizer.zero_grad()
        outputs = model(**inputs)
        logits = outputs.logits
        loss = loss_fn(logits, labels)
        loss.backward()
        optimizer.step()

# Оценка производительности модели
model.eval()
y_true = []
y_pred = []

with torch.no_grad():
    for batch in test_data_loader:
        inputs = tokenizer(batch['text'], return_tensors='pt', padding=True, truncation=True)
        labels = batch['labels']

        outputs = model(**inputs)
        logits = outputs.logits
        predicted_labels = torch.argmax(logits, dim=1)

        y_true.extend(labels.tolist())
        y_pred.extend(predicted_labels.tolist())

accuracy = accuracy_score(y_true, y_pred)
classification_rep = classification_report(y_true, y_pred, target_names=['negative', 'positive'])

print(f"Accuracy: {accuracy}")
print(classification_rep)