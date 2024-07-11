package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func main() {
	//initialized variable
	var num1 int
	var num2 int

	// get the input of num1
	fmt.Print("Enter a number: ")
	fmt.Scanln(&num1)

	// get the input of num2
	fmt.Print("Enter a second number: ")
	fmt.Scanln(&num2)

	//	add two numbers and print it
	result := add(num1, num2)

	fmt.Printf("Sum of %d and %d is %d", num1, num2, result)
}
