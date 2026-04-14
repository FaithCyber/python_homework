# Task 1: Diary Program

import traceback

try:
    # Open file for appending
    with open("diary.txt", "a") as file:

        first = True

        # Loop for user input
        while True:
            if first:
                user_input = input("What happened today? ")
                first = False
            else:
                user_input = input("What else? ")

            # Stop condition
            if user_input == "done for now":
                file.write(user_input + "\n")
                break

            # Write input to file
            file.write(user_input + "\n")

# Exception handling
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()

    for trace in trace_back:
        stack_trace.append(
            f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
        )

    print("An exception occurred.")
    print(f"Exception type: {type(e).__name__}")

    message = str(e)
    if message:
        print(f"Exception message: {message}")

    print(f"Stack trace: {stack_trace}")
    