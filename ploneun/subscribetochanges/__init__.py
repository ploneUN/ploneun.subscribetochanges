from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from five import grok
from collective.grok import gs
from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('ploneun.subscribetochanges')

_ = MessageFactory

class HiddenProducts(grok.GlobalUtility):
    """This hides the upgrade profiles from the quick installer tool."""
    implements(INonInstallable)
    grok.name('ploneun.subscribetochanges.upgrades')

    def getNonInstallableProducts(self):
        return [
            'ploneun.subscribetochanges.upgrades',
        ]

gs.profile(name=u'default',
           title=u'ploneun.subscribetochanges',
           description=_(u''),
           directory='profiles/default')
