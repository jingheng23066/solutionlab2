def main():
    print("ET0735 (DEVOps for AIoT) - Lab 2 Introduction to P")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))

def display_main_menu():
    print("enter some numbers separated by commas 1")
    return

def get_user_input():
    numInp = input()
    inpList = numInp.split(",")
    return inpList

def calc_average_temperature( tempList ):
    est_list = list(map(int, tempList))
    return sum(est_list)/len(est_list)

def calc_min_max_temperature(tempList):
    est_list = list(map(int, tempList))
    min_max_list = [max(est_list), min(est_list)]
    return min_max_list


if __name__ == "__main__":
    main()
