import numpy as np 


def preproccese(x):
    int_feature = []
    for i in x:
        i = i.replace("\t", "")
        int_feature.append(i)
    int_feature = np.transpose(int_feature)

    for i in int_feature:
        if int_feature[1] == "admin":
            int_feature[1] =  8
        if int_feature[1] == "blue-collar":
            int_feature[1] =  1
        if int_feature[1] == "entrepreneur":
            int_feature[1] =  3
        if int_feature[1] == "housemaid":
            int_feature[1] =  2
        if int_feature[1] == "management":
            int_feature[1] =  9
        if int_feature[1] == "mgmt":
            int_feature[1] =  0
        if int_feature[1] == "retired":
            int_feature[1] =  11
        if int_feature[1] == "self-employed":
            int_feature[1] =  7
        if int_feature[1] == "services":
            int_feature[1] =  4
        if int_feature[1] == "student":
            int_feature[1] =  12
        if int_feature[1] == "technician":
            int_feature[1] =  6
        if int_feature[1] == "unemployed":
            int_feature[1] =  10
        if int_feature[1] == "unknown":
            int_feature[1] = 5
        else :
            pass
        
    for i in int_feature:
        if int_feature[3] == "primary":
            int_feature[3] = 0.1346548188653452
        if int_feature[3] == "secondary":
            int_feature[3] = 0.1769591910436981
        if int_feature[3] == "tertiary":
            int_feature[3] =  0.26437086092715234
        if int_feature[3] == "unknown":
            int_feature[3] = 0.21070234113712374

    for i in int_feature:
        if int_feature[10] == "apr":
            int_feature[10] = 1.0
        if int_feature[10] == "aug":
            int_feature[10] = 0.15
        if int_feature[10] == "dec":
            int_feature[10] =  1.0
        if int_feature[10] == "feb":
            int_feature[10] =  1.0
        if int_feature[10] == "jan":
            int_feature[10] =  1.0
        if int_feature[10] == "jul":
            int_feature[10] =  0.0946
        if int_feature[10] == "jun":
            int_feature[10] =  0.11
        if int_feature[10] == "mar":
            int_feature[10] =  1.0
        if int_feature[10] == "may":
            int_feature[10] =  0.10
        if int_feature[10] == "nov":
            int_feature[10] = 0.1
        if int_feature[10] == "oct":
            int_feature[10] =  1
        if int_feature[10] == "sep":
            int_feature[10] = 1.0

    for i in int_feature:
        if int_feature[9] == "1":
            int_feature[9] = 0.64
        if int_feature[9] == "2":
            int_feature[9] = 0.31
        if int_feature[9] == "3":
            int_feature[9] =  0.29
        if int_feature[9] == "4":
            int_feature[9] =  0.31
        if int_feature[9] == "5":
            int_feature[9] =  0.19
        if int_feature[9] == "6":
            int_feature[9] =  0.151
        if int_feature[9] == "7":
            int_feature[9] =  0.13
        if int_feature[9] == "8":
            int_feature[9] =  1.58
        if int_feature[9] == "9":
            int_feature[9] =  .14
        if int_feature[9] == "10":
            int_feature[9] = 0.29
        if int_feature[9] == "11":
            int_feature[9] =  0.20
        if int_feature[9] == "12":
            int_feature[9] = 0.25
        if int_feature[9] == "13":
            int_feature[9] = 0.27
        if int_feature[9] == "14":
            int_feature[9] = 0.18
        if int_feature[9] == "15":
            int_feature[9] =  0.25
        if int_feature[9] == "16":
            int_feature[9] =  0.18
        if int_feature[9] == "17":
            int_feature[9] =  0.22
        if int_feature[9] == "18":
            int_feature[9] =  0.0946
        if int_feature[9] == "19":
            int_feature[9] =  0.11
        if int_feature[9] == "20":
            int_feature[9] =  0.13
        if int_feature[9] == "21":
            int_feature[9] =  0.16
        if int_feature[9] == "22":
            int_feature[9] = 0.19
        if int_feature[9] == "23":
            int_feature[9] =  0.14
        if int_feature[9] == "24":
            int_feature[9] = 0.16
        if int_feature[9] == "25":
            int_feature[9] =  0.23
        if int_feature[9] == "26":
            int_feature[9] =  0.20
        if int_feature[9] == "27":
            int_feature[9] =  0.22
        if int_feature[9] == "28":
            int_feature[9] =  0.146
        if int_feature[9] == "29":
            int_feature[9] = 0.144
        if int_feature[9] == "30":
            int_feature[9] =  0.25
        if int_feature[9] == "31":
            int_feature[9] =0.761
    
    
    int_feature[-4]  = 1.0    

    int_feature[-3] = 1.0

    int_feature[-5] = 0.0


    for i in  int_feature:
        if  int_feature[6] == "yes":
             int_feature[6] = 1
        if  int_feature[6] == "no":
             int_feature[6] = 0
    
    for i in  int_feature:
        if  int_feature[4] == "yes":
             int_feature[4] = 1
        if  int_feature[4] == "no":
             int_feature[4] = 0
    
    for i in  int_feature:
        if  int_feature[7] == "yes":
             int_feature[7] = 1
        if  int_feature[7] == "no":
             int_feature[7] = 0
    
    if int_feature[2] == "married":
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,1)
        int_feature = np.append(int_feature,0)
    elif int_feature[2] == "single":
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,1)
    elif int_feature[2] == "divorced":
        int_feature = np.append(int_feature,1)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)

    

    int_feature = np.delete(int_feature, 2)


    if int_feature[7] == "cellular":
        int_feature = np.append(int_feature,1)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
    elif int_feature[7] == "unknown":
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,1)
    elif int_feature[7] == "telephone":
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,1)
        int_feature = np.append(int_feature,0)

    int_feature = np.delete(int_feature, 7)



    if int_feature[13] == "unknown":
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,1)
    elif int_feature[13] == "failure":
        int_feature = np.append(int_feature,1)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
    elif int_feature[13] == "other":
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,1)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
    elif int_feature[13] == "success":
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,0)
        int_feature = np.append(int_feature,1)
        int_feature = np.append(int_feature,0)

    

    int_feature = np.delete(int_feature, 13)

    
    int_feature = np.append(int_feature,int_feature[4])

    int_feature = np.delete(int_feature, 4)
    
    
    return int_feature
