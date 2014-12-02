# -*- coding: utf-8 -*-

import uvclight
from zope.interface import Interface
from .resources import main_css


class Layout(uvclight.Layout):
    uvclight.context(Interface)

    template = uvclight.get_template('layout.cpt', __file__)
    base = "/"

    def __call__(self, content, **ns):
        main_css.need()
#        main_js.need()
        if 'view' in ns:
            self.title = getattr(ns['view'], 'title', u'KUVB')
        else:
            self.title = u'Fernlehrgang'
        return uvclight.Layout.__call__(self, content, **ns)
