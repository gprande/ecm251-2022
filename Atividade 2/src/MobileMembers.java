public class MobileMembers extends Membros {

    public MobileMembers(String username, String email) {
        super(username, email, "Mobile Members!");
    }
    
    @Override
    public String mensagem(String horario){
        if(horario.equals("Atividade Extra")){{
            System.out.println("Happy_C0d1ng. Maskers");
        }
        else
        System.out.println("Happy Coding!");
    }
}
