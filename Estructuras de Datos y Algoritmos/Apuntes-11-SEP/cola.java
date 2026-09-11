import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;

public class Colas {

  public static void main(String[] args) {
    Queue<String> queue = new LinkedList<>();
    Random random = new Random();
    Scanner input = new Scanner(System.in);
    int randomPrint;

    String[] pcList = { "PC1", "PC2", "PC3", "PC4", "PC5" };
    for (int i = 0; i < pcList.length; i++) {
      randomPrint = random.nextInt(5);
      queue.offer(pcList[randomPrint]);
    }

    System.out.println("Queue ->  " + queue);

    String choice;
    do {
      System.out.println("Quieres imprimer un elemeto de la cola? y o n");
      choice = input.nextLine().toLowerCase();
      if (choice.equals("y")) {
        System.out.println(queue.poll());
      }
      System.out.println("Queue -> " + queue);
    } while (!queue.isEmpty());
  }
}
