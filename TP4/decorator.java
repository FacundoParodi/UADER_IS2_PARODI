interface Numero {
    double getValor();
}


class NumeroBase implements Numero {
    private double valor;

    public NumeroBase(double valor) {
        this.valor = valor;
    }

    public double getValor() {
        return valor;
    }
}


abstract class OperacionDecorator implements Numero {
    protected Numero numero;

    public OperacionDecorator(Numero numero) {
        this.numero = numero;
    }
}

class Sumar2 extends OperacionDecorator {
    public Sumar2(Numero numero) {
        super(numero);
    }

    public double getValor() {
        return numero.getValor() + 2;
    }
}

class MultiplicarPor2 extends OperacionDecorator {
    public MultiplicarPor2(Numero numero) {
        super(numero);
    }

    public double getValor() {
        return numero.getValor() * 2;
    }
}

class DividirPor3 extends OperacionDecorator {
    public DividirPor3(Numero numero) {
        super(numero);
    }

    public double getValor() {
        return numero.getValor() / 3;
    }
}

public class Main {
    public static void main(String[] args) {
        Numero base = new NumeroBase(6);
        System.out.println("Valor base: " + base.getValor());

        Numero suma = new Sumar2(base);
        System.out.println("Luego de sumar 2: " + suma.getValor());

        Numero multiplicado = new MultiplicarPor2(suma);
        System.out.println("Luego de multiplicar por 2: " + multiplicado.getValor());

        Numero dividido = new DividirPor3(multiplicado);
        System.out.println("Luego de dividir por 3: " + dividido.getValor());

        System.out.println("Resultado final: " + dividido.getValor());
    }
}