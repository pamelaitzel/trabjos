#include <stdio.h>
struct Empleado {
    char nombre[50];
    char sexo;
    float sueldo;
};

int main() {
    struct Empleado empleado;
    printf("Ingrese el nombre del empleado: ");
    scanf("%s", empleado.nombre);

    printf("Ingrese el sexo del empleado (M/F): ");
    scanf(" %c", &empleado.sexo);

    printf("Ingrese el sueldo del empleado: ");
    scanf("%f", &empleado.sueldo);
    printf("\nInformación del empleado:\n");
    printf("Nombre: %s\n", empleado.nombre);
    printf("Sexo: %c\n", empleado.sexo);
    printf("Sueldo: %.2f\n", empleado.sueldo);

    return 0;
}