% setdefault('stylesheet', 'main_style')
<!DOCTYPE html>
<html>
    <head>
        <title>Chinook Database</title>
        <link type="text/css" href={{f'/static/{stylesheet}.css'}} rel="stylesheet">
    </head>
    <body>
        <section id="container">
            % include('header.tpl')
            
            {{ !base }}

            % include('footer.tpl')
        </section>
    </body>
</html>