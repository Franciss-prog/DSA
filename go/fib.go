package main

import (
	"fmt"
	"strconv"
	"strings"
)

// fibbonacci
// function to find the largest number
func largestNum(number []int) int {
	// set the largest to the first element (index 0)
	largest := number[0]

	// iterate by using the length of numbers
	for i := 0; i < len(number); i++ {
		//  compare current element to the largest number found so far
		if number[i] > largest {
			// update the largest  new value
			largest = number[i]
		}
	}
	// return the largest number found
	return largest
}
func main() {

	// ask the user
	fmt.Print("Enter numbers separated by spaces: ")

	// get the value
	var input string
	fmt.Scanln(&input)

	// split
	parts := strings.Fields(input)

	// Create a slice to store the numbers as integers
	numbers := make([]int, len(parts))

	// Convert each string to an integer and store it in the numbers slice
	for i, part := range parts {
		number, err := strconv.Atoi(part)
		if err != nil {
			fmt.Println("Invalid Number", part)
			return
		}
		numbers[i] = number
	}

	// Call the largestNum function with the numbers slice
	largestNumber := largestNum(numbers)

	fmt.Println("Largest Number: ", largestNumber)
}
