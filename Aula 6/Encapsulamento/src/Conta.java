public class Conta {
    // atributos da nossa classe
    private int numero;
    private double saldo;

    // Métodos da classe 

    void visualizarSaldo(){
        System.out.println("Saldo atual na conta" +numero + ": R$ " +this.saldo);
    }
    public boolean depositar(double valor){
        //if(valor>0){
          //  saldo = saldo + valor;
          //  return true;

        //}
        //else{
            //return false;

       // }
       if(valor < 0) return false;
       this.saldo += valor; 
       return true;
       

    }
    public boolean sacar(double valor){
        //if(valor<=saldo){
          //  saldo = saldo - valor;
        //}  
        if(valor>saldo) return false;
        if(valor< 0) return false;
        this.saldo -= valor;
        return true;

    }
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;

        if(!destino.depositar(valor)) return false;
        return true;


    }


}
