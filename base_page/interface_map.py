from selene.support.shared.jquery_style import s


def object_creation_mode(type_object):
    s('.map-layers').s('svg[fill="white"]').click()
    s(f'(//*[@class="base-menu layer-item__header-actions-btn"])[{str(type_object)}]').click()
    s('.base-menu-item').hover()
    s('//*[@class="base-menu-item__name"][text()="Редактировать"]').hover()
    s('//*[@class="base-menu-item__name"][text()="Создать объект"]').click()
