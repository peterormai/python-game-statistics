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
        sum_sold_value = 0
        for item in data_list:
            sum_sold_value += float(item[1])
        return sum_sold_value


def get_selling_avg(file_name):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        sum_sold_value = 0
        number_of_games = 0
        for item in data_list:
            sum_sold_value += float(item[1])
            number_of_games += 1
        return (sum_sold_value / number_of_games)


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
        sum_years = 0
        number_of_games = 0
        for item in data_list:
            sum_years += float(item[2])
            number_of_games += 1
        return int(-(-sum_years // number_of_games))


def get_game(file_name, title):
    with open(file_name) as data:
        data_list = data.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        properties = [item for item in data_list if item[0] == title]
        pro_list = properties[0]
        pro_list[1] = float(pro_list[1])
        pro_list[2] = int(pro_list[2])
        return pro_list

        # propertiest megcsinálni h ne listában lista legyne


print(get_game('game_stat.txt', 'Minecraft'))
