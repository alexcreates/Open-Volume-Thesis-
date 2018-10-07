import pandas as pd
import decimal
from matplotlib import pyplot as plt

"""
The open volume thesis calculates a fixed shares float amount
against the increasing volume of the day. Here we are looking for
any correlation between price movement (increasing or decreasing)
and affect on unbiased volume amounts.
in calc_all_openvol() we are calculating 50 iterations per float increase
it is fanning each fixed float point with volume starting from
10,000,
20,000
30,000
40,000
......
to
500,000


our boundaries are set at

1) start Volume = 10,000
2) start Float = 60,000    (60,000 float is unrealistic however we want to monitor all possible correlations)

3) end Volume = 500,000
4) end Float 10,000,000

We are filtering tickers that have
Here the approach is to set the boundaries of the calculation
very low and very high to capture all possible movement.
The idea is to gather this data to later plot
and check the results

"""

def calc_all_openvol():
    Volume = 10000
    Float = 60000
    idx = 0
    vol_list = []
    float_list = []
    results_list = []
    idx_list = []

    for x in range(0,498):
        for y in range(0,51):
            float_list.append(Float)
            vol_list.append(Volume)
            results_list.append(decimal.Decimal(Volume) / decimal.Decimal(Float))
            idx_list.append(idx)
            # print str(decimal.Decimal(Volume) / decimal.Decimal(Float)) + '  results  ' + str(Volume) + '  vol_results  ' + str(Float) + '  float_results'
            Volume += 10000;
            idx += 1
        Volume = 0
        Float += 20000

    dict_results = {'Volume': vol_list,
                    'Float': float_list,
                    'OV_Results': results_list }

    df = pd.DataFrame(data = dict_results, index = idx_list)

    print df.tail(500)



"""
    This method targets a single fixed shares float
    amount and calculates the growth in volume Starting
    at ten-thousand and increasing by ten-thousand at each
    loop (50 times) that allows us to calculate the movement
    of 10,000 - 500,000 in volume with one method call.
    Again this only targets a single float value provided where
    the first methods calulcates all..... O_o
"""
def target_single_float(float):
    print "25 Million Fixed Float Results:"
    StartVolume = 10000
    StockFloat25 = 25000000
    ResultList25F = []
    for x in range(0, 50):
        print 'Current StartVolume Value: ' + str(StartVolume)
        print 'Current Float Fixed amount: ' + str(StockFloat25)
        result = decimal.Decimal(StartVolume) / decimal.Decimal(StockFloat25)
        print "Step# " + str(x) + " | Percentage:   " + str(result)
        ResultList25F.append(StartVolume / StockFloat25)
        StartVolume += 10000
