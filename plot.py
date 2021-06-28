import sys, os, statistics, math, csv


def main():
    #Figure1: 
    # worst case scenario: 51%-49% alpha beta, plot in function of size of x, n= 10.003 
    plotByX(5103,4900,100, 10001,"51-49")

    #Figure2: 
    # 60%-40% alpha beta, plot in function of size of x, n= 10.003 
    plotByX(6003,4000,2, 1001,"60-40")
    plotByX(7003,3000,2, 1001,"70-30")
    plotByX(8003,2000,2, 1001,"80-20")
    plotByX(9003,1000,2, 1001,"90-10")

    #Figure3: 
    # original scenario in the worst case 51%-49% alpha beta, x= 4449 , n= 10675 
    plotDistributionOriginalVector(10675,4449)     #data of the primaire 2017

def plotByX (alpha,beta,step,stop,name):
    path = "./data/"+ name + "-"+ str(step)+ ".csv"
    f = open(path, 'w')
    writer = csv.writer(f)
    header = ["x","ProbOfMiss"]
    writer.writerow(header)
    x=1
    while x <= stop:
        p = probability (alpha,beta,x)*100
        writer.writerow([x,p])
        print (x)
        x=x+step
    f.close

def plotDistributionOriginalVector (n,x):
    f = open('./data/original.csv', 'w')
    writer = csv.writer(f)
    header = ["BetterThanMed","WorseThanMed","Percentage","ProbOfMiss"]
    writer.writerow(header)
    alpha = findPercentage(n,51)
    beta = n-alpha
    p = probability (alpha,beta,x)*100
    s = str(round(alpha/n*100,2)) + "% - " + str(round(beta/n*100,2))+ "%"
    writer.writerow([alpha,beta,s,p])
    for i in range(60,100,10):
        alpha = findPercentage(n,i)
        beta = n-alpha
        p = probability (alpha,beta,x)*100
        s = str(round(alpha/n*100,2)) + "% - " + str(round(beta/n*100,2))+ "%"
        writer.writerow([alpha,beta,s,p])
        print(i)
    f.close

def probability (alpha,beta,x):
    sum = 0
    total = math.comb(alpha+beta,x)
    p1= int((x-1)/2)
    p2= int((x+1)/2)
    while (p2<=x and p1>=0):
        betterHalf = math.comb(alpha,p1)  #math.comb((n+1)/2,(x-1)/2)
        worseHalf = math.comb(beta,p2)
        sum = sum + ((betterHalf*worseHalf))
        p1=p1-1
        p2=p2+1
    return sum/total

def findPercentage (n,p):
    return math.ceil((p * n)/100)

if __name__ == "__main__":
    main()