import subprocess

path_terrier = '/volumes/ext/indeces/terrier-4.2/bin/trec_terrier.sh'
path_index = '/volumes/ext/indeces/terrier-4.2/var/index/aquaint/'
path_query = '/volumes/ext/data/Aquaint_hardtrack_2005/2005_HardTrack.topics.txt'
prefix_run = '/volumes/ext/jimmy/experiments/ipm_fielded_retrieval/data/terrier/ter_hard2005_a'
b_title = 0.75
b_body = 0.75

for alpha in range(0, 11, 1):
    queryParam = ' -r ' \
                 '-Dterrier.index.path={index} ' \
                 '-Dtrec.topics={query} ' \
                 '-DTrecQueryTags.doctag=top ' \
                 '-DTrecQueryTags.process=top,num,title ' \
                 '-DTrecQueryTags.idtag=num ' \
                 '-DTrecQueryTags.skip=desc,narr ' \
                 '-DTrecQueryTags.casesensitive=false ' \
                 '-Dtrec.model=BM25F ' \
                 '-Dtrec.results.file={prefix_run}{file_id}.run ' \
                 '-Dc.0={b_title} -Dc.1={b_body} ' \
                 '-Dw.0={w_title} -Dw.1={w_body}'.\
            format(index=path_index, query=path_query, prefix_run=prefix_run, file_id=alpha,
                   b_title=b_title, b_body=b_body,
                   w_title=alpha, w_body=10-alpha)
    subprocess.call(path_terrier + queryParam, shell=True)
    print('finished:{}'.format(alpha))
