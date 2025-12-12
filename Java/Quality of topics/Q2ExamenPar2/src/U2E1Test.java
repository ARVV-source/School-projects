import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.Test;

class U2E1Test {
  private final DiaFestivo diaFestivo = new DiaFestivo();
  private final DiaDeMuertos diaMuertos = new DiaDeMuertos();

  @Test
  void celebrarDiaFestivo() {
    assertEquals(true, diaFestivo.celebrar());
  }

  @Test
  void fallarPonerAltar() {
    ArrayList<String> arregloVacio = new ArrayList<String>();
    assertFalse(diaMuertos.celebrar("profe paseme plox", arregloVacio));
  }

  @Test
  void celebrarDiaMuertos() {
    ArrayList<String> arregloPruebas = new ArrayList<String>(List.of("Test", "Test", "Test"));
    assertTrue(diaMuertos.celebrar("profe paseme plox", arregloPruebas));
  }
}
