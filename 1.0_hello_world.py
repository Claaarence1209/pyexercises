"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A message and the number of times it should be displayed.
# 2. Process: A loop counts from 1 to 5 and prints the message once per count.
# 3. Out: Five numbered lines containing the chosen message.
# 4. My message is "Keep going, Junyu!" because it is a useful reminder
#    when I am learning something new.


# Store the parts that may change so the loop itself can stay the same.
message = "Keep going, Junyu!"
number_of_times = 5

# Start at 1 and stop after the chosen number so every line has a number.
for line_number in range(1, number_of_times + 1):
    print(f"{line_number}. {message}")
