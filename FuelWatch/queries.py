# This file contains all the queries that are used in the web application.

SELECT_ALL_STATIONS = 'SELECT * FROM Station'

SELECT_ALL_AREAS = '''SELECT Area.name as Area, Region.name as Region 
                        FROM Area, Region
                        WHERE Area.region_id = Region.region_id
                        ORDER BY Area.name
                    '''

SELECT_ALL_DIESEL = '''SELECT Price.date, Price.price, Brand.name, Station.name, Station.city
                        FROM Product, Price, Station, Brand
                        WHERE Product.product_id = Price.product_id
                        AND Price.station_id = Station.station_id
                        AND Station.brand_id = Brand.brand_id
                        AND Product.code = "Diesel"
                        ORDER BY Price.price ASC
                    '''

SELECT_STATIONS_PER_CITY = '''SELECT city, COUNT(city) as "Number of stations" 
                    FROM Station
                    GROUP BY city
					ORDER BY "Number of stations" DESC
                '''

# The following queries require the use of a form.
# NOTE: The parameter names in the queries must match the names of the form fields.

SELECT_STATIONS_IN_AREA = '''SELECT Area.name as Area, Station.city as "City name", COUNT(Station.city) as Stations
                    FROM Station, Area
                    WHERE Station.area_id = Area.area_id
                    AND Area.name = :area
                    GROUP BY Station.city
                '''

SELECT_BRANDS_IN_REGION = '''SELECT Station.name, Station.address, Station.city, Area.name as Area
                    FROM Brand, Station, Area, Region
                    WHERE Brand.brand_id = Station.brand_id 
                      AND Station.area_id = Area.area_id
                      AND Area.region_id = Region.region_id
                      AND Region.name = :region
                      AND Brand.name = :brand
                    ORDER BY Area, city'''

SELECT_STATIONS_IN_REGION = '''SELECT Station.name, Station.address, Station.city, Area.name
                    FROM Station, Area, Region
                    WHERE Region.region_id = Area.region_id
                      AND Area.area_id = Station.area_id
                      AND Region.name = :region
                    ORDER BY Station.name'''

