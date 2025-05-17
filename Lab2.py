

def main():
    print("ET0735 (DEVOps for AIoT) - Lab 2 Introduction to Python Programming")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("Average Temperature:", calc_average_temperature(num_list))
    print("Min and Max Temperature:", calc_min_max_temperature(num_list))
    print("Sorted Temperature List:", sort_temperature_list(num_list))


def display_main_menu():
    print("enter some numbers separated by commas : ")
    return

def get_user_input():
    numInp = input()
    inpList = numInp.split(",")
    est_list = list(map(float, inpList))
    return est_list

def calc_average_temperature( tempList):
    return sum(tempList)/len(tempList)

def calc_min_max_temperature(tempList):
    min_max_list = [min(tempList), max(tempList)]
    return min_max_list

def sort_temperature_list(tempList):
    return sorted(tempList)



if __name__ == "__main__":
    main()
