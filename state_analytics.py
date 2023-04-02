"""
Dayna Mitty Larm
Southern Utah University
CSIS-1300-01-SP23: Programming with Python

Coding Eight 
GitHub: 
Requirements: StatesANC.txt located in folder with state_analytics.py 
"""
# STATE INTO DICTIONARY
# {String("State Name"): Tuple(Name, Abbreviation, Nickname, Capital)}
STATE_INFO = {}

# INDEX CONSTANTS
NAME = 0
ABBREVIATION = 1
NICKNAME = 2
CAPITAL = 3


def main():
    """Main Driver for the state_analytics.py program. 

    Reads a .txt file and adds the information to a dictionary. Enters a loop 
    allowing the user to lookup information about a state by name, until the 
    users quits the program. """

    scan_state_file()  # Scan file to the STATE_INFO

    print_matching_first_letters()  # Print Capital Letters Fun Fact

    program_running = True
    while program_running:

        print("\nSELECT PROGRAM:")
        print("       [1] Lookup State")
        print("       [Q] Quit")

        user_input = input("SELECT: ").upper()

        match user_input:
            case "1":
                lookup_state_info()
            case "Q":
                program_running = False
                print()  # Blank Line
            case _:
                print("Program not found.")


def scan_state_file():
    """Scans a formatted .txt file into the STATE_INFO dictionary, with the 
    state name in all caps as a key and a tuple containing the state's information: 
    (State, Abbreviation, Nickname, Capital). """

    global STATE_INFO  # Write to Global variable

    # Read the file to a list[str], excluding blank lines (\n)
    state_file_contents = open("StatesANC.txt", mode="r",
                               encoding="utf-8").read().splitlines()

    for content in state_file_contents:
        # Separate the formatted information by comma
        state_list = content.split(",")
        info = tuple(state_list)  # Convert list[str] to tuple

        # Add State to dictionary
        STATE_INFO.update({info[NAME].upper(): info})


def print_matching_first_letters():
    """Prints the state capitals which share the first letter of their name with 
    the first letter of their state as: State Capital, State."""

    print("\nFun Fact!")
    print("These state capitals have the same first letter as their state:")
    print("---------------------------------------------------------------")

    # Check every state's first letter with the first letter of their capital
    for state_info in STATE_INFO:
        state = STATE_INFO.get(state_info)
        if state[NAME][0] == state[CAPITAL][0]:
            # If first letters match, print 'Capital City, State' to terminal
            print(state[CAPITAL] + ",", state[NAME])

    print("---------------------------------------------------------------\n")


def lookup_state_info():
    """Takes a user input string representing the state to lookup in the 
    STATE_INFO dictionary. If the state exists the state's information is 
    printed to the terminal. Otherwise, an error message is printed to the 
    terminal."""

    print("\n#######################################\n")

    # get the user input to an uppercase string
    user_input_state = input("    Lookup State: ").upper()

    # Look for state name in STATE_INFO dictionary
    if user_input_state in STATE_INFO:
        state = STATE_INFO.get(user_input_state)  # Get Info Tuple

        # Print State's formatted information from tuple
        print(f"""
        Information for {state[NAME]}:
        -------------------------------
        Abbreviation: {state[ABBREVIATION]}
        Nickname: {state[NICKNAME]}
        State Capitol: {state[CAPITAL]}
        -------------------------------""")

    else:
        # Print error if state is not found/does not exist
        print(f"    No Results for {user_input_state} Found.")

    print("\n#######################################")


# Main Driver
main()

# NOTES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# In this program, the name of the state is saved twice: once in all caps as
# the dictionary key and a second time in title case in the tuple of the
# state's information. More efficient data management would save the state's
# name only once, casting both the user input and dictionary key to uppercase
# to check for matching strings, but this option adds more conversions and
# unecessary lines to the code. Since the program is small, the extra memory
# space is sacraficed to increase code readability.

# The print_matching_first_letters() method is only called once at the start of
# the program, so this code could have been written into the scan_state_file()
# function, printing the capital cities and their states as the file is read
# into the dictionary, which would half the runtime taken. however, this would
# lead to unecessary code written into the file scanning portion, so the
# operations were split into two separate functions for better organization.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
