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
	part1(line1, line2)
	part2(line1, line2)
}

func part1(line1 []int, line2 []int) {
	distance := 0
	for idx := 0; idx < len(line1); idx += 1 {
		distance += abs(line1[idx] - line2[idx])
	}
	fmt.Println(distance)
}

func part2(line1 []int, line2 []int) {
	map12  := make(map[int]int)

	for idx := 0; idx < len(line1); idx += 1 {
		map12[line1[idx]] = 0
	}

	for idx := 0; idx < len(line2); idx += 1 {
		if _, exist := map12[line2[idx]]; exist {
			map12[line2[idx]] += 1
		}
	}

	similar := 0
	for k, v := range map12 {
		similar += (k * v)
	}
	fmt.Println(similar)
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
