from ZODB import Connection
from ZODB.serialize import ObjectWriter

orig_register = Connection.Connection.register


def register(self, obj):
    """
    Serialize early to inspect PicklingErrors

    Raise any PicklingErrors when the object is added to the
    transaction as opposed to when the transaction is committed.
    Under pudb, for example, this allows inspecting the code that made
    the change resulting in the PicklingError.
    """
    orig_register(self, obj)

    if not hasattr(self, '__is_post_mortem'):
        is_post_mortem = False
        try:
            from zope.testing.testrunner import options
            is_post_mortem = bool(options.get_options().post_mortem)
        except SystemExit:
            pass
        setattr(self, '__is_post_mortem', is_post_mortem)

    if self.__is_post_mortem:
        writer = ObjectWriter(obj)

        # Replace the pickler so that it doesn't set oids
        import cPickle as pickle
        writer._p = pickle.Pickler(writer._file, 1)

        # Try to serialize to raise piclkling errors early
        writer.serialize(obj)
