abstract class Handler {
    protected Handler next;

    public void setNext(Handler next) {
        this.next = next;
    }

    public abstract void manejar(int numero);
}

class PrimoHandler extends Handler {
    private boolean esPrimo(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++)
            if (n % i == 0) return false;
        return true;
    }

    Override
    public void manejar(int numero) {
        if (esPrimo(numero)) {
            System.out.println("PrimoHandler consumió: " + numero);
        } else if (next != null) {
            next.manejar(numero);
        }
    }
}

class ParHandler extends Handler {
    Override
    public void manejar(int numero) {
        if (numero % 2 == 0) {
            System.out.println("ParHandler consumió: " + numero);
        } else if (next != null) {
            next.manejar(numero);
        }
    }
}

class DefaultHandler extends Handler {
    Override
    public void manejar(int numero) {
        System.out.println("No consumido: " + numero);
    }
}

public class ChainDemo {
    public static void main(String[] args) {
        Handler primo = new PrimoHandler();
        Handler par = new ParHandler();
        Handler defecto = new DefaultHandler();

        primo.setNext(par);
        par.setNext(defecto);

        for (int i = 1; i <= 100; i++) {
            primo.manejar(i);
        }
    }
}