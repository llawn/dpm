## 0.6.0 (2024-11-30)


- feat(**app**): initialize db before starting the app<br>
- feat(**dbconn**): add a pydantic model for posgresql connexion settings<br>
- feat(**dbconnect**): add a databaseconnmixin to load database settings from dynaconv and use it to connect to posgresql table<br>
- feat(**auth**): add password generation and validation using bcrypt with pydantic<br>
- chore(**conf**): add a secrets.template.toml to know the structure of the .secrets.toml file<br>
- feat(**conf**): use dynaconf inside flask app<br>
- feat(**dynaconf**): add dynaconf to the project<br>
- feat(**app**): flask<br>

## 0.5.0 (2024-11-26)


- style(**todo**): add a todo to change the get_iso method to place it in its own mixin<br>
- chore(**gitignore**): add vscode dotfolder to gitignore<br>
- style(**readme**): add badges inside readme<br>
- build(**dependencies**): add pytz to my dependencies<br>
- test(**models**): add unittest to validate my user model<br>
- fix(**models**): wrong conversion to isoformat when tzinfo is not none<br>
- build(**dependencies**): add pydantic and email validator dependencies<br>
- fix(**import**): correct import<br>
- docs(**types**): add documentation for customtypes<br>
- docs(**models**): add documentation for user model<br>
- feat(**models**): change creation of user to default iso datetime<br>
- feat(**models**): add a user model<br>

## 0.4.0 (2024-11-24)


- fix(**logging**): remove streamhandler for logger_.py<br>
- test(**logging**): test loggers for dpm and test itself<br>
- feat(**logging**): add a specific logger for test<br>
- ci(**dependencies**): use uv in install.bat to setup our dependencies<br>
- docs(**dependencies**): add nose2<br>
- fix(**logging**): unique name for logger between file and __init__<br>

## 0.3.0 (2024-11-24)


- feat(**logging**): add a logging welcome message for package dpm<br>
- feat(**logging**): add a custom logger for dpm package<br>

## 0.2.1 (2024-11-24)


- ci(**setup**): add a setup batch file<br>
- fix(**version**): fix version file<br>

## 0.2.0 (2024-11-24)


- feat(**helloworld**): add a python helloworld<br>
- build(**pyproject**): add a pyproject.toml file<br>
- style(**changelog**): add a custom changelog template<br>
- ci(**version**): add a version file<br>
- docs(**license**): add license<br>
- ci(**pre-commit**): add pre-commit configuration file<br>
- chore(**gitignore**): add gitignore<br>
- docs(**readme**): add readme<br>
