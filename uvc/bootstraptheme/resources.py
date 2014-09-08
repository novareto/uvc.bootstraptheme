# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from js.bootstrap import bootstrap_theme, bootstrap

library = Library('uvc.bootstraptheme', 'static')

main_css = Resource(library, 'main.css', depends=[bootstrap])
