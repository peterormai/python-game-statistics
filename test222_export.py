import reports
import os.path


def data_input_name():
    import_name = input('Please give me the name of the data file: ')
    file_exist = 0
    while file_exist == 0:
        if not os.path.exists(import_name):
            import_name = input('File does not exist, try again: ')
        else:
            file_exist = 1
    return import_name


def export_name():
    export_file_name = input('Please, give me the name of the export file of the answers: ')
    return export_file_name


def title_input(data_file):
    given_title = input("Give me the title I'll tell you which line it is in: ")
    title_name = str(reports.get_line_number_by_title(data_file, given_title))
    return title_name


def year_input(data_file):
    given_year = input("Give me a year and I'll check if it is in the data file: ")
    chosen_year = str(reports.decide(data_file, int(given_year)))
    return chosen_year


def exporter(export_file_name, *args):
    with open(export_file_name, 'w') as file:
        for i in args:
            file.write(i + "\n")

        #    str(reports.sum_sold(data_dict['data_file'])) + "\n" +
        #    str(reports.get_selling_avg(data_dict['data_file'])) + "\n" +
        #    str(reports.count_longest_title(data_dict['data_file'])) + "\n" +
        #    str(reports.get_date_avg(data_dict['data_file'])) + "\n" +
        #    str(reports.get_game(data_dict['data_file'], data_dict['title'])) + "\n" +
        #    str(reports.count_grouped_by_genre(data_dict['data_file'])) + "\n" +
        #    str(reports.get_date_ordered(data_dict['data_file'])))


def main():
    exporter(export_name(), title_input(data_input_name()), year_input(data_input_name()))


if __name__ == '__main__':
    main()
