from pyHS100 import SmartPlug, SmartPlugException
import time, datetime

plug = SmartPlug("10.0.0.44")

with open('logfiles/some.csv', 'wb') as f:
    while True:
        try:
            stamp = str(datetime.datetime.now())
            power = str(plug.get_emeter_realtime()["power"])
            print stamp, power
            f.write(stamp+","+power+"\n")
            time.sleep(5)
        except SmartPlugException:
            pass

