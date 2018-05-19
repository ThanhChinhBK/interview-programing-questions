import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
	private int n, top, bot;
	private int open[][];
	private WeightedQuickUnionUF uf, isFullUF;
	private int openSite;
	 
	public Percolation(int n){
		if (n <= 0)
			throw new IllegalArgumentException();
		this.openSite = 0;
		this.top = n * n;
		this.n = n;
		this.bot = n * n + 1;
		this.uf = new WeightedQuickUnionUF(n * n + 2);
		this.isFullUF = new WeightedQuickUnionUF(n * n + 1);
		this.open = new int[n][n];
	}
	
	private int getIndex(int i, int j){
		return n * (i-1) + j-1;
	}
	
	private void checkValid(int row, int col){
		if (!(row > 0 && row < n + 1 && col > 0 && col < n + 1))
			throw new IllegalArgumentException();
	}
	public void open(int row, int col){
		checkValid(row, col);
		if (isOpen(row, col))
			return;
		open[row-1][col-1] = 1;
		openSite++;
		
		if (row > 1 && isOpen(row - 1, col)){
			uf.union(getIndex(row, col), getIndex(row - 1, col));
			isFullUF.union(getIndex(row, col), getIndex(row - 1, col));
		}
		if (col > 1 && isOpen(row, col - 1)) {
			uf.union(getIndex(row, col), getIndex(row, col - 1));
			isFullUF.union(getIndex(row, col), getIndex(row, col - 1));
		}
		if (row < n  && isOpen(row + 1, col)){
			uf.union(getIndex(row, col), getIndex(row + 1, col));
			isFullUF.union(getIndex(row, col), getIndex(row + 1, col));
		}
		if (col < n  && isOpen(row, col + 1)){
			uf.union(getIndex(row, col), getIndex(row, col + 1));
			isFullUF.union(getIndex(row, col), getIndex(row, col + 1));
		}
		
		if(row == 1){
			uf.union(getIndex(row, col), top);
			isFullUF.union(getIndex(row, col), top);
		}
		if(row == n)
			uf.union(getIndex(row, col), bot);
	}
	
	public boolean isOpen(int row, int col){
		checkValid(row, col);
		return open[row-1][col-1] == 1 ? true:false;

	}
	
	public boolean isFull(int row, int col){
		checkValid(row, col);
		 return isFullUF.connected(getIndex(row, col), top);
	}
	
	public boolean percolates(){
		return uf.connected(top, bot);
				
	}
	
	public int numberOfOpenSites(){
		return openSite;
	}
	
	public static void main(String[] args) {
	    Percolation perc = new Percolation(10);
	    perc.open(10, 2);
	    perc.open( 2,10);
	    perc.open( 6, 8);
	    perc.open( 2, 6);
	    perc.open( 1, 4);
	    perc.open( 8, 4);
	    perc.open(10, 1);
	    perc.open( 4, 2);
	    perc.open( 4, 8);
	    perc.open( 9, 3);
	    perc.open( 2, 2);
	    perc.open( 9, 1);
	    perc.open( 4, 3);
	    perc.open( 5, 5);
	    perc.open( 5, 7);
	    perc.open( 2, 8);
	    perc.open( 6, 4);
	    perc.open( 7, 5);
	    perc.open( 9, 6);
	    perc.open( 3, 7);
	    perc.open( 4, 7);
	    perc.open( 7, 1);
	    perc.open( 9, 4);
	    perc.open( 3,10);
	    perc.open( 1,10);
	    perc.open(10,10);
	    perc.open( 9, 7);
	    perc.open( 1, 5);
	    perc.open( 9, 8);
	    perc.open( 6, 1);
	    perc.open( 2, 5);
	    perc.open( 3, 4);
	    perc.open( 6, 9);
	    perc.open( 5, 8);
	    perc.open( 3, 2);
	    perc.open( 4, 6);
	    perc.open( 1, 7);
	    perc.open( 7, 9);
	    perc.open( 3, 9);
	    perc.open( 4, 4);
	    perc.open( 4,10);
	    perc.open( 3, 5);
	    perc.open( 3, 8);
	    perc.open( 1, 8);
	    perc.open( 3, 1);
	    perc.open( 6, 7);
	    perc.open( 2, 3);
	    perc.open( 7, 4);
	    perc.open( 9,10);
	    perc.open( 7, 6);
	    perc.open( 5, 2);
	    perc.open( 8, 3);
	    perc.open(10, 8);
	    //perc.open( 7,10);
	    //perc.open( 4, 5);
	    //perc.open( 8,10);
	    System.out.println(perc.isFull(10, 8));
	    //boolean c1 = perc.uf.connected(perc.ijTo1D(1, 1), perc.ijTo1D(2, 1));
	    //boolean c2 = perc.percolates();
	    //StdOut.println(c1);
	    //StdOut.println(c2);
	  }
	
}
