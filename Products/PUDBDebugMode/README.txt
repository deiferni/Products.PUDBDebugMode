.. -*-doctest-*-

===============================================
Products.PUDBDebugMode
===============================================
Enable various PUDB debugging when debug-mode=on
-----------------------------------------------

When Zope is running in debug mode this product hooks PUDB debugging
into various parts of a Zope instance.  Some additional Plone specific
hooks are also included.

Requirements
------------

PUDBDebugMode has been tested with Zope 2.8.5 and 2.10 but may well
work with other versions.

Its recommended that you use an editor or IDE that can cooperate with
pudb. Emacs for example, will display the corresponding lines of the
source file alongside the pudb prompt.

Remember that this product does nothing unless zope is being run with
debug-mode=on such as with "instance/bin/zopectl fg"

Post-Mortem Debugging
---------------------

To provide for better investigation of errors, any error or exception
logged with the python logging module will invoke pudb.post_mortem() if
a traceback can be retrieved and set_trace will be invoked otherwise.
Since the Zope error_log exception handler uses the logging module
when logging errors, this provides for post mortem debugging of Zope
errors.  It is often useful, for example, to remove NotFound or
Unauthorized from the ignored exception in error_log and then
investigate such errors with PUDB.

Runcall Requests
----------------

Any request that has the key 'pudb_runcall' will call the result of the
request traversal in the debugger thus allowing for stepping through
the resulting execution.  To debug a POST or any other request which
might be tricky to insert the 'pudb_runcall' key into, use
'?toggle_runcall=1' at the end of a URL immediately preceding the
POST to set a 'pudb_runcall' cookie which will then invoke the
pudb.runcall when the POST is submitted.  Use '?toggle_runcall=1' at
the end of a URL to clear the cookie.  Remember that the cookie will
be set at the level in the hierarchy that it was set.

Alternatively, a view named 'pudb' is registered for all objects that
will simply raise an exception leaving you with the current context to
inspect.

Allow Import of pudb
-------------------

Import of the pudb module is also allowed in unprotected code such as
python scripts.
