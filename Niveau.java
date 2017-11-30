import java.util.ArrayList;
public class Niveau{
	private Immobile[][] grille;
	private ArrayList<Position> cibles;
	private int x,y;
	public int getX(){return x;}
	public int getY(){return y;}
	public String[][] toTabString(){
		String[][] affichage = new String[x][y];
		for (int i = 0;i<y;i++){
			for (int j= 0;j<x;j++){
				affichage[j][i]=""+grille[i][j];
			}
		}
		for(Position cible:cibles){
			affichage[cible.getX()][cible.getY()]=".";
		}
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
	public Niveau(int x, int y){
		this.x= x;
		this.y = y;
	}

	public boolean addMur(Position p){
		if(estVide(p)){
			grille[p.getX()][p.getY()]=new Mur();
			return true;
		}
		return false;
		
	}
	public boolean addCible(Position p){
		if(estVide(p)&&(!estCible(p))){
			cibles.add(p);
			return true;
		}
		return false;
	}

	public boolean estVide(Position p){
		return (grille[p.getX()][p.getY()].type!=Type.MUR);
	}
	public Immobile get(Position position){
		return grille[position.getX()][position.getY()];
	}
	public boolean estCible(Position position){
		for(Position cible : cibles){
			if(cible.equals(position)){return true;}
		}
		return false;
	}
	public boolean assCaisse(Position p){
		return niveau.addCaisse(p);
	}
}