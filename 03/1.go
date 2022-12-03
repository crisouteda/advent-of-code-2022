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
	for _, s := range lines {
		shlen := len(s) / 2
		beg := s[:shlen]
		end := s[shlen:]
		common := commonCharFinder(beg, end)
		points += chartoNumb(common)
	}
	fmt.Println("print points= ", points)
}

func commonCharFinder(beg string, end string) rune {
	var l rune
	for _, s := range beg {
		for _, r := range end {
			if s == r {
				l = s
				break
			}
		}
	}
	return l
}

func chartoNumb(l rune) int {
	ref := int('a')
	val := int(l) - ref + 1
	if val < 0 {
		val += (26 + 32)
	}
	return val
}
