import reports
import os.path


default_data_dict = {'data_file': 'game_stat.txt', 'title': 'Minecraft', 'exported': 'answers.txt'}


def data_input_dict():
    import_name = input('Please give me the name of the data file: ')
    file_exist = 0
    while file_exist == 0:
        if not os.path.exists(import_name):
            import_name = input('File does not exist, try again: ')
        else:
            file_exist = 1
    given_title = input("Give me a title to get every properties of it: ")
    export_file_name = input('Please, give me the name of the export file of the answers: ')
    data_dict = {'data_file': import_name, 'title': given_title, 'exported': export_file_name}
    return data_dict


def exporter(data_dict):
    with open(data_dict['exported'], 'w') as file:
        file.write(reports.get_most_played(data_dict['data_file']) + "\n" +
                   str(reports.sum_sold(data_dict['data_file'])) + "\n" +
                   str(reports.get_selling_avg(data_dict['data_file'])) + "\n" +
                   str(reports.count_longest_title(data_dict['data_file'])) + "\n" +
                   str(reports.get_date_avg(data_dict['data_file'])) + "\n" +
                   str(reports.get_game(data_dict['data_file'], data_dict['title'])) + "\n" +
                   str(reports.count_grouped_by_genre(data_dict['data_file'])) + "\n" +
                   str(reports.get_date_ordered(data_dict['data_file'])))


def export_answers(data_dict=default_data_dict):
    try:
        exporter(data_dict)
        print("Export was successfull!")
    except UnboundLocalError:
        data_dict['title'] = default_data_dict['title']
        export_answers(data_dict)
    except FileNotFoundError:
        data_dict['exported'] = default_data_dict['exported']
        export_answers(data_dict)


def main():
    export_answers(data_input_dict())


if __name__ == '__main__':
    main()
