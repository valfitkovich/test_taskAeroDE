import psycopg2
import requests
from functools import wraps


def database_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            dbname="test_task",
            user="",
            password="",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
        except Exception as e:
            print(f"Ошибка при выполнении функции {func.__name__}: {e}")
            conn.rollback()
            result = None
        finally:
            cursor.close()
            conn.close()

        return result

    return wrapper


@database_connection
def fetch_and_store_data(conn):
    response = requests.get("https://random-data-api.com/api/cannabis/random_cannabis?size=10")
    data = response.json()

    cursor = conn.cursor()
    for item in data:
        cursor.execute("""
            INSERT INTO cannabis_data (id, uid, strain, cannabinoid_abbreviation, cannabinoid, terpene, medical_use, health_benefit, category, type, brand)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            item["id"], item["uid"], item["strain"], item["cannabinoid_abbreviation"], item["cannabinoid"],
            item["terpene"],
            item["medical_use"], item["health_benefit"], item["category"], item["type"], item["brand"]))


@database_connection
def fetch_and_store_nhl_data(conn):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/teams/21/stats")
    data = response.json()

    team_stat = data["stats"][0]["splits"][0]
    stat = team_stat["stat"]
    team = team_stat["team"]

    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO nhl_team_stats_single_season (team_id, team_name, games_played, wins, losses, ot, pts, pt_pctg, goals_per_game, goals_against_per_game, ev_gga_ratio, power_play_percentage, power_play_goals, power_play_goals_against, power_play_opportunities, penalty_kill_percentage, shots_per_game, shots_allowed, face_offs_taken, face_offs_won, face_offs_lost, face_off_win_percentage)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        team["id"], team["name"], stat["gamesPlayed"], stat["wins"], stat["losses"], stat["ot"], stat["pts"],
        float(stat["ptPctg"]), stat["goalsPerGame"], stat["goalsAgainstPerGame"], stat["evGGARatio"],
        float(stat["powerPlayPercentage"]), stat["powerPlayGoals"], stat["powerPlayGoalsAgainst"],
        stat["powerPlayOpportunities"], float(stat["penaltyKillPercentage"]), stat["shotsPerGame"],
        stat["shotsAllowed"], stat["faceOffsTaken"], stat["faceOffsWon"], stat["faceOffsLost"],
        float(stat["faceOffWinPercentage"])))


@database_connection
def fetch_and_store_nhl_data_v2(conn):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/teams/21/stats")
    data = response.json()

    for stats_entry in data["stats"]:
        stats_type = stats_entry["type"]["displayName"]

        # Используем условный оператор для проверки значения gameType
        game_type = None
        if stats_entry["type"].get("gameType"):
            game_type = stats_entry["type"]["gameType"].get("description")

        team_id = stats_entry["splits"][0]["team"]["id"]
        team_name = stats_entry["splits"][0]["team"]["name"]

        stats_values = [str(value) for key, value in stats_entry["splits"][0]["stat"].items()]

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO nhl_team_stats (team_id, team_name, stats_type, game_type, stats_values)
            VALUES (%s, %s, %s, %s, %s)
        """, (team_id, team_name, stats_type, game_type, stats_values))


if __name__ == "__main__":
    fetch_and_store_data()
    fetch_and_store_nhl_data()
    fetch_and_store_nhl_data_v2()

