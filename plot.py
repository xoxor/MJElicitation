import sys, os, statistics, math, csv


def main():
    plotDistributionOriginalVector(10675,5)     #data of the primaire 2017
    #n = 60%-40% , final k = 10% of 10000
    plotPercentageByK(6405,4270,1000)

def plotDistributionOriginalVector (n,k):
    f = open('./data/distributionVector.csv', 'w')
    writer = csv.writer(f)
    header = ["BetterThanMed","WorseThanMed","Percentage","ProbOfMiss"]
    writer.writerow(header)
    n1=int((n+1)/2)
    n2=int((n-1)/2)
    while (n1<=n and n2>=0):
        p = round(probability (n1,n2,k)*100,2)
        s = str(round(n1/n*100,2)) + "% - " + str(round(n2/n*100,2))+ "%"
        writer.writerow([n1,n2,s,p])
        n1=n1+1
        n2=n2-1
    f.close

def plotPercentageByK (n1,n2,stop):
    f = open('./data/changingK_n60-40.csv', 'w')
    writer = csv.writer(f)
    header = ["k","ProbOfMiss"]
    writer.writerow(header)
    k=0
    p = round(probability (n1,n2,k)*100,2)
    writer.writerow([k,p])
    k=1
    while k <= stop:
        p = round(probability (n1,n2,k)*100,2)
        writer.writerow([k,p])
        k=k+2
    f.close


def probability (n1,n2,k):
    betterHalf = math.comb(n1,int((k-1)/2))  #math.comb((n+1)/2,(k-1)/2)
    worseHalf = math.comb(n2,int((k+1)/2))
    total = math.comb(n1+n2,k)
    return (betterHalf*worseHalf)/total

if __name__ == "__main__":
    main()