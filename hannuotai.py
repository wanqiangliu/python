def move(n,a,b,c):
    if n == 1:      # 只有一个盘子时，直接从a移动到c
        print(a,'-->',c)
        return
    move(n-1,a,c,b)     # 大于一个盘子时，开始递归，首先将n-1个盘子从a移到辅助区b
    move(1,a,b,c)       # 然后将最后一个大盘子从a移动到c
    move(n-1,b,a,c)     # 最后将原来移动到b的盘子移动到c

move(4,'A','B','C')     # 收工实验