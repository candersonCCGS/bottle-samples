% rebase('chinook_base.tpl')
<!-- THIS SECTION TO BE ADDED LATER TO CREATE FRESH DATABASE
    <section class="querySection">
    <h4>Scripts to set up a fresh database</h4>
    <p><a href="/create_db">Create a fresh database (with no data)</a></p>
    <p><a href="/insert_data">Insert Test Database</a></p>
</section> 
-->
% include('page_heading.tpl', name='Welcome to Chinook!')
<section class="introduction">
    <p>Chinook music has the most comprehensive collection of music anywhere!</p>
    <nav>
        <a class="button" href="/albums"><strong>Albums</strong></a>
        <a class="button" href="/customers"><strong>Customers</strong></a>
        <a class="button" href="/orders"><strong>Orders</strong></a>
    </nav>
</section>