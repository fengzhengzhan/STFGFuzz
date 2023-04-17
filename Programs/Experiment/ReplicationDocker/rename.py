import os
import re


class FileOperation:
    def __init__(self, log):
        self.log = log

    def gainAllFilepath(self, path: str) -> list:
        filepath_list = []
        for root, dirs, files in os.walk(path):
            # print(root, dirs, files)
            for file in files:
                file_path = os.path.join(root, file)
                # print(file_path)
                filepath_list.append(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                # print(dir_path)
                filepath_list.append(dir_path)
        return filepath_list

    def renameFile(self, src_path, dst_path):
        with open(self.log, "a+") as f:
            f.write("{} : {} , {} \n".format("rename", src_path, dst_path))
        os.rename(src_path, dst_path)

    def renameFileSymboltoSymbol(self, path: str, src_symbol, dst_symbol):
        filepath_list = self.gainAllFilepath(path)
        # print(filepath_list)
        for filepath in filepath_list:
            filename = re.split("/", filepath)[-1]
            # print(filename)
            if re.search(src_symbol, filename):
                # print(filepath)
                dst_filepath = filepath.replace(src_symbol, dst_symbol)
                # print(dst_filepath)
                self.renameFile(filepath, dst_filepath)

def main():
    FileOperation("rename.log").renameFileSymboltoSymbol("/home/fzz/Desktop/STFGFuzz/", ":", "_")


if __name__ == '__main__':
    main()
