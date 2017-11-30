public class Direction{
	private int dx;
	private int dy;
	public static final Direction GAUCHE = new Direction(-1,0);
	public static final Direction DROITE = new Direction(1,0);
	public static final Direction HAUT = new Direction(0,-1);
	public static final Direction BAS = new Direction(0,1);
	public static final ArrayList<Direction> DIRECTIONS = new ArrayList(Arrays.asList({GAUCHE,DROITE,HAUT,BAS}));
	public Direction(int dx, int dy){
		this.dx=dx;
		this.dy=dy;
	}
	public int getX(){return dx;}
	public int getY(){return dy;}
	public static ArrayList<Direction> getDirection(){
		return DIRECTIONS;

	}
}