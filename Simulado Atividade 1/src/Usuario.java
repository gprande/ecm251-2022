public class Usuario {
    private String senha;
    private String nome;
    private String email;
    private Conta conta;

    public Usuario(String nome, String senha, String email, Conta conta){
        this.nome = nome;
        this.senha = senha;
        this.email = email;
        this.conta = conta;
    }

    public void visualizarCliente(){
        System.out.println("Dados do cliente:");
        System.out.println("Nome:" + nome);
        System.out.println("Senha:" + senha);
        System.out.println("E-mail:" + email);
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }
    
    public String getSenha(){
        return senha;
    }

    public String getEmail(){
        return email;
    }

    public Conta getConta(){
        return conta;
    }

   public void setEmail(String email){
        this.email = email;
    }
}
