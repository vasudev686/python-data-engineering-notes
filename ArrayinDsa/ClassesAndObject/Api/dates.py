import datetime

import pytz
# d = datetime.datetime(2026, 9, 30)
# print(d)

# tday = datetime.date.today()
# # print(tday)
# # print(tday.weekday())
# # print(tday.isoweekday())

# tdelta = datetime.timedelta(days=7)
# # print(tday + tdelta)


# bday = datetime.date(2026, 11, 18)
# tell_bday = bday - tday
# print(tell_bday)

# dt_today = datetime.datetime.today()
# td_now = datetime.datetime.now()
# # td_istnow = datetime.datetime.istnow()
# td_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(td_now)
# # print(td_istnow)
# print(td_utcnow)

# dt = datetime.datetime(2026, 9, 30, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_ist = dt_utcnow.astimezone(pytz.timezone("Asia/Kolkata"))
print(dt_ist)


