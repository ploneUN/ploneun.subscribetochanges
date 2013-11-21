from five import grok
from ploneun.subscribetochanges.interfaces import ISubscribeToChangesEnabled
from ploneun.subscribetochanges.interfaces import ISubscriberManager
from z3c.caching.purge import Purge
from zope.event import notify

class SubscribeToChanges(grok.View):
    grok.name('ploneun-subscribetochanges')
    grok.context(ISubscribeToChangesEnabled)

    def render(self):
        ISubscriberManager(self.context).toggle_subscribtion()
        self.request.response.redirect(self.context.absolute_url())
        notify(Purge(self.context))
