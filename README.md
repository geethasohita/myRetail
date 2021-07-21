# MyRetail

![example workflow](https://github.com/geethasohita/myRetail/actions/workflows/github-actions.yml/badge.svg)

This is Python-Flask application using MongoDB as Database
<br><br>
The application is deployed in [Heroku](https://myretailapp.herokuapp.com/) which is connected to [MongoDB Atlas](https://cloud.mongodb.com/v2/60f3634ae8541e66416796fd#clusters) in cloud.
The [postman collection](https://github.com/geethasohita/myRetail/blob/main/myretail.postman_collection.json) has details related to all the endpoints for doing CRUD operations on resource `Product`
GET endpoints will call `redsky` api to get the product name.

`CI` for this app is done through [github actions](https://github.com/geethasohita/myRetail/actions) 
and Heroku-Github integration for `CD`.

<br>
Below is the information to setup this app locally.

##### Prerequisites:
Python (version > 3) is installed and path is set.

##### Setup:

- clone/download the project locally.
- `cd` into project
-  create virtual environment using the below command
```
python -m venv venv
```
- Activate the created venv using the below command
```
.\venv\Scripts\Activate
```
-Install the dependencies using the below command
```
pip install -r requirements.txt
```
- Run the application using the below command
```
flask run
```
- The application should run now and http://127.0.0.1:5000/ will show the welcome message.
