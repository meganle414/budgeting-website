# budgeting-website
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

* A Django app used to retrieve budgeting information securely through Plaid
* Create User -> Make a POST request at /register-user/ with email and password to create new user.
* Login -> Make a POST request at /login/ with email and password. Returns a token if login is successful and is_logged_in is set to true.
* Logout -> Make a POST request at /logout/ with the token generated at login. is_logged_in is set to false.
* Token Exchange -> Make a GET request at /token-exchange/ with email and public_token. Returns access_token if not generated already.
* Get Transaction -> Make a GET request a /get-transactions/ with email, start_date and end_date. Returns transactions within given time period.
* Get Accounts -> Make a GET request at /get-accounts/ with email. Return user accounts.
* Update Transaction -> Make a POST request at /update-transactions/ with user email and transaction id. Fetches the transaction. Updates user by sending email.

<img src="images/test_results.png">

### Built With

* Python
* Django
* Celery
* AMQP
* Plaid

<p align="right">(<a href="#budgeting-website">back to top</a>)</p>

### Budgeting Website
Install dependencies all together<br>
```pip install```<br>
Or install them all individually<br>
```pip install django```<br>
```pip install celery```<br>
```pip install plaid-python```<br>
```pip install amqp```<br>
Make migrations<br>
```python manage.py makemigrations```<br>
```python manage.py migrate```<br>
Run the server with<br>
```python manage.py runserver```<br>
Run the test with<br>
```python manage.py test budgeting```<br>
Open Command Prompt<br>
```cd C:\Users\YOUR_USERNAME_HERE\Downloads\rabbitmq-server-windows-3.13.3\rabbitmq_server-3.13.3\sbin```<br>
```rabbitmq-server.bat```<br>
Start Celery Service<br>
```python -m celery -A budgetingwebsite.celery_app worker -l info```<br>

![Screenshot](https://github.com/meganle414/budgeting-website/blob/main/images/test_results.png?raw=true)

<p align="right">(<a href="#budgeting-website">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Email: meganle414@gmail.com

Project Link: [https://github.com/meganle414/budgeting-website](https://github.com/meganle414/budgeting-website)

[linkedin-url]: https://linkedin.com/in/meganle414/

<p align="right">(<a href="#budgeting-website">back to top</a>)</p>
