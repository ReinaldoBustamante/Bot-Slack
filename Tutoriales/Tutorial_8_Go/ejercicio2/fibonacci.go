package main

import "fmt"

func main() {
	fibonacci := 0

	fmt.Print("que numero de fibonacci quiere calcular: ")
	fmt.Scan(&fibonacci)
	if fibonacci == 1 {
		fmt.Println("el numero de fibonacci es: 0")
	} else if fibonacci == 2 {
		fmt.Println("el numero de fibonacci es: 1")
	} else{
		valor := 1
		anterior := 0
		resultado:= 0
		for i:=2 ; i<fibonacci ; i++ {
			resultado = valor+anterior
			anterior = valor
			valor = resultado
		}
		fmt.Println("el numero de fibonacci es:",valor)
	}
}