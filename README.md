Запуск теста:
1) pip install -r auto_test_geocode/requirements.txt
2) python -m pytest auto_test_geocode/ui_tests .
3) Дождаться завершения теста
4) allure serve allure-results
5) Откроется allure report с видео, скриншотом и логами


Тест находится в папке: ui_tests

Helper для взаимодействия с картой в папке: controls/helper

page_object в папке: base_page

Аттачменты к allure: utils