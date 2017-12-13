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

	newDir := mergeDir + "_MERGED" //createDirectory(mergeDir)

	// get list of files to merge
	var files []string
	getGzs(mergeDir, &files)

	// regex patterns
	regendhead := regexp.MustCompile("</HEADLINE>")
	regstarttext := regexp.MustCompile("<TEXT>")
	regstarthead := regexp.MustCompile("<HEADLINE>")

	// setup goroutine pool
	numCPUs := 5                    //runtime.NumCPU()
	runtime.GOMAXPROCS(numCPUs + 1) // numCPUs hot threads + one for async tasks.

	pool, _ := tunny.CreatePool(numCPUs, func(object interface{}) interface{} {
		input, _ := object.(string)

		// read from file
		foo := getStringFromFile(input)

		// merge fields
		merged := regendhead.ReplaceAllString(foo, "")
		merged = regstarttext.ReplaceAllString(merged, "")
		merged = regstarthead.ReplaceAllString(merged, "<TEXT>")

		// zip and write new file
		var b bytes.Buffer
		w := gzip.NewWriter(&b)
		w.Write([]byte(merged))
		w.Close()

		// effectively ignore parent directory
		pieces := strings.Split(input, "/")
		pieces = pieces[1:]
		input = strings.Join(pieces, "/")
		fmt.Println(input)

		dirExists, _ := exists(newDir + "/" + input)
		if !dirExists {
			pieces = strings.Split(input, "/")
			pieces = pieces[:len(pieces)-1]
			path := strings.Join(pieces, "/")
			createDirectory(newDir + "/" + path)
		}

		ioutil.WriteFile(newDir+"/"+input, b.Bytes(), 0666)

		return newDir + "/" + input
	}).Open()
	defer pool.Close()

	// sync group to handle all jobs
	wg := new(sync.WaitGroup)
	wg.Add(len(files))

	// perform all merges
	for _, file := range files {
		go func(file string) {
			fmt.Println("Starting " + file)
			value, _ := pool.SendWork(file)
			fmt.Println("Finished " + value.(string))

			wg.Done()
		}(file)
	}

	wg.Wait()
}

// exists returns whether the given file or directory exists or not
func exists(path string) (bool, error) {
	_, err := os.Stat(path)
	if err == nil {
		return true, nil
	}
	if os.IsNotExist(err) {
		return false, nil
	}
	return true, err
}

// create dir
func createDirectory(dir string) {
	err := os.MkdirAll(dir, 0711)
	if err != nil {
		log.Println("Error creating directory")
		log.Println(err)
	}
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
