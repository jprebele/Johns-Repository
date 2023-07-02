# John Rebeles
# PSID: 2039426

def equation_solution(u_input_1, u_input_2, u_input_3, u_input_4, u_input_5, u_input_6):
    solution_status = True
    for i in range(-10, 11):
        for j in range(-10, 11):
            if (u_input_1 * i + u_input_2 * j == u_input_3) and ((u_input_4 * i) + (u_input_5 * j) == u_input_6):
                print(i, j)
                return solution_status
    solution_status = False
    return solution_status


user_input_1 = int(input())
user_input_2 = int(input())
user_input_3 = int(input())
user_input_4 = int(input())
user_input_5 = int(input())
user_input_6 = int(input())


equation_s = equation_solution(user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6)

if equation_s is False:
    print("No solution")
