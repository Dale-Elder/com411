import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.user_input as user_input
import basics.input.string_operators as string_operators
import basics.input.review as review
import basics.input.data_types as data_types
import basics.input.ascii_robot as ascii_robot
import basics.decisions.simple_decision.comparison_operators as comparison_operators
import basics.decisions.simple_decision.counter as counter
import basics.decisions.simple_decision.if_ as if_
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.modulo_operator as modulo_operator
import basics.decisions.nested_decision.nestception as nestception
import basics.decisions.nested_decision.nested as nested
import basics.decisions.and_operator as and_operator
import basics.decisions.or_operator as or_operator
import basics.decisions.review as decision_review
import basics.repetitions.while_loop.ascii as ascii
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.while_loop.len as len
import basics.repetitions.while_loop.simple as simple
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers
import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.for_loop.range as range
import basics.repetitions.for_loop.reverse as reverse
import basics.repetitions.for_loop.simple as for_loop_simple
import basics.repetitions.nested_loop.nested as nested_loop_nested
import basics.repetitions.nested_loop.nesting as nesting
import basics.functions.ascii_character as ascii_character
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values
import basics.functions.simple_function as simple_function
import basics.modules.guess_the_number as guess_the_number


def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "escape_characters":
        escape_characters.run()
    elif response == "ascii_art":
        ascii_art.run()
    elif response == "user_input":
        user_input.run()
    elif response == "string_operators":
        string_operators.run()
    elif response == "review":
        review.run()
    elif response == "data_types":
        data_types.run()
    elif response == "ascii_robot":
        ascii_robot.run()
    elif response == "comparison_operators":
        comparison_operators.run()
    elif response == "counter":
        counter.run()
    elif response == "if_":
        if_.run()
    elif response == "if_elif_else":
        if_elif_else.run()
    elif response == "if_else":
        if_else.run()
    elif response == "modulo_operator":
        modulo_operator.run()
    elif response == "nestception":
        nestception.run()
    elif response == "nested_decision":
        nested.run()
    elif response == "and_operator":
        and_operator.run()
    elif response == "or_operator":
        or_operator.run()
    elif response == "decision_review":
        decision_review.run()
    elif response == "ascii":
        ascii.run()
    elif response == "count":
        count.run()
    elif response == "factorial":
        factorial.run()
    elif response == "len":
        len.run()
    elif response == "simple":
        simple.run()
    elif response == "sum_100":
        sum_100.run()
    elif response == "sum_user_numbers":
        sum_user_numbers.run()
    elif response == "characters":
        characters.run()
    elif response == "count_down":
        count_down.run()
    elif response == "membership_operators":
        membership_operators.run()
    elif response == "range":
        range.run()
    elif response == "reverse":
        reverse.run()
    elif response == " for_loop_simple":
        for_loop_simple.run()
    elif response == "nested_loop_nested":
        nested_loop_nested.run()
    elif response == "nesting":
        nesting.run()
    elif response == "ascii_character":
        ascii_character.run()
    elif response == "ascii_code":
        ascii_code.run()
    elif response == "function_calls":
        function_calls.run()
    elif response == "function_with_loop":
        function_with_loop.run()
    elif response == "function_with_nesting":
        function_with_nesting.run()
    elif response == "function_with_parameter":
        function_with_parameter.run()
    elif response == "function_with_parameters":
        function_with_parameters.run()
    elif response == "multiple_functions":
        multiple_functions.run()
    elif response == "return_values":
        return_values.run()
    elif response == "simple_function":
        simple_function.run()
    elif response == "guess_the_number":
        guess_the_number.run()
    else:
        print("Invalid option!")


def run():
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
