# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.rfd20.testing import PLONETHEME_RFD20_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plonetheme.rfd20 is properly installed."""

    layer = PLONETHEME_RFD20_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.rfd20 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.rfd20'))

    def test_browserlayer(self):
        """Test that IPlonethemeRfd20Layer is registered."""
        from plonetheme.rfd20.interfaces import (
            IPlonethemeRfd20Layer)
        from plone.browserlayer import utils
        self.assertIn(
            IPlonethemeRfd20Layer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_RFD20_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plonetheme.rfd20'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plonetheme.rfd20 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.rfd20'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeRfd20Layer is removed."""
        from plonetheme.rfd20.interfaces import \
            IPlonethemeRfd20Layer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPlonethemeRfd20Layer,
            utils.registered_layers())
