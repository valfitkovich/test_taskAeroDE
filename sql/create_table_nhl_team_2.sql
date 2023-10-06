CREATE TABLE nhl_team_stats (
    id SERIAL PRIMARY KEY,
    team_id INT,
    team_name VARCHAR(255),
    stats_type VARCHAR(255),
    game_type VARCHAR(255),
    stats_values TEXT[]
);
