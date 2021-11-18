# code to demonstrate the use of return values. #
def run():
    def sum_weights(beep_weight, bop_weight):
        summed_weight = beep_weight + bop_weight
        return summed_weight

    def calc_avg_weight(beep_weight, bop_weight):
        avg_weight = sum_weights(beep_weight, bop_weight) / 2
        return avg_weight

    def run_program():
        beep_weight = float(input("What is the weight of Beep?\n"))
        bop_weight = float(input("What is the weight of Bop?\n"))
        print("What would you like to calculate (sum or average)?")
        decision = input()
        if decision == "sum":
            answer = sum_weights(beep_weight, bop_weight)
            print(f"The sum of Beep's and Bop's weight is {answer}")
        elif decision == "average":
            answer = calc_avg_weight(beep_weight, bop_weight)
            print(f"The average of Beep's and Bop's weight is {answer}")
        else:
            print("I didn't quiet understand...")

    run_program()


if __name__ == "__main__":
    run()
