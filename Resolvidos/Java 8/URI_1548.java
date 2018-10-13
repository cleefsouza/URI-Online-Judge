import java.io.IOException;
import java.util.Scanner;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner e = new Scanner(System.in);

        int n = 0, alunos = 0, k, aux, qtd;
        int[] vAntes = new int[1000], vDepois = new int[1000];
        boolean trocas;

        n = e.nextInt();

        for (int i = 0; i < n; i++) {
            qtd = 0;
            alunos = e.nextInt();

            for (int j = 0; j < alunos; j++) {
                vAntes[j] = e.nextInt();
                vDepois[j] = vAntes[j];
            }

            do {
                trocas = false;
                k = 0;
                while (k < alunos - 1) {
                    if (vDepois[k] < vDepois[k + 1]) {
                        aux = vDepois[k];
                        vDepois[k] = vDepois[k + 1];
                        vDepois[k + 1] = aux;

                        trocas = true;
                    }
                    k++;
                }
            } while (trocas);

            for (int d = 0; d < alunos; d++) {
                if (vAntes[d] == vDepois[d]) {
                    qtd++;
                }
            }
            System.out.println(qtd);
        }
    }
}