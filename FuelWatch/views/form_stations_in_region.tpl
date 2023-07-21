<!DOCTYPE html>
<html>
    <head>
        <title>Fuel Watch Database</title>
        <link type="text/css" href="/static/forms_style.css" rel="stylesheet">
    </head>
    <body>
        <div id="container">
            <header>
                <p><a href="/">Return to Home Page</a></p>
            </header>
            
            <section class="querySection">
                <div class="queryForm">
                    <h3>Stations in a Region</h3>
                    <form action="/select_stations_in_region" method="post">
                        Find all the stations in a selection region.<br />
                        Enter the area: <input type="text" name="region_value" /><br />
                        <input type="submit">
                    </form>
                    <p>NOTE: Some regions include: Peel, Metro, South-West, Kimberley, Gascoyne</p>
                </div>

                <div class="queryForm">
                    <h3>Stations in a Region (using a dropdown)</h3>
                    <form action="/select_stations_in_region" method="post">
                        <select name="region_value">
                            <option value="Gascoyne">Gascoyne</option>
                            <option value="Goldfields-Esperance">Goldfields-Esperance</option>
                            <option value="Great Southern">Great Southern</option>
                            <option value="Kimberley">Kimberley</option>
                            <option value="Metro">Metro</option>
                            <option value="Mid-West">Mid-West</option>
                            <option value="Peel">Peel</option>
                            <option value="Pilbara">Pilbara</option>
                            <option value="South-West">South-West</option>
                            <option value="Wheatbelt">Wheatbelt</option>
                        </select>
                        <input type="submit">
                    </form>
                </div>
            </section>

            <footer>
                <p><a href="/">Return to Home Page</a></p>
            </footer>
        </div>
    </body>
</html>