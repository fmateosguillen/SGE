package org.example;

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

class CalculadoraTest {
    /*
    Sumar pos + pos
    Sumar neg + neg
    Sumar pos + neg
    Sumar MAX_VALUE + 1
    Sumar MIN_VALUE + (-1)
     */

    static Calculadora calculadora;
    @BeforeAll
    public static void init(){
        calculadora = new Calculadora();
    }

    @BeforeEach
    public void pana(){
     System.out.println("Antes de cada test");
    }

    @AfterEach
    public void panaPeroDespues(){
        System.out.println("Después de cada test");
    }

    @Test
    @DisplayName("1+1=2")
    void sumarDosPositivos(){
        assertEquals(2, calculadora.suma(1, 1), "1 + 1 debe ser igual a 2");
    }

    @Test
    @DisplayName("-1+(-1) = -2")
    void sumarDosNegativos(){
        assertEquals(-2, calculadora.suma(-1, -1), "-1 + (-1) debe ser igual a -2");
    }

}