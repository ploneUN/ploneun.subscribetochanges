from collective.grok import gs
from ploneun.subscribetochanges import MessageFactory as _

@gs.importstep(
    name=u'ploneun.subscribetochanges', 
    title=_('ploneun.subscribetochanges import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ploneun.subscribetochanges.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
