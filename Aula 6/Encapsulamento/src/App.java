public class App {
    public static void main(String[] args) throws Exception {
        Cliente c1 = new Cliente();
        c1.setNome("Gabriel Prande");
        c1.setCpf("123456789");
        c1.setEmail("bielprande@gmail.com");
        c1.setConta(new Conta());
        System.out.println("Nome do cliente: " + c1.getNome());
        System.out.println("E-mail do cliente: " + c1.getEmail());
        System.out.println("CPF do cliente: " + c1.getCpf());
        c1.getConta().visualizarSaldo();
    }
}
