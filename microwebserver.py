import tornado.ioloop
import tornado.web
from bluezero import microbit
from datetime import datetime
import time
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("I am alive")
        
class ComeDownHandler(tornado.web.RequestHandler):
    def get(self):
        sendText("Come Down!")
        self.write("Done.")
        
class FoodsReadyHandler(tornado.web.RequestHandler):
    def get(self):
        sendText("Foods Ready!")
        self.write("Done.")

def sendThrice(text):
    ubit.text = text
    ubit.text = text
    ubit.text = text
    
def sendText(text):
    log("about to run send text")
    try:
        sendThrice(text)
        log("sent text")
    except:
        log("about to connect")
        ubit.connect()
        sendThrice(text)
        log("sent text")
 
def log(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time+" "+message, flush=True)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/comedown", ComeDownHandler),
    (r"/foodsready", FoodsReadyHandler)
])

ubit = microbit.Microbit(adapter_addr="b8:27:eb:66:59:7e",
                                 device_addr="fa:d9:1d:ed:cf:53",
                                 accelerometer_service=True,
                                 button_service=True,
                                 led_service=True,
                                 magnetometer_service=False,
                                 pin_service=False,
                                 temperature_service=True)
        
if __name__ == "__main__":
    application.listen(8080)
    
    log("about to connect")
    succeeded = False
    while not succeeded:
        try:
            ubit.connect()
            succeeded = True
        except:
            log("Connect failed, will try again.")
            time.sleep(5)
    log("after connect")
    tornado.ioloop.IOLoop.instance().start()


