public class Caisse extends Mobile{
	public Caisse(Configuration config, Position position){
		super(Type.CAISSE,config, position);
	}
	public String toString(){return "$";}
}