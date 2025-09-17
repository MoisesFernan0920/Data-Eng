def getSessionCount(timeout, userIds, timestamps):
    """
    Returns the total number of sessions across all users.
    A session for a user is a contiguous sequence of events such that
    no two consecutive events are separated by more than `timeout` seconds.
    """
    # Step 1: Group events by user
    user_events = {}
    for uid, ts in zip(userIds, timestamps):
        user_events.setdefault(uid, []).append(ts)

    total_sessions = 0
    # Step 2: For each user, sort timestamps and count sessions
    for times in user_events.values():
        times.sort()
        if not times:
            continue
        sessions = 1
        for prev, curr in zip(times, times[1:]):
            if curr - prev > timeout:
                sessions += 1
        total_sessions += sessions
    return total_sessions

if __name__ == '__main__':
    import os
    # Input/output for HackerRank-style test runner
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    timeout = int(input().strip())
    userIds_count = int(input().strip())
    userIds = [input().strip() for _ in range(userIds_count)]
    timestamps_count = int(input().strip())
    timestamps = [int(input().strip()) for _ in range(timestamps_count)]

    result = getSessionCount(timeout, userIds, timestamps)
    fptr.write(str(result) + '\n')
    fptr.close()