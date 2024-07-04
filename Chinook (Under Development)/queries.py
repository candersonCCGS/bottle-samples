# This file contains all the queries that are used in the web application.

SELECT_ALL_ALBUMS = "SELECT * FROM Album"

SELECT_ALL_CUSTOMERS = "SELECT * FROM Customer"

SELECT_ALL_ORDERS = "SELECT * FROM Invoice"

SELECT_ALBUM_NAMES = """SELECT Name || ': ' || Title as ArtistAlbum, Title
                        FROM Album, Artist
                        WHERE Album.ArtistId = Artist.ArtistId
                        ORDER BY ArtistAlbum
"""

# The following queries require the use of a form.
# NOTE: The parameter names in the queries must match the names of the form fields.

SELECT_ALBUM_TRACKS = '''SELECT Track.Name as Name, Track.Milliseconds as "Length (ms)", Track.UnitPrice as Cost
                    FROM Album, Track
                    WHERE Album.AlbumId = Track.AlbumId
                    AND Album.Title = :album_title
                '''
