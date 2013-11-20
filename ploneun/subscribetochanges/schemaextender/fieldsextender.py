from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from Products.Archetypes import atapi
from Products.ATContentTypes.interfaces import IATContentType
from zope.interface import Interface
from five import grok
from ploneun.subscribetochanges.interfaces import (
    IProductSpecific,
    ISubscribeToChangesEnabled
)
from ploneun.subscribetochanges import MessageFactory as _

# Visit http://pypi.python.org/pypi/archetypes.schemaextender for full 
# documentation on writing extenders

class ExtensionLinesField(ExtensionField, atapi.LinesField):
    pass

class FieldsExtender(grok.Adapter):

    # This applies to all AT Content Types, change this to
    # the specific content type interface you want to extend
    grok.context(ISubscribeToChangesEnabled)
    grok.name('ploneun.subscribetochanges.fieldsextender')
    grok.implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    grok.provides(IOrderableSchemaExtender)

    layer = IProductSpecific

    fields = [
        ExtensionLinesField(
            'ploneun_changesubscribers',
            required=False,
            schemata='settings',
            widget=atapi.LinesField._properties['widget'](
                label=_(u'Users subscribing to changes'),
            )
        )
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, schematas):
        # you may reorder the fields in the schemata here
        return schematas
