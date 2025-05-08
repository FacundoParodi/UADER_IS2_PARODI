import java.util.ArrayList;
import java.util.List;

abstract class Componente {
    protected String nombre;

    public Componente(String nombre) {
        this.nombre = nombre;
    }

    public abstract void mostrar(String indent);
}

class Pieza extends Componente {
    public Pieza(String nombre) {
        super(nombre);
    }

    public void mostrar(String indent) {
        System.out.println(indent + "- Pieza: " + nombre);
    }
}

class SubConjunto extends Componente {
    private List<Componente> componentes = new ArrayList<>();

    public SubConjunto(String nombre) {
        super(nombre);
    }

    public void agregar(Componente c) {
        componentes.add(c);
    }

    public void mostrar(String indent) {
        System.out.println(indent + "+ Subconjunto: " + nombre);
        for (Componente c : componentes) {
            c.mostrar(indent + "  ");
        }
    }
}