# this is my end to end project

# first initialize the git

```
git init
```

```
git add .
```
```
git commit -m "this is my first commit"
```

```

git pull

```

```
bash your_file_name.sh
```

```
python setup.py install
```

# another way you can mention -e . in your requirement file and you can run

```
pip install -r requirements.txt
```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### local cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/username/
MLFLOW_TRACKING_USERNAME=shanur rahman\
MLFLOW_TRACKING_PASSWORD=3c2c8cd1436ad32b510cfdd84944a528ba4fb650 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/username/

export MLFLOW_TRACKING_USERNAME=shanur rahman\

export MLFLOW_TRACKING_PASSWORD=3c2c8cd1436ad32b510cfdd84944a528ba4fb650

```


### DVC cmd
- dvc init
- dvc repro
- dvc dag

