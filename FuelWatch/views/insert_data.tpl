<!DOCTYPE html>
<html>
    <head>
        <title>Fuel Watch Database</title>
        <link type="text/css" href="/static/results_style.css" rel="stylesheet">
    </head>

    <body>
        <header>
            <p><a href="/">Return to Home Page</a></p>
        </header>

        <h1>Inserting data into empty database</h1>

	    % if success == "success":
        %       description = "Database inserted successfully"
        % else:
        %       description = "Error inserting data into database"
        % end
		<p class="{{ success }}"><strong>{{ description }}</strong></p>

        <footer>
            <p><a href="/">Return to Home Page</a></p>
        </footer>
    </body>
</html>