from plone.directives import form
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.supermodel import model

from plone.dexterity.content import Item, Container

from operun.crm import MessageFactory as _


class IInvoice(model.Schema):
    """ Invoice Content Type
    """
    
    file = NamedBlobFile(
        title=_(u"Invoice"),
        description=_(u"Please upload a invoice"),
        required=False,
        )


class Invoice(Item):
    """ Invoice class
    """