import java.util.Iterator;
import java.util.NoSuchElementException;

class StringIterator implements Iterator<Character> {
    private String data;
    private int index;
    private boolean reverse;

    public StringIterator(String data, boolean reverse) {
        this.data = data;
        this.reverse = reverse;
        this.index = reverse ? data.length() - 1 : 0;
    }

    @Override
    public boolean hasNext() {
        return reverse ? index >= 0 : index < data.length();
    }

    @Override
    public Character next() {
        if (!hasNext()) throw new NoSuchElementException();
        return data.charAt(reverse ? index-- : index++);
    }
}

public class IteratorDemo {
    public static void main(String[] args) {
        String texto = "Ingenieria";
        System.out.println("Directo:");
        StringIterator it = new StringIterator(texto, false);
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }

        System.out.println("\nReverso:");
        StringIterator rev = new StringIterator(texto, true);
        while (rev.hasNext()) {
            System.out.print(rev.next() + " ");
        }
    }
}