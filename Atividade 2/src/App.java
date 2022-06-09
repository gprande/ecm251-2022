import java.util.ArrayList;
import java.util.List;

public class App {

    public static void rodar() {
        System.out.println("Olá, seja bem vindo!");
        List<Membros> Lista = new ArrayList<Membros>();
        Lista.add(new MobileMembers("Zé da Bolacha", "bolacheiro@sampa.com"));
        Lista.add(new HeavyLifters("Zé da Biscoito", "biscoiteiro@vulgorj.com"));
        Lista.add(new ScriptGuys("Soninho_da_tarde", "amimir@zzzz.com"));
        Lista.add(new BigBrothers("GrandeIrmaoBrazil", "redeglobo@bbb.com"));
        exibirMembros1();
        exibirMembros2();
    }

    public void turno(Membros horario) {
        int sortear = ThreadLocalRandom.current().nextInt(0, 2);
        if (sortear == 1)
            horario = "Atividade Regular";
        else
            horario = "Atividade Extra";
    }

    public void exibirMembros1() {
        for (Membros membros : Lista) {
            System.out.println(membros);
            membros.mensagem(Membros.getHorario());
        }
    }

    public void exibirMembros2() {
        for (Membros membros : Lista) {
            System.out.println(membros);
            membros.mensagem(Membros.getHorario());
        }
    }
}