'''
Created on Mar 24, 2015

@author: A. Rupam Mahmood

This module instantiates an algorithm and the standard random walk 
problem (see Mahmood, van Hasselt & Sutton 2014, nips) and runs an experiment.

'''

import os
import sys
sys.path.insert(0, os.getcwd())
import argparse
from pysrc.problems.stdrw import PerformanceMeasure
from pysrc.problems.stdrwsparsereward import StdRWSparseReward
from pysrc.problems.stdrwfreqreward import StdRWFreqReward
from pysrc.algorithms.tdprediction import oislstd
from pysrc.algorithms.tdprediction import wislstd
from pysrc.algorithms.tdprediction import gtd
import cPickle as pickle

def runoneconfig(config, prob, alg, perf):
  prob.setrunseed(config['runseed'])
  for ep in range(config['neps']):
    prob.initepisode()
    alg.initepisode()
    while not prob.isterminal():
      probstep          = prob.step()
      s                 = probstep['s']
      a                 = probstep['act']
      probstep['l']     = config['lambda']
      probstep['lnext'] = config['lambda']
      probstep['rho']   = prob.getRho(s,a)
      alg.step(probstep)
      perf.calcMse(alg, ep)
      
def main():
  parser          = argparse.ArgumentParser()
  parser.add_argument("run", help="used as a seed of an independent run", type=int)
  parser.add_argument("probname", help="name of the problem to run experiment on")
  parser.add_argument("path", help="location of the config file")
  args = parser.parse_args()
  configpathname  = args.path + "config.pkl"
  cf              = open(configpathname, 'rb')
  configs         = pickle.load(cf)  
    
  filepathname  = args.path + "run_"\
                  +str(args.run) + ".dat"
  f             = open(filepathname, 'wb')
  
  algs  = {
           'oislstd':oislstd.OISLSTD,
           'wislstd':wislstd.WISLSTD,
           'gtd':gtd.GTD,
           }
  probs = {
           'StdRWSparseReward'  : StdRWSparseReward,
           'StdRWFreqReward'    : StdRWFreqReward,
           }
  algname   = configs[0]['algname']
  rwprob   = probs[args.probname](configs[0])
  perf      = PerformanceMeasure(configs[0], rwprob)
  print("Running algorithm " + algname + " on problem " + args.probname + ", runseed: " + str(args.run) )
  for config in configs:
    alg            = algs[algname](config)
    config['runseed'] = args.run
    runoneconfig(config, rwprob, alg, perf)
    config['mse']     = perf.mse
    pickle.dump(config, f, -1)

if __name__ == '__main__':
    main()   
    

