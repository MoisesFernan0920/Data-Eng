# Session Counter

This project provides a solution to the session counting problem, often encountered in event stream analytics.

## Problem Description

Given arrays of timestamps for user events and corresponding user IDs, the goal is to compute the total number of sessions across all users.  
A session for a user is defined as a contiguous sequence of events such that no two consecutive events for that user are separated by more than `timeout` seconds.  
If there is a gap greater than `timeout` seconds between consecutive events for the same user, a new session is started.

## Function Signature

```python
def getSessionCount(timeout: int, userIds: List[str], timestamps: List[int]) -> int
```

### Parameters

- `timeout`: int  
  The maximum allowed gap (in seconds) between two consecutive events for a session.

- `userIds`: List[str]  
  The user ID for each event.

- `timestamps`: List[int]  
  The timestamp (in seconds) for each event.

### Returns

- An integer denoting the total number of sessions across all users.

## Example

```python
timeout = 10
userIds = ["u1", "u1", "u1", "u2", "u2", "u2", "u2"]
timestamps = [2, 9, 25, 1, 12, 30]

# Output: 4
```

#### Explanation

| User | Timestamps    | Sessions          | Session Count |
|------|--------------|-------------------|--------------|
| u1   | [2, 9, 25]   | [2, 9], [25]      | 2            |
| u2   | [1, 12, 30]  | [1, 12], [30]     | 2            |

Total sessions: 2 (u1) + 2 (u2) = **4**

## Usage

1. Place the `get_session_count.py` script in your project directory.
2. Make sure `timeout`, `userIds`, and `timestamps` are provided as per the input format.
3. Run the script with the required input. For competitive programming or automated judging, ensure your input matches the required format.

## Input Format for Custom Testing

1. The first line contains an integer, `timeout`.
2. The second line contains an integer, `n`, the number of events.
3. The next `n` lines each contain a string, `userIds[i]`.
4. The next line contains an integer, `n`, the number of timestamps.
5. The next `n` lines each contain an integer, `timestamps[i]`.

## Constraints

- 1 ≤ timeout ≤ 10⁹
- 1 ≤ n ≤ 2 × 10⁵
- 1 ≤ length of userIds[i] ≤ 10
- 0 ≤ timestamps[i] ≤ 10⁹
- Each user ID is an alphanumeric string

## License

This project is open-source and free to use.