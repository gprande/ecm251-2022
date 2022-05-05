public class Tesoura extends Jogada{

    public Tesoura() {
        super(EnumJogadas.PAPEL);
    }
    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.TESOURA;
    }
}
