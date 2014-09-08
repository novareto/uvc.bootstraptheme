# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import uvclight

from grokcore.component import adapter, implementer
from zope.interface import Interface
from cromlech.browser import ITemplate
from dolmen.forms.base.interfaces import IForm


@adapter(IForm, Interface)
@implementer(ITemplate)
def menu_template(context, request):
    """default template for the menu"""
    return uvclight.get_template('form.cpt', __file__)

