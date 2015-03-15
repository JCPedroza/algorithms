import java.util.Arrays;
import java.util.ArrayList;

// todo: check win, play game
// todo: consider a different class separation (logic and board separated, for example)
// todo: switch player should be in the player class

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
        this.board = deepBoardCopy(board);
    }

    public GameLogic(int dimensions, boolean reverse) {
        this.dimensions = dimensions;
        this.reverse = reverse;
        this.board = new int[dimensions][dimensions];
    }

    public GameLogic(int dimensions) {
        this(dimensions, false);
    }


    public void move(int row, int column, int player) {
        if (board[row][column] == EMPTY) {
            board[row][column] = player;
        }
    }
    
    // Helper for the copy method.
    private int[][] deepBoardCopy(int[][] original) {
        if (original == null) {
            return null;
        }
        int[][] boardCopy = new int[dimensions][];
        for (int i = 0; i < dimensions; i++) {
            boardCopy[i] = Arrays.copyOf(original[i], dimensions);
        }
        return boardCopy;
    }

    // Returns a deep copy of the object.
    public GameLogic copy() {
        return new GameLogic(dimensions, reverse, deepBoardCopy(board));
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
                "argument must be the integer 0, 1, or 2, your input was %d", player));
        }
    }


    public int[][] getBoard() {
        return board;
    }

    public int[][] getBoardCopy() {
        return deepBoardCopy(board);
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

    public static int switchPlayer(int player) {
        if (player == PLAYERX) {
            return PLAYERO;
        } else {
            return PLAYERX;
        }
    }

    public static void main(String[] args) {
        
        GameLogic game1 = new GameLogic(3);
        GameLogic game2 = game1.copy();
        game1.move(0, 0, PLAYERX);
        game2.move(2, 2, PLAYERO);
        System.out.println(game1);
        System.out.println(game2);

        System.out.println(String.format("%d %d", PLAYERX, switchPlayer(PLAYERX)));
        System.out.println(String.format("%d %d", PLAYERO, switchPlayer(PLAYERO)));

    }

}