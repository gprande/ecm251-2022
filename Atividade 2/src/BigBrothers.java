public class BigBrothers extends Membros{

    public BigBrothers(string username, string email, string funcao) {
        super(username, email, "Big Brothers!");
    }

    @Override
    public string bigbrothers(Atividades atividade){
        if(atividade="EXTRA"){
            System.out.println("...");
        }
        else
        System.out.println("Sempre ajudando as pessoas membros ou não S2!");
    }

}
