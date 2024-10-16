from datetime import datetime, timedelta

def time_ago(from_datetime):
    diff = datetime.now() - from_datetime
    seconds = diff.total_seconds()

    if seconds < 60:
        return "%d seconds ago" % seconds
    elif seconds < 3600:
        return "%d minutes ago" % (seconds // 60)
    elif seconds < 86400:
        return "%d hours ago" % (seconds // 3600)
    else:
        return "%d days ago" % (seconds // 86400)