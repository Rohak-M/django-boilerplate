# django-boilerplate

## About

A simple [Django](https://www.djangoproject.com/) project boilerplate/template inspired by [Django React Boilerplate](https://github.com/vintasoftware/django-react-boilerplate/).

## Features Catalogue

### Backend

-   `django` for building backend logic using Python
-   `psycopg` for using PostgreSQL database
-   `python-decouple` for reading environment variables on settings files
-   `django-permissions-policy` for setting the draft security HTTP header Permissions-Policy
-   `whitenoise` and `brotlipy` for serving static assets

### Future plans (TO DO)
-   `django-upgrade` for automatically upgrading Django code to the target version on pre-commit
-   `django-defender`


## Project bootstrap

-   [ ] do not install Python yourself, UV is perfect for this job
-   [ ] install [UV](https://docs.astral.sh/uv/getting-started/installation/) with [Shell autocompletion](https://docs.astral.sh/uv/getting-started/installation/#shell-autocompletion)
-   [ ] install [Bun](https://bun.sh/docs/installation)
-   [ ] create git repository for the project and clone it to a local folder (lets say {{project_name}})
-   [ ] initialize a new python virtual enviroment in the same folder:
    ```
    uv init --python 3.13.3 ~/proj/{{project_name}}
    ```
-   [ ] go inside the folder {{project_name}} and install Django with `uv add django`, to have the `django-admin` command available
-   [ ] delete following files from `project_name` folder:
    - .gitignore
    - main.py
    - pyproject.toml
    - README.md
    ```
    rm .gitignore main.py pyproject.toml README.md
    ```
-   [ ] start your project in the current directory using (replace `project_name` with your project name and remove the curly braces, the dot after the `project_name` tells `django-admin` to use current directory):
    ```
    uv run django-admin startproject {{project_name}} . --extension py,json,yml,yaml,toml --name README.md,.env.example,.gitignore --template=https://github.com/Rohak-M/django-boilerplate/archive/refs/heads/main.zip
    ```
In the next steps, always remember to replace {{project_name}} with your project's name (in case it isn't yet):
-   [ ] Above: don't forget the `--extension` and `--name` params!
-   [ ] Go into project's root directory: `cd {{project_name}}`
-   [ ] Change the first line of README to the name of the project
-   [ ] Add an email address to the `ADMINS` settings variable in `{{project_name}}/backend/config/settings/base.py`
-   [ ] Change the `SERVER_EMAIL` to the email address used to send e-mails in `{{project_name}}/backend/config/settings/production.py`

After completing ALL of the above, remove this `Project bootstrap` section from the project README.