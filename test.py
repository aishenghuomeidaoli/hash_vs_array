import os
import random
import time


def hash_vs_arrary(total_nums, target_nums, test_times):
    """

    :param total_nums: 样本总数量
    :param target_nums: 查找的目标元素数量
    :param test_times: 测试次数
    :return:
    """
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'gameofthrones.txt')
    all_data_list = list()
    all_data_set = set()
    target_data = list()

    # 随机生成目标元素索引
    target_data_index = set(random.sample(range(total_nums), target_nums))
    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count in target_data_index:
                target_data.append(line)

            if count < total_nums:
                all_data_list.append(line)
                all_data_set.add(line)
            else:
                break
    print('generating data set finished')

    start = time.time()
    for i in range(test_times):
        for line in target_data:
            if line in all_data_list:
                pass

    break_point = time.time()
    for i in range(test_times):
        for line in target_data:
            if line in all_data_set:
                pass

    end = time.time()

    print('list time is ', break_point - start)
    print('set time is ', end - break_point)


if __name__ == "__main__":
    hash_vs_arrary(10000, 1000, 100)
