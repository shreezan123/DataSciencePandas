import matplotlib.pyplot as plt
import extract
import timeit

def getStats():
    print "****Data Frame Mean****\n"
    print extract.df.mean()
    print "\n"
    print "****Data Frame Median****\n"
    print extract.df.median()
    print "\n"
    print "****Data Frame Mode****\n"
    print extract.df.mode().iloc[0]
    print "\n"
    print "****Data Frame Standard Deviation****\n"
    print extract.df.std()
    print "\n"

def printHistograms():
    hist_plot = extract.df.hist()
    plt.show()

if __name__ == "__main__":
    start_time = timeit.default_timer()
    getStats()
    printHistograms()
    print "***Calculating the time***"
    print(timeit.default_timer() - start_time)
