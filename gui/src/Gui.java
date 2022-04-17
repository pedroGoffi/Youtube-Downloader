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
  static JMenu stdViewMenu;
  static JMenu stdConfigMenu;
  static JMenu stdSearchMenu;
  static JMenu stdHelpMenu;
  static JMenuItem stdHelpAbout;

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
    stdHelpAbout.addActionListener( e -> {
      System.out.println("Hi you is not a man");
    });
  }
  private void HandleMenuBar(){
    menuBar     = new JMenuBar();
    // FILE MENU 
    stdFileMenu = new JMenu("File");
    stdFileExit = new JMenuItem("Exit");

    stdFileMenu.add(stdFileExit);
    // EDIT MENU
    stdEditMenu     = new JMenu("Edit");
    stdEditProfile  = new JMenuItem("Profile");
    stdEditMenu.add(stdEditProfile);

    // VIEW MENU
    stdViewMenu     = new JMenu("View");
    // SEARCH MENU
    stdSearchMenu   = new JMenu("Search");
    // CONFIG MENU
    stdConfigMenu   = new JMenu("Config");
    // HELP MENU
    stdHelpMenu     = new JMenu("Help");
    stdHelpAbout    = new JMenuItem("About");
    stdHelpMenu.add(stdHelpAbout);

    menuBar.add(stdFileMenu);
    menuBar.add(stdEditMenu);
    menuBar.add(stdViewMenu);
    menuBar.add(stdSearchMenu);
    menuBar.add(stdConfigMenu);
    menuBar.add(stdHelpMenu);

    this.setJMenuBar(menuBar);
  }
  private void HandleMainFrame(){
    JPanel TOP      = new JPanel();
    JPanel CENTER   = new JPanel();
    JPanel FOOTER   = new JPanel();
    this.setLayout(new BorderLayout());

    TOP.setBackground(Color.red);
    CENTER.setBackground(Color.yellow);
    FOOTER.setBackground(Color.magenta);

    TOP.setPreferredSize( new Dimension( 100, 100 ) );
    CENTER.setPreferredSize( new Dimension( 100, 100 ) );
    FOOTER.setPreferredSize( new Dimension( 100, 100 ) );

    this.add(TOP, BorderLayout.NORTH);
    this.add(CENTER, BorderLayout.CENTER);
    this.add(FOOTER, BorderLayout.SOUTH);


  }
  Gui(){
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setSize( STD.xFrameSize, STD.yFrameSize );
    HandleMenuBar();
    HandleMenuBarAction();
    HandleMainFrame();
    this.setIconImage(new ImageIcon(STD.imageIconPath).getImage());
    this.setVisible(true);
  }
}
