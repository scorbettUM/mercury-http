class Timeouts:

    def __init__(self, connect_timeout: int=5, socket_read_timeout: int=10, total_timeout: int=60) -> None:
        self.connect_timeout = connect_timeout
        self.socket_read_timeout = socket_read_timeout
        self.total_timeout = total_timeout