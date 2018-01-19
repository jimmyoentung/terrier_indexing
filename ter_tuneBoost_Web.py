import subprocess
import multiprocessing

path_terrier = '/Volumes/ext3/indeces/terrier-4.2/bin/trec_terrier.sh'
path_index = '/Volumes/ext3/indeces/terrier-4.2/var/index/clueweb12b/'
path_query = '/Volumes/ext/data/webTrack2013-2014_eval/web2013_2014_topics_Terrier.xml'
prefix_run = '/Volumes/ext/liam/ter_clueweb_results/ter_web_b'
b_title = 0.75
b_body = 0.75

def ter_search(query_param):
    subprocess.call(path_terrier + query_param, shell=True)
    print('*********** finished ***********')
    return True

# build list of query params for all alpha values
queryParams = []
for alpha in range(0, 11, 1):
    queryParam = ' -r ' \
                 '-Dterrier.index.path={index} ' \
                 '-Dtrec.topics={queryfile} ' \
                 '-DTrecQueryTags.doctag=top ' \
                 '-DTrecQueryTags.process=top,num,title ' \
                 '-DTrecQueryTags.idtag=num ' \
                 '-DTrecQueryTags.skip=desc,narr ' \
                 '-DTrecQueryTags.casesensitive=false ' \
                 '-Dtrec.model=BM25F ' \
                 '-Dtrec.results.file={prefix_run}{file_id}.run ' \
                 '-Dc.0={b_title} -Dc.1={b_body} ' \
                 '-Dw.0={w_title} -Dw.1={w_body}'.\
            format(index=path_index, queryfile=path_query, prefix_run=prefix_run, file_id=alpha,
                   b_title=b_title, b_body=b_body,
                   w_title=alpha, w_body=10-alpha)
    queryParams.append(queryParam)

# call terrier multi - processing
p = multiprocessing.Pool(processes=4)
res = p.map(ter_search, queryParams)


