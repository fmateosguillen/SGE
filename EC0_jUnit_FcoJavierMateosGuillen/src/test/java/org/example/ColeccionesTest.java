package org.example;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ColeccionesTest extends Colecciones{
    static List<Integer> lista = new ArrayList<>();
    @Test
    @BeforeAll
    static void crearLista(){
        lista.add(2);
        lista.add(3);
        lista.add(4);
        lista.add(1);
        lista.add(5);
    }

    @Test
    @DisplayName("ListaOrdenada")
    List<Integer> listaOrdenada(){
        Collections.sort(lista);
        return lista;
    }

    @Test
    @DisplayName("AgregadosTodos")
    List<Integer> addTodos(){
        Collections.addAll(lista, 6, 7, 8);
        return lista;
    }

    @Test
    @DisplayName("MaximoExtraido")
    int maximo(){
        return Collections.max(lista);
    }
}
