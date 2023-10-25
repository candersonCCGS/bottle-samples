<!DOCTYPE html>
<html>
    <head>
        <title>My First App</title>
    </head>
    <body>
        <h1>Customer List</h1>
        <p><a href="/">Home</a></p>
        <p>
            <table>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                </tr>
                % for customer in customers:
                <tr>
                    <td>{{ customer['first_name'] }}</td>
                    <td>{{ customer['last_name'] }}</td>
                </tr>
                % end
            </table>
        </p>
    </body>
</html>