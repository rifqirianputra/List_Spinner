list = [[1,2,3],[4,5,6],[7,8,9]]
list1 = [] #list kosong untuk append setelah di putar
list2 = [] #list kosong untuk append setelah di putar
list3 = [] #list kosong untuk append setelah di putar
listc1 = [] #list kosong untuk append setelah di putar
listc2 = [] #list kosong untuk append setelah di putar
listc3 = [] #list kosong untuk append setelah di putar
listccw = [] #list kosong untuk append setelah di putar
listcw = []
print('list awal adalah')
print('\n',list[0],'\n',list[1],'\n',list[2]) # print list awal untuk membuat kotak dan menunjukkan list permulaan

def counterclockwise (x): 
    list1.append(list[0][2]) # append ke list baru dengan mengakses data spesifik dari list awal
    list1.append(list[1][2]) # append ke list baru dengan mengakses data spesifik dari list awal
    list1.append(list[2][2]) # append ke list baru dengan mengakses data spesifik dari list awal
    list2.append(list[0][1]) # append ke list baru dengan mengakses data spesifik dari list awal
    list2.append(list[1][1]) # append ke list baru dengan mengakses data spesifik dari list awal
    list2.append(list[2][1]) # append ke list baru dengan mengakses data spesifik dari list awal
    list3.append(list[0][0]) # append ke list baru dengan mengakses data spesifik dari list awal
    list3.append(list[1][0]) # append ke list baru dengan mengakses data spesifik dari list awal
    list3.append(list[2][0]) # append ke list baru dengan mengakses data spesifik dari list awal
    listccw.append(list1) # append ke list final (listccw) agar bentuknya seperti list di dalam list pada umumnya
    listccw.append(list2) # append ke list final (listccw) agar bentuknya seperti list di dalam list pada umumnya
    listccw.append(list3) # append ke list final (listccw) agar bentuknya seperti list di dalam list pada umumnya
    print('\n list setelah diputar 1 kali berlawanan arah jarum jam adalah:')
    print('\n',listccw[0],'\n',listccw[1],'\n',listccw[2]) 
    return x

def clockwise (y): #NOTE:  HANYA TEST UNTUK MELIHAT APAKA BISA DILAKUKAN UNTUK PERINTAH CLOCKWISE
    listc1.append(list[2][0]) # append ke list baru dengan mengakses data spesifik dari list awal
    listc1.append(list[1][0]) # append ke list baru dengan mengakses data spesifik dari list awal
    listc1.append(list[0][0]) # append ke list baru dengan mengakses data spesifik dari list awal
    listc2.append(list[2][1]) # append ke list baru dengan mengakses data spesifik dari list awal
    listc2.append(list[1][1]) # append ke list baru dengan mengakses data spesifik dari list awal
    listc2.append(list[0][1]) # append ke list baru dengan mengakses data spesifik dari list awal
    listc3.append(list[2][2]) # append ke list baru dengan mengakses data spesifik dari list awal
    listc3.append(list[1][2]) # append ke list baru dengan mengakses data spesifik dari list awal
    listc3.append(list[0][2]) # append ke list baru dengan mengakses data spesifik dari list awal
    listcw.append(listc1)
    listcw.append(listc2) 
    listcw.append(listc3) 
    print('\n list setelah diputar 1 kali searah arah jarum jam adalah:')
    print('\n',listcw[0],'\n',listcw[1],'\n',listcw[2]) 
    return y

counterclockwise(1)
clockwise(1)