public class Papel extends Jogada{

    public Papel() {
        super(EnumJogadas.PEDRA);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.PAPEL;
    }
    
}
