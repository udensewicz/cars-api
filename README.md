## Cars API

####Setup

First, you need to clone the app:

```git clone https://github.com/udensewicz/cars-api.git```

Then, create a `.env` file in the project root which includes a randomly generated Django secret key (you can use https://miniwebtool.com/django-secret-key-generator/):

```SECRET_KEY="YOUR_RANDOM_KEY"```

To run a standalone Django development server:
1. Create a virtualenv
2. `pip install -r requirements.txt`
1. `python manage.py migrate`
2. `python manage.py runserver`

Or using Docker:

```docker-compose up```


####API

#####POST /cars

Arguments:
* make_name: string up to 64 characters
* model_name: string up to 64 characters

Constraints:
* Car which is posted must exist here https://vpic.nhtsa.dot.gov/api/
* Does not allow posting models which already exist in app's DB

Returns the created car.


#####POST /rate
Arguments:
* car: integer, id of Car instance being rated
* value: integer between 1 and 5

Returns the created rate.

#####GET /cars
Returns a list of all cars with the following data: id, make name, model name, average rate
#####GET /popular
Returns a list of all cars sorted by number of rates descending, with the following data: id, make name, model name, number of rates.