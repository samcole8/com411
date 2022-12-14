"""Allow user to run any task from Block A."""


# Import output
from output import (ascii_art,
                    escape_characters,
                    multiline_message,
                    simple_message)

from input import (ascii_robot,
                   data_types,
                   review,
                   string_operators,
                   user_input)

from decisions import (and_operator,
                       or_operator,
                       review)

from decisions.nested_decision import (nestception,
                                       nested)
                                       
from decisions.simple_decision import (comparison_operators,
                                       counter,
                                       if_,
                                       if_else,
                                       if_elif_else,
                                       modulo_operator)


def run_block_a():
    """Ask user which module to run."""
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    # basics/output/
    if response == "simple_message":
        simple_message.main()
    elif response == "multiline_message":
        multiline_message.main()
    elif response == "ascii_art":
        ascii_art.main()
    elif response == "escape_characters":
        escape_characters.main()
    # basics/input/


def run():
    """Ask user which block to run modules from."""
    while True:
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()
        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")


run()
