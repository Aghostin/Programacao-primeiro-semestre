#include<stdio.h>
#include<conio.h>
//importando as funçoes scanf, printf e getch()

int main(){

	//Exercício 1
	
	//Escreve a frase dentro das aspas
	printf("Meu primeiro programa!!!\n");

	//Exercício 2 e 3
	
	//Declara a variável Numero
	float Numero;
	
	//Imprime e pede um input, depois digita só o numero
	//após digitar só o número digita com texto
	printf("Digite um numero: ");
	scanf("%f", &Numero);
	printf("%0.0f", Numero);
	printf("\nFoi informado o valor: %0.0f\n", Numero);
	
	//Exercício 4
	
	//Declara a variável Numero2
	float Numero2;
	
	//Pede o outro número
	printf("Digite outro numero: ");
	scanf("%f", &Numero2);
	
	//Mostra os números com um texto
	printf("Voce informou os numeros: %0.0f e %0.0f\n", Numero, Numero2);
	
	//Exercício 5
	//Mostra o número da variável Numero com duas casas decimais
	printf("O primeiro numero com duas casas decimais fica: %0.2f\n", Numero);
	
	//Exercício 6
	
	//Declarando variável:
	float Celsius;
	
	//Pede input e armazena
	printf("Digite uma temperatura em Celsius: ");
	scanf("%f", &Celsius);
	
	//Converte e apresenta
	printf("Essa temperatura %0.2fC equivale a %0.2fF", Celsius, Celsius*1.8+32);
	
	//Exercício 7
	//Declarando variáveis (poderia reutilizar as duas primeiras)
	float NumeR;
	int NumeI;
	
	//Pedindo input
	printf("\nDigite um numero inteiro: ");
	scanf("%i", &NumeI);
	
	//Pedindo input2
	printf("Digite um numero real: ");
	scanf("%f", &NumeR);
	
	//Mostrando
	printf("Voce informou os numeros %i e %0.2f", NumeI, NumeR);
	
	//Exercicio 8
	//Declarando variável
	char PLN[1];
	
	//Pedindo input
	printf("\nInforme a primeira letra do seu nome: ");
	scanf("%s", &PLN);
	
	//Mostrando
	printf("Voce digitou: %s", PLN);
	
	//Exercício 9
	
	//Declarando variavel
	char Cor[15];
	
	//pedindo input
	printf("\nQual a sua cor favorita? ");
	scanf("%s", &Cor);
	
	//resposta
	printf("Voce gosta da cor: %s", Cor);
	
	//Exercicio 10
	
	//Declarando variáveis
	char Fruta[25],Verdura[25];
	
	//pedindo input de fruta
	printf("\nQual a sua fruta favorita? ");
	scanf("%s", &Fruta);
	
	//pedindo input de verdura
	printf("Qual a sua verdura favorita? ");
	scanf("%s", &Verdura);
	
	//resposta
	printf("Voce gosta de %s e %s", Fruta, Verdura);
	
	//Exercício 11 
	//Reutilizarei o numero real do exercicio 7, por isso nao declararei outra var
	
	//resposta
	printf("\n-----------------------------------------------------");
	printf("\nNumero real-> %0.2f", NumeR);
	printf("\nDobro deste numero-> %0.2f", NumeR*2);
	
	//Exercício 12
	//novamente reutilizarei a variavel ja criada
	//resposta
	printf("\nQuadrado do numero-> %0.2f", NumeR*NumeR);
	printf("\nCubo do numero-> %0.2f", NumeR*NumeR*NumeR);
	printf("\n-----------------------------------------------------");
	
	//Exercício 13
	//Nota: tentei fazer reutilizando o NumeI, mas nao funcionou
	int NumeI2, NumeI3;
	
	//Pedindo input e armazenando
	printf("\nDigite outro numero inteiro: ");
	scanf("%i", &NumeI2);
	
	printf("Digite mais um numero inteiro: ");
	scanf("%i", &NumeI3);
	
	//resposta
	//printf("Os numeros %i e %i somados correspondem a %i\n", NumeI, NumeI2, NumeI + NumeI2);
	printf("-----------------------------------------------------");
	printf("\nOs numeros %i e %i somados correspondem a %i\n", NumeI2, NumeI3, NumeI2 + NumeI3);
	printf("-----------------------------------------------------");
	
	//Exercicio 14 e 15
	//Declarando mais variaveis
	float RealN2, RealN3;
	
	//pedindo input e armazenando novamente
	printf("\nDigite outro numero real: ");
	scanf("%f", &RealN2);
	
	printf("Digite mais um numero real: ");
	scanf("%f", &RealN3);
	
	//resposta
	printf("-----------------------------------------------------");
	printf("\nO produto dos numeros %0.2f e %0.2f corresponde a: %0.2f", RealN2, RealN3, RealN2 * RealN3);
	printf("\nA soma desses mesmos numeros equivale a: %0.2f", RealN2+RealN3);
	printf("\nA subtracao de %0.2f por %0.2f equivale a a: %0.2f", RealN2, RealN3, RealN2-RealN3);
	printf("\nE a subtracao de %0.2f por %0.2f equivale a : %0.2f", RealN3, RealN2, RealN3-RealN2);
	printf("\nA divisao de %0.2f por %0.2f equivale a: %0.2f", RealN2, RealN3, RealN2/RealN3);
	printf("\nE a divisao de %0.2f por %0.2f equivale a: %0.2f", RealN3, RealN2, RealN3/RealN2);
	printf("\n-----------------------------------------------------");
	
	//Exercicio 16
	//Comando esta cortado mas acho que entendi
	//Declarando variaveis
	float salario, comissao, taxacms;
	
	//Input
	printf("\nQual o salario fixo do vendedor em reais? ");
	scanf("%f", &salario);
	
	printf("Qual o total de vendas do vendedor em reais? ");
	scanf("%f", &comissao);
	
	printf("Qual porcentagem do total de vendas sera repassada ao vendedor (sem o simbolo de percentual)? ");
	scanf("%f", &taxacms);
	
	//resposta
	printf("-----------------------------------------------------");
	printf("\nO salario fixo de %0.2f sera alterado para %0.2f", salario, salario+comissao*(taxacms/100));
	printf("\n-----------------------------------------------------");
	
	getch();
}