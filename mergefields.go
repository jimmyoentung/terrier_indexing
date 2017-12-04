package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
)

func main() {

	reglimit := regexp.MustCompile("<\\/title>\\s*<body>")
	regstart := regexp.MustCompile("<title>")

	foo := getRecordsFromFile("test.xml")

	merged := reglimit.ReplaceAllString(foo, "")
	merged = regstart.ReplaceAllString(merged, "<body>")

	fmt.Println(merged)
}

func getRecordsFromFile(file string) string {
	// read in file
	b, _ := ioutil.ReadFile(file)
	return string(b)
}

func writeRecordsToFile(file string) {
	// open file to write data to
	f, err := os.OpenFile(file, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0666)
	if err != nil {
		fmt.Println("Can't open data file...")
		return
	}
	defer f.Close()

	// write data to file
	f.WriteString("pizza")
	f.Close()

}
