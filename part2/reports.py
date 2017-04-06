def get_most_played(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        most_played_value = 0
        for item in data_list:
            if float(item[1]) > most_played_value:
                most_played_value = float(item[1])
                latest_game = item[0]
        return latest_game


def sum_sold(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        sum_sold_value = sum([float(item[1]) for item in data_list])
        return sum_sold_value


def get_selling_avg(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        sum_sold_value = sum([float(item[1]) for item in data_list])
        return (sum_sold_value / len(data_list))


def count_longest_title(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_games = [item[0] for item in data_list]
        return len(max(list_of_games, key=len))


def get_date_avg(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        sum_years = sum([int(item[2]) for item in data_list])
        return int(-(-sum_years // len(data_list)))


def get_game(file_name, title):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        for item in data_list:
            if item[0] == title:
                properties = item
        properties[1] = float(properties[1])
        properties[2] = int(properties[2])
        return properties


def count_grouped_by_genre(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        genre_dict = {}
        genres = [item[3] for item in data_list]
        for item in genres:
            if item in genre_dict:
                genre_dict[item] += 1
            else:
                genre_dict.update({item: 1})
        return genre_dict


def get_date_ordered(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        date_ordered = sorted(data_list, key=lambda game: game[2], reverse=True)
        for item in date_ordered:
            for i in range(len(date_ordered) - 1):
                if date_ordered[i][2] == date_ordered[i + 1][2]:
                    same_release = [date_ordered[i][0], date_ordered[i + 1][0]]
                    same_release.sort()
                    date_ordered[i][0] = same_release[0]
                    date_ordered[i + 1][0] = same_release[1]
        date_ordered_games = [item[0] for item in date_ordered]
        return date_ordered_games
