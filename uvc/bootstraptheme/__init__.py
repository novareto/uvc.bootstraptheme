import logging
logger = logging.getLogger('uvcsite.uvc.bootstraptheme')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
