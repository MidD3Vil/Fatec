public class Aluno {
    private int ra;
    private String nome;
    private char sexo;
    private String rg;
    private String cpf;
    private Data dataNasc; // Associação com a classe Data

    // Construtor
    public Aluno(int ra, String nome, char sexo, String rg, String cpf, Data dataNasc) {
        this.ra = ra;
        this.nome = nome;
        this.sexo = sexo;
        this.rg = rg;
        this.cpf = cpf;
        this.dataNasc = dataNasc;
    }

    // Métodos Getters e Setters
    public int getRa() { return ra; }
    public void setRa(int ra) { this.ra = ra; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public char getSexo() { return sexo; }
    public void setSexo(char sexo) { this.sexo = sexo; }

    public String getRg() { return rg; }
    public void setRg(String rg) { this.rg = rg; }

    public String getCpf() { return cpf; }
    public void setCpf(String cpf) { this.cpf = cpf; }

    public Data getDataNasc() { return dataNasc; }
    public void setDataNasc(Data dataNasc) { this.dataNasc = dataNasc; }

    // Método para imprimir os dados do aluno
    public void imprimir() {
        System.out.println("RA: " + ra);
        System.out.println("Nome: " + nome);
        System.out.println("Sexo: " + sexo);
        System.out.println("RG: " + rg);
        System.out.println("CPF: " + cpf);
        System.out.println("Data de Nascimento: " + dataNasc.formatarData());
    }
}