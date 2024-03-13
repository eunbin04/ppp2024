temp_c=10
temp_c=int(input("섭씨온도를 입력하시오."))
temp_f=temp_c*1.8+32
print("{}℃ =>{}℉".format(temp_c,temp_f))

temp_f=10
temp_f=int(input("화씨온도를 입력하시오."))
temp_c=(temp_f-32)*5/9
print("{}℉ =>{}℃".format(temp_f,temp_c))