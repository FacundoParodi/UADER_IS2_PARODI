public class PingProxy {
    private Ping ping;

    public PingProxy() {
        this.ping = new Ping();
    }

    public void execute(String ip) {
        if (ip.equals("192.168.0.254")) {
            ping.executefree("www.google.com");
        } else {
            ping.execute(ip);
        }
    }
}