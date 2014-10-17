# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('uvcsite.uvc.bootstraptheme')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)


from uvc.themes.btwidgets import IBootstrapRequest


class IBootstrapThemeRequest(IBootstrapRequest):
    pass

