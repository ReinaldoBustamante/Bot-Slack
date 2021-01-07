package main

import "fmt"

func main() {
	fmt.Println("Ingrese un numero(1-7): ")
	numero := 0
	fmt.Scanln(&numero)
	switch {
	case numero == 1:
		fmt.Println("mala suerte, su numero es:",numero)
	case numero == 2:
		fmt.Println("mala suerte, su numero es:",numero)
	case numero == 3:
		fmt.Println("mala suerte, su numero es:",numero)
	case numero == 4:
		fmt.Println("mala suerte, su numero es:",numero)
	case numero == 5:
		fmt.Println("mala suerte, su numero es:",numero)
	case numero == 6:
		fmt.Println("mala suerte, su numero es:",numero)
	case numero == 7:
		fmt.Println("Numero ganador")
	default:
		fmt.Println("El numero no esta en el rango")
	}
}