def count_games(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        return len(data_list)


def decide(file_name, year):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        return bool(year in i for i in data_list)


def get_latest(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        counter = int(max([item[2] for item in data_list]))
        for item in data_list:
            if int(item[2]) == counter:
                return item[0]


def count_by_genre(file_name, genre):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        quantity = 0
        for item in data_list:
            if genre == item[3]:
                quantity += 1
        return quantity


def get_line_number_by_title(file_name, title):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        for i in range(len(data_list)):
            if title == data_list[i][0]:
                return i + 1
        raise ValueError("Title doesn't exist!!")


def sort_abc(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        games = [item[0] for item in data_list]
        return sorted(games)


def get_genres(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        new = sorted(set([item[3] for item in data_list]), key=str.lower)
        return list(new)


def when_was_top_sold_fps(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        collect = []
        for i in range(len(data_list)):
            if data_list[i][3] == 'First-person shooter':
                collect.append(data_list[i])
        counter = float(max([item[1] for item in data_list]))
        for item in collect:
            if float(item[1]) == counter:
                return int(item[2])
        raise ValueError("Title doesn't exist!!")
