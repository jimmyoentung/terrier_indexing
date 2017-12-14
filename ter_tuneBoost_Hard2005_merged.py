import subprocess

path_terrier = '/Volumes/ext3/indeces/terrier-4.2/bin/trec_terrier.sh'
path_index = '/Volumes/ext3/indeces/terrier-4.2/var/index/hard2005_merged/'
path_query = '/Volumes/ext/data/hard2003_eval/03.topics.nometadata' # TODO determine this dir
prefix_run = '/Volumes/ext/liam/ter_hard2005_merged_results/ter_hard2005_merged_b'

for beta in range(0, 101, 5):
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
                 '-Dc.0={weight} ' \
                 '-Dw.0=1 '.\
            format(index=path_index, queryfile=path_query, prefix_run=prefix_run, file_id=beta, weight=beta/100)
    subprocess.call(path_terrier + queryParam, shell=True)
    print('finished:{}'.format(beta))
