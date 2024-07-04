% rebase('chinook_base.tpl')
<!-- THIS SECTION TO BE ADDED LATER TO CREATE FRESH DATABASE
    <section class="querySection">
    <h4>Scripts to set up a fresh database</h4>
    <p><a href="/create_db">Create a fresh database (with no data)</a></p>
    <p><a href="/insert_data">Insert Test Database</a></p>
</section> 
-->
% include('page_heading.tpl', name='Welcome to Chinook!')
<section class="querySection">
    <h4>Hardcoded scripts to give the user specific information</h4>
    <p><a href="/albums"><strong>Albums</strong></a></p>
    <p><a href="/customers"><strong>Customers</strong></a></p>
    <p><a href="/orders"><strong>Orders</strong></a></p>
</section>