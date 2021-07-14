#
# SPDX-FileCopyrightText: 2020 Splunk, Inc. <sales@splunk.com>
# SPDX-License-Identifier: LicenseRef-Splunk-1-2020
#
#
import pytest

from pytest_splunk_addon.standard_lib.addon_basic import Basic
from pytest_splunk_addon.standard_lib.index_tests.test_templates import IndexTimeTestTemplate



class Test_App(Basic):
    def empty_method(self):
        pass
