# flask-4-ds
Using Flask to create a full-featured webapp for serving data products

Two ways to run the flask app
- `FLASK_APP=app.py FLASK_DEBUG=1 flask run`
- `python app.py` with `app.run()` in `app.py`

The decorator `@app.route('/<endpoint>')` is used to declare functions
that return html (or rendered templates) when the client requests an endpoint.

`render_template` helps pass raw html or rendered Jinja templates.
- it accepts data that can be used to render the page

Use `url_for` as far as possible to access resources under `static/` for example
You can also pass the function name associated with a route.

Create a SECRET_KEY using `secrets.token_hex(16)` from the `secrets` library
and assign it to `app.config`

`flask_sqlalchemy` lets you declare table schemas as `classes`
and work seamlessly with any database backend.

Then, we can fill these tables using `db.session.add(<Object of table-class>)`
The class can be used to query data as `User.query.all()` or `User.query.filter_by(<condition>).all()`

For security, passwords must be hashed using the `flask-bcrypt` library.
`Bcrypt` objects have methods like `generate_password_hash` and `check_password_hash` that are useful.

Use `flask-login` to manage user sessions
