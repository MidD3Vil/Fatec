1)

for (int i = 1; i < 6; i++){

    System.out.println(i);
	}
	
2)
 int i = 1;
	while(i < 6){
	System.out.println(i);
	i = ++i;
	}
	
3)
 int i = 1;
	do{
		System.out.println(i);
	i = ++i;
	}while(i < 6);
	
4)
int i = 1;
	while(i < 16){
		if(i % 2 == 0){
			System.out.println(i);
	}
	i++;
    }
    
5)
int s = 0;
	for(int i = 0; i < 11; ++i){
	s = s + i;
 }
 
6)
int s = 0;
int m = 0;
for(int i = 0; i < 101; i+= 2){
		s += i;
	m++;
}
	System.out.println(s / m);
	
7)
String nome = JOptionPane.showInputDialog("Insira o seu Nome: ");

if (nome != null && !nome.trim().isEmpty()){
	System.out.println("O nome fornecido foi: " + nome.trim());
}else{
	System.out.println("Nenhum nome foi fornecido. ");
}

8)
String n = JOptionPane.showInputDialog("Insira um numero: ");
int s = Interger.parseInt(n);

if (s = s % 2 == 0){
	System.out.println("O numero é par. ");
}else{
	System.out.println("O numero é impar. ");
}