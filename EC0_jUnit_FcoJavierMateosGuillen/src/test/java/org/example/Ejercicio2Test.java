package org.example;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Ejercicio2Test extends Ejercicio2{
    List<Integer> lista = new ArrayList<>();
    @Test
    @DisplayName("CopiarListaTrue")
    void copiarLista(List<Integer> lista, List<Integer> lista2){
        combinarListas(lista, lista2);
        assertEquals(true, lista == lista2);
    }
}
