public class Cliente {
    private String cpf;
    private String nome;
    private String email;
    private Conta conta;

    public void visualizarCliente(){
        System.out.println("Dados do cliente:");
        System.out.println("Nome:" + nome);
        System.out.println("CPF:" + cpf);
        System.out.println("E-mail:" + email);
        System.out.println("E-mail:" + conta);
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getCpf(){
        return cpf;
    }

    public String getEmail(){
        return email;
    }

    public String getConta(){
        return conta;
    }

    public void setCpf(String cpf){
       this.cpf = cpf 
    }

    public void setEmail(String email){
        this.email = email
    }

    public void setConta(String conta){
        this.conta = conta
    }
    
}
