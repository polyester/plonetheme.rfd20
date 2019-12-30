# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.rfd20


class PlonethemeRfd20Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonetheme.rfd20)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.rfd20:default')


PLONETHEME_RFD20_FIXTURE = PlonethemeRfd20Layer()


PLONETHEME_RFD20_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_RFD20_FIXTURE,),
    name='PlonethemeRfd20Layer:IntegrationTesting',
)


PLONETHEME_RFD20_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_RFD20_FIXTURE,),
    name='PlonethemeRfd20Layer:FunctionalTesting',
)


PLONETHEME_RFD20_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_RFD20_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlonethemeRfd20Layer:AcceptanceTesting',
)
