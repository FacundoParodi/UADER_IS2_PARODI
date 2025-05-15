import java.util.*;

interface Observador {
    String getID();
    void notificar(String id);
}

class ObservadorConcreto implements Observador {
    private String id;

    public ObservadorConcreto(String id) {
        this.id = id;
    }

    public String getID() {
        return id;
    }

    public void notificar(String idEmitido) {
        if (this.id.equals(idEmitido)) {
            System.out.println("Observador " + id + " ha sido notificado.");
        }
    }
}

class Emisor {
    private List<Observador> observadores = new ArrayList<>();

    public void registrar(Observador o) {
        observadores.add(o);
    }

    public void emitir(String id) {
        System.out.println("Emitiendo ID: " + id);
        for (Observador o : observadores) {
            o.notificar(id);
        }
    }
}

public class ObserverDemo {
    public static void main(String[] args) {
        Emisor emisor = new Emisor();

        Observador o1 = new ObservadorConcreto("AB12");
        Observador o2 = new ObservadorConcreto("CD34");
        Observador o3 = new ObservadorConcreto("EF56");
        Observador o4 = new ObservadorConcreto("GH78");

        emisor.registrar(o1);
        emisor.registrar(o2);
        emisor.registrar(o3);
        emisor.registrar(o4);

        String[] idsEmitidos = { "AB12", "ZZ99", "CD34", "XY12", "GH78", "AAAA", "EF56", "WXYZ" };
        for (String id : idsEmitidos) {
            emisor.emitir(id);
        }
    }
}