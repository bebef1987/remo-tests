#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base

class NewEvent(Base):

     _name_locator = (By.ID, 'id_name')
     _description_locator = (By.ID, 'id_description')
     _external_link_locator = (By.ID, 'id_external_link')
     _venue_locator = (By.ID, 'id_venue')
     _city_locator = (By.ID, 'id_city')
     _region_locator = (By.ID, 'id_region')
     _country_selector_locator = (By.ID, 'id_country')
     _start_month_locator = (By.ID, 'id_start_form_0_month')
     _start_day_locator = (By.ID, 'id_start_form_0_day')
     _start_year_locator = (By.ID, 'id_start_form_0_year')
     _start_hour_locator = (By.ID, 'id_start_form_1_hour')
     _start_minute_locator = (By.ID, 'id_start_form_1_minute')
     _end_month_locator = (By.ID, 'id_end_form_0_month')
     _end_day_locator = (By.ID, 'id_end_form_0_day')
     _end_year_locator = (By.ID, 'id_end_form_0_year')
     _end_hour_locator = (By.ID, 'id_end_form_1_hour')
     _end_minute_locator = (By.ID, 'id_start_form_1_minute')
     _timezone_locator = (By.ID, 'id_timezone')
     _owner_locator = (By.ID, 'id_owner_form')
     _mozilla_event_locator = (By.CSS_SELECTOR, '#id_mozilla_event ~ span')
     _attendance_locator = (By.ID, 'id_estimated_attendance')
     _extra_content = (By.ID, 'id_extra_content')
     _planing_pad_locator = (By.ID, 'id_planning_pad_url')
     _hashtag_locator = (By.ID, 'id_hashtag')







