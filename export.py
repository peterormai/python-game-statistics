import reports


def export_answers(filename="answers.txt"):
    with open(filename, 'w') as file:
        file.write(str(reports.count_games('game_stat.txt')) + "\n" +
                   str(reports.decide('game_stat.txt', 1999)) + "\n" +
                   reports.get_latest('game_stat.txt') + "\n" +
                   str(reports.count_by_genre('game_stat.txt', 'Survival game')) + "\n" +
                   str(reports.get_line_number_by_title('game_stat.txt', 'World of Warcraft')) + "\n" +
                   str(reports.sort_abc('game_stat.txt')) + "\n" +
                   str(reports.get_genres('game_stat.txt')) + "\n" +
                   str(reports.when_was_top_sold_fps('game_stat.txt')))


export_answers()
