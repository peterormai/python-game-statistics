import reports
import os.path


def data_input_name():
    import_name = input('Please, give me the name of the data file: ')
    return import_name


def title_input(data_file):
    given_title = input("Give me the title I'll tell you which line it is in: ")
    title_valid = 1
    while title_valid:
        try:
            title_name = str(reports.get_line_number_by_title(data_file, given_title))
            title_valid = 0
        except ValueError:
            given_title = input('The given title does not exist, please try again: ')
            continue
    return title_name


def year_input(data_file):
    try:
        given_year = input("Give me a year and I'll check if it is in the data file: ")
        chosen_year = str(reports.decide(data_file, int(given_year)))
    except ValueError:
        chosen_year = 'The given year was not a number!'
    return chosen_year


def genre_input(data_file):
    given_genre = input("Give me the genre I'll tell you how many is in the data file: ")
    chosen_genre = str(reports.count_by_genre(data_file, given_genre))
    return chosen_genre


def top_sold_handler(data_file):
    try:
        top_sold = str(reports.when_was_top_sold_fps(data_file))
    except:
        top_sold = 'There isn\'t First-person shooter genre in the file!'
    return top_sold


def printer(*args):
    print("\n")
    for item in args:
        print(item)


def main(data_file):
    os.system('clear')
    printer(str(reports.count_games(data_file)),
            year_input(data_file),
            reports.get_latest(data_file),
            genre_input(data_file),
            title_input(data_file),
            str(reports.sort_abc(data_file)),
            str(reports.get_genres(data_file)),
            top_sold_handler(data_file))


if __name__ == '__main__':
    os.system('clear')
    import_valid = 1
    while import_valid:
        try:
            main(data_input_name())
            import_valid = 0
        except FileNotFoundError:
            print('File does not exist, try again!')
            continue
