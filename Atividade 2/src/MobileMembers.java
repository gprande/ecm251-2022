public class MobileMembers extends Membros {

    public MobileMembers(string username, string email, string funcao) {
        super(username, email, "Mobile Members!");
    }
    
    @Override
    public string mobilemembers(Atividades atividade){
        if(atividade="EXTRA"){
            System.out.println("Happy_C0d1ng. Maskers");
        }
        else
        System.out.println("Happy Coding!");
    }
}
