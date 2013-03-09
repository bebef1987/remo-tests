#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.page import Page
from pages.base import Base

class Labs(Base):

    _business_card_area_locator = (By.CSS_SELECTOR, 'div.row.top-margined:nth-of-type(2)')

    def go_to_labs_page(self):
        self.selenium.get(self.testsetup.base_url + '/faq/')

    def is_business_card_area_visibile(self):
        return self.is_element_visible(*self._business_card_area_locator)


