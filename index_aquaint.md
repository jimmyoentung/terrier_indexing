# Step by step to index Aquaint using terrier

Pre-requisite:
* Terrier 4.2 binaries (assume located in /volumes/data/tools/terrier-4.2)
* Aquaint source files (assume located in /Volumes/Data/Phd/Data/aquaint_docs)

Working directory where we will put all config and data is:
/Volumes/Data/Github/terrier_indexing/data/

## 1. Generate collection.spec
collection.spec specify list of source files to be indexed.
```bash
find /Volumes/Data/Phd/Data/aquaint_docs -type f -name '*.gz'| sort |grep -v info > /Volumes/Data/Github/terrier_indexing/data/collection_aquaint.spec
```

## 2. Create folder to hold the index
```bash
cd /volumes/data/tools/terrier-4.2/var/index
mkdir aquaint
```

## 3. Index based on the generated collection.spec
```bash
/volumes/data/tools/terrier-4.2/bin/trec_terrier.sh -i -Dcollection.spec=/Volumes/Data/Github/terrier_indexing/data/collection_aquaint.spec -Dterrier.index.path=/volumes/data/tools/terrier-4.2/var/index/aquaint/ -DTrecDocTags.doctag=DOC -DTrecDocTags.idtag=DOCNO -DTrecDocTags.skip=DOCHDR,DOCTYPE,HEADER,SLUG,DATE_TIME -DFieldTags.process=HEADLINE,TEXT -DTrecDocTags.casesensitive=false -Dstopwords.filename=stopword-list.txt -Dtermpipelines=Stopwords,PorterStemmer
```

