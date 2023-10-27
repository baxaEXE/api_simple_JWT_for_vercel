n = int(input())
if 1<=n<=10000:
    form = (n/10000) *100
    if form%1 == 0.0:
        print(form)
    else:
        print(int(form))