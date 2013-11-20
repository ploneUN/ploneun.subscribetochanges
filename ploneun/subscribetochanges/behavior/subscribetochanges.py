from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from ploneun.subscribetochanges.interfaces import ISubscribeToChangesCapable
from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from ploneun.subscribetochanges import MessageFactory as _

class ISubscribeToChanges(form.Schema, ISubscribeToChangesCapable):
    """
       Marker/Form interface for Subscribe To Changes
    """

    # -*- Your Zope schema definitions here ... -*-

alsoProvides(ISubscribeToChanges,IFormFieldProvider)
