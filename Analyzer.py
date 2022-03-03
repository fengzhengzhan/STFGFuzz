

def traceAyalysis(out_info: str):
    out_info = out_info.decode('UTF-8')
    each_line_list: list[str] = out_info.split("\n")
    for each_line in each_line_list:
        each = each_line.split(" ")
        print(each)




