import java.util.concurrent.ThreadLocalRandom;

public class Membros implements PostarMensagem{
    private String username;
    private String email;
    private String funcao;
    private String horario;
    
    public Membros(String username, String email, String funcao) {
        this.username = username;
        this.email = email;
        this.funcao = funcao;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getFuncao() {
        return funcao;
    }

    public void setFuncao(String funcao) {
        this.funcao = funcao;
    }

    public String getHorario() {
        return horario;
    }
    
}
