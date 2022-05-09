# DogecoPredictor

DogecoPredictor is open source ML powered predictor for DogeCoin. The previous day's closing value is used to predict the next day's closing value

Website : [DogecoPredictor](https://dogecopredictor.herokuapp.com/)

ML Model : [Predictor](https://colab.research.google.com/drive/1NMj--2cS245yiCtcg6qvt0LvbqUc-47S?usp=sharing)


![dogecoin-meme](https://user-images.githubusercontent.com/66952088/157790311-179f26ce-e104-46e6-af89-d28960a60c3b.jpg)


## Team members

[Aanand S](https://github.com/unniznd)

Mashood

## Team Id

Team Id - ML/ 71

## Link to product walkthrough

See our [video](https://www.loom.com/share/30d978b2a40b4782a915683ae0249419) for more details

## How it Works ?

1) Go to our website [DogecoPredictor](https://dogecopredictor.herokuapp.com/)
2) Add the close of previous day in the close form in the site
3) Click on the predict button and the predicted value will be shown at the bottom

## Libraries used

Django - 4.0.3

django-crispy-forms - 1.14.0

gunicorn - 20.1.0

joblib - 1.1.0

numpy - 1.22.3

scikit-learn - 1.0.1

scipy - 1.8.0


## How to configure

Clone the repo

```
git clone https://github.com/unniznd/predictor.git
```

Install dependencies

```
pip install -r requirements.txt
```

Create file ```predictor/dev_settings.py``` and Configure SECRET_KEY and ALLOWED_HOSTS

```
SECRET_KEY = "add_secret_key_here"
....
ALLOWED_HOSTS = ['dogecopredictor.herokuapp.com','*'] # '*' means allow all hosts
```

Make migrations 

```
python manage.py makemigrations
python manage.py migrate
```

Set ```debug = False ``` in ```predictor/settings.py```

## How to Run

Run server 

```
python manage.py runserver
```

Go to the link and enjoy the DogecoPredictor

