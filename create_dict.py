import pandas as pd
import re
import pickle
import os

if not os.path.exists('modules/weight/'):
    os.makedirs('modules/weight/')

num_word = 1
dict_filename = 'modules/weight/single_word_dict.pkl'
data =  pd.read_excel('Danh sách các Trung tâm Kiểm nghiệm_13072021.xlsx', sheet_name='Sheet1')

names = data['TÊN CẦN HIỂN THỊ'].tolist()
other_names = data['Tên khác'].tolist()

name_db = open("modules/weight/name_db.txt", "w")
# write to database
for name in names:
    name_db.write(name + "\n")

for i, name in enumerate(names):
    names[i] = ' '.join([word for word in re.sub(r'[^\w\s]', '', name.lower()).split(' ') if word])
for i, name in enumerate(other_names):
    if isinstance(name, str):
        other_names[i] = ' '.join([word for word in re.sub(r'[^\w\s]', '', name.lower()).split(' ') if word])

# get words split
word_set = set()
# for main name
for name in names:
    words_in_name = name.split(' ')
    for i in range(len(words_in_name)):
        word_set.add(' '.join(words_in_name[i:i+num_word]))

# for other/augment name
for name in other_names:
    if isinstance(name, str):
        words_in_name = name.split(' ')
        for i in range(len(words_in_name)):
            word_set.add(' '.join(words_in_name[i:i+num_word]))

# get words dictionary
word_dict = dict()
for word in word_set:
    for i, name in enumerate(names):
        if word in name:
            if word not in word_dict:
                word_dict[word] = []
            word_dict[word].append(i)
    for i, name in enumerate(other_names):
        if isinstance(name, str):
            if word in name:
                if word not in word_dict:
                    word_dict[word] = []
                word_dict[word].append(i)

dict_file = open(dict_filename, "wb")
pickle.dump(word_dict, dict_file)
