public class App {
    public static void main(String[] args) throws Exception {
        Produto cornDog = new Comida(12.5, "Corn Dog", 5, "Salsicha Empanada", EnumCategoriaComida.COREANA, EnumAlergicos.GLUTEN, EnumPimenta.SUAVE);
        Produto acaiMoleza = new Bebida(10.5, "Açaí do Moleza", 1, "Real fonte alternativa de energia", EnumCategoriaBebida.SUCO, EnumTemperatura.FRIO);

        System.out.println("Preços regulares:");
        System.out.println(cornDog.getNome() + ": R$" + cornDog.getPreco());
        System.out.println(acaiMoleza.getNome() + ": R$" + acaiMoleza.getPreco());

        System.out.println("Preços com desconto:");
        System.out.println(cornDog.getNome() + precoComDesconto(cornDog));
        System.out.println(acaiMoleza.getNome() + precoComDesconto(acaiMoleza));
    }

    public static String precoComDesconto(IGerarDesconto produto){
        return ": R$" + produto.gerarDesconto();
    }
}
