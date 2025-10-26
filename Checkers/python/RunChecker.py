from package.CheckerFuns.checkerFun_kkp_Fall25 import checker_kkp_fall25
from solve import *
from package.test import *


def main():
    if Question not in checker_kkp_fall25.keys():
        print("Question not found! :( please check if you entered the question properly")
        return
    test(MY_FA,Question)

if __name__=="__main__":
    main()