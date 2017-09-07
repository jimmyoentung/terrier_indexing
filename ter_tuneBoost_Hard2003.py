import subprocess

path_terrier = '/volumes/data/tools/terrier-4.2/bin/trec_terrier.sh'
path_index = '/volumes/data/tools/terrier-4.2/var/index/hard2003/'
path_query = '/Volumes/Data/Phd/Data/Hard2003_eval/03.topics.nometadata'
prefix_run = '/Volumes/Data/Github/ipm2017_fielded_retrieval/data/terrier/ter_hard2003_a'
b_title = 0.75
b_body = 0.75

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
    subprocess.call(path_terrier + queryParam, shell=True)
    print('finished:{}'.format(alpha))
