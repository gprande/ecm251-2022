public class App {
    public static void main(String[] args) throws Exception {
        Conta c1 = new Conta();
        c1.depositar(300);
        if(c1.sacar(200)){
            System.out.println("Você sacou 200!");
        }
        c1.saldo += 200;
    }
}
