# Terrier - INDEX Clueweb12B

Pre-requisite:
* Terrier 4.2 binaries (assume located in /volumes/ext/indeces/terrier-4.2)
* Clueweb12B source files (assume located in /Volumes/ext/data/ClueWeb12/DiskB/)

Working directory where we will put all config and data is:
/Volumes/Data/Github/terrier_indexing/data/


## 1. Generate collection.spec
collection.spec specify list of source files to be indexed.
```bash
find /Volumes/ext/data/clef2015/ -type f -name '*'| sort |grep -v info > /Volumes/ext/liam/data/collection_clef2015.spec
```


## 2. Create folder to hold the index
```bash
cd /volumes/ext/indeces/terrier-4.2/var/index
mkdir clef2015
```

## 3. Index based on the generated collection.spec
```bash
/volumes/ext/indeces/terrier-4.2/bin/trec_terrier.sh -i -j
-Dcollection.spec=/Volumes/ext/liam/data/collection_clef2015.spec
-Dterrier.index.path=/volumes/ext/indeces/terrier-4.2/var/index/clef2015/
-DFieldTags.process=TITLE,BODY
-DTrecDocTags.skip=SCRIPT,STYLE
-Dignore.empty.documents=true
-Dstopwords.filename=stopword-list.txt
-Dtermpipelines=Stopwords,PorterStemmer
```


/tools/terrier-4.0/bin/trec_terrier.sh -i -j
-Dterrier.index.path=/volumes/data/tools/terrier-4.2/var/index/clueweb12b/
-Dcollection.spec=/Volumes/ext/indeces/terrier/collection.spec.clueweb12b13
-DFieldTags.process=TITLE,BODY
-Dtrec.collection.class=WARC10Collection
-Dindexer.meta.forward.keys=docno
-Dindexer.meta.forward.keylens=26
-Dindexer.meta.reverse.keys=docno
-DTrecDocTags.skip=SCRIPT,STYLE
-Dstopwords.filename=/tools/terrier-core-4.1/share/stopword-list.txt
-Dtermpipelines=Stopwords,TRv2PorterStemmer
-Dindexing.singlepass.max.documents.flush=10000
-Dindexing.max.docs.per.builder=1000000


