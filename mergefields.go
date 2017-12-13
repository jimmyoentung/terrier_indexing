package main

import (
	"bytes"
	"compress/gzip"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"regexp"
	"runtime"
	"strings"
	"sync"

	"github.com/jeffail/tunny"
)

func main() {
	// directory of files to perform merge on
	mergeDir := os.Args[1]

	// get list of files to merge
	var realfiles []string
	getGzs(mergeDir, &realfiles)

}

// Finds .gz files within given dir and all its children
func getGzs(dir string, filelist *[]string) {
	// get list of files in directory
	files, err := ioutil.ReadDir(dir)
	if err != nil {
		log.Fatal(err)
	}

	for _, file := range files {
		// recursively get files from child directories
		if file.IsDir() {
			getGzs(dir+"/"+file.Name(), filelist)
		} else {
			// if file is .gz then add to filelist
			if file.Name()[len(file.Name())-3:] == ".gz" {
				*filelist = append(*filelist, dir+"/"+file.Name())
			}
		}
	}
}

func dothings() {
	// directory of files to perform merge on
	mergeDir := os.Args[1]
	newDir := createDirectory(mergeDir)

	// get list of files in directory
	files, err := ioutil.ReadDir(mergeDir)
	if err != nil {
		log.Fatal(err)
	}

	// remove files that are not of .gz format
	for i := 0; i < len(files); i++ {
		if files[i].Name()[len(files[i].Name())-3:] != ".gz" {
			fmt.Println(files[i].Name()[len(files[i].Name())-3:])
			files = append(files[:i], files[i+1:]...)
		}
	}

	// regex patterns
	//reglimit := regexp.MustCompile("(?s)<\\/HEADLINE>.*<TEXT>")
	regendhead := regexp.MustCompile("</HEADLINE>")
	regstarttext := regexp.MustCompile("<TEXT>")
	regstarthead := regexp.MustCompile("<HEADLINE>")

	// setup goroutine pool
	numCPUs := 5                    //runtime.NumCPU()
	runtime.GOMAXPROCS(numCPUs + 1) // numCPUs hot threads + one for async tasks.

	pool, _ := tunny.CreatePool(numCPUs, func(object interface{}) interface{} {
		input, _ := object.(string)

		// read from file
		foo := getStringFromFile(mergeDir + "/" + input)

		// merge fields
		merged := regendhead.ReplaceAllString(foo, "")
		merged = regstarttext.ReplaceAllString(merged, "")
		//merged := reglimit.ReplaceAllString(foo, "")
		merged = regstarthead.ReplaceAllString(merged, "<TEXT>")

		// zip and write new file
		var b bytes.Buffer
		w := gzip.NewWriter(&b)
		w.Write([]byte(merged))
		w.Close()
		ioutil.WriteFile(newDir+"/"+input, b.Bytes(), 0666)

		return input
	}).Open()
	defer pool.Close()

	// sync group to handle all jobs
	wg := new(sync.WaitGroup)
	wg.Add(len(files))

	// perform all merges
	for i := 0; i < len(files); i++ {
		go func(index int) {
			fmt.Println("Starting " + files[index].Name())
			value, _ := pool.SendWork(files[index].Name())
			fmt.Println("Finished " + value.(string))

			wg.Done()
		}(i)
	}

	wg.Wait()
}

func createDirectory(dir string) string {
	// compose name for new merged dir
	pieces := strings.Split(dir, "/")
	pieces[1] += "_MERGED"
	path := strings.Join(pieces, "/")
	fmt.Println(path)

	// create dir
	err := os.MkdirAll(path, 0711)
	if err != nil {
		log.Println("Error creating directory")
		log.Println(err)
	}

	return path
}

func getStringFromFile(file string) string {
	// read in file
	b, err := ioutil.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}

	buff := bytes.NewBuffer(b)
	r, err := gzip.NewReader(buff)
	data, err := ioutil.ReadAll(r)
	if err != nil {
		log.Fatal(err)
	}

	return string(data)
}

func writeStringToFile(file string, content string) {
	// open file to write data to
	f, err := os.OpenFile(file, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0666)
	if err != nil {
		fmt.Println("Can't open data file...")
		return
	}
	defer f.Close()

	// write data to file
	f.WriteString(content)
	f.Close()

}
