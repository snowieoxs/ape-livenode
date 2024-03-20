from ape.api import ProviderAPI


class LiveNodeProvider(ProviderAPI):
    _is_connected: bool = False

    def connect(self):
        self._is_connected = True

    @property
    def chain_id(self) -> int:
        return 50
