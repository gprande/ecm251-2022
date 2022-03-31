public class Conta {
    private int idConta;
    private double saldo;

    public Conta(Usuario Usuario, int idConta){
        this.idConta = idConta;
        this.Usuario = Usuario;
        saldo = 0;
    }

    public void visualizarSaldo(){
        System.out.println("Saldo atual na conta " + numero+ ": R$" + saldo);
    }
    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }
}
