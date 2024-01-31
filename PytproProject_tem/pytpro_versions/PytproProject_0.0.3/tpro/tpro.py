from tqdm import tqdm
from progress.bar import Bar
from time import sleep

def progresst_01(X):
    p=0
    for i in tqdm(range(X)):
        for j in range(X):
            
            p=j*i
def progresst_02(X,y="Progressing",Z="█"):
        with Bar(y,max=X,fill=Z) as bar:
            for i in range(X):
                for j in range(X):
                    p=j*i
                bar.next()
def progresst_03(X):
    from tqdm.rich import trange
    for i in trange(X):
        for j in range(X):
            p=j*i
def mag():
    print('''   #使用示例
                # progresst_01(进度时长) tqdm进度条
                # progresst_02(进度时长,"进度名称","自定义图标") progress.bar进度条
                # progresst_03(进度时长) tqdm_rich进度条(注：使用时进度条极小几率可能频闪)''')
