package org.example;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Ejercicio2 {


    public List<Integer> combinarListas(List<Integer> lista, List<Integer> lista2){
        lista.add(1);
        lista.add(2);
        lista.add(3);
        lista2.add(4);
        lista2.add(5);
        Collections.copy(lista, lista2);
        return lista2;
    }
}
