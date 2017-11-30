public class Joueur extends Mobile{
	public Joueur(Configuration config, Position position){
		super(Type.JOUEUR,config, position);
	}
	public String toString(){return "@";}
}