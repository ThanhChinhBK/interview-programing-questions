import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
	private double[] fractions ;
	private int T;
	private double mean_val, stddev_val;
	public PercolationStats(int n, int trials){
		if (n < 0 || trials <= 0)
			throw new IllegalArgumentException();
		int row_rand, col_rand;
		fractions = new double[trials];
		T = trials;
		for(int i = 0; i < trials; i++){
			int open_sites = 0;
			Percolation tmp = new Percolation(n);
			while(!tmp.percolates()){
				row_rand = StdRandom.uniform(1, n + 1);
				col_rand = StdRandom.uniform(1, n + 1);
				if (!tmp.isOpen(row_rand, col_rand)){
					tmp.open(row_rand, col_rand);
					open_sites++;
				}				
			}
			fractions[i] = (double)open_sites / (n * n);			
		}
		this.mean_val = StdStats.mean(fractions);
		this.stddev_val = StdStats.stddev(fractions);
	}
	
	public double mean(){
		return mean_val;
	}
	
	public double stddev(){
		return stddev_val;
	}
	
	public double confidenceLo(){
		return mean() - ((1.96 * stddev()) / Math.sqrt(T));
	}
 public double confidenceHi(){
		return mean() + ((1.96 * stddev()) / Math.sqrt(T));
	}
	
	public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        int T = Integer.parseInt(args[1]);
        PercolationStats ps = new PercolationStats(N, T);

        String confidence = ps.confidenceLo() + ", " + ps.confidenceHi();
        StdOut.println("mean                    = " + ps.mean());
        StdOut.println("stddev                  = " + ps.stddev());
        StdOut.println("95% confidence interval = " + confidence);
    }
}
