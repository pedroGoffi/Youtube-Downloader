import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Gui extends JFrame{
  static JMenuBar  menuBar;
  // STD FILE MENU
  static JMenu     stdFileMenu;
  // STD FILE MENU ITEM
  static JMenuItem stdFileExit;
  // STD EDIT MENU
  static JMenu     stdEditMenu; 
  // STD EDIT MENU ITEM
  static JMenuItem stdEditProfile;

  private static class STD{
    static int xFrameSize = 500;
    static int yFrameSize = 500;
    static String imageIconPath = "../assets/icon.png";
  }
  private static void HandleMenuBarAction(){
    stdFileExit.addActionListener( e -> {
      // If the exit button iss being clicked then 
      // we will exit the program
      System.out.println("Thanks for using me");
      System.exit(0);
    });
    stdEditProfile.addActionListener( e ->{
      System.out.println("Oh you clicked me >///<");
    });
  }
  private static void HandleMenuBar(JFrame frame){
    menuBar     = new JMenuBar();
    // FILE MENU 
    stdFileMenu = new JMenu("File");
    stdFileExit = new JMenuItem("Exit");

    stdFileMenu.add(stdFileExit);
    // EDIT MENU
    stdEditMenu     = new JMenu("Edit");
    stdEditProfile  = new JMenuItem("Profile");

    stdEditMenu.add(stdEditProfile);


    menuBar.add(stdFileMenu);
    menuBar.add(stdEditMenu);

    frame.setJMenuBar(menuBar);
  }
  Gui(){
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setSize( STD.xFrameSize, STD.yFrameSize );
    HandleMenuBar(this);
    HandleMenuBarAction();
    this.setIconImage(new ImageIcon(STD.imageIconPath).getImage());
    this.setVisible(true);
  }
}
