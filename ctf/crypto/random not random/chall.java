import java.util.Random;

class IsItRandom {
    public static char[] encrypt(String plaintext) {
        char [] enc = new char[plaintext.length() * 4];
        for (int i = 0; i < plaintext.length(); i++) {
            char a = plaintext.charAt(i);
            Random random = new Random((int) a);
            for (int j = 0; j < 4; j++) {
                char b = (char) (random.nextInt(94) + 33);
                enc[i * 4 + j] = b;
            }
        }
        return enc;
    }

    public static String toString(char[] array) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < array.length; i++) {
            stringBuilder.append(array[i]);
        }
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        String flag = "REDACTED";
        String enc = toString(encrypt(flag));
        System.out.println("encrypted flag: " + enc);
    }
}
