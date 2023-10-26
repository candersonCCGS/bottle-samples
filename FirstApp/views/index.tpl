<!DOCTYPE html>
<html>
    <head>
        <title>My First App</title>
        <link type="text/css" href="/static/style.css" rel="stylesheet">
    </head>
    <body>
        <h1>My First Bottle App!</h1>
        <p><a href="/hello">Hello</a></p>
        <p><a href="/customers">Customers</a></p>
        <p><a href="/create_database">Create a new database</a></p>
        <p><a href="/insert_data">Insert sample data in database</a></p>
        <p><a href="/select_all_teams">Select all teams in the database</a></p>
        <p><a href="/select_players_and_team">Find all players and their team</a></p>
        <p>
            <form action="/select_team_players" method="post">
                Find the players in a team.<br />
                Enter the team name: <input type="text" name="name_value" /><br />
                <input type="submit">
            </form>
        </p>
    </body>
</html>