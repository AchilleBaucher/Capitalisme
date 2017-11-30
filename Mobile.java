public abstract class Mobile extends Element{
	private Position position;
	private Configuration config;
	public Mobile(Type type, Configuration config,Position position){
		super(type);
		this.config = config;
		this.position = position;
	}
	public Position getPosition(){return position;}
}