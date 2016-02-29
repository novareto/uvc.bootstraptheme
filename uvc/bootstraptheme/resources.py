# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('uvc.bootstraptheme', 'static')

bootstrap_css = Resource(
    library, 'site.css', compiler='less',
    source='site.less')

bootstrap_js = Resource(library,'node_modules/bootstrap/dist/js/bootstrap.min.js', depends=[jquery,])


bootstrap = Group([bootstrap_css, bootstrap_js])

main_css = Resource(library, 'main.css', depends=[bootstrap])
