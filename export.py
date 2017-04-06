import reports
import os.path


default_data_dict = {'data_file': 'game_stat.txt', 'year': '1999',
                     'genre': 'Action-adventure', 'title': 'Minecraft', 'exported': 'answers.txt'}


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
    export_file_name = input('Please, give me the name of the export file of the answers: ')
    data_dict = {'data_file': import_name, 'year': given_year,
                 'genre': given_genre, 'title': given_title, 'exported': export_file_name}
    return data_dict


def top_sold_error(data_dict):
    try:
        top_sold = str(reports.when_was_top_sold_fps(data_dict['data_file']))
        return top_sold
    except:
        top_sold = 'There is not First-person shooter genre in the file!'
        return top_sold


def exporter(data_dict=default_data_dict):
    with open(data_dict['exported'], 'w') as file:
        file.write(str(reports.count_games(data_dict['data_file'])) + "\n" +
                   str(reports.decide(data_dict['data_file'], data_dict['year'])) + "\n" +
                   reports.get_latest(data_dict['data_file']) + "\n" +
                   str(reports.count_by_genre(data_dict['data_file'], data_dict['genre'])) + "\n" +
                   str(reports.get_line_number_by_title(data_dict['data_file'], data_dict['title'])) + "\n" +
                   str(reports.sort_abc(data_dict['data_file'])) + "\n" +
                   str(reports.get_genres(data_dict['data_file'])) + "\n" +
                   top_sold_error(data_dict))


def export_answers(data_dict):
    try:
        exporter(data_dict)
    except ValueError:
        print('The given title does not exist, please try again: ')
        data_dict['title'] = input("Give me the title I'll tell you which line it is in: ")
        export_answers(data_dict)
    except FileNotFoundError:
        data_dict['exported'] = "answers.txt"
        export_answers(data_dict)


def main():
    export_answers(data_input_dict())
    print("Export was successfull!")


if __name__ == '__main__':
    main()
