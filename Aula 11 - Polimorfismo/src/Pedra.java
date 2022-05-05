public class Pedra extends Jogada{

    public Pedra() {
        super(EnumJogadas.TESOURA);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.PEDRA;
    }
}
