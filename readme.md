# Phone Book API 

This is an api with a default djangorestframework to handle basic http requests of GET, POST PUT, and delete.

# database
db.sqqlite3 file is used with the following schema:
    1) users table contains fields of:
        1.name of type varchar
        2.address of type varchar
    2) phones table contains fields of:
        1.phone_number of type varchar
        2.user_id a forgein key to the user table where 1 user could have many phone numbers (1:m)
    You could find the model in directory: "phone_book_api/phone_book_app/models.py" where django ORM is used.

# Docker:
    project is dockeried and you could find the docker configuration in Dockerfile, docker-compose

#API
    > Application is written using the Django framework.
    > djangorestframework package is added to give a fast api web page and handle the HTTP requests and responses
    > App still could be used as an API, however if needed, it is recommended to go to "phone_book_api/phone_book_app/urls.py" and change the path from '' to 'api/v1' to separate from frontend urls and specify the version of the api.

# To run the app
    docker-compose run --rm phone_book_api sh -c "django-admin startproject phone_book_api ."