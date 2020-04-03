from datetime import datetime

def timer():
    dt_obj = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
    timestamp = round(dt_obj.timestamp() * 1000)
    return timestamp
