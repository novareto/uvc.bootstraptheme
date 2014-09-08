# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import uvclight
from zope import interface
from dolmen.message import receive
from zope.component import getAdapters
from zope.component import getMultiAdapter
from uvc.design.canvas.managers import IAboveContent
from dolmen.viewlet.interfaces import IViewletManager


class MainNavigation(uvclight.ViewletManager):
    uvclight.context(interface.Interface)
    uvclight.name('uvc-mainnav')


class GlobalNav(uvclight.Viewlet):
    uvclight.viewletmanager(MainNavigation)
    uvclight.context(interface.Interface)
    template = uvclight.get_template('globalnav.cpt', __file__)

    @property
    def title(self):
        return uvclight.getSite().title

    def update(self):
        self.gmentries = []
        self.globalmenu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'globalmenu')
        self.globalmenu.update()
        self.globalmenu.template = uvclight.get_template(
            'globalmenu.cpt',
            __file__
        )
        self.personalmenu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'personal')
        self.personalmenu.update()
        self.personalmenu.template = uvclight.get_template(
            'personalmenu.cpt',
            __file__
        )
        self.submenus = list()
        submenus = getAdapters(
            (self.context, self.request, self.view, self.globalmenu),
            uvclight.interfaces.ISubMenu)
        for name, submenu in submenus:
            submenu.update()
            submenu.template = uvclight.get_template(
                'submenu.cpt',
                __file__
            )
            self.submenus.append(submenu)
        for entry in self.globalmenu.entries:
            self.gmentries.append(entry)
        self.gmentries += self.submenus
        setattr(self.globalmenu, 'gmentries', self.gmentries)


class FlashMessages(uvclight.Viewlet):
    uvclight.viewletmanager(IAboveContent)
    template = uvclight.get_template('flashmessage.cpt', __file__)

    def update(self):
        messages = receive(None)
        if messages
            self.messages = [msg for msg in receive(None)]
        return []
