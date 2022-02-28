#include<stdio.h>
#include<conio.h>
/* importando novamento a bibliotecas para usar scanf e printf (stdio)
e a biblioteca conio para usar o getch e termos tempo de ler */

int main(){
	
	//Declarando variáveis de nota
	float Nota1, Nota2;
	
	//Pedindo o primeiro input
	printf("Digite a primeira nota: ");
	//Lendo input
	scanf("%f", &Nota1);
	
	//Repetindo o processo
	printf("Digite a segunda nota: ");
	scanf("%f", &Nota2);
	
	//If statements para ver qual a maior nota (provavelmente dá pra fazer melhor)
	//Else é para o caso de serem iguais, como ilustra a função de print
	if (Nota1>Nota2)
		printf("\nA maior nota foi:%0.2f", Nota1);
	else if (Nota2>Nota1)
		printf("\nA maior nota foi:%0.2f", Nota2);	
	else
		printf("As duas notas tem o mesmo valor:%0.2f", Nota1);
	getch();
}
