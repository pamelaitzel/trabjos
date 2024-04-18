#include <stdio.h>


unsigned long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1; 
    } else {
        return n * factorial(n - 1); 
    }
}

int main() {
    int numero;
    unsigned long long resultado;

    printf("Ingrese un número para calcular su factorial: ");
    scanf("%d", &numero);

    if (numero < 0) {
        printf("El factorial de un número negativo no está definido.\n");
    } else {
        resultado = factorial(numero);
        printf("El factorial de %d es %llu.\n", numero, resultado);
    }

    return 0;
}