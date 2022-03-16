#include<stdio.h> 
#include<conio.h>


int main() {
	float Nota1, Nota2,Nota3;
	printf("Digite a primeira nota: \n");
	scanf("%f", &Nota1);
	printf("Digite a segunda nota: \n");
	scanf("%f", &Nota2);
	printf("Digite a terceira nota: \n");
	scanf("%f", &Nota3);

	//A seguir estamos apresentando o resultado (a soma das notas) e a média
	printf("A soma das notas foi: %0.2f ",Nota1+Nota2+Nota3);
	printf("\n A media = %0.2f", (Nota1+Nota2+Nota3)/3);
	
	//Aqui a gnt tem uma quantidade excessiva de ifs pra averiguar qual é a maior 
	if (Nota1 > Nota2 && Nota1 > Nota3){
		printf("\nA maior nota foi: %0.2f", Nota1);
		if (Nota2 > Nota3){
			printf("\nE a menor foi a %0.2f", Nota3);
		}
		else{
			printf("\nE a menor foi %0.2f", Nota2);
		}
	}
	else if (Nota2 > Nota1 && Nota2 > Nota3){
		printf("\nA maior nota foi: %0.2f", Nota2);
		if (Nota3 > Nota1){
			printf("\nE a menor foi a %0.2f", Nota1);
		}
		else{
			printf("\nE a menor foi %0.2f", Nota3);
		}
	}
	else if (Nota3 > Nota2 && Nota3 > Nota1){
		printf("\nA maior nota foi: %0.2f", Nota3);
		if (Nota2 > Nota1){
			printf("\nE a menor foi a %0.2f", Nota1);
		}
		else{
			printf("\nE a menor foi %0.2f", Nota2);
		}
	}
	else if (Nota3 == Nota2 or Nota1 == Nota2){
		printf("\nDuas notas sao iguais, com o valor de: %0.2f", Nota2);
		if (Nota2 > Nota3 or Nota2 > Nota1){
			printf("\nEssa mesma nota (%0.2f) foi a maior.", Nota2);
			if (Nota3 > Nota1){
				printf("\nA menor nota foi %0.2ff", Nota1);
			}	
			else if (Nota1 > Nota3){
				printf("\nA menor nota foi %0.2f", Nota3);
			}
		}
	}
	else{
		printf("\ntodas as notas sao iguais, com o valor de %0.2f", Nota3);
	}
	
	getch();	
}