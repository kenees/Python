'''
 文本颜色设置
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER+'HEADER的颜色字体?')
print(bcolors.OKBLUE+'OKBLUE的颜色字体?')
print(bcolors.OKGREEN+'OKGREEN的颜色字体?')
print(bcolors.WARNING+'WARNING的颜色字体?'+bcolors.ENDC)
print(bcolors.FAIL+'FAIL的颜色字体?')
print(bcolors.ENDC+'ENDC字体?')
print(bcolors.BOLD+'BOLD字体?')
print(bcolors.UNDERLINE+bcolors.FAIL+bcolors.BOLD+'UNDERLINE的字体? 加粗，下划线，fail'+bcolors.ENDC)
