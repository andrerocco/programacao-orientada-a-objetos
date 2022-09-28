Escreva um programa em Python que possua cinco classes: Animal, Mamifero, Ave, Cachorro, Gato e Canarinho. Defina uma hierarquia de herança entre essas classes.

A implementação deve atender às seguintes regras:
1. Não existem instâncias de Animal, Mamifero e Ave, somente dos seus sub-tipos
2. Todos os animais possuem um tamanho de passo e quando se movem, retornam a mensagem: "ANIMAL: DESLOCOU " tamanhoPasso
3. As aves quando se movem, retornam a mensagem: "ANIMAL: DESLOCOU "+tamanhoPasso+" VOANDO"
4. Todos os animais produzem algum tipo de som com um volume, mas cada um do seu jeito:
    1. Gato (miar): "MAMIFERO: PRODUZ SOM: "+volumeSom+ " SOM: MIAU"
    2. Cachorro (latir): "MAMIFERO: PRODUZ SOM: "+volumeSom+ " SOM: AU"
    3. Canarinho (cantar): "AVE: PRODUZ SOM: PIU"
5. Somente as aves voam (que é a mesma coisa que mover para uma ave)
6. Somente os canarinhos cantam 
7. Cachorros tem tamanhoPasso = 3 e volumeSom = 3
8. Gatos tem tamanhoPasso = 2 e volumeSom = 2
9. Aves tem tamanhoPasso e alturaVoo parametrizáveis no construtor

Observação:
Ordem de parâmetros dos construtores
- Ave(int tamanhoPasso, int alturaVoo)
- Mamifero(int volumeSom, int tamanhoPasso)
- Canarinho(int tamanhoPasso, int alturaVoo)
- Siga o exemplo anexo e complete com o seu código.

Utilize exatamente os mesmos nomes de classe e das operações.
Veja no anexo a modelagem UML (diagrama de classes).