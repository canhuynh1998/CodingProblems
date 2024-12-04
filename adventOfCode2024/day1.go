package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	file, e := os.Open("day1Input.txt")
	if e != nil {
		fmt.Println("Error!")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var line1 []int
	var line2 []int

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "   ")
		if val, er := strconv.Atoi(line[0]); er == nil {
			line1 = append(line1, val)
		} else {
			break
		}
		if val, er := strconv.Atoi(line[1]); er == nil {
			line2 = append(line2, val)
		} else {
			break
		}

	}
		slices.Sort(line1)
	slices.Sort(line2)
	distance := 0
	for idx := 0; idx < len(line1); idx += 1 {
		distance += abs(line1[idx] - line2[idx])
	}

	fmt.Println(distance)
}

func abs(x int) int {
	if x < 0{
		return -x
	}
	return x
}