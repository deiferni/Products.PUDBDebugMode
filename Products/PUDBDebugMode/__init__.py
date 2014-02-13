"""If debug-mode=on, Monkey-patch the zpublisher_exception_hook to
call pudb.post_mortem on an error and enable import of pudb in
unprotected code.
"""

import sys

import Globals
import AccessControl

if Globals.DevelopmentMode:
    sys.modules['Products.PUDBDebugMode.Globals'] = Globals

    # Allow import of pudb in unprotected code
    AccessControl.allow_module('pudb')
    AccessControl.allow_module('pudb')
