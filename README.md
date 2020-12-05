1. git clone '''ссылочка на проект'''
перейдите в директорию скаченного проекта
2. pip install -r requirements.txt
(вместо python3 может быть python)
3. python3 manage.py migrate
4. python3 manage.py runserver
5. запуск тестов:
  python3 manage.py test my_project/apps/Todoapp - тесты для Todo/view.py и models.py
  python3 manage.py test my_project/apps/Authorization/ -тесты для Authorization/views.

