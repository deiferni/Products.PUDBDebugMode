import pudb

from Products.SiteErrorLog import SiteErrorLog

from Products.PUDBDebugMode import pudblogging

orig_raising = SiteErrorLog.SiteErrorLog.raising

def raising(self, info):
    """Catch the traceback and bypass pudblogging"""
    def error(msg, *args, **kw):
        return pudblogging.orig_error(
            SiteErrorLog.LOG, msg, *args, **kw)
    SiteErrorLog.LOG.error = error
    result = orig_raising(self, info)
    if result:
        pudb.post_mortem(info[2])
    del SiteErrorLog.LOG.error
    return result
