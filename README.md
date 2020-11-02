Basic blog application using Django.

Deploy on pythonanywhere.com.

Virtual environment location on pythonanywhere : /home/haumea/.virtualenvs


**DATABASE MODIFICATION :**

A. Local :
1. python manage.py makemigrations blog
2. python manage.py sqlmigrate blog ****
    (change **** with output from migrations, for example 0002)
3. python manage.py migrate

B. pythonanywhere.com :
1. cd haumea.pythonanyhwere.com
2. rm db.sqlite3
3. git pull
4. cd ..
5. pa_autoconfigure_django.py https://github.com/bagusdewantoro/mysite.git --python=3.8 --nuke
    (--nuke options to replace the files)
6. python manage.py createsuperuser
7. If we have database backup on our local, through __FILE__ tab, we can upload to haumea.pythonanyhwere.com directory

**Credits:**
1. "Django 3 by Example" - Antonio Mele
2. Tutorial from djangogirls.org
