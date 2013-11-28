from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from ploneun.subscribetochanges.interfaces import IProductSpecific
from ploneun.subscribetochanges.interfaces import ISubscriberManager
from ploneun.subscribetochanges.interfaces import ISubscribeToChangesEnabled
grok.templatedir('templates')

class SubscribeViewlet(grok.Viewlet):
    grok.context(ISubscribeToChangesEnabled)
    grok.viewletmanager(manager.IBelowContentTitle)
    grok.template('subscribeviewlet')
    grok.layer(IProductSpecific)

    def available(self):
        return True

    def subscribed(self):
        return ISubscriberManager(self.context).subscribed()
