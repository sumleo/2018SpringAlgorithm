import time
number=int(input())
dalao_list=input().split(" ")
mengxin_list=input().split(" ")
mengxin_perf=[]
mengxin_inv=[]
run_set=set(range(number))
dalao_pref=[]
mengxin_match=[]
dalao_match=[]
def inv(arr,tmp):
    i=0
    dic={}
    for key in arr:
        dic[key]=i
        i=i+1
    tmp.append(dic)
count=0
count_t=0
mengxin_reverse={}
for i in range(number):
    dalao_pref.append(input().split(" "))
    mengxin_match.append(-1)
    dalao_match.append(0)
for i in range(number):
    mengxin_perf.append(input().split(" "))
    inv(mengxin_perf[i],mengxin_inv)
    mengxin_reverse[mengxin_list[i]]=i
while run_set.__len__()!=0:
    dalao_index=run_set.pop()
    dalao_name=dalao_list[dalao_index]
    #relative
    mengxin_relative_index=dalao_match[dalao_index]
    mengxin_name=dalao_pref[dalao_index][mengxin_relative_index]
    mengxin_abs_index=mengxin_reverse[mengxin_name]
    if(mengxin_match[mengxin_abs_index]==-1):
        mengxin_match[mengxin_abs_index]=dalao_index
    else:
        pre_dalao_index=mengxin_match[mengxin_abs_index]
        pre_dalao_name=dalao_list[pre_dalao_index]
        if(mengxin_inv[mengxin_abs_index][pre_dalao_name]<mengxin_inv[mengxin_abs_index][dalao_name]):
            dalao_match[dalao_index]=mengxin_relative_index+1
            run_set.append(dalao_index)
        else:
            run_set.append(pre_dalao_index)
            dalao_match[dalao_index]=mengxin_relative_index
            dalao_match[pre_dalao_index]=dalao_match[pre_dalao_index]+1
            mengxin_match[mengxin_abs_index]=dalao_index
count=0
begin=time.time()
for index in dalao_match:
    print(dalao_pref[count][index]+" ",end='')
    count=count+1
end=time.time()
print(end-begin)