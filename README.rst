=========================
eversql
=========================
      A way of generating simple sql queries.


How does it work?
==============
* It uses python syntax with classes and converts it into sql queries

Install
==============
.. code:: sh
    
    pip install -U git+https://github.com/Sengolda/eversql

Quick Example
==============
.. code:: py
    
    import eversql

    t = eversql.Table()
    c = eversql.Column("name", "TEXT")
    t.add_column(c)
    t.query_sql()
    print(t) # Prints the query.
