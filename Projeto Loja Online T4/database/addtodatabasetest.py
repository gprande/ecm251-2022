#Initial database filling. 

from dao.product_dao import Product_DAO
from models.product_model import Product

data = Product_DAO()

Store_Products = [
                    Product("Cities: Skylines","Cities: Skylines é uma versão moderna dos simuladores de cidade clássicos.","1",74.99,"./assets/cities.jpg"),
                    Product("Phasmophobia","Phasmophobia é um jogo multijogador online (4 jogadores co-op) de terror psicológico.","2",27.90,"./assets/phasmo.png"),
                    Product("Stardew Valley","Será que você vai aprender a viver da terra, a transformar esse matagal em um próspero lar?","3",24.99,"./assets/stardew.jpg"),
                    Product("Devour","Corra. Grite. Esconda-se. Sobreviva a qualquer custo!","4",10.89,"./assets/devour.jpg"),
                    Product("Rise of the Tomb Raider","Explore a Mansão Croft na nova história.","5",29.99,"./assets/rise.jpg"),
                    Product("Dead by Daylight","DBD é um jogo em que você deve fugir do assassino e evitar ser pego.","6",49.99,"./assets/dbd.jpg"),
                    Product("Minecraft Bedrock & Java Edition","Minecraft Launcher é seu portal para o universo do Minecraft","7",129.00,"./assets/mine.jpg"),
                    Product("PowerWash Simulator","Se livre de preocupações com os sons suaves de água em alta pressão.","8",74.90,"./assets/power.jpg"),
                    Product("Forza Horizon 5","Explore o mundo aberto vibrante em terras mexicanas.","9",249.00,"./assets/forza.jpg")]

for game in Store_Products:
    data.add_item(game)

game_data = data.get_all()