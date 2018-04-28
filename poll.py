import time
from meetup_auto_rsvp import auto_rsvp


for i in range(30):
    auto_rsvp()
    time.sleep(60)