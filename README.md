#### Hello everyone, this is my first project where I implemented the backend part with the `Django framework`. I hope you enjoy it.


#### This project is written with `Django version 6`. To find out what version of Python this version of Django works with, you can refer to the [django](https://docs.djangoproject.com/en/6.0/releases/6.0/#python-compatibility)

#### Of course, I have also uploaded this project with `Docker`, which uses Python version `3.12.13`, which we will discuss later.



# Run manually

Follow the steps below to install.

## 1. Cloning the project's `sqlite` branch 

> *Linux*

In Linux, first open the `Terminal` application and navigate to the folder you want for example:
```
cd Dowloads/
```

Then clone the project:
```
git clone -b --single-branch https://github.com/GHESHAE7/shop.git
```
⚠️ Note that this command clones only the `sqlite` branch; if you want to clone all branches, run this command:
```
git clone -b https://github.com/GHESHAE7/shop.git
```
And go to the project folder with the following command:
```
cd shop/
```
You are on this path now. `username@host:~/Downloads/shop`

> *Windows*
>
In Windows, first open the `Git Bash` application and navigate to the folder you want for example:

```
cd Documents/
```

Then clone the project:
```
git clone -b sqlite --single-branch https://github.com/GHESHAE7/shop.git
```
⚠️ Note that this command clones only the `sqlite` branch; if you want to clone all branches, run this command:
```
git clone -b https://github.com/GHESHAE7/shop.git
```

And go to the project folder with the following command:
```
cd shop/
```
You are on this path now. `username@host MINGW64 ~/Documents/shop`

## 2. create virtual environment

> *Linux*
>

The first step is to create a virtual environment:
```
python3 -m venv .venv
```
The second step is to activate the virtual environment:
```
source .venv/bin/activate
```
After activating the virtual environment, you will see this section in your terminal address `((venv) ) username@host:~/Downloads/shop`

> *Windows*
>

The first step is to create a virtual environment:
```
python -m venv .venv
```
The second step is to activate the virtual environment:
```
source .venv/Scripts/activate
```
After activating the virtual environment, you will see this section in your terminal address `(.venv) username@host MINGW64 ~/Documents/shop`

## 3. Install requirements
> *Linux & Windows*
> 
Now it's time to install the packages in the `requirements.txt` file:

```
pip install -r requirements.txt
```

## 4. Config database

To configure the database, create a `db.sqlite3` file in the project folder.

## 7. Config Email & Secret key

This project has placed the required information in the `.env` file to send emails, as well as the `secret_key` in the project `/config/settings.py`. Place the following texts in the `.evn` file.

```
# email
EMAIL_HOST_USER=youremail
EMAIL_HOST_PASSWORD=apppassword

# secret key
SECRET_KEY=yoursecretkey
```

## 6. Migrations
Then type this command in your terminal to prepare the database.

```
python manage.py migrate
```

## 6.Start the project

Now everything is fine. You can run the project with the following command

```
python manage.py runserver
```




