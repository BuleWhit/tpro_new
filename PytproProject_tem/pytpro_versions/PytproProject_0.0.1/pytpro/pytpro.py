
from tqdm import tqdm
from progress.bar import Bar
from time import sleep

def progress_template_01(X):
    p=0
    for i in tqdm(range(X)):
        for j in range(X):
            p=j*i
def progress_template_02(X,y,Z="█"):
        with Bar(y,max=X,fill=Z) as bar:
            for i in range(X):
                for j in range(X):
                    p=j*i
                bar.next()

def mag():
    print('''   #使用示例
                # grogress_template_01(10) tqdm进度条
                # grogress_template_02(10,100,"█") 显示progress.bar进度条''')