from unittest import TestCase, main

from .. import (
    Message, MessageTask, MessageTasksRequest,
    IPOutput, IPerfOutput, PingOutput, SystemMonitorOutput,
    PingCommand
)

class MessageTests(TestCase):
    # NOTE:
    # All floating point tests must be conducted with non-repeating numbers, so that equality
    # comparisons don't fail due to lack of precision in encoding.

    def test_ip_output(self) -> None:
        initial_message = IPOutput('wlan0', True, 1000, 10, 20000, 200)
        message_bytes = initial_message.serialize()
        final_message = Message.deserialize(message_bytes)

        self.assertEqual(initial_message, final_message)

    def test_iperf_output(self) -> None:
        initial_message = IPerfOutput('1.1.1.1', 1.25, 1002.0, 0.5)
        message_bytes = initial_message.serialize()
        final_message = Message.deserialize(message_bytes)

        self.assertEqual(initial_message, final_message)

    def test_ping_output(self) -> None:
        initial_message = PingOutput('9.9.9.9', 10.125, 1.5)
        message_bytes = initial_message.serialize()
        final_message = Message.deserialize(message_bytes)

        self.assertEqual(initial_message, final_message)

    def test_system_monitor_output(self) -> None:
        initial_message = SystemMonitorOutput(20.125, 40.5)
        message_bytes = initial_message.serialize()
        final_message = Message.deserialize(message_bytes)

        self.assertEqual(initial_message, final_message)

    def test_message_tasks(self) -> None:
        initial_message = MessageTask('task-01', 20.0, PingCommand(['8.8.8.8'], 10, 1000.0))
        message_bytes = initial_message.serialize()
        final_message = Message.deserialize(message_bytes)

        self.assertEqual(initial_message, final_message)

    def test_message_tasks_request(self) -> None:
        initial_message = MessageTasksRequest()
        message_bytes = initial_message.serialize()
        final_message = Message.deserialize(message_bytes)

        self.assertEqual(initial_message, final_message)

if __name__ == '__main__':
    main()
