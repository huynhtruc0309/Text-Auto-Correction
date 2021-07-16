import pickle
import re
import collections

class AutoCorrecting(object):
    def __init__(self, dict_file, name_db):
        super(AutoCorrecting, self).__init__()
        f = open(dict_file, "rb")
        word_dict = pickle.load(f)
        self.word_dict = word_dict

        f = open(name_db, "r")
        self.name_database = f.read().split('\n')

    def __call__(self, name):
        indexes = []
        new_name = re.sub(r'[^\w\s]', '', name.lower()).split(' ')
        count = 0
        if len(new_name) <= 4:
            if ' '.join(new_name) == 'trung tâm kiểm nghiệm':
                return name
        for keyword in self.word_dict.keys():
            if keyword in new_name:
                indexes.extend(self.word_dict[keyword])
                count += 1
        if indexes:
            id_dict = collections.Counter(indexes)
            id_dict = dict(sorted(id_dict.items(), key=lambda item: item[1], reverse=True))
            return self.name_database[list(id_dict.keys())[0]]
        return name 