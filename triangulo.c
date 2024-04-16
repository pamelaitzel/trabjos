
#include <stdio.h>

float calcularAreaTriangulo(float lado1, float lado2, float lado3) {
   
    float s = (lado1 + lado2 + lado3) / 2;
    

    float area = s * (s - lado1) * (s - lado2) * (s - lado3);
    
    if (area < 0) {
        
        return -1;
    }
    
    
    float raiz = area;
    float anterior;
    
    do {
        anterior = raiz;
        raiz = (raiz + area / raiz) / 2;
    } while (raiz != anterior);
    
    return raiz;
}

int main() {
    float lado1, lado2, lado3;
    
    
    printf("Ingrese la longitud del lado 1: ");
    scanf("%f", &lado1);
    
    printf("Ingrese la longitud del lado 2: ");
    scanf("%f", &lado2);
    
    printf("Ingrese la longitud del lado 3: ");
    scanf("%f", &lado3);
    
    
    float area = calcularAreaTriangulo(lado1, lado2, lado3);
    
    if (area >= 0) {
        
        printf("El área del triángulo es: %.2f\n", area);
    } else {
        
        printf("Los lados dados no forman un triángulo válido.\n");
    }
    
    return 0;
}