import os

class TravelCrashFile:
    def __init__(self):
        pass

    def find_min_time(time_list):
        """返回给定时间字符串列表中的最小值"""
        min_time = time_list[0]  # 初始化最小值为列表中的第一个元素
        for time_str in time_list[1:]:  # 遍历列表中除第一个元素外的其它元素
            if compare_times(time_str, min_time) == time_str:  # 如果当前元素比最小值小
                min_time = time_str  # 更新最小值为当前元素
        return min_time

    def find_min_time_with_index(self, time_list):
        """返回给定时间字符串列表中的最小值和其索引"""
        min_time = min(time_list)  # 获取最小值
        min_index = time_list.index(min_time)  # 获取最小值的索引
        return min_time, min_index

    def findCrashLocation(self, path, filename, crash_id, crash_str):
        # travel all files in the path find filename file.
        list_time = []
        list_info = []
        for root, dirs, files in os.walk(path):
            # print(root, dirs, files)
            for file in files:
                # print(file, filename)
                # if (file == filename or file[-4:] == ".csv") and (file == "{}.csv".format(crash_id)):
                if (file == filename or file[-4:] == ".csv"):
                    # print(os.path.join(root, file))
                    with open(os.path.join(root, file), 'r') as f:
                        content = f.readlines()
                        # print(content)
                        for cont in content:
                            pos = cont.find(crash_str.strip())
                            # print(pos)
                            if pos != -1:
                                # print(os.path.join(root, file))
                                # print(cont.split(",")[3])
                                # print(cont.split(","))
                                list_time.append(cont.split(",")[3])
                                list_info.append("{} {}".format(os.path.join(root, file), cont.split(",")))
        min_time, min_index = self.find_min_time_with_index(list_time)
        print(min_time, min_index, list_info[min_index])


if __name__ == "__main__":
    TravelCrashFile().findCrashLocation(
        "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/",
        "crashes.csv",
        "",
        "decompile.c:237"
    )