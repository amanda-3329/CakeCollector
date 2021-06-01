After cloning down a Python / Django project follow these steps.

- Create a new virtual environment in your project with
```bash
$ python3 -m venv .env
$ source .env/bin/activate
```
- Install its dependencies with
```bash
pip3 install -r requirements.txt
```
# CakeCollector

CakeCollector is a site for customers interested in tracking new cakes they have tried. From a bride to be or someone planning an event, they can upload details about the cake they tried, when it was tasted, and the origin of the cake!

## Technologies Used

* HTML
* CSS
* Materialize CSS Framework
* Python
* Django
* PostgreSQL
* AWS 


## Existing Features


* Home page with image, clickable navigation bar to log in/log out. 
* Working navigation to also "View All Cakes" tracked and "Add a Cake" to add new cakes
* Two model functionality, with the ability to add/delete pre-existing options from the customization menu.
* Full CRUD of the database entries.
* Pages fully link to each other.
* AWS photo upload and hosting
* Edit button -user can edit their entries.
* Delete button - user can delete their entries


## Planned Features

* User sign-up
* Ability to filter through cake options using database categories. 
* Media query for better screen adaptation
* Deployment to Heroku app
