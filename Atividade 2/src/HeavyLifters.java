public class HeavyLifters extends Membros {

    public HeavyLifters(String username, String email) {
        super(username, email, "Heavy Lifters!");
    }

    @Override
    public String mensagem(String horario){
        if(horario.equals("Atividade Extra")){
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        }
        else
        System.out.println("Podem contar conosco!");
    }
}