import subprocess
import multiprocessing

completed_set = [(0, 0.05, 0.1), (2, 0.1, 0.25), (6, 0.0, 0.25), (0, 0.05, 0.15), (2, 0.1, 0.3), (6, 0.0, 0.3), (0, 0.05, 0.2), (2, 0.1, 0.35), (6, 0.0, 0.35), (0, 0.05, 0.25), (2, 0.1, 0.4), (6, 0.15, 0.15), (0, 0.05, 0.3), (2, 0.1, 0.45), (6, 0.15, 0.2), (0, 0.05, 0.35), (6, 0.15, 0.25), (0, 0.05, 0.4), (2, 0.2, 0.25), (6, 0.15, 0.3), (0, 0.05, 0.45), (2, 0.2, 0.3), (6, 0.15, 0.35), (0, 0.0, 0.0), (2, 0.2, 0.35), (6, 0.15, 0.4), (0, 0.0, 0.05), (2, 0.2, 0.4), (6, 0.15, 0.45), (0, 0.0, 0.1), (2, 0.2, 0.45), (6, 0.15, 0.5), (0, 0.0, 0.15), (2, 0.2, 0.5), (6, 0.1, 0.1), (0, 0.0, 0.2), (2, 0.2, 0.55), (6, 0.1, 0.15), (0, 0.0, 0.25), (2, 0.2, 0.6), (6, 0.1, 0.2), (0, 0.0, 0.3), (3, 0.05, 0.05), (6, 0.1, 0.25), (0, 0.0, 0.35), (3, 0.05, 0.1), (6, 0.1, 0.3), (3, 0.05, 0.15), (0, 0.15, 0.2), (6, 0.1, 0.35), (3, 0.05, 0.2), (0, 0.15, 0.25), (6, 0.1, 0.4), (3, 0.05, 0.25), (0, 0.15, 0.3), (6, 0.1, 0.45), (3, 0.05, 0.3), (0, 0.15, 0.35), (6, 0.2, 0.2), (3, 0.05, 0.35), (0, 0.15, 0.4), (6, 0.2, 0.25), (3, 0.05, 0.4), (0, 0.15, 0.45), (6, 0.2, 0.3), (3, 0.0, 0.0), (0, 0.15, 0.5), (6, 0.2, 0.35), (3, 0.0, 0.05), (0, 0.15, 0.55), (6, 0.2, 0.4), (3, 0.0, 0.1), (0, 0.1, 0.15), (6, 0.2, 0.45), (3, 0.0, 0.15), (0, 0.1, 0.2), (6, 0.2, 0.5), (3, 0.0, 0.2), (0, 0.1, 0.25), (6, 0.2, 0.55), (3, 0.0, 0.25), (0, 0.1, 0.3), (7, 0.05, 0.05), (3, 0.0, 0.3), (0, 0.1, 0.35), (7, 0.05, 0.1), (3, 0.0, 0.35), (0, 0.1, 0.4), (7, 0.05, 0.15), (3, 0.15, 0.15), (0, 0.1, 0.45), (7, 0.05, 0.2), (3, 0.15, 0.2), (0, 0.1, 0.5), (7, 0.05, 0.25), (3, 0.15, 0.25), (0, 0.2, 0.25), (7, 0.05, 0.3), (3, 0.15, 0.3), (0, 0.2, 0.3), (7, 0.05, 0.35), (3, 0.15, 0.35), (0, 0.2, 0.35), (7, 0.05, 0.4), (3, 0.15, 0.4), (0, 0.2, 0.4), (7, 0.0, 0.0), (3, 0.15, 0.45), (0, 0.2, 0.45), (7, 0.0, 0.05), (3, 0.15, 0.5), (0, 0.2, 0.5), (7, 0.0, 0.1), (0, 0.2, 0.55), (3, 0.1, 0.1), (7, 0.0, 0.15), (0, 0.2, 0.6), (3, 0.1, 0.15), (7, 0.0, 0.2), (10, 0.05, 0.05), (3, 0.1, 0.2), (7, 0.0, 0.25), (10, 0.05, 0.1), (3, 0.1, 0.25), (7, 0.0, 0.3), (10, 0.05, 0.15), (3, 0.1, 0.3), (7, 0.0, 0.35), (10, 0.05, 0.2), (3, 0.1, 0.35), (7, 0.15, 0.15), (10, 0.05, 0.25), (3, 0.1, 0.4), (7, 0.15, 0.2), (10, 0.05, 0.3), (3, 0.1, 0.45), (7, 0.15, 0.25), (10, 0.05, 0.35), (3, 0.2, 0.25), (7, 0.15, 0.3), (10, 0.05, 0.4), (3, 0.2, 0.3), (7, 0.15, 0.35), (10, 0.0, 0.0), (3, 0.2, 0.35), (7, 0.15, 0.4), (10, 0.0, 0.05), (3, 0.2, 0.4), (7, 0.15, 0.45), (10, 0.0, 0.1), (3, 0.2, 0.45), (7, 0.15, 0.5), (10, 0.0, 0.15), (3, 0.2, 0.5), (7, 0.1, 0.1), (10, 0.0, 0.2), (3, 0.2, 0.55), (7, 0.1, 0.15), (10, 0.0, 0.25), (3, 0.2, 0.6), (7, 0.1, 0.2), (10, 0.0, 0.3), (4, 0.05, 0.05), (7, 0.1, 0.25), (10, 0.0, 0.35), (4, 0.05, 0.1), (7, 0.1, 0.3), (10, 0.15, 0.15), (4, 0.05, 0.15), (7, 0.1, 0.35), (10, 0.15, 0.2), (4, 0.05, 0.2), (7, 0.1, 0.4), (10, 0.15, 0.25), (4, 0.05, 0.25), (7, 0.1, 0.45), (10, 0.15, 0.3), (4, 0.05, 0.3), (7, 0.2, 0.2), (10, 0.15, 0.35), (4, 0.05, 0.35), (7, 0.2, 0.25), (10, 0.15, 0.4), (4, 0.05, 0.4), (7, 0.2, 0.3), (10, 0.15, 0.45), (4, 0.0, 0.0), (7, 0.2, 0.35), (10, 0.15, 0.5), (4, 0.0, 0.05), (7, 0.2, 0.4), (10, 0.1, 0.1), (4, 0.0, 0.1), (7, 0.2, 0.45), (10, 0.1, 0.15), (4, 0.0, 0.15), (7, 0.2, 0.5), (10, 0.1, 0.2), (4, 0.0, 0.2), (7, 0.2, 0.55), (10, 0.1, 0.25), (4, 0.0, 0.25), (8, 0.05, 0.05), (10, 0.1, 0.3), (4, 0.0, 0.3), (8, 0.05, 0.1), (10, 0.1, 0.35), (4, 0.0, 0.35), (8, 0.05, 0.15), (10, 0.1, 0.4), (4, 0.15, 0.15), (8, 0.05, 0.2), (10, 0.1, 0.45), (4, 0.15, 0.2), (8, 0.05, 0.25), (10, 0.2, 0.2), (4, 0.15, 0.25), (8, 0.05, 0.3), (10, 0.2, 0.25), (4, 0.15, 0.3), (8, 0.05, 0.35), (10, 0.2, 0.3), (4, 0.15, 0.35), (8, 0.05, 0.4), (10, 0.2, 0.35), (4, 0.15, 0.4), (8, 0.0, 0.0), (10, 0.2, 0.4), (4, 0.15, 0.45), (8, 0.0, 0.05), (10, 0.2, 0.45), (4, 0.15, 0.5), (8, 0.0, 0.1), (10, 0.2, 0.5), (4, 0.1, 0.1), (8, 0.0, 0.15), (10, 0.2, 0.55), (4, 0.1, 0.15), (8, 0.0, 0.2), (1, 0.05, 0.05), (4, 0.1, 0.2), (8, 0.0, 0.25), (1, 0.05, 0.1), (4, 0.1, 0.25), (8, 0.0, 0.3), (1, 0.05, 0.15), (4, 0.1, 0.3), (8, 0.0, 0.35), (1, 0.05, 0.2), (4, 0.1, 0.35), (8, 0.15, 0.15), (1, 0.05, 0.25), (4, 0.1, 0.4), (8, 0.15, 0.2), (1, 0.05, 0.3), (4, 0.1, 0.45), (8, 0.15, 0.25), (1, 0.05, 0.35), (4, 0.2, 0.2), (8, 0.15, 0.3), (1, 0.05, 0.4), (4, 0.2, 0.25), (8, 0.15, 0.35), (4, 0.2, 0.3), (8, 0.15, 0.4), (1, 0.0, 0.0), (4, 0.2, 0.35), (8, 0.15, 0.45), (1, 0.0, 0.05), (4, 0.2, 0.4), (8, 0.15, 0.5), (1, 0.0, 0.1), (4, 0.2, 0.45), (8, 0.1, 0.1), (1, 0.0, 0.15), (4, 0.2, 0.5), (8, 0.1, 0.15), (1, 0.0, 0.2), (4, 0.2, 0.55), (8, 0.1, 0.2), (1, 0.0, 0.25), (8, 0.1, 0.25), (1, 0.0, 0.3), (5, 0.05, 0.05), (8, 0.1, 0.3), (1, 0.0, 0.35), (5, 0.05, 0.1), (8, 0.1, 0.35), (1, 0.15, 0.2), (5, 0.05, 0.15), (8, 0.1, 0.4), (1, 0.15, 0.25), (5, 0.05, 0.2), (8, 0.1, 0.45), (1, 0.15, 0.3), (5, 0.05, 0.25), (8, 0.2, 0.2), (1, 0.15, 0.35), (5, 0.05, 0.3), (8, 0.2, 0.25), (1, 0.15, 0.4), (5, 0.05, 0.35), (8, 0.2, 0.3), (1, 0.15, 0.45), (5, 0.05, 0.4), (8, 0.2, 0.35), (1, 0.15, 0.5), (5, 0.0, 0.0), (8, 0.2, 0.4), (1, 0.15, 0.55), (5, 0.0, 0.05), (8, 0.2, 0.45), (1, 0.1, 0.15), (5, 0.0, 0.1), (8, 0.2, 0.5), (1, 0.1, 0.2), (5, 0.0, 0.15), (8, 0.2, 0.55), (1, 0.1, 0.25), (5, 0.0, 0.2), (9, 0.05, 0.05), (1, 0.1, 0.3), (5, 0.0, 0.25), (9, 0.05, 0.1), (1, 0.1, 0.35), (5, 0.0, 0.3), (9, 0.05, 0.15), (1, 0.1, 0.4), (5, 0.0, 0.35), (9, 0.05, 0.2), (1, 0.1, 0.45), (5, 0.15, 0.15), (9, 0.05, 0.25), (1, 0.1, 0.5), (5, 0.15, 0.2), (9, 0.05, 0.3), (1, 0.2, 0.25), (5, 0.15, 0.25), (9, 0.05, 0.35), (1, 0.2, 0.3), (5, 0.15, 0.3), (9, 0.05, 0.4), (1, 0.2, 0.35), (5, 0.15, 0.35), (9, 0.0, 0.0), (1, 0.2, 0.4), (5, 0.15, 0.4), (9, 0.0, 0.05), (1, 0.2, 0.45), (5, 0.15, 0.45), (9, 0.0, 0.1), (1, 0.2, 0.5), (5, 0.15, 0.5), (9, 0.0, 0.15), (1, 0.2, 0.55), (5, 0.1, 0.1), (9, 0.0, 0.2), (1, 0.2, 0.6), (5, 0.1, 0.15), (9, 0.0, 0.25), (2, 0.05, 0.05), (5, 0.1, 0.2), (9, 0.0, 0.3), (2, 0.05, 0.1), (5, 0.1, 0.25), (9, 0.0, 0.35), (2, 0.05, 0.15), (5, 0.1, 0.3), (9, 0.15, 0.15), (2, 0.05, 0.2), (5, 0.1, 0.35), (9, 0.15, 0.2), (2, 0.05, 0.25), (5, 0.1, 0.4), (9, 0.15, 0.25), (2, 0.05, 0.3), (5, 0.1, 0.45), (9, 0.15, 0.3), (2, 0.05, 0.35), (5, 0.2, 0.2), (9, 0.15, 0.35), (2, 0.05, 0.4), (5, 0.2, 0.25), (9, 0.15, 0.4), (2, 0.0, 0.0), (5, 0.2, 0.3), (9, 0.15, 0.45), (2, 0.0, 0.05), (5, 0.2, 0.35), (9, 0.15, 0.5), (2, 0.0, 0.1), (5, 0.2, 0.4), (9, 0.1, 0.1), (2, 0.0, 0.15), (5, 0.2, 0.45), (9, 0.1, 0.15), (2, 0.0, 0.2), (5, 0.2, 0.5), (9, 0.1, 0.2), (2, 0.0, 0.25), (5, 0.2, 0.55), (9, 0.1, 0.25), (2, 0.0, 0.3), (6, 0.05, 0.05), (9, 0.1, 0.3), (2, 0.0, 0.35), (6, 0.05, 0.1), (9, 0.1, 0.35), (2, 0.15, 0.2), (6, 0.05, 0.15), (9, 0.1, 0.4), (2, 0.15, 0.25), (6, 0.05, 0.2), (9, 0.1, 0.45), (2, 0.15, 0.3), (6, 0.05, 0.25), (9, 0.2, 0.2), (2, 0.15, 0.35), (6, 0.05, 0.3), (9, 0.2, 0.25), (2, 0.15, 0.4), (6, 0.05, 0.35), (9, 0.2, 0.3), (2, 0.15, 0.45), (6, 0.05, 0.4), (9, 0.2, 0.35), (2, 0.15, 0.5), (6, 0.0, 0.0), (9, 0.2, 0.4), (2, 0.15, 0.55), (6, 0.0, 0.05), (9, 0.2, 0.45), (2, 0.1, 0.1), (6, 0.0, 0.1), (9, 0.2, 0.5), (2, 0.1, 0.15), (6, 0.0, 0.15), (9, 0.2, 0.55), (2, 0.1, 0.2), (6, 0.0, 0.2)]

