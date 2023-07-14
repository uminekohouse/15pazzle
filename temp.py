from mod import *
import copy
import csv

MOD = 2
Modint(m=MOD)

def createAugmentedMatrix(A, b):
    #拡大係数行列の作成
    augmented_matrix = copy.deepcopy(A)
    for i in range(len(A)):
        augmented_matrix[i].append(copy.deepcopy(b[i]))
    return  augmented_matrix



def select_pivot(A, i):
    k = i
    m = len(A)
    val = copy.deepcopy(A[i][i])
    for j in range(i, m):
        tmp = copy.deepcopy(A[j][i])
        if int(tmp) < 0: tmp *= -1
        if int(val) < int(tmp):
            val = tmp
            k = j
    if k != i:
        A[i], A[k] = A[k], A[i]



def get_stair_matrix(A):
    #print("stop")
    m = len(A)
    n = len(A[-1])
    # 前身消去
    for i in range(m):
        select_pivot(A, i)
        if int(A[i][i]) == 0:
            ok = True
            for j in range(i,m):
                for k in range(k,n):
                    if int(A[j][k]) != 0: ok = False
            if ok:
                m = i
                break
            return None 
        x = copy.deepcopy(A[i][i])
        for j in range(i, n):
            A[i][j] /= x
        for j in range(i+1, m):
            y = copy.deepcopy(A[j][i])
            for k in range(i, n):
                A[j][k] -= A[i][k] * y
    # 後退消去
    for i in range(m-1,0,-1):
        val = n-1
        for j in range(n):
            if(int(A[i][j])!=0):
                val = j
                break
        for j in range(i-1, -1, -1):
            y = copy.deepcopy(A[j][val])
            for k in range(val,n):
                A[j][k] -= A[i][k]*y;

    return A

def get_corank(A):
    A = get_stair_matrix(A)
    m = len(A)
    for i in range(m):
        ok = True
        for j in A[i]:
            if(int(j)!=0):
                ok = False
                break
        if(ok): return m-i
    return 0    

def matrix_product(A,b):
    n = len(A)
    res = []
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += A[i][j] * b[j]
        res.append(tmp)    
    return res    


def can_solve_matrix(A, j):
    #拡大行列の作成
    augmented_matrix = createAugmentedMatrix(A, j)
    augmented_matrix = get_stair_matrix(augmented_matrix)
    m = len(augmented_matrix)
    n = len(augmented_matrix[0])
    for i in augmented_matrix:
        is_zeros = True
        for j in range(n-1):
            if(int(i[j])!=0): is_zeros = False
        if is_zeros:
            if(int(i[n-1])!=0): return False

    return True

def generate_vector_list(n):
    #長さnで1の個数がi個のベクトルのlistを返す
    res = {}
    for i in range(n+1): res[i] = []
    def func(res, x, cnt):
        if len(x)==n:
            res[cnt].append(x)
        else:
            tmp = x[:]
            tmp.append(0)
            func(res,tmp, cnt)

            tmp = x[:]
            tmp.append(1)
            func(res,tmp, cnt+1)
     
    func(res, [], 0) 
    return res


def get_kernel_vectors(A):
    A = get_stair_matrix(A)
    sets = [[Modint(0) for i in range(len(A))]]
    if(get_corank(A)==0): return sets 

    kernel_base_vectors = []

    for i in range(len(A)-get_corank(A), len(A)):
        v = [Modint(0) for i in range(len(A))]
        for j in range(0, i-1):
            if(int(A[j][i])==1):
                v[j] = Modint(1)
        v[i] = Modint(1)    
        kernel_base_vectors.append(v)
 
    for v in kernel_base_vectors:
        sets_tmp = []
        for s in sets:
            sets_tmp.append([i+j for i,j in zip(s,v)])
            sets_tmp.append(s)
        sets = sets_tmp
    return sets    

def solve(A, b):
    A = createAugmentedMatrix(A,b)
    A = get_stair_matrix(A)
    if(A!=None):
        res = []
        for i in A:
            res.append(i[len(A[0])-1])
        return res               
    else:
        return False

with open("lightsout_data.csv", 'w') as csv_file:
    fieldnames = ["n", "A_1(n)", "A_2(n)", "dim_e_n", "dimHn"]
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    writer.writeheader()
    for n in range(1, 11):
        A = [[Modint(0) for i in range(n*n)] for j in range(n*n)]
        for i in range(n*n):
            A[i][i] = Modint(1)
            if(i % n != 0):     A[i][i-1] = Modint(1)
            if((i+1) % n != 0): A[i][i+1] = Modint(1)
            if(i+n <n*n):      A[i][i+n] = Modint(1)
            if(i-n >= 0):       A[i][i-n] = Modint(1)

        A_1 = 0
        for k in range(n*n):
            vec = [Modint(0) for j in range(n*n)]
            vec[k] = Modint(1)
            vec = solve(A,vec)
            if vec:
                A_1 += 1
        A_2 = 0
        for k in range(n*n-1):
            for l in range(k+1,n*n):
                vec = [Modint(0) for j in range(n*n)]
                vec[k] = Modint(1)
                vec[l] = Modint(1)
                vec = solve(A,vec)
                if vec:
                    A_2 += 1
        
        dimH = get_corank(A)
        dimE = n*n-dimH
        writer.writerow({"n":n,"A_1(n)":A_1,"A_2(n)":A_2,"dim_e_n":dimE,"dimHn":dimH})




        
        







