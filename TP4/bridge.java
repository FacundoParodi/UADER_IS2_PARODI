interface TrenLaminador {
    void producir();
}

class Tren5Metros implements TrenLaminador {
    public void producir() {
        System.out.println("Produciendo lámina de 5 metros");
    }
}

class Tren10Metros implements TrenLaminador {
    public void producir() {
        System.out.println("Produciendo lámina de 10 metros");
    }
}

class Lamina {
    private TrenLaminador tren;

    public Lamina(TrenLaminador tren) {
        this.tren = tren;
    }

    public void producir() {
        System.out.print("Lámina de 0.5\" x 1.5m");
        tren.producir();
    }
}
