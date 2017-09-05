import subprocess, os
import glob
import multiprocessing

trecPath = "/Volumes/Data/tools/trec_eval.9.0/"
dataPath = '/Volumes/Data/Github/ipm2017_fielded_retrieval/data/terrier/'
qrelPath = "/volumes/data/phd/data/aquaint_eval/TREC2005.qrels.txt"
topPrefix = 'ter_hard2005_a'
resultFile = "ter_hard2005_tuneWeight.eval"

def eval(fname):
    trecResults = subprocess.getoutput(trecPath +
                                     'trec_eval -q -m map -m P.10 -m ndcg_cut.10,1000 -m bpref -m relstring.10 '
                                     '-m recip_rank ' + qrelPath + " " + fname)
    print(trecResults)
    filename = os.path.basename(fname)
    alpha = filename.replace(topPrefix,"").replace('.run','')

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

                resultString += filename + " " + alpha + " " + qNum + " " + map + " " + p10 + " " + ndcg10 + " " + \
                                ndcg1000 + " " + bpref + " " + str(numUnjudged) + " " + relString + " " + rr + "\n"

    print ("File name: {0} Completed".format(filename))

    return resultString

fileNames = glob.glob(dataPath + topPrefix + "*")

fw = open(dataPath + resultFile, 'w')
fw.write("schema" + " " + "alpha" + " " + " QueryNum"+ " " + "map" + " " + "p10" + " " + "ndcg10" + " " + "ndcg1000" +
         " " + "bpref" + " " + "unjudged" + " " + "relString" + " " + "rr""\n")

p = multiprocessing.Pool()
resultString = p.map(eval, fileNames)
for res in resultString:
    fw.write(res)
p.close()
p.join()

fw.close()
