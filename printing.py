import reports
import pprint


def main():
    pp = pprint.PrettyPrinter(indent=1, width=150, depth=None, stream=None)
    pp.pprint(reports.count_games('game_stat.txt'))
    pp.pprint(reports.decide('game_stat.txt', 1999))
    pp.pprint(reports.get_latest('game_stat.txt'))
    pp.pprint(reports.count_by_genre('game_stat.txt', 'Survival game'))
    pp.pprint(reports.get_line_number_by_title('game_stat.txt', 'World of Warcraft'))
    pp.pprint(reports.sort_abc('game_stat.txt'))
    pp.pprint(reports.get_genres('game_stat.txt'))
    pp.pprint(reports.when_was_top_sold_fps('game_stat.txt'))


if __name__ == '__main__':
    main()
