% rebase('chinook_base.tpl')

% include('page_heading.tpl', name='Customers')

<section id="introduction">
    <p>Use this page to find out all the information about different customers</p>
</section>

<section id="querySection">
    <p><a href="/select_all_customers">Find information about all the customers</a></p>
</section>

<section class="queryForm">
    <form action="/insert_new_customer" method="post">
        <h3>Insert a new customer.</h3>
        <br />
        First Name: <input type="text" name="first_name" /><br />
        Last Name: <input type="text" name="last_name" /><br />
        Email: <input type="text" name="email" /><br />
        <input type="submit">
    </form>
</section>

<section class="queryForm">
    <form action="/remove_customer" method="post">
        <h3>Remove a customer.</h3>
        <br />
        Custoemr Id: <input type="text" name="customer_id" /><br />
        <input type="submit">
    </form>
</section>

