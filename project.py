import re
import pymorphy2

poems_file = 'stihi.rtf'
splitter = '///'
key_words = ['сон', 'ночь', 'луна', 'вечер', 'рассвет', 'закат', 'восход', 'заря', 'сумерки', 'день', 'зима', 'весна', 'лето', 'осень']

dict_of_counts = {}
normal_form_list = []
morph = pymorphy2.MorphAnalyzer()
with open(poems_file, 'r') as file:
    text = file.read()
    poems = text.split(splitter)

def match_key_word(word):
    parsed = morph.parse(word)
    tags = [item.tag.cyr_repr for item in parsed]
    filtered_index_arr = [i for i in range(len(tags)) if 'СУЩ' in tags[i]] 
    if not filtered_index_arr:
        return
    normal_form_of_word = parsed[filtered_index_arr[0]].normal_form
    normal_form_list.append(normal_form_of_word)


    for key_word in key_words:
        if key_word in normal_form_of_word:
            count = dict_of_counts.get(key_word, 0)
            count += 1
            dict_of_counts[key_word] = count
            return




words_list = []



for poem in poems:
    words_list.extend(re.split('\W+', poem))
for word in words_list:
    match_key_word(word)
print(dict_of_counts)

# Построение столбчатой диаграммы
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.bar(list(dict_of_counts.keys()), list(dict_of_counts.values()))

plt.show()

