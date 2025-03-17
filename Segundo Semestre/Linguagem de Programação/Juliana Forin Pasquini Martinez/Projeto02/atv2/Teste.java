public class Teste {
    public static void main(String[] args) {
        // Criando um objeto da classe Data
        Data dataNascimento = new Data(15, 8, 2000);

        // Criando um objeto da classe Aluno
        Aluno aluno1 = new Aluno(12345, "João Silva", 'M', "12.345.678-9", "123.456.789-00", dataNascimento);

        // Imprimindo os dados do aluno
        aluno1.imprimir();
    }
}