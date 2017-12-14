# Terrier - INDEX HARD 2003 corpus

Pre-requisite:
* Terrier 4.2 binaries (assume located in /volumes/data/tools/terrier-4.2)
* Aquaint source files (assume located in /Volumes/Data/Phd/Data/aquaint_docs)

Working directory where we will put all config and data is:
/Volumes/Data/Github/terrier_indexing/data/

## 1. Generate collection.spec
collection.spec specify list of source files to be indexed.
```bash
find /Volumes/ext/data/Aquaint_MERGED -type f -name '*.gz'| sort |grep -v info > /Volumes/ext/liam/data/collection_hard2005_merged.spec
```

## 2. Create folder to hold the index
```bash
cd /Volumes/ext3/indeces/terrier-4.2/var/index
mkdir hard2005_merged
```

## 3. Index based on the generated collection.spec
```bash
/Volumes/ext3/indeces/terrier-4.2/bin/trec_terrier.sh -i -Dcollection.spec=/Volumes/ext/liam/data/collection_hard2005_merged.spec -Dterrier.index.path=/Volumes/ext3/indeces/terrier-4.2/var/index/hard2005_merged/ -DTrecDocTags.doctag=DOC -DTrecDocTags.idtag=DOCNO -DTrecDocTags.skip=DOCHDR,DOCTYPE,HEADER,SLUG,DATE_TIME -DFieldTags.process=TEXT -DTrecDocTags.casesensitive=false -Dstopwords.filename=stopword-list.txt -Dtermpipelines=Stopwords,PorterStemmer
```
