import matplotlib.pyplot as plt


# cve, program_name, no, distance, d+c, d+1/c  (s)

pri_data = [
    # ["CVE-2017-10686", "nasm", ""],
    ["lava292", "file", "7s", "6s", "6s", "6s"],
    ["CVE-2019-6455", "rec2csv", "4s", "5s", "4s", "4s"],
    ["CVE-2017-7210", "objdump", "60s", "47s", "49s", "44s"],
    # ["", "listswf", "", "", "", ""],
    ["", "swftophp", "", "", "", ""],
    ["", "mjs-bin", "16s", "14s", "14s", "14s"],
    # ["", "nasm", "", "", "", ""],
    ["", "c++flit", "", "", "", ""],
]

# 1. no FIFO
# priority_value = 0
# 2. distance
# priority_value = distance
# 3. distance + coverage
# priority_value = int(distance * bit_dis + (coverage) % cover_multiple * bit_cover)
# 4. distance + 1/coverage
# priority_value = int(distance * bit_dis + (1 / (coverage + 1)) * cover_multiple * bit_cover)
