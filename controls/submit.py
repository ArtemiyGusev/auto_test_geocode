from selene import Element


class submit:

    def __init__(self, element: Element):
        self.element = element

    def submit_button_click(self):
        self.element.click()

    def submit_button_enter(self):
        self.element.press_enter()
