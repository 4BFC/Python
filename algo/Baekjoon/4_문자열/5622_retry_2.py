N = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '']  # 11
test = "HELLO"
for i in N:
    print(i, end=" ")
    for ii in i:
        if test in ii:
            print("check")
        # print(f"{ii} : {test.index(ii)}", end=" ")
        # print(test.find('H'))
        # print(f"{ii}:{test.index(ii)}", end=" ")

    print()
# for i in range(len(N)):
#     print(i, end=" ")
#     for ii in range(len(N[i])):
#         print(f"{ii}", end=" ")

#     print()
