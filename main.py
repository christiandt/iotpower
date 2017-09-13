from pyHS100 import SmartPlug, SmartPlugException
import time, datetime
from lookback import Lookback


plug = SmartPlug("10.0.0.44")
interval = 30
look = Lookback(4)


while True:
    try:
        stamp = str(datetime.datetime.now())
        power = float(plug.get_emeter_realtime()["power"])

        look.add_value(power)
        time.sleep(interval)

    except SmartPlugException:
        pass
