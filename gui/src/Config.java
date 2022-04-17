import javax.swing.*;

public class Config extends JFrame {
  //static JFrame frame = new JFrame();
  private static class stdConf{
    static int xSize = 420;
    static int ySize = 420;
  }
  private void HandleStartFrame(){
    //this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setSize(stdConf.xSize, stdConf.ySize);
    this.setLayout(null);
  }
  private void HandleConfigFrame(){
    //TODO
    System.out.println("TODO");
  }
  Config(){
    HandleStartFrame();
    HandleConfigFrame();
    this.setVisible(true);

  }
}
