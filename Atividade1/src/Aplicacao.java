public class Aplicacao {

     public static void rodar() {
         User user = new User("Gabriel Prande");
         System.out.println(user.getVeiculo().testar());

         user.emprestar(new Patinete("Patinete"));
         System.out.println(user.getVeiculo().testar());
      
         user.emprestar(new Moto("Moto"));
         System.out.println(user.getVeiculo().testar());

         user.emprestar(new Bicicleta("Bicicleta"));
         System.out.println(user.getVeiculo().testar());

         user.emprestar(new Carro("Carro"));
         System.out.println(user.getVeiculo().testar());
     }
}