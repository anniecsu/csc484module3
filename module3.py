# initialize sessions and work/break times
completed_sessions = 0
skipped_sessions = 0
focus_time = 0
break_time = 0

# try except block for total number of sessions to start
try:
    sessions = int(input("How many Pomodoro sessions would you like to start? "))
except ValueError:
    print("Please enter a whole number")
finally:
    print("Preparing sessions...")

# try except block for counting length of each session
try:
    session_times = int(input("How many minutes would you like each session to be? "))
except ValueError:
    print("Please enter a whole number")
finally:
    print("Adding work length...")

# try except block for break times for each session
try:
    breaks = int(input("How many minutes would you like your break to be? "))
except ValueError:
    print("Please enter a whole number")
finally:
    print("Adding break length...")

# prompt user if they completed session and add to statistics
answer = input("Completed your sessions? (yes/no): ")

if answer.lower() == "yes":
    completed_sessions += 1
    focus_time += session_times
    break_time += breaks
else:
    skipped_sessions += 1

# print out statistics
print("Pomodoro Statistics")
print(f"Number of sessions planned: {sessions}")
print(f"Number of sessions completed: {completed_sessions}")
print(f"Number of sessions skipped: {skipped_sessions}")
print(f"Total focused time: {focus_time} min")
print(f"Total break time: {break_time} min")

