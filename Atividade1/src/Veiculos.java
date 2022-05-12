import java.util.concurrent.ThreadLocalRandom;

public class Veiculos {
    private String TipoVeiculo;
    private int IdVeiculo = 0;
    private int CustoHora = 0;

    public Veiculos(String tipoVeiculo) {
        this.TipoVeiculo = tipoVeiculo;
        this.IdVeiculo = ThreadLocalRandom.current().nextInt(10000, 100000);
        this.CustoHora = ThreadLocalRandom.current().nextInt(0, 121);
    }

    public String getTipoVeiculo() {
        return TipoVeiculo;
    }

    public int getIdVeiculo() {
        return IdVeiculo;
    }

    public int getCustoHora() {
        return CustoHora;
    }

    public void setTipoVeiculo(String tipoVeiculo) {
        this.TipoVeiculo = tipoVeiculo;
    }

    public void setCustoHora(int custoHora) {
        this.CustoHora = ThreadLocalRandom.current().nextInt(0, 121);
    }

    public void setIdVeiculo(int idVeiculo) {
        this.IdVeiculo = ThreadLocalRandom.current().nextInt(10000, 100000);
    }
   
    public String testar() {
        return String.format("O veículo é do tipo %s, de ID %d e de custo R$%d por hora", getTipoVeiculo(), getIdVeiculo(), getCustoHora());
    }



}
