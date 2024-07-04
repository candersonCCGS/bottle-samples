% rebase('chinook_base.tpl')

% include('page_heading.tpl', name="Albums")

<section class="querySection">
    <section class="queryForm">
        <h3>Tracks in an album (using a dropdown)</h3>
        % if len(records) < 1:
        <form action="/select_album_tracks" method="post">
            List all the tracks from a particular album.<br />
            Some albums inlcude: Let There Be Rock, Facelift, Black Sabbath, Bongo Fury<br />
            Enter the album: <input type="text" name="album_value" /><br />
            <input type="submit">
        </form>
        % else:
        <form action="/select_album_tracks" method="post">
            <select name="album_value">
                % for record in records:
                <option value="{{record[1]}}">{{record[0]}}</option>
                % end
            </select><br />
            <input type="submit">
        </form>
        % end
    </section>
</section>