public class User {
    private String nome;
    private Veiculos veiculo;
    private int contador = 0;

    public User(String nome) {
        this.nome = nome;
        this.veiculo = new Veiculos(null);
    }

    public String getNome() {
        return nome;
    }

    public Veiculos getVeiculo() {
        return veiculo;
    }

    @Override
    public String toString() {
        return "Nome de Usuário: " + nome + ", Veículo: " + veiculo + ".";
    }

    public void emprestar(Veiculos emprestado) {
        veiculo.setTipoVeiculo(emprestado.getTipoVeiculo());
        contador++;
        System.out.println("O Contador está em " + contador);
    }

    public int getContador() {
        return contador;
    }

}
