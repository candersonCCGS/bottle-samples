% rebase('chinook_base.tpl')

% include('page_heading.tpl', name="Albums")

<section id="querySection">
    <p><a href="/select_all_albums">Find information about all the albums</a></p>
</section>

<section class="querySection">
    <p><a href="/select_album_tracks">Find all the tracks in an Album</a></p>

    <section class="queryForm">
        <h3>Tracks for an Album</h3>
        <form action="/select_album_tracks" method="post">
            List all the tracks from a particular album.<br />
            Some albums inlcude: Let There Be Rock, Facelift, Black Sabbath, Bongo Fury<br />
            Enter the album: <input type="text" name="album_value" /><br />
            <input type="submit">
        </form>
    </section>

    <section class="queryForm">
        <h3>Tracks in an album (using a dropdown)</h3>
        <form action="/select_album_tracks" method="post">
            <select name="album_value">
                <option value="Let There Be Rock">Let There Be Rock</option>
                <option value="Facelift">Facelift</option>
                <option value="Black Sabbath">Black Sabbath</option>
                <option value="Bongo Fury">Bongo Fury</option>
            </select>
            <input type="submit">
        </form>
    </section>

</section>
