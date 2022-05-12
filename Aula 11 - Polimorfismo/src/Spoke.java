public class Spoke extends Jogada{

    public Spoke() {
        super(EnumJogadas.PEDRA, EnumJogadas.TESOURA);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.SPOKE;
    }

    @Override
    public String toString() {
        return String.join("\n",
        "                                                ",
        "                                                ",
        "                                                ",
        "                        .                       ",
        "                 ..:::::::::::..                ",
        "              .::...............::              ",
        "             ::...---.............::            ",
        "           ::....:. .:...........:..:.          ",
        "          :......-.  :............:..::         ",
        "        .:.....=.=.  -.........+  =....:.       ",
        "       .:.....:  .:  :..........  =.....:.    .:",
        "      .:......-.  -   -.......-.  -......:   .: ",
        "     .:.......-.  =   +.......:   :.......: .:  ",
        "     :........:   :   -.......:  :. :......:.   ",
        "    :..........    .  .......::  .  .......:.   ",
        "   .:..........    =   :.....:   :  ........:   ",
        "   :............   =   =.....:  ..  :........:  ",
        "  .:...........:   :   :....+   =   -........:  ",
        "  :............=    .  .:....   :   :.......... ",
        " .:............=    :  .:..-   -   :..........: ",
        " ..............=    -   :.::   :   +..........: ",
        " ..............:    .   -::   :    -..........:.",
        " :...............   .    :.   :   -.............",
        " :..............=             .   =............:",
        " :..............=            .:   :............:",
        ".:..............=                ..............:",
        ".:.....-=:......=                ::............:",
        ".:....=   --....=                :.............:",
        ".:....-    .::..=                :.............:",
        " :....:-     ::.-                :.............:",
        " :......-.    ::-                :.............:",
        " :.......-.    :=                :.............:",
        " :........:     .                :............:.",
        " ..........:                     .............: ",
        " .:........:.                    .............: ",
        "  :.........=                    .............. ",
        "  :..........-                   ............:. ",
        "   :.........:.                  ............:  ",
        "   .:.........:                  ...........:   ",
        "    :..........=.                :.........::   ",
        "    .:..........-:              .-.........:    ",
        "     ::...........=              :........:::   ",
        "      ::...........-            -........:.  :. ",
        "       :............            =.......:.    ..",
        "        ::...........           =......:.      .",
        "         ::..........           =.....:.        ",
        "          .::........           =...::          ",
        "            .:.......           =.::.           ",
        " ");
    }
    
}
