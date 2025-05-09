import java.util.*;

public class MemoryGame {
    private static final int SIZE = 4;
    private static final int PAIRS = SIZE * SIZE / 2;
    private static String[][] board = new String[SIZE][SIZE];
    private static boolean[][] revealed = new boolean[SIZE][SIZE];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> values = new ArrayList<>();

        // Generate pairs like A, B, C, D...
        for (char c = 'A'; c < 'A' + PAIRS; c++) {
            values.add(String.valueOf(c));
            values.add(String.valueOf(c));
        }

        // Shuffle and fill board
        Collections.shuffle(values);
        Iterator<String> it = values.iterator();
        for (int i = 0; i < SIZE; i++)
            for (int j = 0; j < SIZE; j++)
                board[i][j] = it.next();

        int matches = 0;

        while (matches < PAIRS) {
            printBoard();
            System.out.println("Enter coordinates of first cell (row and column): ");
            int r1 = scanner.nextInt(), c1 = scanner.nextInt();
            if (!isValid(r1, c1)) continue;

            revealed[r1][c1] = true;
            printBoard();

            System.out.println("Enter coordinates of second cell (row and column): ");
            int r2 = scanner.nextInt(), c2 = scanner.nextInt();
            if (!isValid(r2, c2) || (r1 == r2 && c1 == c2)) {
                revealed[r1][c1] = false;
                continue;
            }

            revealed[r2][c2] = true;
            printBoard();

            if (board[r1][c1].equals(board[r2][c2])) {
                System.out.println("Match found!");
                matches++;
            } else {
                System.out.println("Not a match.");
                revealed[r1][c1] = false;
                revealed[r2][c2] = false;
            }
        }

        System.out.println("Congratulations! You found all pairs.");
    }

    private static boolean isValid(int r, int c) {
        if (r < 0 || r >= SIZE || c < 0 || c >= SIZE) {
            System.out.println("Invalid coordinates.");
            return false;
        }
        if (revealed[r][c]) {
            System.out.println("Cell already revealed.");
            return false;
        }
        return true;
    }

    private static void printBoard() {
        System.out.println("\nMemory Board:");
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (revealed[i][j])
                    System.out.print(" " + board[i][j] + " ");
                else
                    System.out.print(" * ");
            }
            System.out.println();
        }
    }
}
