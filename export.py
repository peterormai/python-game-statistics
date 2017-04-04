import reports

# filename="answers.txt"


def data_input():
    import_name = input('Please give me the name of the data file: ')
    given_year = input("Give me a year an I'll check if it is in the data file: ")
    given_genre = input("Give me the genre I'll tell you how many is in the data file: ")
    given_title = input("Give me the title I'll tell you which line it is in: ")
    export_file_name = input('Please, give me the name of the export file of the answers: ')
    data_input_dict = {'data_file': import_name, 'year': given_year,
                       'genre': given_genre, 'title': given_title, 'exported': export_file_name}
    return data_input_dict


def export_answers(data_dict):
    with open(data_dict['exported'], 'w') as file:
        file.write(str(reports.count_games(data_dict['data_file'])) + "\n" +
                   str(reports.decide(data_dict['data_file'], data_dict['year'])) + "\n" +
                   reports.get_latest(data_dict['data_file']) + "\n" +
                   str(reports.count_by_genre(data_dict['data_file'], data_dict['genre'])) + "\n" +
                   str(reports.get_line_number_by_title(data_dict['data_file'], data_dict['title'])) + "\n" +
                   str(reports.sort_abc(data_dict['data_file'])) + "\n" +
                   str(reports.get_genres(data_dict['data_file'])) + "\n" +
                   str(reports.when_was_top_sold_fps(data_dict['data_file'])))


def main():
    export_answers(data_input())
    print("Export was successfull!")


if __name__ == '__main__':
    main()
