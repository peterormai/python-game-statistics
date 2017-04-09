import reports
import os.path

# teszt


def data_input_name():
    import_name = input('Please, give me the name of the data file: ')
    file_exist = 0
    while file_exist == 0:
        if not os.path.exists(import_name) or import_name == '.':
            import_name = input('File does not exist, try again: ')
        else:
            file_exist = 1
    return import_name


def export_name():
    export_file_name = input('Please, give me the name of the export file of the answers: ')
    return export_file_name


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


def exporter(export_file_name, *args):
    export_name_valid = 1
    while export_name_valid:
        try:
            with open(export_file_name, 'w') as file:
                for item in args:
                    file.write(item + "\n")
            export_name_valid = 0
        except FileNotFoundError:
            export_file_name = 'answers.txt'
            continue


def main(data_file):
    os.system('clear')
    exporter(export_name(),
             str(reports.count_games(data_file)),
             year_input(data_file),
             reports.get_latest(data_file),
             genre_input(data_file),
             title_input(data_file),
             str(reports.sort_abc(data_file)),
             str(reports.get_genres(data_file)),
             top_sold_handler(data_file))
    print("Export was successfull!")


if __name__ == '__main__':
    main(data_input_name())
