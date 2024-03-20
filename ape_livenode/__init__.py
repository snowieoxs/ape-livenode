# Add module top-level imports here
from ape import plugins

from provider import LiveNodeProvider


@plugins.register(plugins.ProviderPlugin)
def providers():
    yield "ethereum", "local", LiveNodeProvider
