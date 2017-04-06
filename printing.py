import reports
import pprint
import os.path


default_data_dict = {'data_file': 'game_stat.txt', 'year': '1999',
                     'genre': 'Action-adventure', 'title': 'Minecraft'}


def data_input_dict():
    import_name = input('Please give me the name of the data file: ')
    file_exist = 0
    while file_exist == 0:
        if not os.path.exists(import_name):
            import_name = input('File does not exist, try again: ')
        else:
            file_exist = 1
    given_year = input("Give me a year and I'll check if it is in the data file: ")
    given_genre = input("Give me the genre I'll tell you how many is in the data file: ")
    given_title = input("Give me the title I'll tell you which line it is in: ")
    data_dict = {'data_file': import_name, 'year': given_year,
                 'genre': given_genre, 'title': given_title}
    return data_dict


def printer(data_dict=default_data_dict):
    pp = pprint.PrettyPrinter(indent=1, width=150, depth=None, stream=None)
    pp.pprint(reports.count_games(data_dict['data_file']))
    pp.pprint(reports.decide(data_dict['data_file'], data_dict['year']))
    pp.pprint(reports.get_latest(data_dict['data_file']))
    pp.pprint(reports.count_by_genre(data_dict['data_file'], data_dict['genre']))
    pp.pprint(reports.get_line_number_by_title(data_dict['data_file'], data_dict['title']))
    pp.pprint(reports.sort_abc(data_dict['data_file']))
    pp.pprint(reports.get_genres(data_dict['data_file']))
    pp.pprint(reports.when_was_top_sold_fps(data_dict['data_file']))


def print_answers(data_dict):
    try:
        reports.get_line_number_by_title(data_dict['data_file'], data_dict['title'])
        printer(data_dict)
    except ValueError:
        print('The given title does not exist, please try again: ')
        data_dict['title'] = input("Give me the title I'll tell you which line it is in: ")
        print_answers(data_dict)


def main():
    print_answers(data_input_dict())


if __name__ == '__main__':
    main()
