import os

cve_list = ['CVE-2014-0160', 'CVE-2015-8540',
            'CVE-2016-4487', 'CVE-2016-4488', 'CVE-2016-4489', 'CVE-2016-4490',
            'CVE-2016-4491', 'CVE-2016-4492', 'CVE-2016-4493', 'CVE-2016-6131', ]


def createCVEFolder(cve_list):
    for cve in cve_list:
        if not os.path.exists(cve):
            os.makedirs(cve)
            print("Create Successful: {}".format(os.getcwd() + "/" + cve))

def cpSourceFiles():
    cve2016 = ['CVE-2016-4487', 'CVE-2016-4488', 'CVE-2016-4489', 'CVE-2016-4490',
                'CVE-2016-4491', 'CVE-2016-4492', 'CVE-2016-4493', 'CVE-2016-6131', ]
    for dir in cve2016:
        #rmcom = "rm -rf "+dir+"/gcc"
        #os.system(rmcom)
        #print(rmcom)
        cpcom = "cp -r binutils-gdb "+dir
        os.system(cpcom)
        print(cpcom)


if __name__ == "__main__":
    # createCVEFolder(cve_list)
    cpSourceFiles()
