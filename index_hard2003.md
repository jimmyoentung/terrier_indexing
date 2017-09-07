# Terrier - INDEX HARD 2003 corpus

Pre-requisite:
* Terrier 4.2 binaries (assume located in /volumes/data/tools/terrier-4.2)
* HARD 2003 source files (assume located in /Volumes/Data/Phd/Data/Hard2003_docs)

Working directory where we will put all config and data is:
/Volumes/Data/Github/terrier_indexing/data/

## 1. Generate collection.spec
collection.spec specify list of source files to be indexed.
```bash
find /Volumes/Data/Phd/Data/Hard2003_docs -type f -name '*.gz'| sort |grep -v info > /Volumes/Data/Github/terrier_indexing/data/collection_hard2003.spec
```

## 2. Create folder to hold the index
```bash
cd /volumes/data/tools/terrier-4.2/var/index
mkdir hard2003
```

## 3. Index based on the generated collection.spec
```bash
/volumes/data/tools/terrier-4.2/bin/trec_terrier.sh -i
-Dcollection.spec=/Volumes/Data/Github/terrier_indexing/data/collection_hard2003.spec
-Dterrier.index.path=/volumes/data/tools/terrier-4.2/var/index/hard2003/
-DTrecDocTags.doctag=DOC
-DTrecDocTags.idtag=DOCNO
-DTrecDocTags.skip=DOCHDR,DOCTYPE,HEADER,SLUG,DATE_TIME
-DFieldTags.process=HEADLINE,TEXT
-DTrecDocTags.casesensitive=false
-Dstopwords.filename=stopword-list.txt
-Dtermpipelines=Stopwords,PorterStemmer
```

# Terrier - QUERY HARD 2003
After we have the HARD2003 corpus indexed, this section will focus on querying using HARD 2005 topics.
Only the title will be used (Description and narrative will be ignored.

```bash
/volumes/data/tools/terrier-4.2/bin/trec_terrier.sh -r
-Dterrier.index.path=/volumes/data/tools/terrier-4.2/var/index/hard2003/
-Dtrec.topics=/Volumes/Data/Phd/Data/Hard2003_eval/03.topics.nometadata
-DTrecQueryTags.doctag=top
-DTrecQueryTags.process=top,num,title
-DTrecQueryTags.idtag=num
-DTrecQueryTags.skip=desc,narr
-DTrecQueryTags.casesensitive=false
-Dtrec.model=BM25F
-Dw.0=1 -Dw.1=1
-Db.0=0.75d -Db.1=0.75d
-Dtrec.results.file=/Volumes/Data/Github/ipm2017_fielded_retrieval/data/terrier/ter_hard2003.run
```