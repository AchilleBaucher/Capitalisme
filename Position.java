public class Position{
	private int x,y;
	public int getX(){return x;}
	public int getY(){return y;}
	public Position(int x, int y){
		this.x = x;
		this.y = y;
	}
	public boolean equals(Position p){
		return ((x==p.x&&y==p.y));
	}
	public Position add(Direction d){
		return new Position(x+d.getX(), y+d.getY());
	}
	public Position sub(Direction d){
		return new Position(x-d.getX(), y-d.getY());
	}
	
}