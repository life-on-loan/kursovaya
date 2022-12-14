import copy
import sys


def get_step(mas, pre_step):
    global second_sosed_index, opponent_index

    if pre_step == (-1, -1):
        chetn = 0
        nechetn = 0
        peremena = 0
        for k in range(len(mas)):
            for m in range(len(mas)):
                if peremena % 2 == 0:
                    if k % 2 == 0 and m % 2 != 0:
                        chetn += mas[k][m]
                    else:
                        nechetn += mas[k][m]
                else:
                    if k % 2 != 0 and m % 2 == 0:
                        chetn += mas[k][m]
                    else:
                        nechetn += mas[k][m]
            peremena += 1
        n = (len(mas) - 1) / 2
        peremena = 0
        result = (-1, -1)
        max_value = -1
        if chetn > nechetn:
            for k in range(int(n) - 1, int(n) + 2):
                for m in range(int(n) - 1, int(n) + 2):
                    if peremena % 2 == 0:
                        if k % 2 == 0 and m % 2 != 0 and mas[k][m] > max_value:
                            max_value = mas[k][m]
                            result = (k, m)
                    else:
                        if k % 2 != 0 and m % 2 == 0 and mas[k][m] > max_value:
                            max_value = mas[k][m]
                            result = (k, m)
                peremena += 1
        else:
            for k in range(int(n) - 1, int(n) + 2):
                if k % 2 == 1:
                    peremena += 1
                for m in range(int(n) - 1, int(n) + 2):
                    if peremena % 2 == 0:
                        if k % 2 == 0 and m % 2 == 0 and mas[k][m] > max_value:
                            max_value = mas[k][m]
                            result = (k, m)
                    else:
                        if k % 2 != 0 and m % 2 != 0 and mas[k][m] > max_value:
                            max_value = mas[k][m]
                            result = (k, m)
                peremena += 1
        if result == (-1, -1):
            return (n + 1, n + 1)
        return result
    else:
        copy_mas = copy.deepcopy(mas)
        copy_mas[pre_step[0]][pre_step[1]] = -1
        x = pre_step[0]
        y = pre_step[1]
        result = (-1, -1)
        dict_maxes = dict.fromkeys([(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)], -1)
        right_soseds_second_indexes = [(x, y + 1), (x + 1, y + 2), (x + 2, y + 1), (x + 3, y), (x + 2, y - 1),
                                       (x + 1, y - 2), (x, y - 1)]
        left_soseds_second_indexes = [(x, y - 1), (x - 1, y - 2), (x - 2, y - 1), (x - 3, y), (x - 2, y + 1),
                                      (x - 1, y + 2), (x, y + 1)]
        up_soseds_second_indexes = [(x - 1, y), (x - 2, y + 1), (x - 1, y + 2), (x, y + 3), (x + 1, y + 2),
                                    (x + 2, y + 1), (x + 1, y)]
        down_soseds_second_indexes = [(x + 1, y), (x + 2, y - 1), (x + 1, y - 2), (x, y - 3), (x - 1, y - 2),
                                      (x - 2, y - 1), (x - 1, y)]
        right_opponent_indexes = [(x + 1, y + 1), (x + 2, y), (x + 1, y - 1)]
        left_opponent_indexes = [(x - 1, y - 1), (x - 2, y), (x - 1, y + 1)]
        down_opponent_indexes = [(x + 1, y - 1), (x, y - 2), (x - 1, y - 1)]
        up_opponent_indexes = [(x - 1, y + 1), (x, y + 2), (x + 1, y + 1)]
        for sosed in dict_maxes.keys():
            if sosed[0] < len(copy_mas) and sosed[1] < len(copy_mas) and sosed[0] >= 0 and sosed[1] >= 0 and \
                    copy_mas[sosed[0]][sosed[1]] > -1:
                dict_maxes[sosed] = mas[sosed[0]][sosed[1]]
                result = sosed
                if sosed == (x + 1, y):
                    second_sosed_index = right_soseds_second_indexes
                    opponent_index = right_opponent_indexes
                if sosed == (x, y - 1):
                    second_sosed_index = down_soseds_second_indexes
                    opponent_index = down_opponent_indexes
                if sosed == (x - 1, y):
                    second_sosed_index = left_soseds_second_indexes
                    opponent_index = left_opponent_indexes
                if sosed == (x, y + 1):
                    second_sosed_index = up_soseds_second_indexes
                    opponent_index = up_opponent_indexes
                for second_sosed in second_sosed_index:
                    if second_sosed[0] < len(mas) and second_sosed[1] < len(mas) and second_sosed[0] >= 0 and \
                            second_sosed[1] >= 0 and mas[second_sosed[0]][second_sosed[1]] > -1:
                        if opponent_index[0][0] >= 0 and opponent_index[0][0] < len(mas)\
                                and opponent_index[0][1] >= 0 and opponent_index[0][1] < len(mas)\
                                and mas[opponent_index[0][0]][opponent_index[0][1]] == -1:
                            copy_mas[second_sosed_index[0][0]][second_sosed_index[0][1]] = 0
                            copy_mas[second_sosed_index[1][0]][second_sosed_index[1][1]] = 0
                        if opponent_index[1][0] >= 0 and opponent_index[1][0] < len(mas) \
                                and opponent_index[1][1] >= 0 and opponent_index[1][1] < len(mas)\
                                and mas[opponent_index[1][0]][opponent_index[1][1]] == -1:
                            copy_mas[second_sosed_index[3][0]][second_sosed_index[3][1]] = 0
                        if opponent_index[2][0] >= 0 and opponent_index[2][0] < len(mas) \
                                and opponent_index[2][1] >= 0 and opponent_index[2][1] < len(mas)\
                                and mas[opponent_index[2][0]][opponent_index[2][1]] == -1:
                            copy_mas[second_sosed_index[5][0]][second_sosed_index[5][1]] = 0
                            copy_mas[second_sosed_index[6][0]][second_sosed_index[6][1]] = 0
                        if opponent_index[0][0] >= 0 and opponent_index[0][0] < len(mas) \
                                and opponent_index[0][1] >= 0 and opponent_index[0][1] < len(mas)\
                                and opponent_index[1][0] >= 0 and opponent_index[1][0] < len(mas)\
                                and opponent_index[1][1] >= 0 and opponent_index[1][1] < len(mas)\
                                and mas[opponent_index[0][0]][opponent_index[0][1]] == -1\
                                and mas[opponent_index[1][0]][opponent_index[1][1]] == -1:
                            copy_mas[second_sosed_index[2][0]][second_sosed_index[2][1]] = 0
                        if opponent_index[2][0] >= 0 and opponent_index[2][0] < len(mas) \
                                and opponent_index[2][1] >= 0 and opponent_index[2][1] < len(mas)\
                                and opponent_index[1][0] >= 0 and opponent_index[1][0] < len(mas) \
                                and opponent_index[1][1] >= 0 and opponent_index[1][1] < len(mas)\
                                and mas[opponent_index[2][0]][opponent_index[2][1]] == -1 \
                                and mas[opponent_index[1][0]][opponent_index[1][1]] == -1:
                            copy_mas[second_sosed_index[4][0]][second_sosed_index[4][1]] = 0
                        dict_maxes[sosed] += copy_mas[second_sosed[0]][second_sosed[1]]
        sorted_dict_maxes = dict(sorted(dict_maxes.items(), key=lambda item: item[1]))
        max = next(reversed(sorted_dict_maxes))
        max_value = dict_maxes[max]
        sorted_dict_maxes.pop(max)
        pre_max = next(reversed(sorted_dict_maxes))
        pre_max_value = dict_maxes[pre_max]
        sorted_dict_maxes.pop(pre_max)
        pre_pre_max = next(reversed(sorted_dict_maxes))
        pre_pre_max_value = dict_maxes[pre_pre_max]
        sorted_dict_maxes.pop(pre_pre_max)
        pre_pre_pre_max = next(reversed(sorted_dict_maxes))
        pre_pre_pre_max_value = dict_maxes[pre_pre_pre_max]
        sorted_dict_maxes.clear()
        if max_value == pre_max_value or max_value == pre_pre_max_value or max_value == pre_pre_pre_max_value:
            dict_opponent_maxes = dict.fromkeys([(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)], -1)
            for sosed in dict_opponent_maxes.keys():
                dict_opponent_maxes[sosed] = 0
                if sosed[0] < len(mas) and sosed[1] < len(mas) and sosed[0] >= 0 and sosed[1] >= 0 and \
                        mas[sosed[0]][sosed[1]] > -1:
                    if sosed == (x + 1, y):
                        opponent_index = right_opponent_indexes
                    if sosed == (x, y - 1):
                        opponent_index = down_opponent_indexes
                    if sosed == (x - 1, y):
                        opponent_index = left_opponent_indexes
                    if sosed == (x, y + 1):
                        opponent_index = up_opponent_indexes
                    for opponent_hod in opponent_index:
                        if opponent_hod[0] < len(mas) and opponent_hod[1] < len(mas) \
                                and opponent_hod[0] >= 0 and opponent_hod[1] >= 0 \
                                and mas[opponent_hod[0]][opponent_hod[1]] > -1:
                            dict_opponent_maxes[sosed] += mas[opponent_hod[0]][opponent_hod[1]]
            if max_value == pre_max_value and max_value != pre_pre_max_value and max_value != pre_pre_pre_max_value:
                return max if dict_opponent_maxes.get(max) <= dict_opponent_maxes.get(pre_max) else pre_max
            elif max_value == pre_max_value and max_value == pre_pre_max_value and max_value != pre_pre_pre_max_value:
                if dict_opponent_maxes.get(max) < dict_opponent_maxes.get(pre_max) and dict_opponent_maxes.get(
                        max) < dict_opponent_maxes.get(pre_pre_max):
                    return max
                if dict_opponent_maxes.get(pre_max) < dict_opponent_maxes.get(max) and dict_opponent_maxes.get(
                        pre_max) < dict_opponent_maxes.get(pre_pre_max):
                    return pre_max
                else:
                    return pre_pre_max
            else:
                sorted_dict_mins = dict(sorted(dict_opponent_maxes.items(), key=lambda item: item[1]))
                min = next(iter(sorted_dict_mins))
                return min
        else:
            return max
        return result


if __name__ == '__main__':
    #первый ход
    data = []
    while True:
        values = input()
        if values:
            data.append(values)
        else:
            break
    matrix_str = [data[i].split(" ") for i in range(1, int(data[0]) + 1)]
    matrix = []
    for i in matrix_str:
        matrix.append(list(map(int, i)))
    x = int(data[int(data[0]) + 1].split(" ")[0])
    y = int(data[int(data[0]) + 1].split(" ")[1])
    answer = get_step(matrix, (x, y))
    matrix[answer[0]][answer[1]] = -1
    #последующие ходы
    while True:
        values = sys.stdin.readline().split("\n")
        x = int(values[0].split(" ")[0])
        y = int(values[0].split(" ")[1])
        matrix[x][y] = -1
        answer = get_step(matrix, (x, y))
        matrix[answer[0]][answer[1]] = -1
        sys.stdout.write(str(answer[0]) + ' ' + str(answer[1]))