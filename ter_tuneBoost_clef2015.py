import subprocess

path_terrier = '/Volumes/ext3/indeces/terrier-3.6/bin/trec_terrier.sh'

# NOTE: index has temporarily been changed to local version
path_index = '/Volumes/ext3/indeces/terrier-3.6/var/index/clef2015local/'
path_query = '/Volumes/ext/data/clef2015_eval/clef2015.test.queries-EN.txt'
prefix_run = '/Volumes/ext/liam/ter_clef2015_results/ter_clef2015_a'
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
