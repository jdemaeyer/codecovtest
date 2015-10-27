from twisted.internet import defer


@defer.inlineCallbacks
def good_generator():
    yield defer.succeed(None)


@defer.inlineCallbacks
def bad_generator():
    yield defer.fail(ValueError())
