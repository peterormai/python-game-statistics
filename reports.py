def count_games(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        return len(data_list)


def decide(file_name, year):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        return bool(year in [int(item[2]) for item in data_list])


def get_latest(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        latest_year = 0
        for item in data_list:
            if int(item[2]) > latest_year:
                latest_year = int(item[2])
                latest_game = item[0]
        return latest_game


def count_by_genre(file_name, genre):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        quantity_of_genre = 0
        for item in data_list:
            if genre == item[3]:
                quantity_of_genre += 1
        return quantity_of_genre


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
        games.sort()
        return games


def get_genres(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        sorted_genres = sorted(set([item[3] for item in data_list]), key=str.lower)
        return list(sorted_genres)


def when_was_top_sold_fps(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_given_genre = [item for item in data_list if item[3] == 'First-person shooter']
        top_sold_amount = max([float(item[1]) for item in list_of_given_genre])
        top_sold_games_year = []
        for item in list_of_given_genre:
            if float(item[1]) == top_sold_amount:
                top_sold_games_year.append(int(item[2]))
        return min(top_sold_games_year)
        raise ValueError("Title doesn't exist!!")
