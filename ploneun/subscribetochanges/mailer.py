from five import grok
from Products.DCWorkflow.interfaces import IAfterTransitionEvent
from zope.component import getUtility
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email import Encoders
from zope.component.interfaces import ComponentLookupError
from Products.CMFPlone.utils import safe_unicode
from plone import api
from zope.component.hooks import getSite
from ploneun.subscribetochanges.interfaces import ISubscriberManager
from ploneun.subscribetochanges.interfaces import IProductSpecific
from ploneun.subscribetochanges.interfaces import ISubscribeToChangesEnabled
from zope.lifecycleevent import IObjectModifiedEvent
from zope.globalrequest import getRequest

@grok.subscribe(ISubscribeToChangesEnabled, IObjectModifiedEvent)
def mail_notification(obj, event):
    request = getRequest()
    if not IProductSpecific.providedBy(request):
        return

    mailhost = obj.MailHost

    if not mailhost:
        raise ComponentLookupError('You must have a Mailhost utility to'
                                   'execute this action')

    from_address = obj.email_from_address
    if not from_address:
        raise ValueError('You must provide a source address for this'
                         'action or enter an email in the portal properties')

    from_name = obj.email_from_name
    source = "%s <%s>" % (from_name, from_address)

    type_title = obj.portal_types[obj.portal_type].Title()
    subject = safe_unicode(u'%s: %s have just been updated' % (
        type_title, obj.Title())
    )

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = source

    body = """A content you are following have just been updated. Visit the link
    below to view the content:

    %(url)s

    --
    This is a system message from %(site_name)s.

    """ % {
        'url': obj.absolute_url(),
        'site_name': getSite().title
    }

    body_safe = body.encode('utf-8')
    htmlPart = MIMEText(body_safe, 'plain', 'utf-8')
    msg.attach(htmlPart)

    #send email
    for recipient in ISubscriberManager(obj
            ).email_addresses(exclude=[api.user.get_current().getId()]):
        del msg['To']
        msg['To'] = recipient
        mailhost.send(msg.as_string())
