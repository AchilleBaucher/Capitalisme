public class Position{
	private int x,y;
	public int getX(){return x;}
	public int getY(){return y;}
	public boolean equals(Position p){
		return ((x==p.getX()&&y==p.getY()));
	}
}