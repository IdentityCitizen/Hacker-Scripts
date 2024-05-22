import gdb

# Function to automate stepping through a function and checking register values
def step_and_check_function(function_name):
    # Set a breakpoint at the beginning of the function
    gdb.execute("break " + function_name)
    
    # Run the program
    gdb.execute("run")

    file1 = open("extract.txt", "w")
    # Step through the function
    while True:
        gdb.execute("step")
        reg_list = ["$rax","$rbx","$rcx","$rdx","$rsp","$rbp","$rsi","$rdi","$rip","$r8","$r9","$r10","$r11","$r12","$r13","$r14","$r15"]
        for reg in reg_list:
            i = 0
            while i < 30:
                hexVal = hex(i)
                string_flag = str(gdb.execute(f"x/s {reg} + -{hexVal}", False, True))
                # Check register values and ignore empty/irrelevant values
                if "Cannot access memory" not in string_flag and "<" not in string_flag:
                    file1.write(f"{reg}:" + string_flag)
                # Check if we've reached the end of the function
                i += 1
            x = 0
            while x < 30:
                hexVal = hex(x)
                string_flag = str(gdb.execute(f"x/s {reg} + {hexVal}", False, True))
                # Check register values and ignore empty/irrelevant values
                if "Cannot access memory" not in string_flag and "<" not in string_flag:
                    file1.write(f"{reg}:" + string_flag)
                # Check if we've reached the end of the function
                x += 1
            file1.write("\n")
        if gdb.selected_frame().name() == function_name + ' ()':
            break
    file1.close()

step_and_check_function("welcome")
# Call the function with the name of the function to inspect and the name of the flag register
