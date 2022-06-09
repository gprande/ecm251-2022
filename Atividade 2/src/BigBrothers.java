public class BigBrothers extends Membros {

    public BigBrothers(String username, String email) {
        super(username, email, "Big Brothers!");
    }

    @Override
    public String mensagem(Membros horario) {
        if (horario.equals("Atividade Extra")) {
            System.out.println("...");
        } else
            System.out.println("Sempre ajudando as pessoas membros ou não S2!");
    }

}
