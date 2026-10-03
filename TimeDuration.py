# Rahul's Study Duration Problem

# Input number of works
N = int(input())

for _ in range(N):
    # Input start and end times
    SH, SM, EH, EM = map(int, input().split())

    # Convert both times to minutes
    start_minutes = SH * 60 + SM
    end_minutes = EH * 60 + EM

    # Calculate duration in minutes
    duration = end_minutes - start_minutes

    # Convert duration back to hours and minutes
    hours = duration // 60
    minutes = duration % 60

    # Print the result
    print(hours, minutes)