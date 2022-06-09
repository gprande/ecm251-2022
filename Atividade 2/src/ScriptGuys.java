public class ScriptGuys extends Membros {

    public ScriptGuys(String username, String email) {
        super(username, email, "Script Guy!");
    }

    @Override
    public String mensagem(String horario){
        if(horario.equals("Atividade Extra")){{
            System.out.println("QU3Ro_S3us_r3curs0s.py");
        }
        else
        System.out.println("Prazer em ajudar novos amigos de código!");
    }
}
