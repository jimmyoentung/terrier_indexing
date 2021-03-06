import subprocess, os
import glob
import multiprocessing
import argparse

parser = argparse.ArgumentParser()


parser.add_argument("-d",
                    "--dataset",
                    help="CLEF2015,  CLEF2016, HARD2005, or WEB2013-2014",
                    choices=["CLEF2015", "CLEF2016", "HARD2003", "HARD2005", "WEB2013-2014"])
args = parser.parse_args()

dataSet = args.dataset

trecPath = "/volumes/ext/tools/trec_eval.9.0/"
dataPath = '/Volumes/ext/liam/ter_hard2003_merged_results/'

if dataSet == "CLEF2015":
    qrelPath = "/volumes/ext/data/clef2015_eval/qrels.eng.clef2015.test.graded.txt"
    topPrefix = "topTuneBoost_Clef2015_alpha"
    resultFile = "evalTuneBoost_Clef2015.txt"
elif dataSet == "CLEF2016":
    dataPath = '/Volumes/ext/liam/ter_clef2016_merged_results/'
    qrelPath = "/Volumes/ext/data/clef2016_eval/task1.qrels.30Aug"
    topPrefix = "ter_clef2016_merged_b"
    resultFile = "ter_clef2016_tuneWeight_unifield.eval"
elif dataSet == "HARD2003":
    dataPath = '/Volumes/ext/liam/ter_hard2003_merged_results/'
    qrelPath = "/volumes/ext/data/hard2003_eval/qrels.actual.03.txt"
    topPrefix = "ter_hard2003_merged_b"
    resultFile = "ter_hard2003_tuneWeight_unifield.eval"
elif dataSet == "HARD2005":
    dataPath = '/Volumes/ext/liam/ter_hard2005_merged_results/'
    qrelPath = "/Volumes/ext/data/aquaint_eval/TREC2005.qrels.txt"
    topPrefix = "ter_hard2005_merged_b"
    resultFile = "ter_hard2005_tuneWeight_unifield.eval"
elif dataSet == "WEB2013-2014":
    dataPath = '/Volumes/ext/liam/ter_clueweb_merged_results/'
    qrelPath = "/Volumes/ext/data/webTrack2013-2014_eval/qrels.adhoc2013-2014.txt"
    topPrefix = "ter_web_merged_b"
    resultFile = "ter_web_tuneWeight_unifield.eval"


def eval(fname):
    trecResults = subprocess.getoutput(trecPath +
                                     'trec_eval -q -m map -m P.10 -m ndcg_cut.10,1000 -m bpref -m relstring.10 '
                                     '-m recip_rank ' + qrelPath + " " + fname)
    filename = os.path.basename(fname)
    beta = filename.replace(topPrefix,"").replace('.run','')

    map = p10 = ndcg10 = ndcg1000 = bpref = numUnjudged = rr = "*"
    relString = qNum = "*"
    resultString = ""
    for res in trecResults.splitlines():
        measure = res.split()[0]
        qNum = res.split()[1]
        score = res.split()[2]
        if qNum != "all":
            if measure == "map":
                map = score
            elif measure == "bpref":
                bpref = score
            elif measure == "P_10":
                p10 = score
            elif measure == "relstring_10":
                relString = score
                numUnjudged = relString.count('-')
            elif measure == "recip_rank":
                rr = score
            elif measure == "ndcg_cut_10":
                ndcg10 = score
            elif measure == "ndcg_cut_1000":
                ndcg1000 = score

                resultString += filename + " " + beta + " " + qNum + " " + map + " " + p10 + " " + ndcg10 + " " + \
                                ndcg1000 + " " + bpref + " " + str(numUnjudged) + " " + relString + " " + rr + "\n"

    print ("File name: {0} Completed".format(filename))

    return resultString

fileNames = glob.glob(dataPath + topPrefix + "*.run")
print(len(fileNames))

fw = open(dataPath + resultFile, 'w')
fw.write("schema" + " " + "b" + " " + " QueryNum"+ " " + "map" + " " + "p10" + " " + "ndcg10" + " " + "ndcg1000" +
         " " + "bpref" + " " + "unjudged" + " " + "relString" + " " + "rr""\n")

if os.path.exists(qrelPath):
    p = multiprocessing.Pool(processes=5)
    resultString = p.map(eval, fileNames)
    for res in resultString:
        fw.write(res)
    p.close()
    p.join()

    fw.close()