from tqdm import tqdm
from progress.bar import Bar
from time import sleep
from math import *
# 定义进度条函数，参数X为进度条长度
def progresst01(X):
    p=0
    # 使用tqdm库的tqdm函数，创建进度条，参数X为进度条长度
    for i in tqdm(range(X)):
        for j in range(X):
            
            p=j*i
# 定义进度条函数，参数X为进度条长度，y为进度条名称，Z为进度条图标
def progresst02(X,y="Progressing",Z="█"):
        # 使用progress.bar库的Bar函数，创建进度条，参数X为进度条长度，y为进度条名称，Z为进度条图标
        with Bar(y,max=X,fill=Z) as bar:
            for i in range(X):
                for j in range(X):
                    p=j*i
                # 调用bar.next()函数，进度条每次增加1
                bar.next()
# 定义进度条函数，参数X为进度条长度
def progresst03(X):
    # 使用tqdm.rich库的trange函数，创建进度条，参数X为进度条长度
    from tqdm.rich import trange
    for i in trange(X):
        for j in range(X):
            p=j*i
# 定义计算绝对值函数，参数X为数字
def jdzt(X):
    # 如果X为0，则返回0
    if X==0:
        print(0)
    # 如果X小于0，则返回X的绝对值
    elif X<0:
        print(-X)
    # 如果X大于0，则返回X的绝对值
    else:
        print(X)  
# 定义计算阶乘函数，参数X为数字
def jct(X):
    # 计算并返回X的阶乘
    print(factorial(X))   
# 定义查找炸弹函数，参数nums为数组
def findbombt(nums):
    # 获取数组nums的长度
    n = len(nums)
    # 遍历数组nums，从索引0开始，每次循环增加4
    for i in range(n - 4):
        # 初始化乘积为1
        product = 1
        # 遍历数组nums，从索引i开始，每次循环增加4
        for j in range(i, i + 4):
            # 乘积乘以数组nums中的元素
            product *= nums[j]
        # 如果乘积等于数组nums中从索引i开始，每次循环增加4的元素之和
        if product == sum(nums[i:i + 4]):
            # 打印炸弹找到了
            print("炸弹找到了：", nums[i:i + 4])         
# 定义说明函数
def magt():
    # 打印函数的示例
    print('''   #使用示例
                # progresst_01(进度时长) tqdm进度条
                # progresst_02(进度时长,"进度名称","自定义图标") progress.bar进度条
                # progresst_03(进度时长) tqdm_rich进度条(注：使用时进度条极小几率可能频闪)
                # jdzt(数字) 返回绝对值
                # jct(数字) 计算并返回阶乘
                # ''')