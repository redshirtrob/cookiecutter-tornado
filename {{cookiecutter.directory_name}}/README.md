# {{cookiecutter.title}}

{{cookiecutter.description}}

It stubs out:
 * An async web server
 * Routes
 * GET/POST handlers
 * A SQLite memory store

To try it out:
```bash
$ mkvirtualenv {{cookiecutter.directory_name}}
$ pip install -r requirements
$ python run.py # Listens on port 9000
```

