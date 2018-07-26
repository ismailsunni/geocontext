# coding=utf-8
"""Test import data."""

import os

from django.test import TestCase

from django.conf import settings

from base.management.commands.utilities import import_data

test_data_directory = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'data')


class TestGeoContextView(TestCase):
    """Test for geocontext view."""

    def test_import_geocontext_data(self):
        """Setup test data."""
        geocontext_path = os.path.join(
            settings.BASE_DIR, '../base/management/commands/geocontext.json', )
        self.assertTrue(os.path.exists(geocontext_path))
        # It should not raise an error
        import_data(geocontext_path)