public class Data {
    private int dia;
    private int mes;
    private int ano;

    // Construtor
    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    // Método para formatar a data como string
    public String formatarData() {
        return dia + "/" + mes + "/" + ano;
    }
}