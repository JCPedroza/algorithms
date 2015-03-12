import java.util.Arrays;
import java.util.ArrayList;

// todo: check win, clone, switch player, play game (maybe in another class?)
// todo: consider a different class separation (logic and board separated, for example)

public class GameLogic {

    public static final int EMPTY = 0;
    public static final int PLAYERX = 1;
    public static final int PLAYERO = 2;
    public static final int DRAW = 3;

    private int dimensions;
    private boolean reverse;
    private int[][] board;


    public GameLogic(int dimensions, boolean reverse, int[][] board) {
        this.dimensions = dimensions;
        this.reverse = reverse;
        this.board = board;
    }

    public GameLogic(int dimensions, boolean reverse) {
        this(dimensions, reverse, new int[dimensions][dimensions]);
    }

    public GameLogic(int dimensions) {
        this(dimensions, false);
    }

    public void move(int row, int column, int player) {
        if (board[row][column] == EMPTY) {
            board[row][column] = player;
        }
    }

    @Override
    public String toString() {
        String rep = "";
        for (int row = 0; row < dimensions; row++) {
            for (int col = 0; col < dimensions; col++) {
                rep += playerToSymbol(board[row][col]);
                if (col == dimensions - 1) {
                    rep += "\n";
                } else {
                    rep += " | ";
                }

            }
            if (row != dimensions - 1) {
                rep += generate_dashes();
                rep += "\n";
            }
        }
        return rep;
    }

    // Helper for toString(), generates dashes (---) for the representation.
    private String generate_dashes() {
        String return_string = "";
        int iterations = 4 * dimensions -3;
        for (int i = 0; i < iterations; i++) {
            return_string += "-";
        }
        return return_string;
    }

    // Map player constants to letters for printing
    private String playerToSymbol(int player) {
        if (player == EMPTY) {
            return " ";
        } else if (player == PLAYERX) {
            return "X";
        } else if (player == PLAYERO) {
            return "O";
        } else {
            throw new IllegalArgumentException(String.format(
                "argument must be the integer 1, 2, or 3, your input was %d", player));
        }
    }


    public int[][] getBoard() {
        return board;
    }

    public boolean getReverse() {
        return reverse;
    }

    public int getDimensions() {
        return dimensions;
    }

    // Return the status (EMPTY, PLAYERX, PLAYERO) of the square at position (row, col).
    public int getSquare(int row, int col) {
        return board[row][col];
    }

    // Return a list of [row, col] for all empty squares.
    public ArrayList<Integer[]> getEmptySquares() {
        ArrayList<Integer[]> empty = new ArrayList<Integer[]>();
        for (int row = 0; row < dimensions; row++) {
            for (int col = 0; col < dimensions; col++) {
                if (board[row][col] == EMPTY) {
                    empty.add(new Integer[]{row, col});
                }
            }
        }
        return empty;
    }

    public static void main(String[] args) {
        
        GameLogic game = new GameLogic(3);
        game.move(0, 0, PLAYERX);
        game.move(1, 1, PLAYERO);
        game.move(1, 2, PLAYERX);
        game.move(2, 1, PLAYERO);
        ArrayList<Integer[]> emptySquares = game.getEmptySquares();

        System.out.println(game.toString());
        for (Integer[] i : emptySquares) {
            System.out.print(i[0]);
            System.out.print(" ");
            System.out.print(i[1]);
            System.out.print("\n");
        }


    }

}