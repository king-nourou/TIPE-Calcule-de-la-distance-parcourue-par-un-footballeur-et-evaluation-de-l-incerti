import matplotlib.pyplot as plt
import seaborn as sns
import random as rd
import numpy as np
def distance_euclidienne(liste_abcisses, liste_ordonnees):
    n = len(liste_abcisses)
    distance = 0 
    for i in range(n-1):
        x1 = liste_abcisses[i]
        x2 = liste_abcisses[i+1]
        y1 = liste_ordonnees[i]
        y2 = liste_ordonnees[i+1]
        
        distance += np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

lx = [660,656,644,615,598,588,582,579,590,610,629,645,655,
      676,701,713,715,712,653,631,604,579,554,538,537,541,
      541,545,539,528,526,533,544,551,556,561,566,564,565,
      563,560,558,560,563,567,572,589,594,600,605,607,
      607,604,602,609,618,628,638,648,650,649,
      646,637,625,608,553,522,491,487,480,492,501,
      512,529,549,585,612,631,639,602,594,592,604,615,
      617,607,598,588,578,559,554,538,517,507,498,501,
      503,509,519,538,546,544,544,546,546,538,526,517,506,496,
      483,471,453,441,432,439,450,463,472,478,]

ly = [770,761,744,739,719,724,720,740,766,792,808,832,857,
      881,850,839,828,827,850,834,813,801,799,796,798,801,
      805,815,817,809,804,800,806,809,814,819,825,830,837,
      831,828,827,832,837,838,835,831,823,816,
      816,808,804,797,792,790,789,788,790,792,806,819,
      838,855,873,885,890,887,871,866,856,843,839,
      836,823,813,807,816,838,847,848,861,850,840,842,
      850,856,861,863,864,866,867,874,876,874,868,864,
      860,857,859,863,861,852,846,845,841,840,846,858,864,852,
      825,817,837,861,876,873,872,868,857,840]

print(distance_euclidienne(lx, ly))

print(len(lx))

liste_abcisses = [(e-396)/5 for e in lx]
liste_ordonnees = [(e-548)/5 for e in ly]

print(liste_abcisses)
print(liste_ordonnees)
    