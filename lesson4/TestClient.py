from common.variables import TIME, USER, ACTION, ACCOUNT_NAME, RESPONSE, ERROR, PRESENCE
import time, unittest


def create_presence(acc_name='Guest'):
    msg_out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: acc_name
        }
    }
    return msg_out


def process_an(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        if message[RESPONSE] == 400:
            return '400 : error'
        return f'400 : {message[ERROR]}'
    raise ValueError


class Test_Client(unittest.TestCase):
    def test_create_presence(self):
        test = create_presence('Guest')
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})


    def test_process_an_True(self):
        self.assertEqual(process_an({RESPONSE: 200}), '200 : OK')

    def test_process_an_False(self):
        self.assertEqual(process_an({RESPONSE: 400}), '400 : error')


if __name__ == '__main__':
    unittest.main()



# Testing started at 16:40 ...
# Launching unittests with arguments python -m unittest /home/max/PycharmProjects/Ansy_chat/lesson4/TestClient.py in /home/max/PycharmProjects/Ansy_chat/lesson4
#
#
#
# Ran 3 tests in 0.001s
#
# OK
#
# Process finished with exit code 0
