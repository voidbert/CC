import struct
from typing import Any, Self

from .Message import Message, SerializationException

class IPerfOutput(Message):
    def __init__(self, target: str, jitter: float, bandwidth: float, loss: float):
        self.target = target
        self.jitter = jitter
        self.bandwidth = bandwidth
        self.loss = loss

    def _message_serialize(self) -> bytes:
        target_bytes = self.target.encode('utf-8')
        jitter_bytes = struct.pack('>f', self.jitter)
        bandwidth_bytes = struct.pack('>f', self.bandwidth)
        loss_bytes = struct.pack('>f', self.loss)

        return b''.join([jitter_bytes, bandwidth_bytes, loss_bytes, target_bytes])

    @classmethod
    def deserialize(cls, data: bytes) -> Self:
        if len(data) <= 12:
            raise SerializationException('Incomplete IPerfOutput message')

        try:
            jitter = struct.unpack('>f', data[:4])[0]
            bandwidth = struct.unpack('>f', data[4:8])[0]
            loss = struct.unpack('>f', data[8:12])[0]
            target = data[12:].decode('utf-8')
        except (struct.error, UnicodeDecodeError) as e:
            raise SerializationException() from e

        return cls(target, jitter, bandwidth, loss)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, IPerfOutput):
            return \
                self.target == other.target and \
                self.jitter == other.jitter and \
                self.bandwidth == other.bandwidth and \
                self.loss == other.loss

        return False

    def __repr__(self) -> str:
        return 'IPerfOutput(' \
            f'target={self.target}, ' \
            f'jitter={self.jitter}, ' \
            f'bandwidth={self.bandwidth}, ' \
            f'loss={self.loss})'
