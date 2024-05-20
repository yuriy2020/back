.\venv\Scripts\activate

cd .\rosmorport

# надо после того как поместил фронт в папку ту статик
python manage.py collectstatic
python .\manage.py runserver

pip install -r .\requirements.txt

