for one in comparison_diffreport:
    print(one)
    content = str(str(one.mutseed) + "\n" +
                  str(one.sttype) + "\n" +
                  str(one.init_sttrace) + "\n" +
                  str(one.mut_sttrace) + "\n" +
                  str(one.startguard) + "\n" +
                  str(one.endguard) + "\n" +
                  str(one.stpcguard) + "\n" +
                  "\n")
    print(content)
    with open("test.txt", "a+", ) as f:
        f.write(content)
raise Exception