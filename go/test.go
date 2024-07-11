package main

import (
	"fmt"
	"strconv"
)

func main() {

	for {
		var age int
		fmt.Sscanln(&age)

		convertage, err := strconv.Atoi(age)

		if err != nil {
			fmt.Println("Invalid input: Please input a numeric value")
			continue
		}

		// if not were gonna validate the age if your a adult or minor
		if age > 18 {
			fmt.Println("You're a adult")
		}
		fmt.Println("You're a minor")

	}

}
