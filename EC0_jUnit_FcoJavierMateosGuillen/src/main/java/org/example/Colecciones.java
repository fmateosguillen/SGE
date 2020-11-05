package org.example;

import java.util.Collections;
import java.util.List;

public class Colecciones {
    public List<Integer> lista(){
        lista().add(1);
        lista().add(2);
        lista().add(3);
        lista().add(4);
        lista().add(5);
        Collections.sort(lista());
        return lista();
    }
}
