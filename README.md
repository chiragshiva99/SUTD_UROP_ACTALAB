# UROP_SUTD_ACTALAB

### Contributors 
- Chirag Shivakumar 
- Prachi Jayesh Suthar 

UROP Requirements- Development of a Database for Chalcogenide Material Properties. The purpose of the website was for the SUTD ACTAlab research students to store their data files which can also be accessible to the public.

## Run Server
- **Step 1:** Clone

```shell
$ git clone https://github.com/chiragshiva99/SUTD_UROP_ACTALAB.git
```
- **Step 2:** Create virtual environment and install `requirements.txt`
```shell

$ python -m venv virtenv

for Mac
$ source virtenv/bin/activate

for Windows
> virtenv/bin/activate

$ python -m pip install -U --force-reinstall -r requirements.txt
```
- **Step 3:** Run Server 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
-**Step 4:** Open this link  [`http://127.0.0.1:8000/`] to access our webpage

To stop the web app type `CTRL+C`. 
