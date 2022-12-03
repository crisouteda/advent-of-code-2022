package main

import (
	"bufio"
	"fmt"
	"os"
)

func readInputFile() []string {
	var s []string
	readFile, err := os.Open("input.txt")

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		s = append(s, fileScanner.Text())
	}

	readFile.Close()

	return s
}

func main() {
	var points int = 0
	var lines = readInputFile()
	for i := 0; i < len(lines); i = i + 3 {
		common := commonCharFinder(lines[i], lines[i+1], lines[i+2])
		points += chartoNumb(common)
	}
	fmt.Println("print points= ", points)
}

func commonCharFinder(firs string, scnd string, thir string) rune {
	var l rune
	for _, s := range firs {
		for _, r := range scnd {
			if s == r {
				for _, t := range thir {
					if s == t {
						l = s
						break
					}
				}
			}
		}
	}
	return l
}

func chartoNumb(l rune) int {
	ref := int('a')
	val := int(l) - ref + 1
	if val < 0 {
		val += 58
	}
	return val
}
