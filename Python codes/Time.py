import time

class Consoletimer():
    def __init__(self):
        print("GMT Time: ",time.asctime(time.gmtime()))

    def localtime(self):
        print("Local time: ",time.asctime(time.localtime()))

    def processtime(self):
        print("Process time: ",time.process_time())

    

timer=Consoletimer()
timer.localtime()
timer.processtime()

        
