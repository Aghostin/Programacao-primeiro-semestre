#include<stdio.h>
#include<conio.h>

//Bibliotecas

//Funcao principal

int main(){
	int QtdProvas, ProvasContadas;
	float Media, AnotherMediaCuzIdk;
	
	//Qual a quantidade de provas?
	printf("Qual a quantidade de provas que voce deseja calcular? ");
	scanf("%d", &QtdProvas);
	
	//Loop (Gosto mais de while do que de for)
	while (ProvasContadas < QtdProvas){
		
		//Pedido das notas e atribuiçao
		printf("Digite a nota da prova %d: ", ProvasContadas+1);
		scanf("%f", &Media);
		
		//Salvando o valor da media em outra variavel já q o += nao funcionou so com 1 var
		AnotherMediaCuzIdk += Media;
		
		//Aumentando o contador para igualar com a Qtd de Provas num futuro plausível
		ProvasContadas += 1;	

	}
	
	printf("A media total das %d provas foi: %0.2f", QtdProvas, AnotherMediaCuzIdk/QtdProvas);
	
	getch();
}