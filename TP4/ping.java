public class Ping {
    public void execute(String ip) {
        if (ip.startsWith("192")) {
            System.out.println("Haciendo ping a " + ip );
        } else {
            System.out.println("IP no permitida");
        }
    }

    public void executefree(String ip) {
        System.out.println("Haciendo ping libre a " + ip + "");
    }
}