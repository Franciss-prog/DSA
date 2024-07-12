package main

import "fmt"

func main() {
	var a [3]int // declare an array of 3 integers

	a[0] = 1
	a[1] = 2
	a[2] = 3

	// shorthand
	b := [3]int{1, 2, 3}
	fmt.Println(b)
}
