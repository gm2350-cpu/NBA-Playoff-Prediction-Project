import time
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelogs

seasons = ['2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25', '2025-26']

max_attempts = 3

for season in seasons:
    for team in teams.get_teams():
        team_id = team['id']
        for attempt in range(1, max_attempts+1):
            try:
                log = teamgamelogs.TeamGameLogs(team_id_nullable=team_id, season_nullable=season, measure_type_player_game_logs_nullable = 'Advanced').get_data_frames()[0]
                log.to_csv('games.csv', mode='a', header = False, index = False)
                time.sleep(2)
                break

            except Exception as e:
                time.sleep(10)
