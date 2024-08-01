<!DOCTYPE html>
<html>
    <head>
        <title>My To Do List</title>
        <link type="text/css" href='/static/style.css' rel="stylesheet">
    </head>
    <body>
        <h1>My To Do List</h1>
        <section>
            <p><a href="/create_todo_list">Create new To Do List</a></p>
        </section>
        <section>
            <p><a href="/insert_sample_data">Insert Sample Tasks into the To Do List</a></p>
        </section>
        <section>
            <p><a href="/show_to_do_list">Show the current To Do Items</a></p>
            <h3>My Tasks</h3>
            % if defined('records'):
                % if len(records) < 1:
                <p><strong>You have no items in your To Do list</strong></p>
                % else:
                <table>
                    <tr>
                        % for field in records[0].keys():
                        <th> {{ field }} </th>
                        % end
                    </tr>
                    % for record in records:
                    <tr>
                        % for field in record:
                        <td>{{ field }}</td>
                        % end
                    </tr>
                    % end
                </table>
                % end
            % end
        </section>
        <section>
            <form action="/add_task" method="post">
                <h3>Add a new task.</h3>
                Title: <input type="text" name="title" /><br />
                Description: <input type="text" name="description" /><br />
                <input type="submit">
            </form>
        </section>
        <section>
            <form action="/complete_task" method="post">
                <h3>Mark a task as completed.</h3>
                Task Id: <input type="text" name="task_id" /><br />
                <input type="submit">
            </form>
        </section>
        <section>
            <form action="/remove_task" method="post">
                <h3>Remove a task.</h3>
                Task Id: <input type="text" name="task_id" /><br />
                <input type="submit">
            </form>
        </section>
        <footer>
            <p>A To Do list using the Bottle framework</p>
        </footer>
    </body>
</html>
