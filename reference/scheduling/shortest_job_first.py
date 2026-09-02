"""Reusable reference: non-preemptive shortest-job-first scheduling."""

def average_waiting_time(durations):
 elapsed=waiting=0
 for duration in sorted(durations):waiting+=elapsed;elapsed+=duration
 return waiting/len(durations) if durations else 0.0
