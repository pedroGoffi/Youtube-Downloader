import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Gui extends JFrame{
  static class STD{
    static JFrame frame;
    static JMenuBar menuBar;

    static int xFrameSize   = 500;
    static int yFrameSize   = 500;
    static String Title     = "My aplication";
    public static void InitWindow(
      JFrame newFrame,
      JMenuBar newBar
    ){
      frame     = newFrame;
      menuBar   = newBar;
      frame.setSize(STD.xFrameSize, STD.yFrameSize);
      frame.setTitle(STD.Title);


      STD.addToMenuBar(new JMenu("File"));
      STD.addToMenuBar(new JMenu("Edit"));
      STD.addToMenuBar(new JMenu("Help"));

      frame.add(menuBar);

      frame.setVisible(true);
    }
    public static void addToMenuBar(JMenu newbar){
      menuBar.add(newbar);
    }
  }
  static class MENU{}
  private void initVar(){
    STD.InitWindow( 
      new JFrame(), 
      new JMenuBar() 
    );
  }
  Gui(){
    initVar();
  }
}
