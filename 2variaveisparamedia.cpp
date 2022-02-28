#include<stdio.h>
#include<conio.h>
//importando biblioteca stdio para usarmos printf e scanf
//importando biblioteca conio para usarmos o (getch())


int main() {
	
    //definindo variáveis
    float Nota1, Nota2;
    
    //imprimindo na tela o texto com a instrução
    printf("Digite a primeira nota: \n");
    
    //recebendo o input
    scanf("%f", &Nota1);
    
    //repetindo o passo anterior
    printf("Digite a segunda nota: \n");
    scanf("%f", &Nota2);
    
    //Cálculo do resultado e mostrar ele na tela:
    printf("O resultado do semestre foi: %0.2f", Nota1 + Nota2);
    
    //Cálculo da média
    printf("\nA media foi: %0.2f", (Nota1+Nota2)/2);
    
    //Agora usaremos o getch() para termos tempo de ler
    getch();

}