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

    public static char[] decrypt(char[] enc) {
        int length = enc.length / 4;
        char dec[] = new char[length];
        for (int i = 0; i < length; i++) {
            char[] encBlock = new char[4];
            for (int j = 0; j < 4; j++) {
                encBlock[j] = enc[i * 4 + j];
            }
            for (int ascii = 33; ascii <= 126; ascii++) {
                Random random = new Random(ascii);
                char[] genBlock = new char[4];
                for (int j = 0; j < 4; j++) {
                    genBlock[j] = (char) (random.nextInt(94) + 33);
                }
                if (compareBlocks(encBlock, genBlock)) {
                    dec[i] = (char) ascii;
                    break;
                }
            }
        }
        return dec;
    }

    public static boolean compareBlocks(char[] block1, char[] block2) {
        for (int i = 0; i < block1.length; i++) {
            if (block1[i] != block2[i]) {
                return false;
            }
        }
        return true;
    }

    public static String toString(char[] array) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < array.length; i++) {
            stringBuilder.append(array[i]);
        }
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        String flag = "Kaliber{15_17_7ru11y_r4nd0m_7h0?}";
        String enc = toString(encrypt(flag));
        System.out.println("encrypted flag: " + enc);
        String dec = toString(decrypt(enc.toCharArray()));
        System.out.println("decrypted flag: " + dec);
    }
}