path_terrier = '/Volumes/ext3/indeces/terrier-4.2/bin/trec_terrier.sh'
path_index = '/Volumes/ext3/indeces/terrier-4.2/var/index/clueweb12b/'
path_query = '/Volumes/ext/data/webTrack2013-2014_eval/web2013_2014_topics_Terrier.xml'
prefix_run = '/Volumes/ext/liam/ter_clueweb_results/ter_tuneB_web_a'

def ter_search(query_param):
    subprocess.call(path_terrier + query_param, shell=True)
    print('*********** finished ***********')
    return True

# build list of query params for all alpha values
queryParams = []
for b_title in range(0, 101, 5):
    for b_body in range(0, 101, 5):
        for alpha in range(0, 11, 1):
            # only create jobs for parameter combos not in completed_set
            if (alpha, b_title, b_body) not in completed_set:
                queryParam = ' -r ' \
                            '-Dterrier.index.path={index} ' \
                            '-Dtrec.topics={queryfile} ' \
                            '-DTrecQueryTags.doctag=top ' \
                            '-DTrecQueryTags.process=top,num,title ' \
                            '-DTrecQueryTags.idtag=num ' \
                            '-DTrecQueryTags.skip=desc,narr ' \
                            '-DTrecQueryTags.casesensitive=false ' \
                            '-Dtrec.model=BM25F ' \
                            '-Dtrec.results.file={prefix_run}{file_id}_bt{b_title}_bb{b_body}.run ' \
                            '-Dc.0={b_title} -Dc.1={b_body} ' \
                            '-Dw.0={w_title} -Dw.1={w_body}'.\
                        format(index=path_index, queryfile=path_query, prefix_run=prefix_run, file_id=alpha,
                            b_title=float(b_title) / 100, b_body=float(b_body) / 100,
                            w_title=alpha, w_body=10-alpha)
                queryParams.append(queryParam)

# call terrier multi - processing
p = multiprocessing.Pool(processes=5)
res = p.map(ter_search, queryParams)


