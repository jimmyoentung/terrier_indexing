import subprocess
import multiprocessing

path_terrier = '/Volumes/ext3/indeces/terrier-4.2/bin/trec_terrier.sh'
path_index = '/Volumes/ext3/indeces/terrier-4.2/var/index/clueweb12b_merged/'
path_query = '/Volumes/ext/data/clef2016/queries2016.xml'
prefix_run = '/Volumes/ext/liam/ter_clef2016_merged_results/ter_clef2016_merged_b'

def ter_search(query_param):
    subprocess.call(path_terrier + query_param, shell=True)
    print('*********** finished ***********')
    return True

# build list of query params for all alpha values
queryParams = []
for beta in range(0, 101, 5):
    queryParam = ' -r ' \
                 '-Dterrier.index.path={index} ' \
                 '-Dtrec.topics={queryfile} ' \
                 '-DTrecQueryTags.doctag=top ' \
                 '-DTrecQueryTags.process=top,num,title ' \
                 '-DTrecQueryTags.idtag=num ' \
                 '-DTrecQueryTags.skip=desc,narr ' \
                 '-DTrecQueryTags.casesensitive=false ' \
                 '-Dtrec.model=BM25 ' \
                 '-Dtrec.results.file={prefix_run}{file_id}.run ' \
                 '-Dc.0={weight}' \
                 '-Dw.0=1'.\
            format(index=path_index, queryfile=path_query, prefix_run=prefix_run, file_id=beta, weight=beta/100)
    queryParams.append(queryParam)

# call terrier multi - processing
p = multiprocessing.Pool(processes=4)
res = p.map(ter_search, queryParams)


