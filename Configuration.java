import java.util.ArrayList;
public class Configuration{
	private ArrayList<Caisse> caisses;
	private Joueur joueur;
	private Niveau niveau;
	public Joueur getJoueur(){return joueur;}
	public Niveau getNiveau(){return niveau;}
	public ArrayList<Caisse> getcaisses(){return caisses;}
	public int getX(){return niveau.getX();}
	public int getY(){return niveau.getY();}
	public String[][] toTabString(){
		String[][] affichage = niveau.toTabString();
		for(Caisse caisse : caisses){
			affichage[caisse.getPosition().getY()][caisse.getPosition().getX()]  = ""+caisse;
		}
		affichage[joueur.getPosition().getY()][joueur.getPosition().getX()] = ""+joueur;
		return affichage;
	}
	public String toString(){
		String affichage = "";
		for(String[] i:toTabString()){
			for (String j : i){
				affichage+=j;
			}
			affichage+="\n";
		}
		return affichage;
	}
	public Configuration(Niveau niveau, Joueur joueur){
		this.niveau = niveau;
		this.joueur = joueur;
	}
	public Configuration(Configuration conf){

		this(conf.getNiveau(),conf.getJoueur());
		caisses = conf.getcaisses();
	}
	public boolean addCaisse(Position position){
		if(estVide(position)){
			caisses.add(new Caisse(this, position));
			return true;
		}
		return false;
	}
	public boolean estCible(Position position){
		return niveau.estCible(position);
	}
	public boolean estVide(Position position){
		return niveau.estVide(position);
	}
	public Element get(Position position){
		if (estVide(position)){
			if(position.equals(joueur.getPosition())){return joueur;}
			for(Caisse caisse : caisses){
				if(position.equals(caisse.getPosition())){return caisse;}
			}
		}
		return niveau.get(position);
	}

	public boolean bougerJoueurVers(Direction d){
		if(estVide(Joueur.getPosition().add(d))){

		}
		return false;
	}
	public boolean addCaisse(Position p){
		return niveau.addCaisse(p);
	}
	public boolean victoire(){

	}
	
}