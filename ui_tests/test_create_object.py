import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s
from selene import be
from auto_test_geocode.base_page.login import open_page_and_login
from auto_test_geocode.base_page.interface_map import object_creation_mode
from auto_test_geocode.controls.helper.ui_tests_helper import double_click_to, drag_and_drop_to


'''
    Так как на тестовом окружении баг с полями координат, то проверяем только блок в окне создания объекта
'''


def test_visible_coordinate_block():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тест geocode")
    allure.dynamic.story("Проверка что система добавила блок координат, после установки точки на карте")

    with allure.step('Открываем /maps/68'):
        open_page_and_login(url='/maps/68')

    with allure.step('Выбираем тип режима создания объекта: Режим точки'):
        object_creation_mode(type_object=1)

    with allure.step('В окне создания объекта выбираем координаты'):
        s('//*[@class="base-text-switch-option-text"][text()="Координаты"]').click()

    with allure.step('Увеличиваем размер окна создания объекта'):
        s('//*[@class="base-info-box__resize bottom"]').perform(drag_and_drop_to(200, 100))

    with allure.step('Ставим объект на карте: Точку'):
        s('.geocode-map').perform(double_click_to(-100, 100))

    with allure.step('Проверяем что блок координат добавился после установки точки'):
        s('.create-layer-object-content__coordinates__existing').should(be.visible)
