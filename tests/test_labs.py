#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.home import Home

class TestLabs:

    @pytest.mark.nondestructive
    def test_check_card_generator(self, mozwebqa):
        home = Home(mozwebqa)
        home.go_to_homepage()

        labs = home.header.click_labs_link()


