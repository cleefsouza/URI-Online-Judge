class conversaohoras1019:
    s1 = int(input())
    
    s2 = int(s1%60)
    m1 = int(s1/60)
    m2 = int(m1%60)
    h = int(m1/60)
    
    print('{}:{}:{}'.format(h,m2,s2))
