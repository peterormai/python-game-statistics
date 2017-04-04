import reports

print(reports.count_games('game_stat.txt'))

print(reports.decide('game_stat.txt', 1999))

print(reports.get_latest('game_stat.txt'))

print(reports.count_by_genre('game_stat.txt', 'Survival game'))

print(reports.get_line_number_by_title('game_stat.txt', 'World of Warcraft'))

print(reports.sort_abc('game_stat.txt'))

print(reports.get_genres('game_stat.txt'))

print(reports.when_was_top_sold_fps('game_stat.txt'))
