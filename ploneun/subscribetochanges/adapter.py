from five import grok
from ploneun.subscribetochanges.interfaces import ISubscriberManager
from ploneun.subscribetochanges.interfaces import ISubscribeToChangesEnabled
from plone import api

class SubscriberManager(grok.Adapter):
    grok.implements(ISubscriberManager)
    grok.context(ISubscribeToChangesEnabled)

    def __init__(self, context):
        self.context = context

    def subscribe(self, user=None):
        if user is None:
            user = api.user.get_current().getId()
        subscribers = self.raw_subscribers()
        if user in subscribers:
            return
        subscribers.append(user)
        self.context.ploneun_changesubscribers = subscribers

    def unsubscribe(self, user=None):
        if user is None:
            user = api.user.get_current().getId()
        subscribers = self.raw_subscribers()
        if user in subscribers:
            subscribers.remove(user)
        self.context.ploneun_changesubscribers = subscribers

    def raw_subscribers(self):
        return getattr(self.context, 'ploneun_changesubscribers', []) or []

    def subscribers(self):
        result = []
        for user in self._raw_subscribers():
            member = api.user.get(user)
            if member:
                result.append(member)
        return result
            
    def email_addresses(self):
        result = []
        for subscriber in self.subscribers():
            result.append(
                '%s <%s>' % (
                    subscriber.getProperty('fullname'),
                    subscriber.getProperty('email'),
                )
            )
        return result
