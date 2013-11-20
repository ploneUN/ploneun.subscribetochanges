from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from ploneun.subscribetochanges.interfaces import ISubscribeToChangesEnabled
from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from ploneun.subscribetochanges import MessageFactory as _

class ISubscribeToChanges(form.Schema, ISubscribeToChangesEnabled):
    """
       Marker/Form interface for Subscribe To Changes
    """

    # -*- Your Zope schema definitions here ... -*-
    model.fieldset(
        'settings',
        label=_(u"Settings"),
        fields=['ploneun_changesubscribers']
    )

    ploneun_changesubscribers = schema.List(
        title=_(u'Users subscribing to changes'),
        required=False,
    )

alsoProvides(ISubscribeToChanges,IFormFieldProvider)
