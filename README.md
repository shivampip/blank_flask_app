# blank_flask_app

Blank Modular Flask App with Blueprints for APIs

#### Add `.env` file

```
FLASK_APP=app.app:create_app
FLASK_ENV=development
KEY="KEY_FROM_ENV"
```

#### Install deps

```
pip install -r requirements.txt
```

#### Run

```
flask run --host=0.0.0.0 --port=3001
```

#### Bash Script

```
#!/bin/bash

PPATH=/root/absolute/path/to/project
ENV="proenv"


cd ${PPATH}
source ${ENV}/bin/activate
fuser -n tcp -k ${3001}
sudo kill -9 $(sudo lsof -t -i:3001)
flask run --host=0.0.0.0 --port=3001

```

#### Add New Blueprint

-   Add blueprint folder
-   Register blueprint in app.py
