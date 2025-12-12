import static org.junit.Assert.assertArrayEquals;
//import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class FibonacciTest {

  private final Fibonacci fib = new Fibonacci();

  /*@Test
  void primerValorEsUno() {
    int[] serie = fib.generateFibSerie(5); // {1, 1, 2, 3, 5}
    assertEquals(1, serie[0]);
  }
}*/

  @Test
  void primerosCincoValores() {
    int[] serie = fib.generateFibSerie(5); // {1, 1, 2, 3, 5}
    int[] expected = {1, 1, 2, 3, 5};
    assertArrayEquals(expected, serie);
  }
}