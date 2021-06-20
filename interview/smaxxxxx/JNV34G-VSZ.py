# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def check_neighbour(A, row_ind, col_ind, num_rows, num_cols):
    if A[row_ind][col_ind] == 0:
        return;
    curr_area = A[row_ind][col_ind]
    A[row_ind][col_ind] = 0
    if row_ind + 1 < num_rows and A[row_ind+1][col_ind] == curr_area:
        check_neighbour(A, row_ind+1, col_ind, num_rows, num_cols)
    if row_ind - 1 >= 0 and A[row_ind - 1][col_ind] == curr_area:
        check_neighbour(A, row_ind - 1, col_ind, num_rows, num_cols)
    if col_ind + 1 < num_cols and A[row_ind][col_ind + 1] == curr_area:
        check_neighbour(A, row_ind, col_ind + 1, num_rows, num_cols)
    if col_ind - 1 >= 0 and A[row_ind][col_ind - 1] == curr_area:
        check_neighbour(A, row_ind, col_ind - 1, num_rows, num_cols)
    

def solution(A):
    # write your code in Python 3.6
    res = 0
    num_rows = len(A)
    num_cols = len(A[0])
    for row_ind in range(num_rows):
        for col_ind in range(num_cols):
            if A[row_ind][col_ind] > 0:
                check_neighbour(A, row_ind, col_ind, num_rows, num_cols)
                res += 1
    return res


