# Authentication Assignment

## Applied all authentication features in a existing django-blog for convenience

<b>Language Choice:</b> Python, JavaScript <br>
<b>Frameworks:</b> Django, Bootstrap <br>
<b>Database:</b> PostgreSQL <br>
## for installing dependencies and testing <pre><code>pip3 install -r requirements.txt </code></pre>
## Then migrate the database by <pre><code>python manage.py makemigrations</code></pre>
##                              <pre><code>python manage.py migrate</code></pre>
## Run the local server by <pre><code>python manage.py runserver</code></pre>
## For testing purpose <br>
    Admin name: zilani
    password: django12
    
* or create a superuser by: <pre><code>python manage.py createsuperuser</code></pre>


## Registration route and filling information ...
![register process](https://user-images.githubusercontent.com/42479575/55678492-87929e00-591c-11e9-9d64-feab425b943c.png)

## A confirmation email sent to the email ...
![confirmation email](https://user-images.githubusercontent.com/42479575/55678504-db9d8280-591c-11e9-9d23-7225487ad998.png)

## Confirm registration ...
![account activation confirm](https://user-images.githubusercontent.com/42479575/55678515-08ea3080-591d-11e9-99ae-1133546e6be5.png)

## After that, User added to database, password saved in hash format not in plain text.
![user added to db with hashed password](https://user-images.githubusercontent.com/42479575/55678522-23bca500-591d-11e9-82bd-cdfc5e22cb9c.png)

* Now, user can login by the same credentials ...
