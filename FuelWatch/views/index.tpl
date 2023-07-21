<!DOCTYPE html>
<html>
    <head>
        <title>Fuel Watch Database</title>
        <link type="text/css" href="/static/main_style.css" rel="stylesheet">
    </head>
    <body>
        <div id="container">
            <h1>Data from the Fuel Watch website</h1>

            <div class="querySection">
                <p><a href="/create_db">Create a fresh database (with no data)</a></p>
                <p><a href="/insert_data">Insert Test Database</a></p>
            </div>

            <div class="querySection">
                    <p><a href="/select_all_stations">Find information about all the stations</a></p>
                    <p><a href="/select_all_areas">Find information about all the areas</a></p>
                    <p><a href="/select_all_diesel">Find the price of diesel</a></p>
                    <p><a href="/select_stations_per_city">Find number of stations in each city</a></p>
                </ul>
            </div>

            <div class="querySection">
                <div class="queryForm">
                    <h3>Stations in an area</h3>
                    <form action="/select_stations_in_area" method="post">
                        Find the cities with stations in a particular area of the state.<br />
                        Enter the area: <input type="text" name="area_value" /><br />
                        <input type="submit">
                    </form>
                </div>
                <div class="queryForm">
                    <h3>Brands in a Region</h3>
                    <form action="/select_brands_in_region" method="post">
                        Find all the station of a particular brand in a region.<br />
                        Enter the brand: <input type="text" name="brand_value" /><br />
                        Enter the region: <input type="text" name="region_value" /><br />
                        <input type="submit">
                    </form>
                </div>
                    <p><a href="/select_stations_in_region">Find all the stations in an area</a></p>
            </div>
            <footer>
                <p>This is a sample database based on data from the <a href="https://www.fuelwatch.wa.gov.au/">FuelWatch</a> website demonstrating the use of Bottle to create a database application.</p>
            </footer>
        </div>
    </body>
</html>