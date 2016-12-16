from line import LineClient, LineGroup, LineContact

try:
   client = LineClient("xxxxx@gmail.com", "xxx123")
   #client = LineClient(authToken="AUTHTOKEN")
   receiver = []
   message = []
   msg_id = []

except:
   print "Login Failed"

while True:
   op_list = []
   j = 1  
   for op in client.longPoll():
      op_list.append(op)
   
   for op in op_list:
      sender   = op[0]
      receiver = op[1]
      message  = op[2]
   
   if type(receiver) is LineContact and msg_id != id(message):
      sender.sendMessage("[%s] %s\r\n %s" % (sender.name, "He is busy right now!!!", "send from bot"))
   msg_id = id(message)

