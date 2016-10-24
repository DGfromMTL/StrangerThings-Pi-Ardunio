from ArduinoInterface import ArduinoInterface
from ApiInterface import ApiInterface

api_comm= ApiInterface()
arduino_comm= ArduinoInterface()


def generateRandom():
    pass

q_pos =- 1
# Always loop listening for message from arduino
while True:        
    incoming_msg=arduino_comm.ser.readline()
    print "Received arduino message {} ".format(incoming_msg);
    if q_pos != -1:
        api_comm.remove_message(q_pos)

    (message, q_pos) = api_comm.get_next_message()
    message = ''.join(c for c in message if message.isalpha())
    message = message.lower()
    print "sending message {}".format(message)
    for letter in message:
        arduino_comm.push_message(str(letter)
