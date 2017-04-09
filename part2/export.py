import reports
import os.path


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
    given_title = input("Give me a title to get every properties of it: ")
    title_valid = 1
    while title_valid:
        try:
            title_name = str(reports.get_game(data_file, given_title))
            title_valid = 0
        except UnboundLocalError:
            given_title = input('The given title does not exist, please try again: ')
            continue
    return title_name


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
             reports.get_most_played(data_file),
             str(reports.sum_sold(data_file)),
             str(round(reports.get_selling_avg(data_file), 2)),
             str(reports.count_longest_title(data_file)),
             str(reports.get_date_avg(data_file)),
             title_input(data_file),
             str(reports.count_grouped_by_genre(data_file)),
             str(reports.get_date_ordered(data_file)))
    print("Export was successfull!")


if __name__ == '__main__':
    main(data_input_name())
