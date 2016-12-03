import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {
    public static final String SEPARATOR = "@";
    public static final String COLON = ":";

    /*
     * Complete the function below.
     *
 	 * Note: The questions in this test build upon each other. We recommend you
	 * copy your solutions to your text editor of choice before proceeding to
	 * the next question as you will not be able to revisit previous questions.
	 */

    static String printHoldingsWithWeight(String inputString) {
		String[] portBench = inputString.split(COLON);
        String portfolio = portBench[0];
        String benchmark = portBench[1];
        String[] portfolioHoldings = portfolio.split(SEPARATOR);
        String[] benchmarkHoldings = benchmark.split(SEPARATOR);
        Arrays.sort(portfolioHoldings);
        HashMap<String,Holding> map = new HashMap<String, Holding>();
        for(String s : benchmarkHoldings){
            String[] elements = s.split(",");
            Holding benchTemp = new Holding(elements[0],elements[1],Integer.parseInt(elements[2]),Double.parseDouble(elements[3]));
            map.put(benchTemp.ticker,benchTemp);
        }
        ArrayList<Holding> portObjects = new ArrayList<Holding>();
        double value=0;
        for(String s: portfolioHoldings){
            String[] elements = s.split(",");
            Holding portTemp = new Holding(elements[0],elements[1],Integer.parseInt(elements[2]),map.get(elements[0]).price);
            value+=portTemp.getValue();
            portObjects.add(portTemp);
        }
        String ret="";
        for(Holding h: portObjects){
             ret+="["+h.ticker+", "+h.name+", "+h.quantity+", "+String.format("%.2f",h.price)+", "+String.format("%.2f",h.getValue())+", "+String.format("%.2f", h.getValue()*100/value)+"], ";
        }
        return ret.substring(0,ret.length()-2);
    }


    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        String res;
        String _input;
        try {
            _input = in.nextLine();
        } catch (Exception e) {
            _input = null;
        }
        res = printHoldingsWithWeight(_input);
        System.out.println(res);
    }
}
class Holding{
    String ticker;
    String name;
    int quantity;
    double price;
    public Holding(String ticker, String name, int quantity){
        this.ticker=ticker;
        this.name=name;
        this.quantity=quantity;
        this.price=0.0;
    }
    public Holding(String ticker, String name, int quantity, double price){
        this.ticker=ticker;
        this.name=name;
        this.quantity=quantity;
        this.price=price;
    }
    public double getValue(){
        return price*quantity;
    }
    public void setPrice(double price){
        this.price=price;
    }

}
