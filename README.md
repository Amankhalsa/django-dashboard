# django-dashboard


pipenv install django==3.2

pipenv shell

pipenv install django-ckeditor nad pipenv install stripe(for payment)


Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\backends\utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\backends\sqlite3\base.py", line 423, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.OperationalError: no such table: account_user

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Apna\AppData\Local\Programs\Python\Python38\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "C:\Users\Apna\AppData\Local\Programs\Python\Python38\lib\threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\core\management\commands\runserver.py", line 110, in inner_run
    autoreload.raise_last_exception()
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\utils\autoreload.py", line 87, in raise_last_exception
    raise _exception[1]
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\core\management\__init__.py", line 375, in execute
    autoreload.check_errors(django.setup)()
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\apps\registry.py", line 114, in populate
    app_config.import_models()
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\apps\config.py", line 301, in import_models
    self.models_module = import_module(models_module_name)
  File "C:\Users\Apna\AppData\Local\Programs\Python\Python38\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\Apna\Desktop\Django\django\app\models.py", line 103, in <module>
    admin=User.objects.get(email='firat.cavit@hotmail.com')
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\models\manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\models\query.py", line 431, in get
    num = len(clone)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\models\query.py", line 262, in __len__
    self._fetch_all()
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\models\query.py", line 1324, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\models\query.py", line 51, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\models\sql\compiler.py", line 1175, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\backends\utils.py", line 98, in execute
    return super().execute(sql, params)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\backends\utils.py", line 66, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\backends\utils.py", line 75, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\backends\utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\backends\utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Apna\Desktop\Django\venv\lib\site-packages\django\db\backends\sqlite3\base.py", line 423, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.OperationalError: no such table: account_user

