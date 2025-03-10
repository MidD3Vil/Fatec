public class Dog {
    String nome;
    int peso;
    
    void latir(){
        if (peso >= 9){
            System.out.println("AUUUUU!");
        }
        
        else if (peso < 9){
            System.out.println("AU!");
        }    
    }
}