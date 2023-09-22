import unittest

from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR


def process_client_message(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and message[USER][
        ACCOUNT_NAME] == "Guest":
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'

    }


class TestServer(unittest.TestCase):
    def test_process_client_message(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
                         {RESPONSE: 200})

    def test_process_client_message_400(self):
        # Отсутствует ключ ACTION со значением PRESENCE.
        self.assertEqual(process_client_message({TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
                         {RESPONSE: 400, ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()



# Testing started at 17:06 ...
# Launching unittests with arguments python -m unittest /home/max/PycharmProjects/Ansy_chat/lesson4/TestServer.py in /home/max/PycharmProjects/Ansy_chat/lesson4
#
#
#
# Ran 2 tests in 0.001s
#
# OK
#
# Process finished with exit code 0